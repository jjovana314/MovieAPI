from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from schema import movie_schema
import exception_messages as ex_m
import helper
import exceptions
import sqlite3


app = Flask(__name__)
api = Api(app)


class Movie(Resource):
    def post(self):
        data = request.get_json()
        try:
            movies = data["movies"]
        except KeyError:
            return jsonify(
                {
                    "message": "please enter movies data",
                    "code": ex_m.BAD_REQUEST
                }
            )
        else:
            for movie in movies:
                try:
                    helper.validate_schema(movie, movie_schema)
                except exceptions.MovieSchemaError as ex:
                    return jsonify({"message": ex.args[0], "code": ex.args[1]})

            # establish connection with database and save data
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()
            create_table = """
            CREATE TABLE IF NOT EXISTS movies (
                id int, movie_title text, 
                year_release int, rate real)
            """

            cursor.execute(create_table)
            all_movies = helper.data_generate(movies)
            insert_query = "INSERT INTO movies VALUES (?, ?, ?, ?)"
            # here we can also insert one by one row with loop
            cursor.executemany(insert_query, all_movies)
            connection.commit()
            connection.close()

            return jsonify(
                {
                    "message": "data saved in database",
                    "code": ex_m.OK
                }
            )


api.add_resource(Movie, "/movie")
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

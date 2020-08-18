from json import dumps, loads
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from flask import jsonify
import exception_messages as ex_m
import exceptions


def validate_schema(data: dict, schema: dict) -> None:
    """ Schema validation.

    Args:
        data (dict): dictionary for validation
        schema (dict): shcema for validation

    Raises:
        One of schema exceptions if data dictionary does not
        match schema
    """
    data = dumps(data)
    try:
        validate(loads(data), schema)
    except ValidationError as ex:
        # convert exception message into string
        ex_str = str(ex)
        # iterate thru all schema_errors elements
        for idx, value in enumerate(ex_m.schema_errors):
            if value in ex_str:
                raise ex_m.schema_exceptions[idx] from None


def data_generate(movies: list) -> list:
    """ Generate movie data.

    Args:
        movies (list): list with movies data

    Returns:
        list with filtrated movies data
    """
    # generate helper lists
    titles = [dict_data["movie_title"] for dict_data in movies]
    years = [dict_data["year_release"] for dict_data in movies]
    rates = [dict_data["rate"] for dict_data in movies]

    # titles, years and rates are all lists of the same length
    data_movies = [(id_, titles[id_], years[id_], rates[id_]) 
                   for id_ in range(len(titles))]

    return data_movies

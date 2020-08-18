movie_schema = {
    "type": "object",
    "properties": {
        "movie_title": {
            "type": "string", "minLength": 2, "maxLength": 50
        },
        "year_release": {
            "type": "integer", "minimum": 1900, "maximum": 2021
        },
        "rate": {
            "type": "number", "minimum": 0.0, "maximum": 10.0
        },
        "director": {
            "type": "string", "minLegth": 2, "maxLength": 30
        },
        "stars": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 3,
            "maxItems": 10,
            "uniqueItems": True
        }
    },
    "required": ["movie_title", "year_release", "rate"],
    "additionalItems": False
}

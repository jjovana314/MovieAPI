class MovieError(Exception):
    """ General movie exception. """


class MovieSchemaError(MovieError):
    """ General schema exception. """


class TypeSchemaError(MovieSchemaError):
    """ Raised if type of data is not valid. """


class RequiredSchemaError(MovieSchemaError):
    """ Raised if required data is missing. """


class MinLengthSchemaError(MovieSchemaError):
    """ Raised if length of sequence is less than minimum. """


class MaxLengthSchemaError(MovieSchemaError):
    """ Raised if length of sequience is greather than maximum. """


class MinimumSchemaError(MovieSchemaError):
    """ Raised if value from data is less than minimum. """


class MaximumSchemaError(MovieSchemaError):
    """ Raised if value from data is greather than maximum. """


class MinimumItmesError(MovieSchemaError):
    """ Raised if length of sequence is less than minimum. """


class MaximumItemsError(MovieSchemaError):
    """ Raised if length of sequence is greather than maximum. """

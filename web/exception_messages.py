from http import HTTPStatus
import exceptions


OK = HTTPStatus.OK
BAD_REQUEST = HTTPStatus.BAD_REQUEST
INVALID_SCHEMA = 451

schema_errors = [
    "Failed validating 'type' in schema",
    "Failed validating 'required' in schema",
    "Failed validating 'minLength' in schema",
    "Failed validating 'maxLength' in schema",
    "Failed validating 'minimum' in schema",
    "Failed validating 'maximum' in schema",
    "Failed validating 'minItems' in schema",
    "Failed validating 'maxItems' in schema"
]

error_messages = [
    "Invalid type of data",
    "Please enter all required fields",
    "String length is less than minimum",
    "String length exceeded maximum",
    "Value is less than minimum",
    "Value is greather than maximum",
    "Sequence length is less than minimum",
    "Sequence length is greather than maximum"
]

all_exceptions = [
    exceptions.TypeSchemaError,
    exceptions.RequiredSchemaError,
    exceptions.MinLengthSchemaError,
    exceptions.MaxLengthSchemaError,
    exceptions.MinimumSchemaError,
    exceptions.MaximumSchemaError,
    exceptions.MinimumItmesError,
    exceptions.MaximumItemsError
]

schema_exceptions = []
for i in range(len(all_exceptions)):
    schema_exceptions.append(
        all_exceptions[i](schema_errors[i], INVALID_SCHEMA)
    )

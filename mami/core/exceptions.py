from django.core.exceptions import ValidationError


class BaseCustomError(ValidationError):
    """
    A base custom error class that generates detailed error messages based on the provided context.

    Examples:
    ----------
    InstanceAlreadyExistsError() -> "Instance already exists!"
    InstanceAlreadyExistsError(model=User) -> "User already exists!"
    InstanceDoesNotExistError(f"A user with email {dto.email} already exists!") ->
    "A user with email email@example.com already exists!"

    Attributes:
    -----------
    default_error_message: str
        The default message to be used if no custom message is provided.

    custom_message: str
        The custom error message if provided.

    model: Type[Model]
        An optional Django model class to be used in the error message.

    Methods:
    --------
    get_model_str() -> str:
        Returns the name of the model or "Instance" if not provided.

    __str__() -> str:
        Returns the error message.
    """

    default_error_message = "An error occurred."

    def __init__(self, message=None, model=None, *args, **kwargs):
        super().__init__(message or self.default_error_message, *args, **kwargs)
        self.custom_message = message
        self.model = model

    def get_model_str(self):
        """
        Retrieves the name of the model or "Instance" if model is not provided.

        Returns:
            str: The name of the model or "Instance".
        """

        return self.model.__name__ if self.model else "Instance"

    def __str__(self):
        """
        Generates the error message.

        Returns:
            str: The error message.
        """

        return (self.custom_message or self.default_error_message).format(model=self.get_model_str())


class InstanceAlreadyExistsError(BaseCustomError):
    """
    Raised when trying to create an instance that already exists.
    """

    default_error_message = "{model} already exists!"


class InstanceCreationError(BaseCustomError):
    """
    Raised when there's an error during the creation of an instance.
    """

    default_error_message = "An error occurred while creating the {model}."


# class InstanceDoesNotExistError(BaseCustomError):
#     default_error_message = "{model} doesn't exist!"

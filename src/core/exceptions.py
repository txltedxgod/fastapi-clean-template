"""Domain and application exception hierarchy."""

from fastapi import status


class AppException(Exception):
    """Base application exception mapped to structured JSON errors."""

    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ) -> None:
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class ResourceNotFoundError(AppException):
    """Raised when an entity cannot be found by identifier."""

    def __init__(self, resource: str, identifier: str) -> None:
        super().__init__(
            f"{resource} with ID '{identifier}' was not found",
            status.HTTP_404_NOT_FOUND,
        )


class DuplicateResourceError(AppException):
    """Raised on conflicting unique constraints."""

    def __init__(self, resource: str, identifier: str) -> None:
        super().__init__(
            f"{resource} '{identifier}' already exists",
            status.HTTP_409_CONFLICT,
        )


class ValidationError(AppException):
    """Raised when domain validation rules are violated."""

    def __init__(self, detail: str) -> None:
        super().__init__(
            f"Validation failed: {detail}",
            status.HTTP_422_UNPROCESSABLE_ENTITY,
        )

"""Response objects."""
from typing import Any
from typing import Dict
from typing import Optional
from typing import Union


class ResponseTypes:
    """Response types class."""

    PARAMETERS_ERROR = "ParametersError"
    RESOURCE_ERROR = "ResourceError"
    SYSTEM_ERROR = "SystemError"
    SUCCESS = "Success"


class ResponseFailure:
    """Response failure class."""

    def __init__(self, type_: str, message: Union[str, Exception, None]) -> None:
        """Constructor."""
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self, msg: Union[str, Exception, None]) -> Optional[str]:
        """Format message when it is an exception.

        Args:
            msg: string, exception or None.

        Returns:
            Union[str, None]: formatted message or None.
        """
        if isinstance(msg, Exception):
            return f"{msg.__class__.__name__}: {msg}"
        return msg

    @property
    def value(self) -> Dict[str, Optional[str]]:
        """Value property.

        Returns:
            Dict[str, str]: type and message.
        """
        return {"type": self.type, "message": self.message}

    def __bool__(self) -> bool:
        """Bool return for success."""
        return False


class ResponseSuccess:
    """Response success class."""

    def __init__(self, value: Any = None) -> None:
        """Constructor."""
        self.type = ResponseTypes.SUCCESS
        self.value = value

    def __bool__(self) -> bool:
        """Bool return for success."""
        return True

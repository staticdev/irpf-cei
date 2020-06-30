# incomplete

from typing import Any, TypeVar, overload
from unittest.mock import MagicMock

_T = TypeVar("_T")

class MockFixture:
    mock_module: Any  # unittest.mock module
    def __init__(self, config: Any) -> None: ...
    patch: _Patcher

    class _Patcher:
        mock_module: Any  # unittest.mock module
        @overload
        def __call__(self, target: Any, new: _T, *args: Any, **kwargs: Any) -> _T: ...
        @overload
        def __call__(self, target: Any, *args: Any, **kwargs: Any) -> MagicMock: ...

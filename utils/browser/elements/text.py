from ....utils.logger import LoggerUtils
from .base import BaseElement


class Text(BaseElement):
    """Class for text elements."""

    def __init__(self, name: str, locator: tuple, default_max_timeout: int):
        super().__init__(name, locator, default_max_timeout)

    def get_content(self, max_timeout: int = 0) -> str:
        """Method to get text element content."""
        LoggerUtils.log_element_action("get content", self._name)
        max_timeout = self._wait_max_timeout_handler(max_timeout)
        return self._find(max_timeout).text

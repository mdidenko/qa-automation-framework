from ....utils.logger import LoggerUtils
from ..common import UiWait
from .base import BaseElement


class TextField(BaseElement):
    """Class for text field elements."""

    def __init__(self, name: str, locator: tuple, default_max_timeout: int):
        super().__init__(name, locator, default_max_timeout)

    def clear_text(self, max_timeout: int = 0) -> None:
        """Method to clear text field."""
        LoggerUtils.log_element_action("clear text", self._name)
        max_timeout = self._wait_max_timeout_handler(max_timeout)
        self.scroll_for_visibility(max_timeout)
        UiWait(max_timeout).element_to_be_clickable(self._locator).clear()

    def insert_text(self, text: str, max_timeout: int = 0) -> None:
        """Method to insert text in text field."""
        LoggerUtils.log_element_action("insert text", self._name)
        max_timeout = self._wait_max_timeout_handler(max_timeout)
        self.clear_text(max_timeout)
        element = UiWait(max_timeout).element_to_be_clickable(self._locator)
        element.send_keys(text)

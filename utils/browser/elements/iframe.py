from selenium.webdriver.remote.webelement import WebElement
from ....utils.logger import LoggerUtils
from ..common import UiWait
from .base import BaseElement


class Iframe(BaseElement):
    """Class for iframe elements."""

    def __init__(self, name: str, locator: tuple, default_max_timeout: int):
        super().__init__(name, locator, default_max_timeout)

    def open_frame(self, max_timeout: int = 0) -> None:
        """Method to open frame."""
        LoggerUtils.log_element_action("open frame", self._name)
        max_timeout = self._wait_max_timeout_handler(max_timeout)
        UiWait(max_timeout).iframe_to_be_available(self._locator)

    def find_frame_element(self, locator: tuple, max_timeout: int = 0) -> \
            WebElement:
        """Method to find element in frame."""
        LoggerUtils.log_element_action("find frame element", self._name)
        max_timeout = self._wait_max_timeout_handler(max_timeout)
        element = UiWait(max_timeout).presence_of_element_located(locator)
        return element

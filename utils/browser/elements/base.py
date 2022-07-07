from selenium.webdriver.remote.webelement import WebElement
from ....utils.logger import LoggerUtils
from ..common import UiWait, ActionChain
from ..webdriver import WebDriver


class BaseElement:
    """Parent class for all elements."""
    __slots__ = ('_name', '_locator', '_default_max_timeout')

    def __init__(self, name: str, locator: tuple, default_max_timeout: int):
        self._name = name
        self._locator = locator
        self._default_max_timeout = default_max_timeout

    def get_locator(self) -> tuple:
        """Method to get element locator."""
        return self._locator

    def update_locator(self, locator: tuple) -> None:
        """Method to update element locator."""
        self._locator = locator

    def _wait_max_timeout_handler(self, input_max_timeout: int) -> int:
        """Method to handle wait max timeout."""
        if self._default_max_timeout > input_max_timeout:
            return self._default_max_timeout
        return input_max_timeout

    def _find(self, max_timeout: int = 0) -> WebElement:
        """Method to find element."""
        max_timeout = self._wait_max_timeout_handler(max_timeout)
        return UiWait(max_timeout).presence_of_element_located(self._locator)

    def get_attribute(self, name: str, max_timeout: int = 0) -> str:
        """Method to get element attribute."""
        LoggerUtils.log_element_action(f"get {name} attribute for", self._name)
        max_timeout = self._wait_max_timeout_handler(max_timeout)
        return self._find(max_timeout).get_attribute(name)

    def scroll_for_visibility(self, max_timeout: int = 0) -> None:
        """Method to scroll for element visibility."""
        LoggerUtils.log_element_action(
            "scroll for element visibility", self._name
        )
        max_timeout = self._wait_max_timeout_handler(max_timeout)
        element = self._find(max_timeout)
        WebDriver.scroll_to_element(element)

    def click(self, max_timeout: int = 0, pre_scroll=True) -> None:
        """Method to click on element."""
        LoggerUtils.log_element_action("click on", self._name)
        max_timeout = self._wait_max_timeout_handler(max_timeout)
        if pre_scroll:
            self.scroll_for_visibility(max_timeout)
        UiWait(max_timeout).element_to_be_clickable(self._locator).click()

    def focus(self, max_timeout: int = 0) -> None:
        """Method to focus element."""
        LoggerUtils.log_element_action("focus", self._name)
        max_timeout = self._wait_max_timeout_handler(max_timeout)
        self.scroll_for_visibility(max_timeout)
        element = UiWait(max_timeout).visibility_of_element_located(
            self._locator
        )
        ActionChain().get().move_to_element(element)

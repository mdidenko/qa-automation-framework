from selenium.webdriver.common.action_chains import ActionChains
from ..webdriver import WebDriver


class ActionChain:
    """Class for working with action chains."""
    __slots__ = ()

    @staticmethod
    def get() -> ActionChains:
        """Method for get action chain instance."""
        return ActionChains(WebDriver.get_driver())

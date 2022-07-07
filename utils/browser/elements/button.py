from .base import BaseElement


class Button(BaseElement):
    """Class for button elements."""

    def __init__(self, name: str, locator: tuple, default_max_timeout: int):
        super().__init__(name, locator, default_max_timeout)

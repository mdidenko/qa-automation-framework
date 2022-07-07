from .base import BaseElement


class DropdownMenu(BaseElement):
    """Class for dropdown menu elements."""

    def __init__(self, name: str, locator: tuple, default_max_timeout: int):
        super().__init__(name, locator, default_max_timeout)

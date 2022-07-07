from .base import BaseElement


class Link(BaseElement):
    """Class for link elements."""

    def __init__(self, name: str, locator: tuple, default_max_timeout: int):
        super().__init__(name, locator, default_max_timeout)

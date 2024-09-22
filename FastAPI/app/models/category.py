""" Module containing the Category class."""
from pydantic import BaseModel

class Category(BaseModel):
    """
    Class representing a category.

    Attributes:
        id (int): Unique identifier of the category.
        name (str): Name of the category.
    """
    id: int
    name: str

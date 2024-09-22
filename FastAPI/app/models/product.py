"""
product.py

This module defines the Product model using Pydantic's BaseModel.

Classes:
    Product: Represents a product entity with attributes such as id, nombre,
    descripcion, precio, and categoria_id.

Attributes:
    Decimal (module): Provides support for fast correctly-rounded decimal floating point arithmetic.
    BaseModel (class): Pydantic's base class for creating data models.
"""

from decimal import Decimal
from pydantic import BaseModel


class Product(BaseModel):
    """
    Product model representing a product entity.

    Attributes:
        id (int): Unique identifier for the product.
        nombre (str): Name of the product.
        descripcion (str): Description of the product.
        precio (Decimal): Price of the product.
        categoria_id (int): Identifier for the category to which the product belongs.
    """

    id: int
    nombre: str
    descripcion: str
    precio: Decimal
    categoria_id: int

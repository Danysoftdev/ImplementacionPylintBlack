""" This module contains the routes for the product service. """
from fastapi import APIRouter
from app.services.product_service import ProductService

product_route = APIRouter()
product_service = ProductService()

@product_route.get("/products/")
def get_products():
    """
    Get all products
    
    Returns:
    list: A list of all products
    """
    return product_service.get_products()

@product_route.get("/products/{product_id}")
def get_product(product_id: int):
    """
    Get product
    
    Returns:
    Product: A product object
    
    Parameters:
    product_id (int): The ID of the product
    """
    return product_service.get_product(product_id)

@product_route.post("/products")
def create_product(product):
    """
    Create a new product
    
    Returns:
    Product: A product object
    
    Parameters:
    product (Product): The product object
    """
    return product_service.create_product(product)

@product_route.put("/products/{product_id}")
def update_product(product_id: int, product_data: dict):
    """
    Update a product
    
    Returns:
    str: A message indicating the success of the operation
    
    Parameters:
    product_id (int): The ID of the product
    product_data (dict): The updated product data
    """
    return product_service.update_product(product_id, product_data)

@product_route.delete("/products/{product_id}")
def delete_product(product_id: int):
    """
    Delete a product
    
    Returns:
    str: A message indicating the success of the operation
    
    Parameters:
    product_id (int): The ID of the product
    """
    return product_service.delete_product(product_id)

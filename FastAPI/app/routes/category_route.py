""" This module contains the routes for the category service. """
from fastapi import APIRouter
from models.category import Category
from services.category_service import CategoryService

category_service = CategoryService()
category_route = APIRouter()

@category_route.get("/categories/")
def get_categories():
    """
    Get all categories
    
    Returns:
    list: A list of all categories
    """
    return category_service.get_categories()

@category_route.get("/categories/{category_id}")
def get_category(category_id: int):
    """
    Get category
    
    Returns:
    Category: A category object
    
    Parameters:
    category_id (int): The ID of the category
    """
    return category_service.get_category(category_id)

@category_route.post("/categories")
def create_category(category: Category):
    """
    Create a new category
    
    Returns:
    Category: A category object
    
    Parameters:
    category (Category): The category object
    """
    return category_service.create_category(category)

@category_route.put("/categories/{category_id}")
def update_category(category_id: int, category_data: dict):
    """
    Update a category
    
    Returns:
    str: A message indicating the success of the operation
    
    Parameters:
    category_id (int): The ID of the category
    category_data (dict): The updated category data
    """
    return category_service.update_category(category_id, category_data)

@category_route.delete("/categories/{category_id}")
def delete_category(category_id: int):
    """
    Delete a category
    
    Returns:
    str: A message indicating the success of the operation
    
    Parameters:
    category_id (int): The ID of the category
    """
    return category_service.delete_category(category_id)

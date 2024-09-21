""" This module contains the CRUD operations for the category model """
#added comment to validate pylint on github
from config.database import CategoryModel
from peewee import DoesNotExist
from models.category import Category
from fastapi import APIRouter, Body

category_router = APIRouter()

def get_categories():
    """
    Get all categories
    
    Returns:
    list: A list of all categories
    """
    categories = CategoryModel.select().where(CategoryModel.id > 0).dicts()
    return list(categories)

def get_category(category_id: int):
    """
    Get category
    
    Returns:
    Category: A category object
    
    Parameters:
    category_id (int): The ID of the category
    """
    try:
        category = CategoryModel.get(CategoryModel.id == category_id)
        return category
    except DoesNotExist:
        return "Category not found"

def create_category(category: Category = Body(...)):
    """
    Create a new category
    
    Returns:
    Category: A category object
    
    Parameters:
    category (Category): The category object
    """
    CategoryModel.create(name=category.name)
    return category

def update_category(category_id: int, category_data: dict):
    """
    Update a category
    
    Returns:
    str: A message indicating the success of the operation
    
    Parameters:
    category_id (int): The ID of the category
    category_data (dict): The updated category data
    """
    CategoryModel.update(category_data).where(CategoryModel.id == category_id).execute()
    return "Category updated successfully"

def delete_category(category_id: int):
    """
    Delete a category
    
    Returns:
    str: A message indicating the success of the operation
    
    Parameters:
    category_id (int): The ID of the category
    """
    try:
        category = CategoryModel.get(CategoryModel.id == category_id)
        category.delete_instance()
        return "Category deleted successfully"
    except DoesNotExist:
        return "Category not found"

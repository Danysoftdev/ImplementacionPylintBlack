""" This module contains the CRUD operations for the product model """
from peewee import DoesNotExist
from config.database import ProductModel
from models.product import Product
from fastapi import Body

class ProductService:
    """
    A service class for the product model
    """

    def get_products(self):
        """
        Get all products
        
        Returns:
        list: A list of all products
        """
        products = ProductModel.select().where(ProductModel.id > 0).dicts()
        return list(products)

    def get_product(self, product_id: int):
        """
        Get product
        
        Returns:
        Product: A product object
        
        Parameters:
        product_id (int): The ID of the product
        """
        try:
            product = ProductModel.get(ProductModel.id == product_id)
            return product.__data__  # Return product as a dictionary
        except DoesNotExist:
            return {"error": "Product not found"}

    def create_product(self, product: Product = Body(...)):
        """
        Create a new product
        
        Returns:
        Product: A product object
        
        Parameters:
        product (Product): The product object
        """
        new_product = ProductModel.create(
            nombre=product.nombre,
            precio=product.precio,
            categoria=product.categoria
        )
        return new_product.__data__  # Return the created product as a dictionary

    def update_product(self, product_id: int, product_data: dict):
        """
        Update a product
        
        Returns:
        str: A message indicating the success of the operation
        
        Parameters:
        product_id (int): The ID of the product
        product_data (dict): The updated product data
        """
        ProductModel.update(product_data).where(ProductModel.id == product_id).execute()
        return {"message": "Product updated successfully"}

    def delete_product(self, product_id: int):
        """
        Delete a product
        
        Returns:
        str: A message indicating the success of the operation
        
        Parameters:
        product_id (int): The ID of the product
        """
        try:
            product = ProductModel.get(ProductModel.id == product_id)
            product.delete_instance()
            return {"message": "Product deleted successfully"}
        except DoesNotExist:
            return {"error": "Product not found"}

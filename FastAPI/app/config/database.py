"""
This module configures the MySQL database connection and defines
the Peewee model for interacting with the 'employees' table.
"""
# pylint: disable=too-few-public-methods
import os
from dotenv import load_dotenv
from peewee import Model, MySQLDatabase, AutoField, CharField, DecimalField, ForeignKeyField

load_dotenv()

database = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        passwd=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT")),
    )

class CategoryModel(Model):
    """
    Defines the CategoryModel class for representing categories in the database.

    Attributes:
        id (AutoField): The auto-incrementing primary key for the category.
        name (CharField): The name of the category with a maximum length of 50 characters.
    """
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    class Meta:
        """
        Metadata for the CategoryModel.

        Attributes:
            database (MySQLDatabase): The database connection to use for this model.
            table_name (str): The name of the table in the database to which this model is mapped.
        """
        database = database
        table_name = "categories"

class ProductModel(Model):
    """
    ProductModel represents the product entity in the database.

    Attributes:
        id (AutoField): Unique identifier for the product, automatically incremented.
        name (CharField): Name of the product with a maximum length of 50 characters.
        price (DecimalField): Price of the product.
        category (ForeignKeyField): Foreign key to the Categoria model, establishing
        a relationship between products and categories.

    Meta:
        database: The database connection to use for this model.
        table_name (str): The name of the table in the database.
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=255)
    price = DecimalField()
    category_id = ForeignKeyField(CategoryModel, backref="products")

    class Meta:
        """
        Meta class for ProductModel.

        Attributes:
        database (Database): The database connection to use for this model.
        table_name (str): The name of the table in the database.
        """

        database = database
        table_name = "products"

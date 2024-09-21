"""
This module sets up the database connection and defines the ORM models for the application.
Classes:
    Categoria(Model): Represents the 'categoria' table in the database.
    ProductoModel(Model): Represents the 'productos' table in the database.
Attributes:
    database (MySQLDatabase): The database connection object.
Usage:
    The module uses environment variables to configure the database connection.
    Ensure that the following environment variables are set:
        - MYSQL_DATABASE: Name of the MySQL database.
        - MYSQL_USER: Username for the MySQL database.
        - MYSQL_PASSWORD: Password for the MySQL database.
        - MYSQL_HOST: Hostname of the MySQL server.
        - MYSQL_PORT: Port number of the MySQL server.
"""
import os
from dotenv import load_dotenv
from peewee import *
load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)

class Categoria(Model):
    id




class ProductoModel(Model):
    """
ProductoModel represents the product entity in the database.

Attributes:
    id (AutoField): Unique identifier for the product, automatically incremented.
    nombre (CharField): Name of the product with a maximum length of 50 characters.
    precio (DecimalField): Price of the product.
    categoria (ForeignKeyField): Foreign key to the Categoria model, establishing
    a relationship between products and categories.

Meta:
    database: The database connection to use for this model.
    table_name (str): The name of the table in the database.
"""
    id = AutoField(primary_key=True)
    nombre = CharField(max_length=50)
    precio = DecimalField()
    categoria = ForeignKeyField(Categoria, backref='productos')
    class Meta:
        """
        Meta class for ProductoModel.

        Attributes:
        database (Database): The database connection to use for this model.
        table_name (str): The name of the table in the database.
        """
        database = database
        table_name = "productos"
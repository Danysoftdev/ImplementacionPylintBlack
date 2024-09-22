# FastAPI/app/routes/producto_route.py
from fastapi import APIRouter, Body

from FastAPI.app.config.database import ProductoModel
from ..services.producto_service import (
    create_producto,
    get_all_productos,
    get_producto,
    update_producto,
    delete_producto
)

producto_route = APIRouter()

# Crear un nuevo producto
@producto_route.post("/productos/")
def create_producto_route(producto: ProductoModel = Body(...)):
    return create_producto(producto)

# Obtener todos los productos
@producto_route.get("/productos/")
def get_all_productos_route():
    return get_all_productos()

# Obtener un producto por ID
@producto_route.get("/productos/{producto_id}")
def get_producto_route(producto_id: int):
    return get_producto(producto_id)

# Actualizar un producto por ID
@producto_route.put("/productos/{producto_id}")
def update_producto_route(producto_id: int, producto_data: dict):
    return update_producto(producto_id, producto_data)

# Eliminar un producto por ID
@producto_route.delete("/productos/{producto_id}")
def delete_producto_route(producto_id: int):
    return delete_producto(producto_id)

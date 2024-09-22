""" Main module of the FastAPI application """
from contextlib import asynccontextmanager
from starlette.responses import RedirectResponse
from fastapi import FastAPI, Depends
from helpers.api_key_auth import get_api_key
from config.database import database as connection
from routes.category_route import category_route
from routes.product_route import product_route


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Context manager to manage the lifespan of the application
    
    Parameters:
    app (FastAPI): The FastAPI application
    """
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar la conexión cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

@app.get("/", include_in_schema=False)
def read_root():
    """
    Redirect to the API documentation
    
    Returns:
    RedirectResponse: A redirect response to the API documentation
    """
    return RedirectResponse(url="/docs")


app.include_router(category_route, prefix="/api", tags=["categories"],
                   dependencies=[Depends(get_api_key)])
app.include_router(product_route, prefix="/api", tags=["products"],
                   dependencies=[Depends(get_api_key)])

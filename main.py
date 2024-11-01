from fastapi import FastAPI
from router import product, category, supplier, order, client, sale

app = FastAPI()

app.include_router(product.router, prefix="/api/products", tags=["products"])
app.include_router(category.router, prefix="/api/categories", tags=["categories"])
app.include_router(supplier.router, prefix="/api/suppliers", tags=["suppliers"])
app.include_router(order.router, prefix="/api/orders", tags=["orders"])
app.include_router(client.router, prefix="/api/clients", tags=["clients"])
app.include_router(sale.router, prefix="/api/sales", tags=["sales"])

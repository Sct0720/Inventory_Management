from pydantic import BaseModel
from typing import Optional
from datetime import date

class Product(BaseModel):
    id_product: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    quantity: int
    id_category: int
    id_supplier: int

    class Config:
        orm_mode = True

class Category(BaseModel):
    id_category: Optional[int] = None
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

class Supplier(BaseModel):
    id_supplier: Optional[int] = None
    name: str
    email: str
    phone: str

    class Config:
        orm_mode = True

class Order(BaseModel):
    id_order: Optional[int] = None
    date: date
    id_supplier: int

    class Config:
        orm_mode = True

class Client(BaseModel):
    id_client: Optional[int] = None
    name: str
    phone: str
    email: str
    address: Optional[str] = None

    class Config:
        orm_mode = True

class Sale(BaseModel):
    id_sale: Optional[int] = None
    sale_date: date
    id_client: int
    total_amount: float

    class Config:
        orm_mode = True

class SaleProduct(BaseModel):
    id_sale_product: Optional[int] = None
    id_sale: int
    id_product: int
    quantity: int
    price: float

    class Config:
        orm_mode = True

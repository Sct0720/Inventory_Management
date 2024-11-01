from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    id_category: int
    id_supplier: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id_product: int
    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str
    description: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id_category: int
    class Config:
        orm_mode = True


class SupplierBase(BaseModel):
    name: str
    email: str
    phone: str

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id_supplier: int
    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    date: date
    id_supplier: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id_order: int
    class Config:
        orm_mode = True


class OrderProductBase(BaseModel):
    id_order: int
    id_product: int
    quantity: int
    price: float

class OrderProductCreate(OrderProductBase):
    pass

class OrderProduct(OrderProductBase):
    id_order_product: int
    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    name: str
    phone: str
    email: str
    address: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id_client: int
    class Config:
        orm_mode = True


class SaleBase(BaseModel):
    sale_date: date
    id_client: int
    total_amount: float

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id_sale: int
    class Config:
        orm_mode = True


class SaleProductBase(BaseModel):
    id_sale: int
    id_product: int
    quantity: int
    price: float

class SaleProductCreate(SaleProductBase):
    pass

class SaleProduct(SaleProductBase):
    id_sale_product: int
    class Config:
        orm_mode = True

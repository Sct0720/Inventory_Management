from fastapi import APIRouter, Depends, HTTPException
from database import get_db_connection
from schema import Product
from mysql.connector import MySQLConnection

router = APIRouter()

@router.post("/", response_model=Product)
def create_product(product: Product, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "INSERT INTO products (name, description, price, quantity, id_category, id_supplier) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (product.name, product.description, product.price, product.quantity, product.id_category, product.id_supplier)
    cursor.execute(query, values)
    db.commit()
    product.id_product = cursor.lastrowid
    cursor.close()
    return product

@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM products WHERE id_product = %s"
    cursor.execute(query, (product_id,))
    result = cursor.fetchone()
    cursor.close()
    if result is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return Product(**result)

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "UPDATE products SET name = %s, description = %s, price = %s, quantity = %s, id_category = %s, id_supplier = %s WHERE id_product = %s"
    values = (product.name, product.description, product.price, product.quantity, product.id_category, product.id_supplier, product_id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return product

@router.delete("/{product_id}", response_model=Product)
def delete_product(product_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "DELETE FROM products WHERE id_product = %s"
    cursor.execute(query, (product_id,))
    db.commit()
    cursor.close()
    return {"detail": "Product deleted successfully"}


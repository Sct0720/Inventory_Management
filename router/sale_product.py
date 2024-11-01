from fastapi import APIRouter, Depends, HTTPException
from database import get_db_connection
from schema import SaleProduct
from mysql.connector import MySQLConnection

router = APIRouter()

@router.post("/", response_model=SaleProduct)
def create_sale_product(sale_product: SaleProduct, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "INSERT INTO sale_products (id_sale, id_product, quantity, price) VALUES (%s, %s, %s, %s)"
    values = (sale_product.id_sale, sale_product.id_product, sale_product.quantity, sale_product.price)
    cursor.execute(query, values)
    db.commit()
    sale_product.id_sale_product = cursor.lastrowid
    cursor.close()
    return sale_product

@router.get("/{sale_product_id}", response_model=SaleProduct)
def read_sale_product(sale_product_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM sale_products WHERE id_sale_product = %s"
    cursor.execute(query, (sale_product_id,))
    result = cursor.fetchone()
    cursor.close()
    if result is None:
        raise HTTPException(status_code=404, detail="SaleProduct not found")
    return SaleProduct(**result)

@router.put("/{sale_product_id}", response_model=SaleProduct)
def update_sale_product(sale_product_id: int, sale_product: SaleProduct, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "UPDATE sale_products SET id_sale = %s, id_product = %s, quantity = %s, price = %s WHERE id_sale_product = %s"
    values = (sale_product.id_sale, sale_product.id_product, sale_product.quantity, sale_product.price, sale_product_id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return sale_product

@router.delete("/{sale_product_id}")
def delete_sale_product(sale_product_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "DELETE FROM sale_products WHERE id_sale_product = %s"
    cursor.execute(query, (sale_product_id,))
    db.commit()
    cursor.close()
    return {"detail": "SaleProduct deleted successfully"}


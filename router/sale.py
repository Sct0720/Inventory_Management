from fastapi import APIRouter, Depends, HTTPException
from database import get_db_connection
from schema import Sale
from mysql.connector import MySQLConnection

router = APIRouter()

@router.post("/", response_model=Sale)
def create_sale(sale: Sale, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "INSERT INTO sales (sale_date, id_client, total_amount) VALUES (%s, %s, %s)"
    values = (sale.sale_date, sale.id_client, sale.total_amount)
    cursor.execute(query, values)
    db.commit()
    sale.id_sale = cursor.lastrowid
    cursor.close()
    return sale

@router.get("/{sale_id}", response_model=Sale)
def read_sale(sale_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM sales WHERE id_sale = %s"
    cursor.execute(query, (sale_id,))
    result = cursor.fetchone()
    cursor.close()
    if result is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return Sale(**result)

@router.put("/{sale_id}", response_model=Sale)
def update_sale(sale_id: int, sale: Sale, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "UPDATE sales SET sale_date = %s, id_client = %s, total_amount = %s WHERE id_sale = %s"
    values = (sale.sale_date, sale.id_client, sale.total_amount, sale_id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return sale

@router.delete("/{sale_id}")
def delete_sale(sale_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "DELETE FROM sales WHERE id_sale = %s"
    cursor.execute(query, (sale_id,))
    db.commit()
    cursor.close()
    return {"detail": "Sale deleted successfully"}

from fastapi import APIRouter, Depends, HTTPException
from database import get_db_connection
from schema import Order
from mysql.connector import MySQLConnection

router = APIRouter()

@router.post("/", response_model=Order)
def create_order(order: Order, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "INSERT INTO orders (date, id_supplier) VALUES (%s, %s)"
    values = (order.date, order.id_supplier)
    cursor.execute(query, values)
    db.commit()
    order.id_order = cursor.lastrowid
    cursor.close()
    return order

@router.get("/{order_id}", response_model=Order)
def read_order(order_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM orders WHERE id_order = %s"
    cursor.execute(query, (order_id,))
    result = cursor.fetchone()
    cursor.close()
    if result is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return Order(**result)

@router.put("/{order_id}", response_model=Order)
def update_order(order_id: int, order: Order, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "UPDATE orders SET date = %s, id_supplier = %s WHERE id_order = %s"
    values = (order.date, order.id_supplier, order_id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return order

@router.delete("/{order_id}")
def delete_order(order_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "DELETE FROM orders WHERE id_order = %s"
    cursor.execute(query, (order_id,))
    db.commit()
    cursor.close()
    return {"detail": "Order deleted successfully"}

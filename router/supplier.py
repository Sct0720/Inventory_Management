from fastapi import APIRouter, Depends, HTTPException
from database import get_db_connection
from schema import Supplier
from mysql.connector import MySQLConnection

router = APIRouter()

@router.post("/", response_model=Supplier)
def create_supplier(supplier: Supplier, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "INSERT INTO suppliers (name, email, phone) VALUES (%s, %s, %s)"
    values = (supplier.name, supplier.email, supplier.phone)
    cursor.execute(query, values)
    db.commit()
    supplier.id_supplier = cursor.lastrowid
    cursor.close()
    return supplier

@router.get("/{supplier_id}", response_model=Supplier)
def read_supplier(supplier_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM suppliers WHERE id_supplier = %s"
    cursor.execute(query, (supplier_id,))
    result = cursor.fetchone()
    cursor.close()
    if result is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return Supplier(**result)

@router.put("/{supplier_id}", response_model=Supplier)
def update_supplier(supplier_id: int, supplier: Supplier, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "UPDATE suppliers SET name = %s, email = %s, phone = %s WHERE id_supplier = %s"
    values = (supplier.name, supplier.email, supplier.phone, supplier_id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return supplier

@router.delete("/{supplier_id}")
def delete_supplier(supplier_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "DELETE FROM suppliers WHERE id_supplier = %s"
    cursor.execute(query, (supplier_id,))
    db.commit()
    cursor.close()
    return {"detail": "Supplier deleted successfully"}

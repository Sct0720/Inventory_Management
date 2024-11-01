from fastapi import APIRouter, Depends, HTTPException
from database import get_db_connection
from schema import Client
from mysql.connector import MySQLConnection

router = APIRouter()

@router.post("/", response_model=Client)
def create_client(client: Client, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "INSERT INTO clients (name, phone, email, address) VALUES (%s, %s, %s, %s)"
    values = (client.name, client.phone, client.email, client.address)
    cursor.execute(query, values)
    db.commit()
    client.id_client = cursor.lastrowid
    cursor.close()
    return client

@router.get("/{client_id}", response_model=Client)
def read_client(client_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM clients WHERE id_client = %s"
    cursor.execute(query, (client_id,))
    result = cursor.fetchone()
    cursor.close()
    if result is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return Client(**result)

@router.put("/{client_id}", response_model=Client)
def update_client(client_id: int, client: Client, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "UPDATE clients SET name = %s, phone = %s, email = %s, address = %s WHERE id_client = %s"
    values = (client.name, client.phone, client.email, client.address, client_id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return client

@router.delete("/{client_id}")
def delete_client(client_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "DELETE FROM clients WHERE id_client = %s"
    cursor.execute(query, (client_id,))
    db.commit()
    cursor.close()
    return {"detail": "Client deleted successfully"}

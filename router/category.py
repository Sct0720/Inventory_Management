from fastapi import APIRouter, Depends, HTTPException
from database import get_db_connection
from schema import Category
from mysql.connector import MySQLConnection

router = APIRouter()

@router.post("/", response_model=Category)
def create_category(category: Category, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "INSERT INTO categories (name, description) VALUES (%s, %s)"
    cursor.execute(query, (category.name, category.description))
    db.commit()
    category.id_category = cursor.lastrowid
    cursor.close()
    return category

@router.get("/{category_id}", response_model=Category)
def read_category(category_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM categories WHERE id_category = %s"
    cursor.execute(query, (category_id,))
    result = cursor.fetchone()
    cursor.close()
    if result is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return Category(**result)

@router.put("/{category_id}", response_model=Category)
def update_category(category_id: int, category: Category, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "UPDATE categories SET name = %s, description = %s WHERE id_category = %s"
    cursor.execute(query, (category.name, category.description, category_id))
    db.commit()
    cursor.close()
    return category

@router.delete("/{category_id}", response_model=Category)
def delete_category(category_id: int, db: MySQLConnection = Depends(get_db_connection)):
    cursor = db.cursor()
    query = "DELETE FROM categories WHERE id_category = %s"
    cursor.execute(query, (category_id,))
    db.commit()
    cursor.close()
    return {"detail": "Category deleted successfully"}

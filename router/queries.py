# routers/queries.py

from fastapi import APIRouter, Depends, HTTPException
from mysql.connector import MySQLConnection, Error
from database import get_db
from queries import QUERIES

router = APIRouter()

@router.get("/inner_join_products_categories")
def inner_join_products_categories(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "inner_join_products_categories")

@router.get("/left_join_products_suppliers")
def left_join_products_suppliers(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "left_join_products_suppliers")

@router.get("/right_join_orders_suppliers")
def right_join_orders_suppliers(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "right_join_orders_suppliers")

@router.get("/cross_join_products_categories")
def cross_join_products_categories(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "cross_join_products_categories")

@router.get("/count_total_products")
def count_total_products(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "count_total_products")

@router.get("/sum_total_sales")
def sum_total_sales(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "sum_total_sales")

@router.get("/average_product_price")
def average_product_price(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "average_product_price")

@router.get("/min_product_price")
def min_product_price(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "min_product_price")

@router.get("/max_product_price")
def max_product_price(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "max_product_price")

@router.get("/group_by_category")
def group_by_category(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "group_by_category")

@router.get("/having_more_than_5_orders")
def having_more_than_5_orders(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "having_more_than_5_orders")

@router.get("/order_by_price")
def order_by_price(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "order_by_price")

@router.get("/distinct_categories")
def distinct_categories(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "distinct_categories")

@router.get("/subquery_above_average_price")
def subquery_above_average_price(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "subquery_above_average_price")

@router.get("/join_with_multiple_conditions")
def join_with_multiple_conditions(db: MySQLConnection = Depends(get_db)):
    return execute_query(db, "join_with_multiple_conditions")

def execute_query(db: MySQLConnection, query_key: str):
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute(QUERIES[query_key])
        result = cursor.fetchall()
        return result
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()

QUERIES = {
    "inner_join_products_categories": """
        SELECT p.name AS product_name, c.name AS category_name
        FROM products p
        INNER JOIN categories c ON p.id_category = c.id_category;
    """,
    "left_join_products_suppliers": """
        SELECT p.name AS product_name, s.name AS supplier_name
        FROM products p
        LEFT JOIN suppliers s ON p.id_supplier = s.id_supplier;
    """,
    "right_join_orders_suppliers": """
        SELECT o.id_order, s.name AS supplier_name
        FROM orders o
        RIGHT JOIN suppliers s ON o.id_supplier = s.id_supplier;
    """,
    "cross_join_products_categories": """
        SELECT p.name AS product_name, c.name AS category_name
        FROM products p
        CROSS JOIN categories c;
    """,
    "count_total_products": """
        SELECT COUNT(*) AS total_products FROM products;
    """,
    "sum_total_sales": """
        SELECT SUM(total_amount) AS total_sales FROM sales;
    """,
    "average_product_price": """
        SELECT AVG(price) AS average_price FROM products;
    """,
    "min_product_price": """
        SELECT MIN(price) AS min_price FROM products;
    """,
    "max_product_price": """
        SELECT MAX(price) AS max_price FROM products;
    """,
    "group_by_category": """
        SELECT c.name AS category_name, COUNT(p.id_product) AS product_count
        FROM categories c
        LEFT JOIN products p ON c.id_category = p.id_category
        GROUP BY c.name;
    """,
    "having_more_than_5_orders": """
        SELECT id_supplier, COUNT(*) AS order_count
        FROM orders
        GROUP BY id_supplier
        HAVING order_count > 5;
    """,
    "order_by_price": """
        SELECT name, price
        FROM products
        ORDER BY price DESC;
    """,
    "distinct_categories": """
        SELECT DISTINCT category_id
        FROM products;
    """,
    "subquery_above_average_price": """
        SELECT name, price
        FROM products
        WHERE price > (SELECT AVG(price) FROM products);
    """,
    "join_with_multiple_conditions": """
        SELECT p.name AS product_name, s.name AS supplier_name
        FROM products p
        JOIN suppliers s ON p.id_supplier = s.id_supplier AND p.price > 100;
    """
}

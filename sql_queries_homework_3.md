--Part 1: WHERE

--Task 1: Find all the clients from the 'USA', who are over 25
SELECT 
	first_name,
    last_name,
    age,
    country
FROM 
	customers
WHERE 
	country = 'USA' AND age > 25;

--Task 2: Print all orders with an amount greater than 1000.

SELECT
    order_id,
    item,
    amount,
    customer_id
FROM
    orders
WHERE
    amount > 1000;

-- Part 2: JOIN

--Task 1: Get a list of orders along with the name of the customer who placed the order.
SELECT
    c.first_name,
    c.last_name,
    o.item,
    o.amount
FROM
    orders o
LEFT JOIN 
    customers c ON o.customer_id = c.customer_id;

--Task 2: Display a list of deliveries with the customer's status and name.
SELECT
    s.status,
    c.first_name,
    c.last_name
FROM 
    customers c
LEFT JOIN 
    shippings s ON c.customer_id = s.customer;

--Part 3: GROUP BY

--Task 1: Calculate the number of customers in each country.
SELECT
    country, 
    COUNT(country) AS count
FROM 
    customers
GROUP BY
    country;

--Task 2: Calculate the total number of orders and the average amount for each product.
SELECT 
    item,
    COUNT(item),
    ROUND(AVG(amount), 2) AS avg_amount
FROM   
    orders
GROUP BY 
    item
ORDER BY
    item;

--Part 4: ORDER BY

--Task 1: Display a list of clients sorted by age in descending order.
SELECT 
    first_name,
    age
FROM 
    customers
ORDER BY
    age DESC;

--Part 5: SUBQUERIES

--Task 1: Find all the customers who have placed an order with the maximum amount.
SELECT
    c.first_name,
    c.last_name,
    o.amount
FROM 
    customers c, orders o
WHERE
    o.amount = (SELECT MAX(amount) FROM orders) 
    AND c.customer_id = o.customer_id;

--Part 6: WINDOW FUNCTIONS

--Task 1: For each order, add a column with the sum of all the orders of this customer (using the window function).
SELECT 
    o.order_id,
    o.customer_id,
    o.item,
    o.amount,
    SUM(o.amount) OVER(PARTITION BY o.customer_id) AS total_by_customer
FROM 
    orders o
ORDER BY 
    o.order_id;

--Part 7 (optional)

/*
    Task: Find customers who:
    1. Have made at least any 2 orders
    2. Hhave at least one delivery with the status 'Delivered'
    For each such customer, specify: 
    1. first name, last name
    2. country of residence
    3. total number of orders
    4. total amount of orders
*/
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name,
    c.country,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM
    customers c
INNER JOIN
    orders o ON c.customer_id = o.customer_id
WHERE
    c.customer_id IN (
        SELECT 
            customer_id
        FROM 
            orders
        GROUP BY 
            customer_id
        HAVING 
            COUNT(order_id) >= 2
    )
    AND c.customer_id IN (
        SELECT 
            o.customer_id
        FROM
            orders o
        INNER JOIN
            shippings s ON s.customer = o.customer_id
        WHERE
            s.status = 'Delivered' 
    )
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.country
ORDER BY    
    full_name;

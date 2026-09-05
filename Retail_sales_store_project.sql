CREATE DATABASE Retail_sales;
USE Retail_sales;
CREATE TABLE customer(
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(50),
    join_date DATE,
    phone VARCHAR(20)
);


CREATE TABLE Employee(
    employee_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    branch VARCHAR(50),
    role VARCHAR(50)
);


CREATE TABLE product(
    product_id INT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    category VARCHAR(50) NOT NULL,
    brand_id INT,
    cost_price DECIMAL(10,2) NOT NULL,
    sell_price DECIMAL(10,2) NOT NULL,
     supplier_id INT,
    stock_qty INT NOT NULL DEFAULT 0,
    CONSTRAINT chk_price CHECK(sell_price >= cost_price),
    
 
warranty_months INT,
weight DECIMAL(6,2),
color VARCHAR(50),
launch_date DATE
);


CREATE TABLE orders(
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    employee_id INT,
    payment_method VARCHAR(10) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL DEFAULT 0,
    order_date DATE NOT NULL DEFAULT GETDATE(),

    FOREIGN KEY(customer_id)
    REFERENCES customer(customer_id),

    FOREIGN KEY(employee_id)
    REFERENCES Employee(employee_id),

    CHECK(payment_method IN ('cash','card','wallet'))
);


CREATE TABLE order_items(
    order_items_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,

    FOREIGN KEY(order_id)
    REFERENCES orders(order_id)
    ON DELETE CASCADE,

    FOREIGN KEY(product_id)
    REFERENCES product(product_id),

    CHECK(quantity > 0)
);
CREATE TABLE brand
(
    brand_id INT  PRIMARY KEY,
    brand_name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    founded_year INT,
    website VARCHAR(200),
    support_email VARCHAR(100),
    phone VARCHAR(20),
    status VARCHAR(20) DEFAULT 'Active'
);
CREATE TABLE supplier
(
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    city VARCHAR(100),
    country VARCHAR(100),
    address VARCHAR(200),
    rating DECIMAL(3,2),
    contract_start DATE,
    status VARCHAR(20) DEFAULT 'Active'
);
CREATE TABLE promotion
(
    promotion_id INT  PRIMARY KEY,
    promotion_name VARCHAR(100),
    promotion_type VARCHAR(50),
    discount_percent DECIMAL(5,2),
    minimum_order DECIMAL(10,2),
    start_date DATE,
    end_date DATE,
    coupon_code VARCHAR(50),
    usage_limit INT,
    status VARCHAR(20)
);
CREATE TABLE returns
(
    return_id INT IDENTITY(1,1) PRIMARY KEY,
    order_items_id INT NOT NULL,
    return_date DATE,
    order_id INT,
    customer_id INT,
    return_reason VARCHAR(200),
    return_status VARCHAR(50),
    refund_amount DECIMAL(10,2),
    approved_by VARCHAR(100),
    notes VARCHAR(300),

    CONSTRAINT FK_returns_orderitems
    FOREIGN KEY(order_items_id)
    REFERENCES order_items(order_items_id),
    FOREIGN KEY(order_id) REFERENCES orders(order_id),

FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);


ALTER TABLE orders
ADD
promotion_id INT,
delivery_status VARCHAR(30),
shipping_cost DECIMAL(10,2),
delivery_date DATE;

ALTER TABLE orders
ADD CONSTRAINT FK_Orders_Promotion
FOREIGN KEY (promotion_id)
REFERENCES promotion(promotion_id);

ALTER TABLE product
ADD CONSTRAINT FK_Product_Brand
FOREIGN KEY (brand_id)
REFERENCES brand(brand_id);

ALTER TABLE product
ADD CONSTRAINT FK_Product_Supplier
FOREIGN KEY (supplier_id)
REFERENCES supplier(supplier_id);



BULK INSERT customer
FROM 'C:\Users\aa\Downloads\Ecommerce_Project\customer_data.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0A',
    TABLOCK
);

BULK INSERT Employee
FROM 'C:\Users\aa\Downloads\Ecommerce_Project\employee_data.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0A',
    TABLOCK
);
BULK INSERT product
FROM 'C:\Users\aa\Downloads\Ecommerce_Project\products_data.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0A',
    TABLOCK
);
BULK INSERT orders
FROM 'C:\Users\aa\Downloads\Ecommerce_Project\orders_data.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0A',
    TABLOCK
);

BULK INSERT order_items
FROM 'C:\Users\aa\Downloads\Ecommerce_Project\order_items_data.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0A',
    TABLOCK
);
BULK INSERT brand
FROM 'C:\Users\aa\Downloads\Ecommerce_Project\brand_data.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0A',
    TABLOCK
);
BULK INSERT promotion 
FROM 'C:\Users\aa\Downloads\Ecommerce_Project\promotion_data.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0A',
    TABLOCK
);
BULK INSERT returns
FROM 'C:\Users\aa\Downloads\Ecommerce_Project\returns_data.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0A',
    TABLOCK
);
BULK INSERT supplier
FROM 'C:\Users\aa\Downloads\Ecommerce_Project\supplier_data.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0A',
    TABLOCK
);
select top(5) p.name,sum(oi.quantity)as total_qty
from product p
left join order_items oi on p.product_id=oi.product_id
group by p.name
order by total_qty desc;


select sum(total_amount) as total_revenue,
month( order_date) as mth
from orders 
where year(order_date)='2026'
group by month( order_date)
order by total_revenue desc;

select top(10) c.name,sum(o.total_amount) as total_revenue
from orders o
join customer c on o.customer_id =c.customer_id
group by c.name
order by total_revenue desc;

select p.category , sum((p.sell_price- p.cost_price)*oi.quantity)as total_profit
from product p
join order_items oi on p.product_id=oi.product_id
group by p.category
order by total_profit desc ;


select category , sum(sell_price- cost_price)as profit
from product
group by  category;


select category , round(((sell_price - cost_price) * 100.0) / sell_price,2)as profit_margin
from product;

select avg(o.total_amount) as avg_amount,o.order_id,c.customer_id
from  orders o
join customer c on c.customer_id=o.customer_id
group by o.order_id,c.customer_id
order by avg_amount desc;

select c.customer_id ,c.name ,max(o.order_date)as last_order
from customer c
join orders o on c.customer_id =o.customer_id
group by c.customer_id ,c.name
having max(o.order_date)<dateadd(month,-3,getdate());



select name , stock_qty from product 
where stock_qty <10;

select  top(1)payment_method ,count(payment_method)as count_pay
from orders
group by payment_method 
order by count_pay desc;


DELETE FROM order_items;
DELETE FROM orders;
DELETE FROM product;

DROP TABLE order_items;
DROP TABLE orders;
DROP TABLE promotion;
DROP TABLE product;
ALTER TABLE orders
DROP CONSTRAINT FK_Orders_Promotion;
DROP TABLE promotion;
sp_help returns;
DELETE FROM returns;
DELETE FROM order_items;
DELETE FROM orders;
DELETE FROM product;
DELETE FROM promotion;
DELETE FROM supplier;
DELETE FROM brand;
DELETE FROM Employee;
DELETE FROM customer;
-- Analysis__
--  Total Sales
SELECT 
    SUM(total_amount) AS total_sales
FROM orders;


-- Total Orders and Average Order Value
SELECT 
    COUNT(*) AS total_orders,
    AVG(total_amount) AS avg_order_value
FROM orders;


-- Monthly Sales
SELECT 
    MONTH(order_date) AS month_number,
    SUM(total_amount) AS total_sales
FROM orders
GROUP BY MONTH(order_date)
ORDER BY month_number;


-- Top 5 Best-Selling Products
SELECT TOP 5
    p.name AS product_name,
    SUM(oi.quantity) AS total_quantity
FROM product p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.name
ORDER BY total_quantity DESC;


-- Sales by Category
SELECT 
    p.category,
    SUM(oi.quantity * oi.unit_price) AS total_sales
FROM product p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY total_sales DESC;


-- Profit by Category
SELECT 
    p.category,
    SUM((p.sell_price - p.cost_price) * oi.quantity) AS total_profit
FROM product p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY total_profit DESC;


-- Profit Margin by Category
SELECT 
    p.category,
    ROUND(
        SUM((p.sell_price - p.cost_price) * oi.quantity) * 100.0
        / SUM(p.sell_price * oi.quantity),
        2
    ) AS profit_margin
FROM product p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY profit_margin DESC;


-- Top 10 Customers
SELECT TOP 10
    c.customer_id,
    c.name,
    SUM(o.total_amount) AS total_spending
FROM customer c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spending DESC;


-- Most Used Payment Method
SELECT 
    payment_method,
    COUNT(*) AS number_of_orders
FROM orders
GROUP BY payment_method
ORDER BY number_of_orders DESC;


-- Low Stock Products
SELECT 
    name AS product_name,
    category,
    stock_qty
FROM product
WHERE stock_qty < 10
ORDER BY stock_qty;


-- Top 10 Products by Profit per Unit
SELECT TOP 10
    name AS product_name,
    category,
    (sell_price - cost_price) AS profit_per_unit
FROM product
ORDER BY profit_per_unit DESC;



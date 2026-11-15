
-- DTS 304: TIMA RETAIL STORE PROJECT
-- Database: tima_retail_db

-- 1. CREATE DATABASE
CREATE DATABASE IF NOT EXISTS tima_retail_db;

USE tima_retail_db;


-- 2. CREATE TABLE
CREATE TABLE IF NOT EXISTS customer_purchases (
    purchase_id INT(11) NOT NULL AUTO_INCREMENT,
    customer_id VARCHAR(10) NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    purchase_date DATE NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    product_category VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    amount DECIMAL(12,2) NOT NULL,

    PRIMARY KEY (purchase_id),
    INDEX idx_customer_id (customer_id),
    INDEX idx_product_category (product_category),
    INDEX idx_purchase_date (purchase_date)
);


-- 3. CHECK TOTAL NUMBER OF RECORDS
SELECT COUNT(*) AS total_records
FROM customer_purchases;


-- 4. VIEW ALL CUSTOMER PURCHASES
SELECT *
FROM customer_purchases;


-- 5. DATE-RANGE QUERY
SELECT *
FROM customer_purchases
WHERE purchase_date BETWEEN '2026-01-01' AND '2026-11-30';


-- 6. CATEGORY QUERY
SELECT *
FROM customer_purchases
WHERE product_category = 'Electronics';


-- 7. VIEW TABLE STRUCTURE
DESCRIBE customer_purchases;


-- 8. VIEW ALL INDEXES
SHOW INDEX FROM customer_purchases;

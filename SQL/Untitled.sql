create database scheme;

USE scheme;

CREATE TABLE Customers1 (
    Cust_ID INTEGER PRIMARY KEY NOT NULL,
    Cust_Name VARCHAR(100),
    Cust_City VARCHAR(100),
    Cust_RoomNo INTEGER,
    CheckIn_Time DATETIME
);

INSERT INTO Customers1 (Cust_ID, Cust_Name, Cust_City, Cust_RoomNo, CheckIn_Time)
VALUES
(1, 'John Doe', 'New York', 101, '2024-06-12 14:00:00'),
(2, 'Jane Smith', 'Los Angeles', 102, '2024-06-12 15:00:00'),
(3, 'Alice Johnson', 'Chicago', 103, '2024-06-12 16:00:00'),
(4, 'Bob Brown', 'Houston', 104, '2024-06-12 17:00:00'),
(5, 'Charlie Davis', 'Phoenix', 105, '2024-06-12 18:00:00');

SELECT * FROM Customers1;

SELECT DISTINCT City FROM Customers;

SELECT COUNT(DISTINCT City) AS DistinctCityCount FROM Customers;

SELECT
    MIN(Quantity) AS LeastQuantity,
    MAX(Quantity) AS HighestQuantity
FROM
    order_details;

SELECT
    SUM(Quantity) AS TotalQuantities,
    AVG(Quantity) AS AverageQuantity
FROM
    order_details;
    
SELECT ProductName FROM products ORDER BY ProductID LIMIT 11 OFFSET 4;

SELECT * FROM suppliers WHERE SupplierName LIKE '_A%';

SELECT * FROM customers WHERE Country NOT IN ('USA', 'Canada');

SELECT * FROM orders AS o JOIN order_details AS od ON o.OrderID = od.OrderID WHERE YEAR(o.OrderDate) BETWEEN 2020 AND 2021 ORDER BY od.OrderID DESC;

SELECT City, COUNT(*) AS CustomerCount FROM customers GROUP BY City;

SELECT * FROM employees WHERE FirstName NOT IN ('Sanjay', 'Sonia');

CREATE TABLE supplierDetail AS SELECT * FROM suppliers;

SET SQL_SAFE_UPDATES = 0;
DELETE FROM customers WHERE Country = 'Venezuela';

SELECT * FROM customers;

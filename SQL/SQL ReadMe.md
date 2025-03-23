# SQL Interview Questions and Solutions

## 1. How do you find the second highest salary from an employee table?
```sql
SELECT DISTINCT salary
FROM employee
ORDER BY salary DESC
OFFSET 1 ROWS FETCH NEXT 1 ROW ONLY;
```

## 2. Write a SQL query to fetch the top N highest salaries without using LIMIT or TOP.
```sql
WITH SalaryRank AS (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employee
)
SELECT salary FROM SalaryRank WHERE rnk <= N;
```

## 3. Difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN
- **INNER JOIN**: Returns matching records from both tables.
- **LEFT JOIN**: Returns all records from the left table and matching records from the right.
- **RIGHT JOIN**: Returns all records from the right table and matching records from the left.
- **FULL JOIN**: Returns all records when there is a match in either table.

## 4. How to remove duplicate rows while keeping only one occurrence?
```sql
DELETE FROM employee
WHERE id NOT IN (
    SELECT MIN(id) FROM employee GROUP BY name, salary, department
);
```

## 5. Calculate cumulative sum of transactions per user ordered by date.
```sql
SELECT user_id, transaction_date, amount,
       SUM(amount) OVER (PARTITION BY user_id ORDER BY transaction_date) AS cumulative_sum
FROM transactions;
```

## 6. Difference between GROUP BY and PARTITION BY
- **GROUP BY** aggregates data and returns one row per group.
- **PARTITION BY** does not collapse rows but performs calculations within partitions.

## 7. Moving average of sales for past 7 days per product.
```sql
SELECT product_id, sale_date,
       AVG(sales) OVER (PARTITION BY product_id ORDER BY sale_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg
FROM sales;
```

## 8. Rank transactions per user using ROW_NUMBER(), RANK(), and DENSE_RANK()
```sql
SELECT user_id, transaction_id, amount,
       ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY amount DESC) AS row_num,
       RANK() OVER (PARTITION BY user_id ORDER BY amount DESC) AS rank_num,
       DENSE_RANK() OVER (PARTITION BY user_id ORDER BY amount DESC) AS dense_rank_num
FROM transactions;
```

## 9. Find the first and last transaction date for each user.
```sql
SELECT user_id, MIN(transaction_date) AS first_transaction, MAX(transaction_date) AS last_transaction
FROM transactions
GROUP BY user_id;
```

## 10. Calculate percentage contribution of each transaction to total sales.
```sql
SELECT transaction_id, amount,
       (amount / SUM(amount) OVER ()) * 100 AS percentage_contribution
FROM transactions;
```

## 11. What are CTEs (Common Table Expressions) and when to use them?
- CTEs improve readability and allow reuse within a query.
- Example:
```sql
WITH SalesData AS (
    SELECT user_id, SUM(amount) AS total_sales FROM transactions GROUP BY user_id
)
SELECT * FROM SalesData WHERE total_sales > 1000;
```

## 12. How to optimize a slow SQL query?
- Use proper **indexes**.
- Avoid **SELECT ***.
- Optimize **JOINs**.
- Use **EXPLAIN ANALYZE** to identify bottlenecks.

## 13. What is an index, and how does it impact performance?
- An index speeds up data retrieval but increases write operation overhead.

## 14. Difference between clustered and non-clustered indexes.
- **Clustered Index**: Determines the physical order of rows.
- **Non-clustered Index**: A separate structure pointing to row locations.

## 15. Detect missing or incorrect data in a large dataset.
```sql
SELECT * FROM users WHERE email IS NULL OR phone_number IS NULL;
```

## 16. Identify churned users from a transactions table.
```sql
SELECT user_id FROM transactions WHERE last_transaction_date < NOW() - INTERVAL '30 days';
```

## 17. Find users who made their first transaction in the last 30 days.
```sql
SELECT user_id FROM transactions
WHERE transaction_date = (SELECT MIN(transaction_date) FROM transactions)
AND transaction_date >= NOW() - INTERVAL '30 days';
```

## 18. Find top 3 most frequently purchased items per user.
```sql
SELECT user_id, item_id, COUNT(*) AS purchase_count
FROM purchases
GROUP BY user_id, item_id
ORDER BY user_id, purchase_count DESC
LIMIT 3;
```

## 19. Identify fraudulent transactions based on user behavior.
```sql
SELECT user_id, transaction_id FROM transactions
WHERE amount > (SELECT AVG(amount) FROM transactions) * 3;
```

## 20. Average ride distance per city from a rideshare dataset.

```sql
SELECT city, AVG(distance) AS avg_distance FROM rides GROUP BY city;
```

---

## 21. DEFINE PRIMARY KEY ? 
 ```
 A column (or a set of column ) whose value exists and is unique for every record in a table called a primary key 

 **NOTES** - each table can have one and only one primary key and In one table, you cannot have 3 or 4 primary keys.

 **Primary Key**- may be composed of a set of columns.one-column primary key = all purchases will be recorded under a 
different number

**NOTES ON PRIMARY KEY** -a column (or a set of columns) whose value exists and is unique for 
every record in a table is called a primary key and cannot contain null values

 

 ```

 ## 22. DEFINE FOREIGN KEY ?

 ```
points to a column of another table and, thus, links the two tables.the foreign key maintains the referential integrity within the database.if a specific value from the parent table’s primary key has been 
deleted, all the records from the child table referring to this value 
will be removed as well


```
 **unique key** --> used whenever you would like to specify that you don’t want to see 
duplicate data in a given field

#
**Relationships**
relationships tell you how much of the data from a foreign key field can 
be seen in the primary key column of the table the data is related to 
and vice versa


 ```
```
** WHERE clause** 
it will allow us to set a condition upon which we will specify what part 
of the data we want to retrieve from the database

aggregate functions
they are applied on multiple rows of a single column of a table and 
return an output of a single value
```

```
##
**COUNT()** 

counts the number of non-null records in a field and it is frequently used in combination with the reserved word “DISTINCT”.

**SUM()**

sums all the non-null values in a column

**MIN()**

returns the minimum value from the entire list

**MAX()**

returns the maximum value from the entire list

**AVG()**

calculates the average of all non-null values belonging to a certain 
column of a table

```

```
### GROUP BY--

When working in SQL, results can be grouped according to a specific 
field or fields

---GROUP BY must be placed immediately after the WHERE conditions, if 
any, and just before the ORDER BY clause

in most cases, when you need an aggregate function, you must add a 
GROUP BY clause in your query, too



```


```
### HAVING 

refines the output from records that do not satisfy a certain condition
- frequently implemented with GROUP BY

**SYNTAX** : SELECT column_name(s)
FROM table_name
WHERE conditions
GROUP BY column_name(s)
HAVING conditions
ORDER BY column_name(s);

**after HAVING, you can have a condition with an aggregate function,** 
**while WHERE cannot use aggregate functions within its conditions**

- you cannot have both an aggregated and a non-aggregated condition in 
the HAVING clause

```



```
## COALESCE() Function in SQL

The COALESCE() function in SQL is used to return the first non-null value from a list of expressions. 
It is useful for handling NULL values and ensuring that meaningful default values are returned instead of NULL.

**COALESCE(expression1, expression2, ..., expressionN)*

*Evaluates expressions from left to right.*

*Returns the first non-null expression.*

*If all expressions are NULL, it returns NULL.*

*The COALESCE() function is essential for data handling, ensuring robust and clean query results by replacing NULL values with appropriate alternatives.*


```





This document provides theory explanations along with SQL queries to help in interviews and practical database usage.


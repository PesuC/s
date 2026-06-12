
# ========================================================
# What is DBMS?
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 1 — Database Foundations
# ========================================================

'''
[Definition]
  - DBMS stands for Database Management System
  - It is a software system used to store, retrieve, and sometimes manipulate data
  - It was developed to handle large amounts of data efficiently
  - It acts as an interface between the user/application and the physical database
  - Real-world example: A bank uses DBMS to manage customer account details, employee data, and device records from one place
  - Key benefit: It provides security — end users and programmers can access the same data without compromising its integrity
  - Other benefits include reduced redundancy, data consistency, concurrent access, and easy backup/recovery
[Why DBMS? (Real-World Need)]
  - Consider a bank that maintains customer account details, employee details, and device details
  - All this data needs to be added, deleted, updated, and retrieved from one central place
  - DBMS is software designed exactly for these operations
  - It provides security — end users and programmers can access the same data without compromising its integrity
[Advantages of DBMS]
  - Centralised data storage — all data in one place
  - Reduces data redundancy (duplicate data)
  - Provides data security and access control
  - Supports data integrity — maintains accuracy and consistency
  - Allows concurrent access by multiple users
  - Easy data backup and recovery
'''


# ========================================================
# What is RDBMS?
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 1 — Database Foundations
# ========================================================

'''
[Definition]
  - RDBMS stands for Relational Database Management System
  - It allows you to store, retrieve, and manipulate data in a more efficient way than plain DBMS
  - Data is stored in the form of related tables (rows and columns)
  - Apart from rows and columns, an RDBMS table has these additional components:
 
 Domain — set of valid values for an attribute 
 Instance — data stored at a particular moment in time 
 Schema — logical blueprint/structure of the database 
 Keys — used to uniquely identify records 
 It is more efficient than plain DBMS because it supports relationships between tables 
 Each row = one record/tuple; each column = one attribute of the entity 
 Example: MySQL, Oracle, PostgreSQL, and Microsoft SQL Server are all RDBMS systems
[Structure of Data Storage (Hierarchy)]
  NOTE: Database Server → Databases → Tables (defined by columns) → Rows
[Database Table Explained]
  - A database consists of one or more tables
  - A table is the most significant component in an RDBMS
  - A table makes up of rows & columns
  - Each column represents an attribute of the entity (e.g., last name of a customer)
  - Each row in a table is a record / tuple — all information for one object (e.g., one person or one product)
'''


# ========================================================
# Types of Keys in RDBMS
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 1 — Database Foundations
# ========================================================

'''
[Definition of Key]
  - A key is a data item (column or set of columns) used to uniquely identify a record in a table
  - Used to fetch a single or a set of records from a table
  - Keys also provide constraints — e.g., a unique key constraint avoids duplicate values
  - Primary Key: One candidate key selected to uniquely identify records; cannot be NULL; only one per table
  - Foreign Key: A column in one table that references the Primary Key of another table; links child table to parent table
  - Alternate Key: Candidate keys not selected as Primary Key
  - Unique Key: Uniquely identifies a record but can contain NULL values; multiple unique keys allowed per table
[1. Candidate Key]
  - An attribute or a set of attributes that can uniquely identify a record
  - There can be multiple candidate keys in one table
  - Each candidate key qualifies to be a Primary Key
  - Example: In a customer transaction table — CustomerID + StoreID + LocationID together form a candidate key
[2. Primary Key]
  - Identifies each record uniquely in a table
  - Must never be the same for two records
  - Cannot contain NULL values
  - A table can have only ONE primary key
  - Example: CustomerID in a Customer table
[3. Foreign Key]
  - A column (or set of columns) in one table that points to the Primary Key of another table
  - Used to link two tables together
  - The table containing the foreign key is called the child table
  - The table being referenced is called the parent table / referenced table
  - Prevents orphan records and maintains referential integrity
  - Example: CustomerID in the Orders table points to CustomerID in the Customer table
[4. Alternate Key]
  - A candidate key that is NOT selected as the primary key
  - All candidate keys except the chosen primary key become alternate keys
  - Example: Store Name + Store Location in a Store Information table
[5. Unique Key]
  - An attribute or set of attributes that uniquely identifies a record
  - Similar to primary key but CAN contain NULL values
  - A table can have multiple unique keys but only one primary key
  - Example: Store Name in a Store Information table
'''


# ========================================================
# Domain
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 1 — Database Foundations
# ========================================================

'''
[Definition]
  - A domain is the set of valid values that an attribute can take
  - An attribute will NOT accept any value outside of its domain
  - For example: In a bank customer table, the field account_no will only accept integer values if its domain is set to integer
  - Apart from data type, you can also set constraints on attributes
  - Such a combination of data type + constraints is called Domain Constraints
  - Attributes reject any value outside their domain
'''


# ========================================================
# Schema (Logical vs Physical)
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 1 — Database Foundations
# ========================================================

'''
[Definition]
  - A database schema is a blueprint that represents the logical view of the database
  - It defines tables and the relationships between them
  - A database schema is broadly categorised into two types:
 
 Physical Schema 
 Logical Schema
[Physical Schema]
  - Describes how data is stored in actual physical storage
  - Designed by database administrators
  - Includes actual data types, primary keys, foreign keys, and constraints
  - Represents the actual blueprint of the relational database
[Logical Schema]
  - Designed based on information gathered from business requirements
  - Need not have column types defined — or if defined, it is to assist in business analysis
  - Pertains to logical constraints and design applied to the data stored
  - Does not directly describe how data is physically stored
'''


# ========================================================
# Instance
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 1 — Database Foundations
# ========================================================

'''
[Definition]
  - In RDBMS, lots of changes take place in a table over time — data gets inserted, manipulated, and deleted in parallel
  - The data stored in a database at a particular moment of time is called an instance
  - It keeps changing as records are inserted, updated, or deleted
  - Example: If a customer table has 10,000 records today, the instance is 10,000. After adding 1,000 more records, it becomes 11,000
  - Schema defines the structure; instance defines the current snapshot of data
[Example]
  - The customer table in the bank database has 10,000 records right now → instance = 10,000
  - If we add 1,000 more records tomorrow → instance will be 11,000
  - The schema stays the same; only the instance changes
  NOTE: 💡 Exam Tip: Schema = structure (does not change often). Instance = data at a point in time (changes constantly).
'''


# ### Section 2 — SQL Introduction & Command Categories
# *DDL · DML · DQL · DCL · TCL*


# ========================================================
# SQL Introduction & Command Categories
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 2 — SQL Introduction & Command Categories
# ========================================================

'''
[Definition]
  - SQL stands for Structured Query Language
  - It is the standard language used to communicate with relational databases
  - SQL commands are broadly categorised into five types:
  - DDL — defines/modifies database objects: CREATE, ALTER, DROP, TRUNCATE
  - DML — manipulates data inside tables: INSERT, UPDATE, DELETE
  - DQL — retrieves data from tables: SELECT
  - DCL — controls access permissions: GRANT, REVOKE
  - TCL — manages transactions: COMMIT, ROLLBACK, SAVEPOINT, SET TRANSACTION
[1. DDL — Data Definition Language]
  - Used to define and modify database structure/objects
  - Commands: CREATE , ALTER , DROP , TRUNCATE
[2. DML — Data Manipulation Language]
  - Used to insert, update, or delete data inside tables
  - Commands: INSERT , UPDATE , DELETE
[3. DQL — Data Query Language]
  - Used to query/retrieve data from tables
  - Commands: SELECT
[4. DCL — Data Control Language]
  - Used to control access and permissions
  - Commands: GRANT , REVOKE
[5. TCL — Transactional Control Language]
  - Used to manage transactions in the database
  - Commands: COMMIT , ROLLBACK , SAVEPOINT , SET TRANSACTION
  NOTE: 💡 Note: SQL keywords are case-insensitive (SELECT = select) but are conventionally written in ALL CAPITALS. MySQL has a configuration option to enable or disable case sensitivity.
'''


# ### Section 3 — Data Definition Language (DDL)
# *CREATE · ALTER · DROP · TRUNCATE*


# ========================================================
# DDL Overview
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 3 — Data Definition Language (DDL)
# ========================================================

'''
[Definition]
  - DDL stands for Data Definition Language
  - Any operation that creates, modifies, or deletes database objects is called DDL
  - Used to create a new schema as well as modify an existing schema
  - Databases and tables are referred to as database objects
[DDL Commands]
  - CREATE — creates a new database or table
  - ALTER — modifies an existing table structure
  - DROP — permanently deletes a database or table
  - TRUNCATE — deletes all rows inside a table (structure remains)
'''


# ========================================================
# CREATE DATABASE
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 3 — Data Definition Language (DDL)
# ========================================================

'''
[Definition]
  - The CREATE DATABASE statement is used to create a new SQL database
  - The semicolon character ( ; ) is the SQL statement terminator
  - After creating a database, you must select it before creating tables inside it
  - CREATE DATABASE creates a new SQL database on the server
  - Syntax: CREATE DATABASE databasename;
  - Use SHOW DATABASES; to verify creation
  - Example: CREATE DATABASE company; then USE company;
[Syntax]
[Example]
'''


# Example 1 — CREATE DATABASE
sql = '''
CREATE DATABASE databasename;

-- To select/use the database after creation:
USE databasename;

-- To verify the database was created:
SHOW DATABASES;
'''


# Example 2 — CREATE DATABASE
sql = '''
-- Step 1: Create the database
CREATE DATABASE company;

-- Step 2: Select the database to use it
USE company;

-- Step 3: Verify it was created
SHOW DATABASES;
'''


# ========================================================
# DROP DATABASE
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 3 — Data Definition Language (DDL)
# ========================================================

'''
[Definition]
  - The DROP DATABASE statement is used to permanently delete an existing SQL database
  - This deletes the database along with ALL tables and data inside it
  - Syntax: DROP DATABASE databasename;
  - Example: DROP DATABASE company;
  - Use SHOW DATABASES; to verify the database has been removed
  - Warning: This action is irreversible — all data is permanently lost
[Syntax]
[Example]
  NOTE: ⚠️ Warning: Dropping a database permanently deletes it along with all tables and data. There is NO undo. Use with extreme caution.
'''


# Example 1 — DROP DATABASE
sql = '''
DROP DATABASE databasename;
'''


# Example 2 — DROP DATABASE
sql = '''
-- Drop the company database:
DROP DATABASE company;

-- Verify it is gone:
SHOW DATABASES;
'''


# ========================================================
# MySQL Data Types
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 3 — Data Definition Language (DDL)
# ========================================================

'''
[Definition]
  - When defining columns in a table, you must specify: column name , data type , and optionally a default value
  - Data type tells MySQL what kind of data the column can store
  - Every relational database has its own max/min limits for data types — focus on which data type to use in a specific scenario , not the exact limits
  - MySQL data types are grouped into four categories: Numeric, Floating Point, String, and Date/Time
  - Numeric: BIT, TINYINT, SMALLINT, MEDIUMINT, INT, BIGINT
  - Floating Point: DECIMAL (exact), FLOAT, DOUBLE
  - String: CHAR (fixed), VARCHAR (variable), BLOB, TEXT, ENUM, SET
  - Date/Time: DATE (YYYY-MM-DD), TIME (HH:MI:SS), DATETIME, TIMESTAMP, YEAR
[Category 1: Numeric Types]
  - BIT — stores 0 or 1 (binary)
  - TINYINT — range 0 to 255
  - SMALLINT — range −32,768 to 32,767
  - MEDIUMINT — range −8,388,608 to 8,388,607
  - INT — range −2,147,483,648 to 2,147,483,647 (most commonly used)
  - BIGINT — very large integers (up to ±9.2 × 10¹⁸)
[Category 2: Floating Point / Decimal Types]
  - DECIMAL — exact fixed-point numbers; range −10³⁸+1 to 10³⁸−1; used for financial data
  - FLOAT — approximate floating-point number; range −1.79E+308 to 1.79E+308
  - DOUBLE — double-precision floating point (larger range than FLOAT)
[Category 3: String Types]
  - CHAR — fixed length; maximum 8,000 characters; pads with spaces if shorter
  - VARCHAR — variable length; maximum 8,000 characters; stores only actual characters
  - BINARY — fixed length binary storage; max 8,000 bytes
  - VARBINARY — variable length binary; max 8,000 bytes
  - BLOB — Binary Large Object; for storing large binary data (images, audio)
  - TEXT — variable length; max size 1 GB; for large text data
  - ENUM — stores one value from a predefined list
  - SET — stores zero or more values from a predefined list
[Category 4: Date and Time Types]
  - DATE — format: YYYY-MM-DD
  - TIME — format: HH:MI:SS
  - DATETIME — format: YYYY-MM-DD HH:MI:SS
  - TIMESTAMP — stores number of seconds since Unix epoch ('1970-01-01 00:00:00' UTC)
  - YEAR — stores year; 4-digit format range 1901–2155; 2-digit range 70–69 (1970–2069)
  NOTE: 💡 Instructor Note: You don't need to memorise every limit. Know which data type to use in a specific scenario. For complete details, refer to MySQL documentation: https://dev.mysql.com/doc/refman/8.0/en/data-types.html
'''


# ========================================================
# CREATE TABLE
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 3 — Data Definition Language (DDL)
# ========================================================

'''
[Definition]
  - The CREATE TABLE statement is used to create a new table in a database
  - You must first select the database using USE databasename;
  - Each column must be defined with a name and data type
  - Prerequisites: A database must exist and be selected using USE
  - Syntax: CREATE TABLE table_name (col1 datatype, col2 datatype, ...);
  - Use DESCRIBE tablename; to verify the table structure after creation
[Syntax]
[Example — Create customers table]
'''


# Example 1 — CREATE TABLE
sql = '''
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    ...
);
'''


# Example 2 — CREATE TABLE
sql = '''
-- First select the database
USE company;

-- Create the customers table
CREATE TABLE customers (
    CustomerId   INT,
    first_name   VARCHAR(20),
    last_name    VARCHAR(20),
    country      VARCHAR(20)
);

-- Verify the table structure
DESCRIBE customers;
'''


# ========================================================
# DROP TABLE
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 3 — Data Definition Language (DDL)
# ========================================================

'''
[Definition]
  - The DROP TABLE statement is used to permanently delete an existing table from a database
  - This removes both the table structure AND all data inside it
  - Syntax: DROP TABLE table_name;
  - Example: DROP TABLE customers;
  - Warning: Irreversible — complete loss of table structure and data
[Syntax]
[Example]
  NOTE: ⚠️ Warning: Be careful before dropping a table. Deleting a table will result in loss of ALL information stored in that table. This action is irreversible!
'''


# Example 1 — DROP TABLE
sql = '''
DROP TABLE table_name;
'''


# Example 2 — DROP TABLE
sql = '''
-- Drop the customers table entirely:
DROP TABLE customers;
'''


# ========================================================
# TRUNCATE TABLE
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 3 — Data Definition Language (DDL)
# ========================================================

'''
[Definition]
  - The TRUNCATE TABLE statement is used to delete all data inside a table , but NOT the table structure itself
  - After truncation, the table still exists but is empty
  - TRUNCATE TABLE deletes all rows inside a table but keeps the table structure intact
  - Syntax: TRUNCATE TABLE table_name;
  - Example: TRUNCATE TABLE customers; — table exists but is empty
  - Faster than DELETE for removing all rows because it does not log individual row deletions
[Syntax]
[Example]
'''


# Example 1 — TRUNCATE TABLE
sql = '''
TRUNCATE TABLE table_name;
'''


# Example 2 — TRUNCATE TABLE
sql = '''
-- Remove all rows but keep the table structure:
TRUNCATE TABLE customers;
'''


# ### Section 4 — Data Manipulation Language (DML)
# *INSERT · UPDATE · DELETE*


# ========================================================
# DML Overview
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 4 — Data Manipulation Language (DML)
# ========================================================

'''
[Definition]
  - DML stands for Data Manipulation Language
  - As a data analyst, the majority of your work will focus on insight generation, and you will primarily work with DML commands
  - DML commands: INSERT , UPDATE , DELETE , and SELECT (SELECT is technically DQL but often grouped with DML)
'''


# ========================================================
# INSERT INTO
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 4 — Data Manipulation Language (DML)
# ========================================================

'''
[Definition]
  - The INSERT INTO statement is used to insert new records into a table
  - There are two ways to write an INSERT statement
  - Method 1 (with column names): INSERT INTO table (col1, col2) VALUES (v1, v2);
  - Method 2 (without column names): INSERT INTO table VALUES (v1, v2, ...); — values must be in same order as table columns
  - Multiple rows can be inserted in one query by separating value sets with commas
  - String values must be in single quotes; integer values need no quotes
[Syntax — Method 1: With Column Names (Recommended)]
[Syntax — Method 2: Without Column Names]
[Example — Insert multiple rows]
  NOTE: ⚠️ When using Method 2 (no column names), the order of values MUST exactly match the order of columns as defined in the table.
'''


# Example 1 — INSERT INTO
sql = '''
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
'''


# Example 2 — INSERT INTO
sql = '''
INSERT INTO table_name
VALUES (value1, value2, value3, ...);

-- Note: Order of values MUST match the order of columns in the table!
'''


# Example 3 — INSERT INTO
sql = '''
INSERT INTO customers (CustomerId, first_name, last_name, country)
VALUES
    (1, 'Mike', 'Christensen', 'USA'),
    (2, 'Andy', 'Hollands', 'Australia'),
    (3, 'Ravi', 'Vedantam', 'India');
'''


# ========================================================
# UPDATE
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 4 — Data Manipulation Language (DML)
# ========================================================

'''
[Definition]
  - The UPDATE statement is used to modify existing records in a table
  - Always use with a WHERE clause to specify which records to update
  - Syntax: UPDATE table SET col=val WHERE condition;
  - The WHERE clause is essential — without it, ALL rows are updated
  - Multiple columns can be updated in one statement using comma-separated SET assignments
  - Example: UPDATE customers SET first_name='John' WHERE country='USA';
[Syntax]
[Example]
  NOTE: ⚠️ Critical Warning: If you omit the WHERE clause, ALL records in the table will be updated! Always use WHERE with UPDATE.
'''


# Example 1 — UPDATE
sql = '''
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
'''


# Example 2 — UPDATE
sql = '''
-- Update first_name and last_name for the customer from USA
UPDATE customers
SET first_name = 'John', last_name = 'Kent'
WHERE country = 'USA';
'''


# ========================================================
# DELETE
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 4 — Data Manipulation Language (DML)
# ========================================================

'''
[Definition]
  - The DELETE statement is used to delete existing records from a table
  - Always use a WHERE clause to specify which records to delete
  - Syntax: DELETE FROM table_name WHERE condition;
  - The WHERE clause is critical — omitting it deletes ALL rows
  - DELETE is a DML command — it can be rolled back in a transaction (unlike TRUNCATE)
  - Example: DELETE FROM customers WHERE first_name='John';
[Syntax]
[Example]
  NOTE: ⚠️ Critical Warning: If you omit the WHERE clause, ALL records in the table will be deleted! Always verify your WHERE condition before running DELETE.
'''


# Example 1 — DELETE
sql = '''
DELETE FROM table_name WHERE condition;
'''


# Example 2 — DELETE
sql = '''
-- Delete the row where first_name is 'John'
DELETE FROM customers WHERE first_name = 'John';
'''


# ### Section 5 — Data Query Language (DQL)
# *SELECT · WHERE · Operators · Compound Conditions · NULL Handling*


# ========================================================
# SELECT Statement
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 5 — Data Query Language (DQL)
# ========================================================

'''
[Definition]
  - The SELECT statement is used to retrieve data from a table
  - The data returned is stored in a result table called the result-set
  - It is the most frequently used SQL command
  - To select specific columns: SELECT col1, col2 FROM table_name;
  - To select all columns: SELECT * FROM table_name;
  - The asterisk (*) is a wildcard that represents all columns
  - Example: SELECT first_name, country FROM customers; — returns only those two columns
[Syntax — Select specific columns]
[Syntax — Select all columns]
[Example 1 — Select specific columns]
[Output of Example 1]
  - Returns only two columns: first_name and country
  - Rows: Mike / USA, Andy / Australia, Rahul / India, Jeevan / India
[Example 2 — Select all columns]
[Output of Example 2]
  - Returns all four columns: CustomerID, first_name, last_name, country
  - All rows in the table are returned
  NOTE: 💡 Best Practice: Use SELECT * only for exploration. In production, always list specific column names to improve performance and clarity.
'''


# Example 1 — SELECT Statement
sql = '''
SELECT column1, column2, ... FROM table_name;
'''


# Example 2 — SELECT Statement
sql = '''
SELECT * FROM table_name;
'''


# Example 3 — SELECT Statement
sql = '''
-- Retrieve only first_name and country from customers table
SELECT first_name, country FROM customers;
'''


# Example 4 — SELECT Statement
sql = '''
-- Retrieve all columns from customers table
SELECT * FROM customers;
'''


# ========================================================
# WHERE Clause
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 5 — Data Query Language (DQL)
# ========================================================

'''
[Definition]
  - The WHERE clause is used to filter records
  - It extracts only those records that fulfill a specified condition
  - WHERE is not only used in SELECT — it is also used in UPDATE and DELETE
  - Syntax: SELECT columns FROM table WHERE condition;
  - Example: SELECT * FROM customers WHERE country='India'; — returns only Indian customers
[Syntax]
[Example]
'''


# Example 1 — WHERE Clause
sql = '''
SELECT column1, column2, ...
FROM table_name
WHERE condition;
'''


# Example 2 — WHERE Clause
sql = '''
-- Select all customers from India
SELECT * FROM customers WHERE country = 'India';
'''


# ========================================================
# Operators in the WHERE Clause
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 5 — Data Query Language (DQL)
# ========================================================

'''
[Definition]
  - Operators are special keywords/symbols used to form conditions in the WHERE clause
  - WHERE clause supports multiple operators: =, >, <, >=, <=, <> (comparison)
  - BETWEEN : filters within a range — WHERE id BETWEEN 1 AND 5
  - LIKE : pattern search — WHERE name LIKE 'A%' (names starting with A)
  - IN : multiple values — WHERE country IN ('India','USA')
  - <> means "not equal to"; can also be written as != in MySQL
[Comparison Operators]
  - = — Equal to
  - > — Greater than
  - < — Less than
  - >= — Greater than or equal to
  - <= — Less than or equal to
  - <> — Not equal to (also written as != in some SQL versions)
[Special Operators]
  - BETWEEN — filters records within a certain range (inclusive)
  - LIKE — searches for a pattern (used with wildcards)
  - IN — specifies multiple possible values for a column
  - IS NULL — checks if a field is null/missing
  - IS NOT NULL — checks if a field has a value
[Examples of Each Operator]
  NOTE: 💡 Note from instructor: SQL keywords (SELECT, FROM, WHERE, etc.) are case-insensitive by default but conventionally written in ALL CAPITALS. MySQL has a configuration option to enable or disable case sensitivity for identifiers.
'''


# Example 1 — Operators in the WHERE Clause
sql = '''
-- Equal operator
SELECT * FROM customers WHERE country = 'India';

-- Not equal operator
SELECT * FROM customers WHERE country <> 'India';

-- BETWEEN operator (inclusive range)
SELECT * FROM customers WHERE CustomerId BETWEEN 1 AND 3;

-- LIKE operator (pattern matching)
SELECT * FROM customers WHERE first_name LIKE 'M%';

-- IN operator (multiple values)
SELECT * FROM customers WHERE country IN ('India', 'USA');
'''


# ========================================================
# Compound Search Conditions (AND / OR)
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 5 — Data Query Language (DQL)
# ========================================================

'''
[Definition]
  - Compound conditions are made up of multiple simple conditions connected by AND or OR
  - There is no limit to the number of simple conditions in a single query
  - They enable fine-tuned data retrieval requirements
  - AND requires ALL conditions to be true; OR requires AT LEAST ONE to be true
  - Use parentheses to control evaluation order and avoid logical errors
  - Works with SELECT, UPDATE, and DELETE statements
[Logic]
  - AND — both conditions must be TRUE for the row to be included
  - OR — at least one condition must be TRUE for the row to be included
  - Use parentheses to control the order of evaluation
[Example 1 — AND + OR in SELECT]
[Explanation of Example 1]
  - First condition group: state = 'maharashtra' AND distributor_id ≠ 7000 — both must be true together
  - Second condition: distributor_id = 1000 — independent condition
  - OR connects them — rows satisfying either condition block appear in the result
[Example 2 — AND + OR in UPDATE]
'''


# Example 1 — Compound Search Conditions (AND / OR)
sql = '''
-- Returns distributors from Maharashtra with id != 7000,
-- OR any distributor with id = 1000
SELECT * FROM employeee.distributor
WHERE (state = 'maharashtra' AND distributor_id <> 7000)
   OR (distributor_id = 1000);
'''


# Example 2 — Compound Search Conditions (AND / OR)
sql = '''
-- Update state to Rajasthan for distributors who:
-- have id = 6000, OR have id > 5000 and are NOT in Lucknow
UPDATE employeee.distributor
SET state = 'rajasthan'
WHERE distributor_id = 6000
   OR (distributor_id > 5000 AND city <> 'lucknow');
'''


# ========================================================
# Handling NULL Values (IS NULL / IS NOT NULL)
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 5 — Data Query Language (DQL)
# ========================================================

'''
[Definition]
  - SQL NULL represents a missing or unknown value
  - A NULL value in a table is a field that appears to be blank
  - You cannot use = or ≠ to check for NULL — you MUST use IS NULL or IS NOT NULL
  - You CANNOT use = or <> to compare NULL — always use IS NULL or IS NOT NULL
  - WHERE SALARY IS NOT NULL — returns rows that have a value in SALARY
  - WHERE SALARY IS NULL — returns rows where SALARY is missing/blank
  - Common mistake: WHERE SALARY = NULL — this returns 0 rows and is always wrong
[Sample Data — Employee Table]
[IS NOT NULL — Find employees who HAVE a salary]
[Output]
  - Returns 3 rows: Kellie (2000), Pete (1500), Popy (2000)
  - Sam and Jhon are excluded because their SALARY is NULL
[IS NULL — Find employees with missing salary]
[Output]
  - Returns 2 rows: Sam (Florida, NULL), Jhon (Hawaii, NULL)
  - Their SALARY column is blank/missing
  NOTE: ⚠️ Common Mistake: Never write WHERE SALARY = NULL . This will return 0 rows because NULL cannot be compared with =. Always use IS NULL or IS NOT NULL .
'''


# Example 1 — Handling NULL Values (IS NULL / IS NOT NULL)
sql = '''
-- Create and populate Employee table for examples
CREATE TABLE Employee (
    ID      INT,
    NAME    VARCHAR(50),
    AGE     INT,
    ADDRESS VARCHAR(100),
    SALARY  INT
);

INSERT INTO Employee (ID, NAME, AGE, ADDRESS, SALARY) VALUES
    (1, 'Kellie', 32, 'California', 2000),
    (2, 'Pete',   25, 'Texas',      1500),
    (3, 'Popy',   23, 'Boston',     2000),
    (4, 'Sam',    25, 'Florida',    NULL),
    (5, 'Jhon',   27, 'Hawaii',     NULL);
'''


# Example 2 — Handling NULL Values (IS NULL / IS NOT NULL)
sql = '''
SELECT ID, NAME, AGE, ADDRESS, SALARY
FROM Employee
WHERE SALARY IS NOT NULL;
'''


# Example 3 — Handling NULL Values (IS NULL / IS NOT NULL)
sql = '''
SELECT ID, NAME, AGE, ADDRESS, SALARY
FROM Employee
WHERE SALARY IS NULL;
'''


# ### Section 6 — ALTER, DROP & RENAME Commands
# *CHANGE · MODIFY · ADD · DROP · RENAME*


# ========================================================
# ALTER Command Overview
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 6 — ALTER, DROP & RENAME Commands
# ========================================================

'''
[Definition]
  - The ALTER command is used to make modifications to an already existing table
  - Use cases: renaming a field, changing the data type, adding a column, removing a column
  - ALTER is a DDL command
  - ALTER is commonly used with the following clauses:
 
 CHANGE — rename a column and/or change its definition 
 MODIFY — change data type or constraints (cannot rename) 
 ADD — add a new column or add a constraint 
 DROP — drop a column or drop a constraint 
 Used when we need to rename fields, change data types, add columns, or remove columns from an existing table 
 ALTER does NOT affect the data already stored in the table (unless the column is dropped)
'''


# ========================================================
# ALTER — CHANGE Clause
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 6 — ALTER, DROP & RENAME Commands
# ========================================================

'''
[Definition]
  - The CHANGE clause allows you to:
 
 Change the name of the column 
 Change the column data type 
 Change column constraints 
 Syntax: ALTER TABLE tablename CHANGE old_col new_col datatype; 
 You must always specify the data type even if it is unchanged 
 Example: ALTER TABLE Customer CHANGE Second_name last_name VARCHAR(20); 
 Use DESCRIBE tablename to verify the change
  - You must specify both the old column name AND the new column name
[Syntax]
[Example — Rename column]
'''


# Example 1 — ALTER — CHANGE Clause
sql = '''
ALTER TABLE table_name
CHANGE old_column_name new_column_name datatype;
'''


# Example 2 — ALTER — CHANGE Clause
sql = '''
-- Rename 'Second_name' to 'last_name' and increase character width to 20
ALTER TABLE Customer
CHANGE Second_name last_name VARCHAR(20);

-- Verify the change:
DESCRIBE Customer;
'''


# ========================================================
# ALTER — MODIFY Clause
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 6 — ALTER, DROP & RENAME Commands
# ========================================================

'''
[Definition]
  - The MODIFY clause allows you to:
 
 Modify the column data type 
 Modify column constraints 
 Syntax: ALTER TABLE tablename MODIFY col_name new_datatype constraint; 
 Example: ALTER TABLE Customer MODIFY First_name VARCHAR(25) NOT NULL; 
 Use DESCRIBE tablename to verify the modification
  - MODIFY cannot rename a column — this is the key difference from CHANGE
[Syntax]
[Example — Increase column width and add constraint]
  NOTE: ⚠️ Important: MODIFY clause CANNOT be used to rename a column. Use CHANGE for renaming.
'''


# Example 1 — ALTER — MODIFY Clause
sql = '''
ALTER TABLE table_name
MODIFY current_column_name datatype constraint;
'''


# Example 2 — ALTER — MODIFY Clause
sql = '''
-- Increase First_name width from 10 to 25 and add NOT NULL
ALTER TABLE Customer
MODIFY First_name VARCHAR(25) NOT NULL;

-- Verify:
DESCRIBE Customer;
'''


# ========================================================
# ALTER — ADD Clause
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 6 — ALTER, DROP & RENAME Commands
# ========================================================

'''
[Definition]
  - The ADD clause allows you to:
 
 Add a new column to an existing table 
 Add a Primary Key constraint to an existing column 
 Syntax to add column: ALTER TABLE t ADD COLUMN colname datatype; 
 By default, column is added at the end; use AFTER keyword for specific position 
 Syntax to add Primary Key: ALTER TABLE t ADD PRIMARY KEY(colname); 
 Example position: ALTER TABLE Customer ADD Date_of_Birth DATE AFTER last_name;
  - By default, the ADD clause adds a column at the end of the table
  - Use the AFTER keyword to add a column at a specific position
[Syntax — Add new column]
[Syntax — Add column at specific position]
[Syntax — Add PRIMARY KEY to existing column]
[Example 1 — Add Salary column at end]
[Example 2 — Add Date_of_Birth after last_name]
[Example 3 — Add Primary Key to existing column]
'''


# Example 1 — ALTER — ADD Clause
sql = '''
ALTER TABLE table_name ADD COLUMN column_name datatype;
'''


# Example 2 — ALTER — ADD Clause
sql = '''
ALTER TABLE table_name ADD column_name datatype AFTER existing_column_name;
'''


# Example 3 — ALTER — ADD Clause
sql = '''
ALTER TABLE table_name ADD PRIMARY KEY(column_name);
'''


# Example 4 — ALTER — ADD Clause
sql = '''
-- Add new Salary column at end of Customer table
ALTER TABLE Customer ADD COLUMN Salary INT;

-- Verify:
DESCRIBE Customer;
'''


# Example 5 — ALTER — ADD Clause
sql = '''
-- Add Date_of_Birth column positioned after last_name
ALTER TABLE Customer
ADD Date_of_Birth DATE AFTER last_name;

-- Verify:
DESCRIBE Customer;
'''


# Example 6 — ALTER — ADD Clause
sql = '''
-- Assign customer_id as Primary Key on existing table
ALTER TABLE Customer ADD PRIMARY KEY(customer_id);

-- Verify:
DESCRIBE Customer;
'''


# ========================================================
# ALTER — DROP Clause
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 6 — ALTER, DROP & RENAME Commands
# ========================================================

'''
[Definition]
  - The DROP clause with ALTER allows you to:
 
 Delete a column from the table 
 Remove a constraint from a column (e.g., drop Primary Key) 
 Syntax to drop primary key: ALTER TABLE tablename DROP PRIMARY KEY; 
 No column name needed for DROP PRIMARY KEY since only one PK exists per table
[Syntax — Drop a column]
[Syntax — Drop Primary Key]
[Example 1 — Drop Salary column]
[Example 2 — Drop Primary Key]
  NOTE: 💡 Note: Since there is only ONE Primary Key in a table, you do NOT need to specify the column name when dropping it using ALTER TABLE DROP PRIMARY KEY.
'''


# Example 1 — ALTER — DROP Clause
sql = '''
ALTER TABLE table_name DROP COLUMN column_name;
'''


# Example 2 — ALTER — DROP Clause
sql = '''
ALTER TABLE table_name DROP PRIMARY KEY;
'''


# Example 3 — ALTER — DROP Clause
sql = '''
-- Remove the Salary column from Customer table
ALTER TABLE Customer DROP COLUMN Salary;

-- Verify:
DESCRIBE Customer;
'''


# Example 4 — ALTER — DROP Clause
sql = '''
-- Drop the Primary Key constraint from Customer table
ALTER TABLE Customer DROP PRIMARY KEY;

-- Verify:
DESCRIBE Customer;
'''


# ========================================================
# DROP and RENAME Queries
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 6 — ALTER, DROP & RENAME Commands
# ========================================================

'''
[DROP — Full Summary]
  - DROP allows you to delete a database or a table
  - Syntax to drop a database: DROP DATABASE database_name;
  - Syntax to drop a table: DROP TABLE table_name;
  - Both are irreversible — all data is permanently lost
  - RENAME TABLE changes the name of an existing table without affecting its data
  - Syntax: RENAME TABLE old_name TO new_name;
  - Example: RENAME TABLE Customer TO Customer_info;
  - Use SHOW TABLES to verify the new table name appears
  - All data, columns, and constraints are preserved after rename
[RENAME Command]
  - The RENAME TABLE command is used to change the name of an existing table
  - Renaming a table does NOT cause it to lose any data
  - Only the name changes — all columns and rows remain intact
[Syntax — RENAME TABLE]
[Example]
'''


# Example 1 — DROP and RENAME Queries
sql = '''
RENAME TABLE current_table_name TO new_table_name;
'''


# Example 2 — DROP and RENAME Queries
sql = '''
-- Rename the Customer table to Customer_info
RENAME TABLE Customer TO Customer_info;

-- Verify using SHOW TABLES (check all tables in current database)
SHOW TABLES;
'''


# ### Section 7 — SQL Constraints
# *NOT NULL · UNIQUE · PRIMARY KEY · FOREIGN KEY · CHECK · DEFAULT · INDEX*


# ========================================================
# SQL Constraints Overview
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 7 — SQL Constraints
# ========================================================

'''
[Definition]
  - SQL constraints are rules that enforce data integrity in a table
  - They specify conditions that data must meet to be stored in a column
  - Constraints can be specified:
 
 When the table is created — in the CREATE TABLE statement 
 After creation — using the ALTER TABLE statement 
 They can be added during CREATE TABLE or later through ALTER TABLE 
 7 common constraints: NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK, DEFAULT, INDEX 
 Syntax: CREATE TABLE t (col1 datatype constraint, col2 datatype constraint, ...);
[Syntax — Constraints in CREATE TABLE]
[Common SQL Constraints]
  - NOT NULL — Ensures that a column cannot have a NULL value
  - UNIQUE — Ensures that all values in a column are different
  - PRIMARY KEY — Combination of NOT NULL and UNIQUE; uniquely identifies each row
  - FOREIGN KEY — Uniquely identifies a row/record in another table; maintains referential integrity
  - CHECK — Ensures that all values in a column satisfy a specific condition
  - DEFAULT — Sets a default value for a column when no value is specified
  - INDEX — Used to create and retrieve data from the database very quickly
'''


# Example 1 — SQL Constraints Overview
sql = '''
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    column3 datatype constraint,
    ...
);
'''


# ========================================================
# NOT NULL Constraint
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 7 — SQL Constraints
# ========================================================

'''
[Definition]
  - By default, a column can hold NULL values
  - The NOT NULL constraint enforces a column to NOT accept NULL values
  - This ensures that a field always contains a value
  - You cannot insert a new record or update a record without providing a value for this field
  - By default, columns allow NULL — NOT NULL overrides this
  - Any INSERT or UPDATE that omits this field or sets it to NULL will be rejected
  - Syntax: column_name datatype NOT NULL inside CREATE TABLE
  - Example: first_name VARCHAR(20) NOT NULL
[Syntax — NOT NULL on CREATE TABLE]
'''


# Example 1 — NOT NULL Constraint
sql = '''
CREATE TABLE customers (
    id         INT NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name  VARCHAR(20) NOT NULL,
    country    VARCHAR(20)
);
'''


# ========================================================
# UNIQUE Constraint
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 7 — SQL Constraints
# ========================================================

'''
[Definition]
  - The UNIQUE constraint ensures that all values in a column are different
  - A PRIMARY KEY constraint automatically has a UNIQUE constraint
  - You can have many UNIQUE constraints per table but only one PRIMARY KEY
  - UNIQUE columns can contain NULL values (unlike PRIMARY KEY)
  - Syntax: column_name datatype UNIQUE
[Syntax — UNIQUE on CREATE TABLE]
'''


# Example 1 — UNIQUE Constraint
sql = '''
CREATE TABLE customers (
    id         INT NOT NULL UNIQUE,
    first_name VARCHAR(20) NOT NULL,
    last_name  VARCHAR(20) NOT NULL,
    country    VARCHAR(20)
);
'''


# ========================================================
# PRIMARY KEY Constraint
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 7 — SQL Constraints
# ========================================================

'''
[Definition]
  - The PRIMARY KEY constraint uniquely identifies each record in a table
  - Primary keys must contain UNIQUE values and cannot contain NULL values
  - A table can have only ONE primary key
  - PRIMARY KEY = NOT NULL + UNIQUE combined
  - It combines NOT NULL + UNIQUE — no duplicate values, no NULL values allowed
  - Syntax: PRIMARY KEY (column_name) inside CREATE TABLE
  - Example: CREATE TABLE customers (..., PRIMARY KEY (id));
[Syntax — PRIMARY KEY on CREATE TABLE]
'''


# Example 1 — PRIMARY KEY Constraint
sql = '''
CREATE TABLE customers (
    id         INT NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name  VARCHAR(20) NOT NULL,
    country    VARCHAR(20),
    PRIMARY KEY (id)
);
'''


# ========================================================
# FOREIGN KEY Constraint
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 7 — SQL Constraints
# ========================================================

'''
[Definition]
  - A FOREIGN KEY is used to link two tables together
  - It is a field (or set of fields) in one table that refers to the PRIMARY KEY of another table
  - The table with the foreign key = child table
  - The table being referenced = parent table / referenced table
  - FOREIGN KEY links two tables by referencing the PRIMARY KEY of the parent table
  - Prevents: invalid data in FK column, and deletion of parent records referenced by child
  - Syntax: FOREIGN KEY (col) REFERENCES parent_table(parent_col)
  - Example: Orders.CustomerID references Customer.CustomerID
[What FOREIGN KEY Prevents]
  - Actions that would destroy links between tables (e.g., deleting a parent record that is referenced by a child)
  - Invalid data being inserted into the foreign key column — value must exist in the parent table
[Data Example]
  - Customer table — CustomerID (PK), FirstName, LastName, country
  - Orders table — OrderID (PK), OrderNumber, CustomerID (FK → Customer.CustomerID)
  - CustomerID in Orders points to CustomerID in Customer — linking orders to customers
[Syntax — FOREIGN KEY on CREATE TABLE]
'''


# Example 1 — FOREIGN KEY Constraint
sql = '''
-- First create the parent table
CREATE TABLE Customer (
    CustomerID INT NOT NULL,
    first_name VARCHAR(20),
    last_name  VARCHAR(20),
    country    VARCHAR(20),
    PRIMARY KEY (CustomerID)
);

-- Then create the child table with FOREIGN KEY
CREATE TABLE Orders (
    OrderID      INT NOT NULL,
    OrderNumber  INT NOT NULL,
    CustomerID   INT,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);
'''


# ========================================================
# Adding / Dropping Constraints Using ALTER
# 1 — SQL Foundations, DDL, DML, DQL & Constraints
# SECTION: Section 7 — SQL Constraints
# ========================================================

'''
[Purpose]
  - Sometimes a table is created without constraints and we need to add them later
  - Or we need to remove an existing constraint
  - Both operations use ALTER TABLE
  - Constraints can be added or removed from existing tables using ALTER TABLE
  - To add Primary Key: ALTER TABLE tablename ADD PRIMARY KEY(colname);
  - To drop Primary Key: ALTER TABLE tablename DROP PRIMARY KEY;
  - No column name needed when dropping PK since only one PK exists per table
  - Use DESCRIBE tablename to verify changes
[Add Primary Key to Existing Column]
[Drop Primary Key from Existing Column]
  NOTE: 💡 Since there is only ONE Primary Key per table, you do NOT need to specify the column name when dropping it — MySQL knows which column is the PK.
  NOTE: ⚠️ Instructor note: It is NOT good practice to declare First_name as a Primary Key because names are not unique and cannot guarantee uniqueness across records.
'''


# Example 1 — Adding / Dropping Constraints Using ALTER
sql = '''
ALTER TABLE table_name ADD PRIMARY KEY(column_name);

-- Example:
ALTER TABLE Customer ADD PRIMARY KEY(customer_id);

-- Verify:
DESCRIBE Customer;
'''


# Example 2 — Adding / Dropping Constraints Using ALTER
sql = '''
ALTER TABLE table_name DROP PRIMARY KEY;

-- Example:
ALTER TABLE Customer DROP PRIMARY KEY;

-- Verify:
DESCRIBE Customer;
'''


# ---

# ## Session 2 — WHERE Predicates, Set Ops, Functions & Sorting

# *Predicates · Wildcards · Set Ops · Functions · ORDER BY*


# ### Section 1 — WHERE Clause Predicates
# *Comparison · BETWEEN · IN · IS NULL · LIKE*


# ========================================================
# WHERE Clause Predicates — Overview
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 1 — WHERE Clause Predicates
# ========================================================

'''
[Definition]
  - A WHERE clause predicate is an expression that evaluates to a Boolean value (TRUE or FALSE) to determine which rows are relevant to a query
  - By using predicates in the WHERE clause, we can filter out unwanted rows from the result set
[Types of Predicates Supported]
  - Comparison — = , <> , < , <= , > , >=
  - Pattern Matching — LIKE (used for wildcard filtering)
  - BETWEEN — selects rows within a range of values
  - IN — selects rows matching a set of specified values
  - IS NULL — selects rows where a column contains a NULL value
[Reference Table: tblUser]
  - All predicate examples in this section use the tblUser table
  - Columns: UserID, Name, City, Salary
  - Sample cities: Kolkata, Lucknow, Hyderabad, Bangalore, Jaipur, Mumbai
'''


# ========================================================
# Comparison Predicate
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 1 — WHERE Clause Predicates
# ========================================================

'''
[Definition]
  - Comparison predicates compare a column value against a specified value using standard comparison operators
  - Supported operators: = , <> , < , <= , > , >=
[Example 1 — Greater Than (>)]
[Output Explanation]
  - Returns only rows where Salary column value is strictly greater than 50,000
  - Returns three columns: UserID, Name, and Salary (not all columns)
[Example 2 — Equal (=)]
[Output Explanation]
  - Returns all columns for rows where city is exactly Kolkata
  - String values in WHERE conditions are enclosed in single quotes
'''


# Example 1 — Comparison Predicate
sql = '''
-- Retrieve UserID, Name and Salary of users where salary > 50000
SELECT UserID, Name, Salary
FROM tblUser
WHERE Salary > 50000;
'''


# Example 2 — Comparison Predicate
sql = '''
-- Retrieve all users who belong to Kolkata
SELECT * FROM tblUser WHERE city = 'Kolkata';
'''


# ========================================================
# BETWEEN Predicate
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 1 — WHERE Clause Predicates
# ========================================================

'''
[Definition]
  - The BETWEEN predicate is used to select rows within a specified range of values
  - The range is inclusive — both the start and end values are included in the result
  - Can be used on numeric, date, and even text columns
[Syntax]
[Example]
'''


# Example 1 — BETWEEN Predicate
sql = '''
SELECT column_list FROM table_name
WHERE column_name BETWEEN value1 AND value2;
'''


# Example 2 — BETWEEN Predicate
sql = '''
-- Display users whose UserID is between 33 and 36 (inclusive)
SELECT UserID, Name
FROM tblUser
WHERE UserID BETWEEN 33 AND 36;
'''


# ========================================================
# IN Predicate
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 1 — WHERE Clause Predicates
# ========================================================

'''
[Definition]
  - The IN predicate is used to select rows where a column matches any value in a specified set
  - It is a shorthand for multiple OR conditions
  - Works with both numeric and string values
[Syntax]
[Example]
'''


# Example 1 — IN Predicate
sql = '''
SELECT column_list FROM table_name
WHERE column_name IN (value1, value2, value3, ...);
'''


# Example 2 — IN Predicate
sql = '''
-- Display users whose UserID is 4, 22, or 36
SELECT UserID, Name
FROM tblUser
WHERE UserID IN (4, 22, 36);
'''


# ========================================================
# IS NULL Predicate
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 1 — WHERE Clause Predicates
# ========================================================

'''
[Definition]
  - IS NULL is used to select rows where a specified column contains a NULL value
  - NULL represents a missing or unknown value — it cannot be compared using = or <>
  - You must always use IS NULL or IS NOT NULL to check for null
[Example]
  NOTE: ⚠️ Common Mistake: Writing WHERE City = NULL — this always returns 0 rows. Always use IS NULL .
'''


# Example 1 — IS NULL Predicate
sql = '''
-- Select all users where City is NULL (missing)
SELECT * FROM tblUser WHERE City IS NULL;
'''


# ### Section 2 — Wildcard Filtering
# *LIKE · % · _ · NOT LIKE · ESCAPE*


# ========================================================
# Wildcards — Overview
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 2 — Wildcard Filtering
# ========================================================

'''
[Definition]
  - Wildcard filtering is a method for comparing and displaying text in a column against a search pattern
  - Wildcards are characters used to filter/search data from a database on the basis of certain patterns
  - They are used with the operators LIKE and NOT LIKE in conjunction with the WHERE clause
[Why Use Wildcard Filtering?]
  - You do not know the exact spelling of someone's last name but know the starting letter
  - You do not know the name of a song but know some lyrics
  - You want to search a product based on its description when you don't remember the product name
  - Using wildcards in MySQL can increase application performance and reduce record-filtering time
  - Complex SQL queries can be converted into simpler ones using wildcards
  - Essential for building powerful search engines in large data-driven applications
[Types of Wildcards]
  - % — Percent: matches any string of zero or more characters
  - _ — Underscore: matches exactly one character
  - [] — Square brackets: matches any one character within the brackets
  - - — Hyphen inside brackets: indicates a range of characters e.g. [a-c]
  - ^ — Caret inside brackets: matches all characters except those in the brackets e.g. [^xyz]
  - # — Hash: matches a single numeric character
  NOTE: 💡 In MySQL, the most commonly used wildcards are % and _ . The [] , ^ , and # wildcards are primarily used in SQL Server / MS Access.
[Dataset Used for Wildcard Examples]
  - All wildcard examples use the MovieLens dataset (movies table)
  - Table: MOVIES — columns: movieId , title , genres
  - To load the dataset:
 
 Download from: http://files.grouplens.org/datasets/movielens/ml-latest.zip 
 Run: SHOW VARIABLES LIKE "secure_file_priv"; — copy movies.csv to that folder
[Create and Load the MOVIES Table]
'''


# Example 1 — Wildcards — Overview
sql = '''
-- Step 1: Create the table
CREATE TABLE MOVIES (
    movieId INT,
    title   VARCHAR(200),
    genres  VARCHAR(200)
);

-- Step 2: Load data from CSV file
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/movies.csv'
INTO TABLE MOVIES
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Step 3: Verify the data loaded correctly
SELECT * FROM MOVIES LIMIT 10;
'''


# ========================================================
# % (Percent) Wildcard
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 2 — Wildcard Filtering
# ========================================================

'''
[Definition]
  - The % wildcard is used to match any string of zero or more characters
  - Used with the LIKE operator in the WHERE clause
[Syntax]
[Placement Rules]
  - End position — 'xxx%' : rows where the column starts with 'xxx' followed by zero or more characters
  - Start position — '%xxx' : rows where the column ends with 'xxx' preceded by zero or more characters
  - Both ends — '%xxx%' : rows where the column contains 'xxx' anywhere in the string
[Example 1 — Starts With (Scenario: Forgotten movie name)]
  - Returns all movies whose title begins with the string 'eternal'
  - Followed by zero or more occurrences of any character
  - Helps recall: "Eternal Sunshine of the Spotless Mind" would appear in results
  - The LIKE comparison is case-insensitive by default in MySQL
[Example 2 — Contains String (Scenario: All Harry Potter movies)]
  - Returns all titles containing 'harry potter' at any position
  - Reveals non-book movies too — e.g., 'The Greater Good - Harry Potter Fan Film'
  - % at both ends = contains search
[Example 3 — Multiple Conditions with % (Scenario: Film-noir movies from 1990)]
  - Combines two LIKE conditions with AND
  - No year column exists in the table — year is embedded in the title string
  - Shows that wildcards can be used on multiple columns in the same query
'''


# Example 1 — % (Percent) Wildcard
sql = '''
SELECT statement... WHERE column_name LIKE 'xxx%';
'''


# Example 2 — % (Percent) Wildcard
sql = '''
-- You remember the movie starts with "Eternal"
-- Use % at the end to match everything after "eternal"
SELECT * FROM movies
WHERE title LIKE 'eternal%';
'''


# Example 3 — % (Percent) Wildcard
sql = '''
-- Find all movies with "harry potter" anywhere in the title
-- % on both sides matches any characters before AND after
SELECT * FROM movies
WHERE title LIKE '%harry potter%';
'''


# Example 4 — % (Percent) Wildcard
sql = '''
-- Find film-noir movies from 1990
-- genres contains 'film-noir' AND title contains '1990'
SELECT * FROM movies
WHERE genres LIKE '%film-noir%'
AND title LIKE '%1990%';
'''


# ========================================================
# _ (Underscore) Wildcard
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 2 — Wildcard Filtering
# ========================================================

'''
[Definition]
  - The underscore _ wildcard matches exactly one character
  - Unlike % which matches zero or more characters, _ matches precisely one
  - You can use multiple underscore characters to match multiple characters — e.g., ___ matches exactly 3 characters
[Syntax]
[Placement Rules]
  - End position — 'xxx_' : rows where string starts with 'xxx' followed by exactly one character
  - Start position — '_xxx' : rows where string starts with any single character then ends with 'xxx'
  - Both ends — '_xxx_' : rows where 'xxx' is surrounded by exactly one character on each side
  - Multiple underscores — '__' matches exactly 2 characters, '___' matches exactly 3, and so on
[Example — Pure genre movies from 2010]
  - 'children_' — matches genres that start with 'children' and have exactly one more character
  - Cross-genre movies like 'Children|Animation' have more than one extra character and are excluded
  - This is how _ helps filter pure single-genre movies vs blended/cross-genre movies
  NOTE: 💡 Most movies in the MovieLens dataset are cross-genre (blended genres) — the underscore wildcard is useful to isolate pure single-genre entries.
'''


# Example 1 — _ (Underscore) Wildcard
sql = '''
SELECT statement... WHERE column_name LIKE 'xxx_';
'''


# Example 2 — _ (Underscore) Wildcard
sql = '''
-- Find Children-only genre movies from 2010
-- "children_" matches 'children' followed by exactly one character
-- This filters out cross-genre movies like "Children|Animation"
SELECT * FROM movies
WHERE genres LIKE 'children_'
AND title LIKE '%2010%';
'''


# ========================================================
# NOT Logical Operator with Wildcards
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 2 — Wildcard Filtering
# ========================================================

'''
[Definition]
  - The NOT logical operator can be used together with wildcards to return rows that do NOT match the specified pattern
  - Syntax: WHERE column NOT LIKE 'pattern'
  - You can combine multiple wildcards ( % and _ together) in the same pattern
[Example — Movies NOT from the 1900s]
'''


# Example 1 — NOT Logical Operator with Wildcards
sql = '''
-- Retrieve movies NOT released in the 1900s
-- '%19__%' matches titles containing '19' followed by exactly 2 more digits (1900-1999)
-- NOT LIKE excludes all such titles
SELECT * FROM movies
WHERE title NOT LIKE '%19__%';
'''


# ========================================================
# ESCAPE Operator
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 2 — Wildcard Filtering
# ========================================================

'''
[Definition]
  - The ESCAPE keyword is used to treat pattern matching characters (% and _) as literal string characters rather than wildcards
  - Required when the data itself contains % or _ characters
  - Example scenario: a movie title like "100% Love" contains a % in the title — without ESCAPE, MySQL would treat that % as a wildcard
[Syntax]
[Example — Search for titles containing the % character]
[Wildcard Summary]
  - The LIKE predicate & WILDCARDS are powerful tools for searching data matching complex patterns
  - % — matches any number of characters (zero or more)
  - _ — matches exactly one character
  - NOT LIKE — returns rows that do not match the pattern
  - ESCAPE — treats % or _ as literal characters when they appear in data
'''


# Example 1 — ESCAPE Operator
sql = '''
SELECT * FROM table_name
WHERE column_name LIKE 'pattern' ESCAPE 'escape_char';
'''


# Example 2 — ESCAPE Operator
sql = '''
-- Find movies whose title contains the literal '%' character
-- '#' is declared as the escape character
-- '#%' means: treat the % that follows as a literal character, not a wildcard
SELECT * FROM movies
WHERE title LIKE '%#%%' ESCAPE '#';
'''


# ### Section 3 — Set Operations
# *UNION · UNION ALL · INTERSECT · MINUS*


# ========================================================
# Set Operations — Overview
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 3 — Set Operations
# ========================================================

'''
[Definition]
  - Set operators are used to join the results of two or more SELECT statements into a single result set
  - All SELECT statements involved must have the same number of columns and compatible data types
  - Types of SET operations: UNION , UNION ALL , INTERSECT , MINUS
  NOTE: ⚠️ MySQL natively supports only UNION and UNION ALL . INTERSECT and MINUS are NOT supported in MySQL — they must be emulated using JOINs (covered in later sessions).
'''


# ========================================================
# UNION
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 3 — Set Operations
# ========================================================

'''
[Definition]
  - The UNION operator combines the results of two or more SELECT statements into a single result set
  - Removes duplicate rows — each row appears only once in the final result, even if both queries return the same row
  - Works like the Union operation in Set theory — duplicates appear only once
[Rules for UNION]
  - Both SELECT statements must have the same number of columns
  - Column names from the first SELECT statement are used as column names for the result set
  - Corresponding columns must have compatible data types
[Syntax]
[Example — Users from Kolkata OR salary ≥ 50,000]
'''


# Example 1 — UNION
sql = '''
SELECT col1, col2, col3 FROM table1 [WHERE conditions]
UNION
SELECT col1, col2, col3 FROM table2 [WHERE conditions];
'''


# Example 2 — UNION
sql = '''
-- Find all users in Kolkata UNION all users with salary >= 50000
-- Duplicates (users in both groups) will appear only ONCE
SELECT UserID, Name, City, Salary FROM tblUser WHERE City = 'Kolkata'
UNION
SELECT UserID, Name, City, Salary FROM tblUser WHERE Salary >= 50000;
'''


# ========================================================
# UNION ALL
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 3 — Set Operations
# ========================================================

'''
[Definition]
  - The UNION ALL operator combines results of two or more SELECT statements into a single result set
  - Does NOT remove duplicate rows — all rows from both queries appear in the result, including duplicates
  - Faster than UNION because no deduplication step is performed
[Syntax]
[Example — Same query as above using UNION ALL]
'''


# Example 1 — UNION ALL
sql = '''
SELECT col1, col2, col3 FROM table1 [WHERE conditions]
UNION ALL
SELECT col1, col2, col3 FROM table2 [WHERE conditions];
'''


# Example 2 — UNION ALL
sql = '''
-- Same query as UNION example but using UNION ALL
-- UserID 22 will now appear TWICE in the result
SELECT UserID, Name, City, Salary FROM tblUser WHERE City = 'Kolkata'
UNION ALL
SELECT UserID, Name, City, Salary FROM tblUser WHERE Salary >= 50000;
'''


# ========================================================
# INTERSECT
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 3 — Set Operations
# ========================================================

'''
[Definition]
  - The INTERSECT operation combines two SELECT statements and returns only the rows that are common to both result sets
  - Operates like the Intersection operation in Set theory — only common elements appear
  - In the tblUser example: running Kolkata query INTERSECT salary ≥ 50,000 query returns only UserID 22 — the only row present in both sets
  NOTE: ⚠️ MySQL does NOT support the INTERSECT operator. You can emulate INTERSECT using INNER JOINs. This will be covered in upcoming sessions on JOINs.
'''


# ========================================================
# MINUS
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 3 — Set Operations
# ========================================================

'''
[Definition]
  - The MINUS operation combines results of two SELECT statements and returns only the rows from the first result set that do NOT appear in the second
  - Operates like Set Difference (A − B) in Set theory
  NOTE: ⚠️ MySQL does NOT support the MINUS operator. You can emulate MINUS using LEFT JOIN with a NULL check. This will be covered in upcoming sessions on JOINs.
'''


# ### Section 4 — Duplicate Rows & DISTINCT
# *Identifying and eliminating duplicate records*


# ========================================================
# Duplicate Rows & DISTINCT Keyword
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 4 — Duplicate Rows & DISTINCT
# ========================================================

'''
[What are Duplicate Rows?]
  - Duplicate rows (or duplicate records) are identical rows in a table
  - It is NOT desired for a relation or table to have duplicate records
  - Constraints like Primary Key, Candidate Key, and Unique Key can prevent duplicates during database design
  - However, unavoidable situations exist — e.g., when a staging table is used and data is loaded from different sources, duplicates can occur
[DISTINCT Keyword]
  - The DISTINCT keyword in the SELECT statement eliminates duplicate rows and displays a unique list of values
[Syntax]
[Example]
[Notes on the Store Table Context]
  - The ItemID column is an auto-generated primary key — its values are generated automatically in sequential incremental fashion
  - Because ItemID is auto-generated and always unique, duplicates can exist in the other columns (supplied from external sources)
  - DISTINCT removes rows where all column values are identical
'''


# Example 1 — Duplicate Rows & DISTINCT Keyword
sql = '''
SELECT DISTINCT column_list FROM table_name;
'''


# Example 2 — Duplicate Rows & DISTINCT Keyword
sql = '''
-- Get all unique rows from the Store table
-- Eliminates any exact duplicate rows from the result
SELECT DISTINCT * FROM Store;
'''


# ### Section 5 — Operator Precedence
# *Understanding evaluation order to write correct queries*


# ========================================================
# Operator Precedence
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 5 — Operator Precedence
# ========================================================

'''
[Definition]
  - Operator precedence specifies the order in which operators are evaluated when two or more operators with different precedence appear in an expression
  - These rules greatly affect MySQL queries — incorrect assumptions about precedence cause wrong results
[Problem Example — Wrong result due to precedence]
  - LIKE operator is evaluated first
  - Then AND is evaluated (higher precedence than OR)
  - Then OR is evaluated — this means Pete (salary 1500, name starts with 'p') also appears in results even though salary < 1800
  - This is the wrong result — not what was intended
[Corrected Query — Using Parentheses]
  - Parentheses override the default precedence
  - The OR condition inside parentheses is resolved first: names starting with 's' or 'p'
  - Then the AND applies the salary filter — only high-salary s/p employees returned
  - Pete (salary 1500) is now correctly excluded
[MySQL Operator Precedence Order (Highest to Lowest)]
  - 1. INTERVAL
  - 2. BINARY, COLLATE
  - 3. ! (Negate)
  - 4. - (unary minus), ~ (unary bit inversion)
  - 5. ^ (Bitwise XOR)
  - 6. *, /, % (Multiplication, Division, Modulo)
  - 7. -, + (Subtraction, Addition)
  - 8. <<, >> (Bit shifts)
  - 9. & (Bitwise AND)
  - 10. | (Bitwise OR)
  - 11. =, <=>, >=, >, <=, <, <>, !=, IS, LIKE, REGEXP, IN (Comparison operators)
  - 12. BETWEEN, CASE WHEN THEN ELSE
  - 13. NOT
  - 14. AND, && (Logical AND)
  - 15. XOR (Logical XOR)
  - 16. OR, || (Logical OR) ← lowest practical precedence
  - 17. = (assignment), := (lowest overall)
  NOTE: 💡 Key Rule: AND always has higher precedence than OR. Always use parentheses when mixing AND and OR to make your intent explicit and avoid incorrect results.
'''


# Example 1 — Operator Precedence
sql = '''
-- INTENT: Employees with salary > 1800 AND whose name starts with 's' or 'p'
-- PROBLEM: AND has higher precedence than OR, so this is evaluated as:
-- (Salary > 1800 AND Name LIKE 's%') OR (Name LIKE 'p%')
-- This incorrectly returns employees named 'p%' regardless of salary!
SELECT * FROM Employee
WHERE Salary > 1800 AND Name LIKE 's%'
OR Name LIKE 'p%';
'''


# Example 2 — Operator Precedence
sql = '''
-- CORRECT: Parentheses force the OR condition to be evaluated first
-- Now: Salary > 1800 AND (name starts with 's' OR name starts with 'p')
SELECT * FROM Employee
WHERE Salary > 1800
AND (Name LIKE 's%' OR Name LIKE 'p%');
'''


# ### Section 6 — SQL Built-in Functions
# *Numeric · String · Date · BIN · CAST · COALESCE*


# ========================================================
# Built-in Functions — Overview
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 6 — SQL Built-in Functions
# ========================================================

'''
[Definition]
  - Built-in functions are functions that are shipped with MySQL — ready to use without any installation
  - They can be categorised according to the data types they operate on: String , Numeric , Date , BIN , and CAST
  - All examples use the Employee table: ID, NAME, AGE, ADDRESS, SALARY
'''


# ========================================================
# Numeric Functions
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 6 — SQL Built-in Functions
# ========================================================

'''
[Definition]
  - Numeric functions perform mathematical operations on numeric data and return a numeric result
  - Used in the SELECT clause with or without a FROM clause
[General Syntax]
[Example 1 — Basic Arithmetic]
[Example 2 — COS Function]
[Example 3 — DIV (Integer Division)]
[Key Numeric Functions Reference]
  - ABS(n) — returns absolute value of n
  - CEIL(n) / CEILING(n) — smallest integer ≥ n (rounds up)
  - FLOOR(n) — largest integer ≤ n (rounds down)
  - ROUND(n, d) — rounds n to d decimal places
  - MOD(n, m) — remainder of n divided by m
  - POW(m, n) — m raised to the power n
  - SQRT(n) — square root of n
  - RAND() — returns a random number between 0 and 1
  - PI() — returns π (3.141593)
  - GREATEST(v1, v2, ...) — returns the greatest value from a list
  - LEAST(v1, v2, ...) — returns the smallest value from a list
  - LOG10(n) — base-10 logarithm
  - LN(n) — natural logarithm
  - EXP(n) — returns e raised to the power n
  - DEGREES(n) — converts radians to degrees
  - RADIANS(n) — converts degrees to radians
  - SIGN(n) — returns the sign of n (-1, 0, or 1)
  - TRUNCATE(n, d) — truncates n to d decimal places (not rounding)
'''


# Example 1 — Numeric Functions
sql = '''
SELECT numerical_expression AS OPERATION_NAME
[FROM table_name WHERE CONDITION];
'''


# Example 2 — Numeric Functions
sql = '''
-- Add two numbers and alias the result column
SELECT (25 + 7) AS ADDITION;
-- Output: ADDITION = 32
'''


# Example 3 — Numeric Functions
sql = '''
-- Return the cosine of 1 radian
SELECT COS(1) AS Cos;
-- Output: Cos = 0.5403023058681398
'''


# Example 4 — Numeric Functions
sql = '''
-- Integer division: 20 divided by 6 (no remainder)
SELECT 20 DIV 6 AS DIVISION;
-- Output: DIVISION = 3 (remainder discarded)
'''


# ========================================================
# String Functions
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 6 — SQL Built-in Functions
# ========================================================

'''
[Definition]
  - String functions perform operations on input strings and return an output string or numeric value
  - Used to manipulate, format, search, and transform text data
[Example 1 — CHAR_LENGTH()]
[Example 2 — CONCAT_WS()]
[Example 3 — LCASE()]
[Example 4 — REPLACE()]
[Example 5 — TRIM()]
[Example 6 — SUBSTR()]
[Key String Functions Reference]
  - ASCII(char) — returns ASCII code value of a character
  - CHAR(n) — converts ASCII value to a character
  - CHAR_LENGTH(str) — returns length of string (MySQL equivalent of LEN)
  - CONCAT(s1, s2, ...) — joins two or more strings into one
  - CONCAT_WS(sep, s1, s2, ...) — concatenates with separator
  - LOWER(str) / LCASE(str) — converts to lowercase
  - UPPER(str) — converts to uppercase
  - LTRIM(str) — removes leading spaces
  - RTRIM(str) — removes trailing spaces
  - TRIM(str) — removes leading and trailing spaces (or specified characters)
  - REPLACE(str, from, to) — replaces all occurrences of a substring
  - REVERSE(str) — returns the string in reverse order
  - LEFT(str, n) — extracts n characters from the left
  - RIGHT(str, n) — extracts n characters from the right
  - SUBSTR(str, pos, len) — extracts a substring from position pos with length len
  - SOUNDEX(str) — returns a 4-character phonetic code
  - SPACE(n) — returns a string of n repeated spaces
  - REPLICATE(str, n) — repeats str n times
  NOTE: 💡 MySQL vs SQL Server Note: Some string function names differ: MySQL uses CHAR_LENGTH() while SQL Server uses LEN() . MySQL uses LCASE() / UCASE() as well as LOWER() / UPPER() . The notes include both for completeness.
'''


# Example 1 — String Functions
sql = '''
-- Find the length (number of characters) of the string 'MySQL'
-- Note: LEN() is used in SQL Server; use CHAR_LENGTH() in MySQL
SELECT CHAR_LENGTH('MySQL') AS CHAR_LEN;
-- Output: CHAR_LEN = 5
'''


# Example 2 — String Functions
sql = '''
-- Concatenate two strings with '_' as the separator
SELECT CONCAT_WS('_', 'great', 'learning') AS CONCAT_STR;
-- Output: CONCAT_STR = great_learning
'''


# Example 3 — String Functions
sql = '''
-- Convert string to lowercase
SELECT LCASE('Greatlearning To Learn') AS LCASE;
-- Output: LCASE = greatlearning to learn
'''


# Example 4 — String Functions
sql = '''
-- Replace all occurrences of 'Lakes' with 'Learning' inside 'Great Lakes'
SELECT REPLACE('Great Lakes', 'Lakes', 'Learning') AS Replaced;
-- Output: Replaced = Great Learning
'''


# Example 5 — String Functions
sql = '''
-- Remove the word 'Great' from the beginning of 'Great Learning'
SELECT TRIM('Great' FROM 'Great Learning') AS TrimmedString;
-- Output: TrimmedString = Learning
'''


# Example 6 — String Functions
sql = '''
-- Extract 5 characters starting from position 1
-- SUBSTR(string, start_position, length)
SELECT SUBSTR('Great Learning', 1, 5) AS ExtractedString;
-- Output: ExtractedString = Great
'''


# ========================================================
# Date Functions
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 6 — SQL Built-in Functions
# ========================================================

'''
[Definition]
  - Date functions operate on date and time data types in MySQL
  - The format of the date in the table must match the input date when inserting
  - In various scenarios, instead of DATE, the DATETIME type is used
[Example 1 — NOW()]
[Example 2 — CURDATE()]
[Example 3 — CURTIME()]
[Key Date Functions Reference]
  - NOW() — returns current date and time (YYYY-MM-DD HH:MI:SS)
  - CURDATE() — returns current date only (YYYY-MM-DD)
  - CURTIME() — returns current time only (HH:MI:SS)
  - DATE(expr) — extracts the date part from a date/datetime expression
  - EXTRACT(unit FROM date) — returns a single part of a date/time (e.g., YEAR, MONTH, DAY)
  - DATE_ADD(date, INTERVAL n unit) — adds a specified time interval to a date
  - DATE_SUB(date, INTERVAL n unit) — subtracts a specified time interval from a date
  - DATEDIFF(date1, date2) — returns the number of days between two dates
  - DATE_FORMAT(date, format) — displays date/time data in a specified format
'''


# Example 1 — Date Functions
sql = '''
-- Returns the current date and time
SELECT NOW();
-- Output: 2020-03-23 17:54:13 (format: YYYY-MM-DD HH:MI:SS)
'''


# Example 2 — Date Functions
sql = '''
-- Returns the current date only (no time)
SELECT CURDATE();
-- Output: 2020-03-23 (format: YYYY-MM-DD)
'''


# Example 3 — Date Functions
sql = '''
-- Returns the current time only (no date)
SELECT CURTIME();
-- Output: 18:27:17 (format: HH:MI:SS)
'''


# ========================================================
# BIN Function
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 6 — SQL Built-in Functions
# ========================================================

'''
[Definition]
  - MySQL BIN() returns the string representation of the binary value of a BIGINT number
  - Takes one argument: the number whose binary representation is needed
[Syntax]
[Example]
'''


# Example 1 — BIN Function
sql = '''
BIN(num1)
'''


# Example 2 — BIN Function
sql = '''
-- Returns binary string representation of 255
SELECT BIN(255);
-- Output: '11111111' (255 in binary)
'''


# ========================================================
# CAST Function
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 6 — SQL Built-in Functions
# ========================================================

'''
[Definition]
  - The CAST() function converts a value of any type into a specified data type
  - Parameters: value (required — value to convert) and datatype (required — target data type)
[Syntax]
[Example 1 — Convert to CHAR]
[Example 2 — Convert to TIME]
'''


# Example 1 — CAST Function
sql = '''
CAST(value AS datatype)
'''


# Example 2 — CAST Function
sql = '''
-- Convert the integer 150 to a CHAR (string) data type
SELECT CAST(150 AS CHAR);
-- Output: '150' (as a string, not integer)
'''


# Example 3 — CAST Function
sql = '''
-- Convert a string to TIME data type
SELECT CAST('14:06:10' AS TIME);
-- Output: 14:06:10 (as TIME type)
'''


# ========================================================
# COALESCE Function
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 6 — SQL Built-in Functions
# ========================================================

'''
[Definition]
  - The COALESCE() function returns the first non-NULL value in a list of expressions
  - Evaluates each value in order from left to right and returns the first one that is not NULL
  - Very useful for handling NULL values and providing fallback/default values
[Syntax]
[Example]
'''


# Example 1 — COALESCE Function
sql = '''
COALESCE(val1, val2, ..., val_n)
'''


# Example 2 — COALESCE Function
sql = '''
-- Returns the first non-null value from the list
-- NULL is skipped; 1 is the first non-null value
SELECT COALESCE(NULL, 1, 2, 'greatlearning.in');
-- Output: 1
'''


# ### Section 7 — Sorting & Limiting Results
# *ORDER BY · ASC · DESC · LIMIT · OFFSET*


# ========================================================
# ORDER BY Clause
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 7 — Sorting & Limiting Results
# ========================================================

'''
[Definition]
  - The ORDER BY clause causes the tuples (rows) in the result of a query to appear in sorted order
  - By default, ORDER BY lists items in ascending order (ASC)
  - Use DESC for descending order and ASC (optional) for ascending order
  - Ordering can be performed on multiple attributes — specify them as a comma-separated list
[Syntax]
[Example 1 — Ascending Order (Default)]
  - Returns all users with the lowest salary first and highest last
  - ASC is the default sort order — omitting it gives the same result
[Example 2 — Descending Order]
  - Returns all users with the highest salary first
  - Useful for finding top earners, most expensive items, latest dates, etc.
[Example 3 — Multiple Column Sorting]
  - Primary sort: City in descending alphabetical order (Z → A)
  - Secondary sort: Within each city group, salary in ascending order (lowest first)
  - Multiple sort columns are evaluated left to right — first column is the primary sort key
'''


# Example 1 — ORDER BY Clause
sql = '''
SELECT column_list FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC];
'''


# Example 2 — ORDER BY Clause
sql = '''
-- Show users sorted by salary in ascending order (lowest first)
-- ASC is the default — no keyword needed, but can be explicit
SELECT UserID, Name, Salary
FROM tblUser
ORDER BY Salary;
'''


# Example 3 — ORDER BY Clause
sql = '''
-- Show users sorted by salary in descending order (highest first)
SELECT UserID, Name, Salary
FROM tblUser
ORDER BY Salary DESC;
'''


# Example 4 — ORDER BY Clause
sql = '''
-- Sort by City in descending alphabetical order,
-- then within the same city, sort by Salary in ascending order
SELECT UserID, Name, Salary
FROM tblUser
ORDER BY City DESC, Salary ASC;
'''


# ========================================================
# LIMIT Clause
# 2 — WHERE Predicates, Set Ops, Functions & Sorting
# SECTION: Section 7 — Sorting & Limiting Results
# ========================================================

'''
[Definition]
  - The LIMIT clause restricts the number of rows returned by a SELECT query
  - Supports an optional OFFSET to skip a specified number of rows before returning results
  - Offset of the first row is 0 (zero-based, not 1)
[Syntax]
[Example — Basic LIMIT with OFFSET]
  - 2 = offset: skip the first 2 rows (rows at position 0 and 1)
  - 3 = row_count: return a maximum of 3 rows
  - Returns rows at positions 2, 3, and 4 (zero-indexed)
[Example 1 — Top 5 Highest Salaried Employees]
  - ORDER BY salary DESC — sorts from highest salary to lowest
  - LIMIT 5 — returns only the first 5 rows from the sorted result
  - Combined: returns the 5 highest-paid employees
[Example 2 — Third Highest Salary for a Specific Job]
  - WHERE job_id = 'ST_MAN' — filters to only ST_MAN employees
  - ORDER BY salary DESC — sorts by salary highest first
  - LIMIT 2, 1 — skip the top 2 (1st and 2nd highest), return exactly 1 row → the 3rd highest
  - This is the standard SQL pattern for finding the Nth highest value
  NOTE: 💡 N-th Highest Pattern: To find the Nth highest salary, use ORDER BY salary DESC LIMIT (N-1), 1 . The offset skips the top N-1 rows, returning the Nth one.
'''


# Example 1 — LIMIT Clause
sql = '''
SELECT select_list FROM table_name
LIMIT [offset,] row_count;

-- offset: number of rows to skip (0-based). Optional.
-- row_count: maximum number of rows to return.
'''


# Example 2 — LIMIT Clause
sql = '''
-- Skip first 2 rows, then return the next 3 rows
SELECT * FROM employees LIMIT 2, 3;
'''


# Example 3 — LIMIT Clause
sql = '''
-- Display employee_id, first_name, last_name, job_id of top 5 highest earners
SELECT employee_id, first_name, last_name, job_id, salary
FROM employees
ORDER BY salary DESC
LIMIT 5;
'''


# Example 4 — LIMIT Clause
sql = '''
-- Display the 3rd highest salaried employee with job_id = 'ST_MAN'
-- offset = 2 (skip the 1st and 2nd highest), row_count = 1 (return only 1 row)
SELECT employee_id, first_name, last_name, salary
FROM employees
WHERE job_id = 'ST_MAN'
ORDER BY salary DESC
LIMIT 2, 1;
'''


# ---

# ## Session 3 — Aggregate Functions, GROUP BY & HAVING

# *COUNT · SUM · AVG · MIN / MAX · GROUP BY · HAVING*


# ### Section 1 — Aggregate Functions
# *COUNT · SUM · AVG · MIN · MAX*


# ========================================================
# Aggregate Functions — Overview
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 1 — Aggregate Functions
# ========================================================

'''
[Definition]
  - Aggregate functions perform calculations on multiple rows of a single column and return a single value
  - The ISO standard defines five aggregate functions : COUNT, SUM, AVG, MIN, MAX
[Why Use Aggregate Functions?]
  - Allow us to easily produce summarised data from our database
  - Real-world use cases from a company database:
 
 Minimum salary of a particular department 
 Highest paid employee details 
 Average salary of the HR department
  NOTE: 💡 Aggregate functions return zero (not NULL) when no matching rows exist in the table.
'''


# ========================================================
# Sample Table Setup — employee & employee1
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 1 — Aggregate Functions
# ========================================================

'''
[Table: employee (used for basic aggregate examples)]
[Table Data Summary]
  - 8 employees total across 3 departments: HR (2), IT (4), SALES (2)
  - One employee (Robert) has a NULL value in the month column
  - Salary range: 3,000 (Jacob) to 123,456 (Charlie)
  - Total salary: 404,979 | Average salary: 50,622.375
[Table: employee1 (used for GROUP BY with multiple columns)]
[Key Difference from employee table]
  - Column renamed from month to joining_month
  - 3 employees join in month 1 (Oliver, George, Harry) instead of 2 — enabling multi-column GROUP BY demonstrations
'''


# Example 1 — Sample Table Setup — employee & employee1
sql = '''
CREATE TABLE employee (
    month     INT,
    emp_id    INT,
    emp_name  VARCHAR(15),
    dept_name VARCHAR(15),
    salary    INT
);

INSERT INTO employee VALUES
(1,    101, 'Oliver',  'HR',    9000),
(1,    102, 'George',  'IT',    8000),
(3,    103, 'Harry',   'HR',    20000),
(6,    104, 'Jack',    'IT',    110123),
(6,    105, 'Jacob',   'SALES', 3000),
(12,   106, 'Noah',    'SALES', 101000),
(12,   107, 'Charlie', 'IT',    123456),
(NULL, 108, 'Robert',  'IT',    30400);
'''


# Example 2 — Sample Table Setup — employee & employee1
sql = '''
CREATE TABLE employee1 (
    joining_month INT,
    emp_id        INT,
    emp_name      VARCHAR(15),
    dept_name     VARCHAR(15),
    salary        INT
);

INSERT INTO employee1 VALUES
(1,    101, 'Oliver',  'HR',    9000),
(1,    102, 'George',  'IT',    8000),
(1,    103, 'Harry',   'HR',    20000),
(3,    104, 'Jack',    'IT',    110123),
(6,    105, 'Jacob',   'SALES', 3000),
(6,    106, 'Noah',    'SALES', 101000),
(3,    107, 'Charlie', 'IT',    123456),
(NULL, 108, 'Robert',  'IT',    30400);
'''


# ========================================================
# COUNT Function
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 1 — Aggregate Functions
# ========================================================

'''
[Definition]
  - The COUNT function counts the total number of records matching a condition
  - COUNT(*) counts all rows including those with NULL values
  - COUNT(field_name) counts only rows where the field is NOT NULL
  - COUNT(DISTINCT field_name) returns the number of distinct non-NULL rows
[Syntax]
[Example — Count total employees]
[Output & Explanation]
  - Output: COUNT(*) = 8
  - COUNT(*) counts ALL rows regardless of NULL values — 8 employees in total
  - Even the row where month is NULL (Robert) is counted by COUNT(*)
[Variation — COUNT with DISTINCT]
'''


# Example 1 — COUNT Function
sql = '''
SELECT COUNT([DISTINCT] field_name)
FROM target_table
[WHERE test_expr];
'''


# Example 2 — COUNT Function
sql = '''
-- Count the total number of rows in the employee table
SELECT COUNT(*) FROM employee;
'''


# Example 3 — COUNT Function
sql = '''
-- Count distinct (unique) department names
SELECT COUNT(DISTINCT dept_name) FROM employee;
-- Output: 3 (HR, IT, SALES)

-- Count employees where month is NOT NULL
SELECT COUNT(month) FROM employee;
-- Output: 7 (Robert's NULL month is excluded)
'''


# ========================================================
# SUM Function
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 1 — Aggregate Functions
# ========================================================

'''
[Definition]
  - The SUM function returns the total sum of a set of numeric values
  - Ignores NULL values — only non-NULL values are summed
  - The argument ( field_name ) is the column or expression that will be summed
[Syntax]
[Example — Sum of all employee salaries]
[Output & Explanation]
  - Output: SUM(salary) = 404979
  - All 8 salaries are summed: 9000 + 8000 + 20000 + 110123 + 3000 + 101000 + 123456 + 30400 = 404,979
'''


# Example 1 — SUM Function
sql = '''
SELECT SUM(field_name)
FROM target_table
[WHERE test_expr];
'''


# Example 2 — SUM Function
sql = '''
-- Find the total of all employee salaries
SELECT SUM(salary) FROM employee;
'''


# ========================================================
# AVG Function
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 1 — Aggregate Functions
# ========================================================

'''
[Definition]
  - The AVG function returns the arithmetic average (mean) of a set of values
  - Ignores NULL values — only non-NULL values are included in the average calculation
  - Returns a decimal result even if the input values are integers
[Syntax]
[Example — Average of all employee salaries]
[Output & Explanation]
  - Output: AVG(salary) = 50622.3750
  - Calculated as: 404,979 ÷ 8 = 50,622.375
  - MySQL returns 4 decimal places by default for AVG
'''


# Example 1 — AVG Function
sql = '''
SELECT AVG(field_name)
FROM target_table
[WHERE test_expr];
'''


# Example 2 — AVG Function
sql = '''
-- Find the average salary across all employees
SELECT AVG(salary) FROM employee;
'''


# ========================================================
# MIN Function
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 1 — Aggregate Functions
# ========================================================

'''
[Definition]
  - The MIN function returns the smallest value from a set of values
  - Ignores NULL values
  - Works on numeric, string, and date columns
[Syntax]
[Example — Lowest employee salary]
[Output & Explanation]
  - Output: MIN(salary) = 3000
  - Jacob (SALES department, month 6) has the lowest salary of 3,000
'''


# Example 1 — MIN Function
sql = '''
SELECT MIN(field_name)
FROM target_table
[WHERE test_expr];
'''


# Example 2 — MIN Function
sql = '''
-- Find the lowest salary received by any employee
SELECT MIN(salary) FROM employee;
'''


# ========================================================
# MAX Function
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 1 — Aggregate Functions
# ========================================================

'''
[Definition]
  - The MAX function returns the largest value from a set of values
  - Ignores NULL values
  - Works on numeric, string, and date columns
[Syntax]
[Example — Highest employee salary]
[Output & Explanation]
  - Output: MAX(salary) = 123456
  - Charlie (IT department, month 12) has the highest salary of 123,456
'''


# Example 1 — MAX Function
sql = '''
SELECT MAX(field_name)
FROM target_table
[WHERE test_expr];
'''


# Example 2 — MAX Function
sql = '''
-- Find the highest salary received by any employee
SELECT MAX(salary) FROM employee;
'''


# ### Section 2 — GROUP BY
# *Grouped Queries · Single & Multiple Columns · Rules & Restrictions*


# ========================================================
# GROUP BY — Overview & Syntax
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 2 — GROUP BY
# ========================================================

'''
[Definition]
  - The GROUP BY statement groups rows that have the same values into summary rows
  - Used together with aggregate functions (COUNT, SUM, AVG, MIN, MAX) to group the result set by one or more columns
  - GROUP BY comes after the WHERE clause and before the HAVING clause
[Syntax]
[Syntax Components Explained]
  - GROUP BY column_name1 — the clause that performs the grouping based on this column
  - [,column_name2,...] — optional; additional columns when grouping on more than one column
  - [HAVING condition] — optional; used to restrict the rows affected by the GROUP BY clause (filter on grouped results)
'''


# Example 1 — GROUP BY — Overview & Syntax
sql = '''
SELECT statements...
GROUP BY column_name1 [, column_name2, ...]
[HAVING condition];
'''


# ========================================================
# Grouping Using a Single Column
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 2 — GROUP BY
# ========================================================

'''
[Without GROUP BY — All department entries (raw)]
  - Output: 8 rows — HR, IT, HR, IT, SALES, SALES, IT, IT (with duplicates)
  - This gives a single ungrouped list — no summarisation
[With GROUP BY — Unique departments only]
  - Output: 3 rows — HR, IT, SALES
  - GROUP BY collapses all rows with the same dept_name into one group
  - Result: there are 3 unique departments in the office
'''


# Example 1 — Grouping Using a Single Column
sql = '''
-- Returns all dept_name values including duplicates
SELECT dept_name FROM employee;
'''


# Example 2 — Grouping Using a Single Column
sql = '''
-- Returns only unique department names
SELECT dept_name FROM employee GROUP BY dept_name;
'''


# ========================================================
# COUNT with GROUP BY
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 2 — GROUP BY
# ========================================================

'''
[Example — Employee count per department]
[Output & Explanation]
  - HR: 2 employees | IT: 4 employees | SALES: 2 employees
  - Out of 8 total employees: 2 in HR, 4 in IT, 2 in SALES
  - GROUP BY groups all rows by dept_name first, then COUNT(*) counts rows in each group
'''


# Example 1 — COUNT with GROUP BY
sql = '''
-- Count the number of employees in each department
SELECT COUNT(*), dept_name
FROM employee
GROUP BY dept_name;
'''


# ========================================================
# SUM with GROUP BY
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 2 — GROUP BY
# ========================================================

'''
[Example 1 — Sum of salaries per department]
  - HR: 29,000 (Oliver 9000 + Harry 20000)
  - IT: 271,979 (George 8000 + Jack 110123 + Charlie 123456 + Robert 30400)
  - SALES: 104,000 (Jacob 3000 + Noah 101000)
[Example 2 — Month-wise sum of salaries]
  - Month 1: 17,000 | Month 3: 20,000 | Month 6: 113,123 | Month 12: 224,456
  - NULL month (Robert): 30,400 — NULL values form their own group in GROUP BY
'''


# Example 1 — SUM with GROUP BY
sql = '''
-- Find the total salary paid to each department
SELECT dept_name, SUM(salary)
FROM employee
GROUP BY dept_name;
'''


# Example 2 — SUM with GROUP BY
sql = '''
-- Find the total salary paid per month
SELECT month, SUM(salary)
FROM employee
GROUP BY month;
'''


# ========================================================
# AVG with GROUP BY
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 2 — GROUP BY
# ========================================================

'''
[Example 1 — Average salary per department]
  - HR: 14,500.0000 | IT: 67,994.7500 | SALES: 52,000.0000
[Example 2 — Month-wise average salary]
  - Month 1: 8,500.0000 | Month 3: 20,000.0000 | Month 6: 56,561.5000 | Month 12: 112,228.0000 | NULL: 30,400.0000
'''


# Example 1 — AVG with GROUP BY
sql = '''
-- Find the average salary in each department
SELECT dept_name, AVG(salary)
FROM employee
GROUP BY dept_name;
'''


# Example 2 — AVG with GROUP BY
sql = '''
-- Find the average salary per month
SELECT month, AVG(salary)
FROM employee
GROUP BY month;
'''


# ========================================================
# MIN with GROUP BY
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 2 — GROUP BY
# ========================================================

'''
[Example 1 — Minimum salary per department]
  - HR: 9,000 (Oliver) | IT: 8,000 (George) | SALES: 3,000 (Jacob)
[Example 2 — Month-wise minimum salary]
  - Month 1: 8,000 | Month 3: 20,000 | Month 6: 3,000 | Month 12: 101,000 | NULL: 30,400
'''


# Example 1 — MIN with GROUP BY
sql = '''
-- Find the lowest salary in each department
SELECT dept_name, MIN(salary)
FROM employee
GROUP BY dept_name;
'''


# Example 2 — MIN with GROUP BY
sql = '''
-- Find the minimum salary per month
SELECT month, MIN(salary)
FROM employee
GROUP BY month;
'''


# ========================================================
# MAX with GROUP BY
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 2 — GROUP BY
# ========================================================

'''
[Example — Maximum salary per department]
  - HR: 20,000 (Harry) | IT: 123,456 (Charlie) | SALES: 101,000 (Noah)
'''


# Example 1 — MAX with GROUP BY
sql = '''
-- Find the highest salary in each department
SELECT dept_name, MAX(salary)
FROM employee
GROUP BY dept_name;
'''


# ========================================================
# Multiple Grouping Columns
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 2 — GROUP BY
# ========================================================

'''
[Definition]
  - A GROUP BY clause can contain two or more columns
  - In other words, a grouping can consist of two or more columns combined
  - Each unique combination of the grouped columns forms its own group
[Example — Sum and Average salary by department AND joining month]
[Output & Explanation]
  - HR / Month 1: SUM=29000, AVG=14500.0000 (Oliver + Harry both joined month 1)
  - IT / Month 1: SUM=8000, AVG=8000.0000 (only George joined month 1)
  - IT / Month 3: SUM=233579, AVG=116789.5000 (Jack + Charlie joined month 3)
  - SALES / Month 6: SUM=104000, AVG=52000.0000 (Jacob + Noah joined month 6)
  - IT / NULL month: SUM=30400, AVG=30400.0000 (Robert — unknown month)
  - Grouping is done by using multiple columns: dept_name AND joining_month together
'''


# Example 1 — Multiple Grouping Columns
sql = '''
-- Get sum AND average of salaries per department per joining month
-- Using employee1 table (which has joining_month column)
SELECT dept_name, joining_month, SUM(salary), AVG(salary)
FROM employee1
GROUP BY dept_name, joining_month;
'''


# ========================================================
# GROUP BY Rules & Restrictions
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 2 — GROUP BY
# ========================================================

'''
[Rule 1 — All SELECT columns must appear in GROUP BY (only_full_group_by mode)]
  - In MySQL's default only_full_group_by mode, all non-aggregated columns in the SELECT list must be included in the GROUP BY clause
  - Violating this causes error: "SELECT list is not in GROUP BY clause and contains nonaggregated column… which is not functionally dependent on columns in GROUP BY clause"
[Wrong vs Correct Example]
[Rule 2 — Aggregate functions cannot appear in GROUP BY clause]
  - You cannot use aggregate functions (like SUM, COUNT) directly in the GROUP BY clause
  - Violating this causes error: Error Code: 1056. Can't group on 'sum(salary)'
[Rule 3 — Comparison conditions cannot appear in GROUP BY clause]
  - Comparison conditions (like sum(salary) > 10000 ) cannot be placed inside the GROUP BY clause
  - They cannot act on grouped result sets
  - Violating this causes error: Error Code: 1111. Invalid use of group function
  - Use the HAVING clause for filtering grouped results instead
[Rule 4 — WHERE clause must come BEFORE GROUP BY]
  - WHERE clause with conditions can be used before GROUP BY to filter rows first, then group
  - WHERE always comes before GROUP BY — never after
[Best Practices for Grouping Columns]
  - Grouping columns should have less unique values (fewer distinct values = better grouping)
  - Grouping columns should be primary business entities and facts (department, month, category) — NOT transactional data (salary, individual IDs)
  - Example: dept and month are less unique — summarising results on these columns is useful and meaningful
  - Grouping by salary (highly unique) produces no summarised result — each row becomes its own group
'''


# Example 1 — GROUP BY Rules & Restrictions
sql = '''
-- ❌ WRONG: joining_month is in SELECT but NOT in GROUP BY
SELECT dept_name, joining_month, SUM(salary)
FROM employee1
GROUP BY dept_name;
-- Error: SELECT list is not in GROUP BY clause

-- ✅ CORRECT: both dept_name and joining_month are in GROUP BY
SELECT dept_name, joining_month, SUM(salary)
FROM employee1
GROUP BY dept_name, joining_month;
'''


# Example 2 — GROUP BY Rules & Restrictions
sql = '''
-- ❌ WRONG: aggregate function in GROUP BY
SELECT dept_name, joining_month, SUM(salary)
FROM employee1
GROUP BY SUM(salary);
-- Error Code: 1056. Can't group on 'sum(salary)'

-- ✅ CORRECT: group only on columns, not functions
SELECT dept_name, joining_month, SUM(salary)
FROM employee1
GROUP BY dept_name, joining_month;
'''


# Example 3 — GROUP BY Rules & Restrictions
sql = '''
-- ❌ WRONG: comparison condition inside GROUP BY
SELECT dept_name, joining_month, SUM(salary)
FROM employee1
GROUP BY SUM(salary) > 10000;
-- Error Code: 1111. Invalid use of group function

-- ✅ Note: comparison on column values in GROUP BY is technically allowed
--    but produces no useful summarisation (grouping by salary gives each row its own group)
SELECT dept_name, joining_month, SUM(salary)
FROM employee1
GROUP BY dept_name, joining_month > 10000;
'''


# ========================================================
# NULL Values in Grouping Columns
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 2 — GROUP BY
# ========================================================

'''
[Behaviour]
  - When a grouping column contains NULL values, MySQL still calculates and shows the aggregate summary for those NULL values
  - All rows where the grouping column is NULL are placed into their own special NULL group
  - NULL values in the grouping column appear as a separate row in the output with NULL as the group label
[Example]
[Output Explanation]
  - A row appears: IT | NULL | 30400 — showing Robert's salary grouped under NULL month
  - This is expected MySQL behaviour: NULL values in GROUP BY columns form their own group
  - The aggregate (sum) is still calculated for this NULL group
'''


# Example 1 — NULL Values in Grouping Columns
sql = '''
-- Robert has NULL joining_month — his salary still appears in output
-- grouped under NULL joining_month
SELECT dept_name, joining_month, SUM(salary)
FROM employee1
GROUP BY dept_name, joining_month;
'''


# ### Section 3 — HAVING Clause
# *Filtering grouped results · Restrictions · HAVING without GROUP BY*


# ========================================================
# HAVING Clause — Overview & Example
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 3 — HAVING Clause
# ========================================================

'''
[Definition]
  - The HAVING clause is used together with GROUP BY to apply conditions on the grouped result set
  - WHERE filters individual rows before grouping; HAVING filters groups after grouping
  - HAVING conditions must involve aggregate functions (because they act on grouped results)
[Syntax]
[Example — Departments where collective salary exceeds 35,000]
[Output & Explanation]
  - Output: IT/Month 3: 233,579 | SALES/Month 6: 104,000
  - HR/Month 1 (29,000) and IT/Month 1 (8,000) are excluded — their sums ≤ 35,000
  - IT/NULL (30,400) is also excluded — below the threshold
  - HAVING filters the grouped results: only groups where SUM(salary) > 35,000 are returned
'''


# Example 1 — HAVING Clause — Overview & Example
sql = '''
SELECT col1, col2, AGG_FUNC(col3)
FROM table_name
[WHERE row_condition]
GROUP BY col1, col2
HAVING AGG_FUNC(col3) condition;
'''


# Example 2 — HAVING Clause — Overview & Example
sql = '''
-- Find department-month combinations where total salary > 35,000
SELECT joining_month, dept_name, SUM(salary)
FROM employee1
GROUP BY joining_month, dept_name
HAVING SUM(salary) > 35000;
'''


# ========================================================
# Restrictions on Grouped Search Condition (HAVING)
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 3 — HAVING Clause
# ========================================================

'''
[Rule 1 — HAVING must contain at least one aggregate function]
  - The HAVING clause must be enclosed with grouped (aggregate) functions on columns issued in the SELECT query
  - Conditions in HAVING must always have at least one grouping function for comparison since it acts on grouped result sets
[Example — HAVING with IS NOT NULL on aggregate]
  - Returns all groups where the sum of salary is not null — effectively all groups since all salaries have values
  - Output: 5 rows (HR/1, IT/1, IT/3, SALES/6, IT/NULL) all with their SUM and AVG
  - This query is valid because HAVING condition uses SUM() — an aggregate function
'''


# Example 1 — Restrictions on Grouped Search Condition (HAVING)
sql = '''
-- Find department-month groups where sum of salary is not null
-- HAVING uses an aggregate function (SUM) with IS NOT NULL
SELECT dept_name, joining_month, SUM(salary), AVG(salary)
FROM employee1
GROUP BY dept_name, joining_month
HAVING SUM(salary) IS NOT NULL;
'''


# ========================================================
# NULL Values and Grouped Search Condition
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 3 — HAVING Clause
# ========================================================

'''
[Example — Employee details where salary is not null, grouped by joining month]
[Output & Explanation]
  - Returns: all employees with their joining month and salary where salary sum is not null
  - Sample output rows: 1/Oliver/9000, 1/George/8000, 1/Harry/20000, 3/Jack/110123, 6/Jacob/3000, 6/Noah/101000, 3/Charlie/123456, NULL/Robert/30400
  - HAVING SUM(salary) IS NOT NULL — filters out any group where all salaries would be NULL (none in this dataset, so all rows returned)
  - Robert (NULL month) still appears because his salary has a value — it is not null
'''


# Example 1 — NULL Values and Grouped Search Condition
sql = '''
-- Full salary details per employee, grouped by joining_month
-- where salary sum is not null
SELECT joining_month, emp_name, SUM(salary)
FROM employee1
GROUP BY joining_month
HAVING SUM(salary) IS NOT NULL;
'''


# ========================================================
# HAVING Without GROUP BY
# 3 — Aggregate Functions, GROUP BY & HAVING
# SECTION: Section 3 — HAVING Clause
# ========================================================

'''
[Definition]
  - HAVING can be used without GROUP BY to apply a condition on an aggregate result over the entire table as a single group
  - Useful for producing a single high-level summary report with a threshold check
  - The entire table is treated as one group, and HAVING filters whether that single aggregate value meets the condition
[Example — Check if total company salary exceeds 299,999]
[Output & Explanation]
  - Output: SUM(salary) = 404979
  - The entire table is treated as one group — SUM(salary) = 404,979
  - Since 404,979 > 299,999, the condition is TRUE and the result is returned
  - If total salary were ≤ 299,999, the query would return an empty result (0 rows)
  - Use case: quickly check whether total payroll exceeds a budget threshold
'''


# Example 1 — HAVING Without GROUP BY
sql = '''
-- Print the sum of all salaries ONLY IF the total exceeds 299,999
-- Useful to quickly verify if total payroll exceeds a threshold
SELECT SUM(salary)
FROM employee1
HAVING SUM(salary) > 299999;
'''


# ---

# ## Session 4 — Multiple Table Queries & JOINs

# *INNER JOIN · LEFT / RIGHT · NATURAL JOIN · SELF JOIN · CROSS JOIN*


# ### Section 1 — Introduction to JOINs
# *Why JOINs exist · Fact & Dimension tables · ER Diagram*


# ========================================================
# What is a JOIN?
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 1 — Introduction to JOINs
# ========================================================

'''
[Definition]
  - The JOIN clause allows retrieval of data from two or more tables that have related data
  - These relations are established or identified with the help of key attributes (Primary Keys and Foreign Keys)
  - Fact and Dimensional tables are joined using key columns to produce an output of records with more meaningful relationships between each data field
[Why Use JOINs?]
  - Avoids repetition of data across tables — data is stored once and combined on demand
  - Presents data in a more systematic and meaningful way
  - Real-world use cases from a bank database:
 
 How many accounts are maintained by each customer? 
 Different modes of customer payments? 
 Customers using Smart Cash (digital) payment through UPI, IVR, or point-of-sale channels?
[ISO Standard JOIN Types]
  - Self-Join / Equi-Join
  - Non-Equi Join
  - Natural Join
  - Inner Join
  - Left Outer Join
  - Right Outer Join
  NOTE: 💡 Did you know? With JOINs, queries avoid a lot of data repetition. Instead of duplicating customer names in every transaction row, the JOIN pulls them together at query time.
'''


# ========================================================
# Fact vs Dimension Tables
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 1 — Introduction to JOINs
# ========================================================

'''
[Fact Table]
  - Contains real-time data , usually static in nature
  - Does not change frequently
  - Example: Customer data — a customer has one identity that rarely changes
[Dimension Table]
  - Contains data that changes more frequently than fact tables
  - Captures transactional or event-based records
  - Example: Transaction data — updated constantly as payments occur
  NOTE: ℹ️ In the bank database used throughout this session, CUSTOMER acts as the Fact table (static master data) while TRANSACTION acts as the Dimension table (frequently updated event data).
'''


# ========================================================
# ER Diagram — Bank Database Overview
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 1 — Introduction to JOINs
# ========================================================

'''
[Tables in the Study Database]
  - CUSTOMER — master customer records (PK: Cust_Id)
  - ACCOUNT — bank accounts linked to customers (PK: Acct_Num, FK: Cust_Id → CUSTOMER)
  - TRANSACTION — all debit/credit transactions (FK: Acct_Num → ACCOUNT)
  - INTEREST — interest rates per account type per month/year (PK: Acct_type)
  - MESSAGE — bank notification messages keyed by Event
  - CUST_MSG — links customers to messages (FK: Cust_Id → CUSTOMER)
  - ACCT_RELATION — tracks the parent–child relationship between accounts (PK: Acct_Num, FK: Link_Acct)
[Key Relationships]
  - One CUSTOMER → Many ACCOUNTs (through Cust_Id)
  - One ACCOUNT → Many TRANSACTIONs (through Acct_Num)
  - INTEREST → ACCOUNT join uses Acct_type as the common dimension
  - ACCT_RELATION links a secondary account (e.g., Fixed Deposit) to its primary account (Savings) through Link_Acct
  NOTE: ℹ️ All tables are provided in the module 6 tables.sql file required for this session.
'''


# ========================================================
# Table Schema Details
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 1 — Introduction to JOINs
# ========================================================

'''
[CUSTOMER Table — Columns]
  - Cust_Id — INT — Primary Key : Uniquely identifies each customer in the bank
  - Name — VARCHAR(20) — Full name of the customer
  - Address — VARCHAR(20) — Residential address of the customer
  - State — VARCHAR(3) — State code of customer residence (e.g., CA, MN, NY)
  - Phone — VARCHAR(10) — Personal phone/contact number
  - Age — INT — Age of the customer
[ACCOUNT Table — Columns]
  - Cust_Id — INT — Foreign Key → CUSTOMER: A customer can have multiple accounts
  - Acct_Num — VARCHAR(20) — Primary Key : Uniquely identifies an account in the bank
  - Acct_type — VARCHAR(20) — Type of account: SAVINGS, FIXED DEPOSITS, CREDITCARD
  - Balance — INT — Current balance maintained in the account
  - Acct_Status — VARCHAR(10) — ACTIVE or INACTIVE (accounts unused over time become inactive)
  - Relation — CHAR(1) — P = Primary account, S = Secondary account (e.g., a FD is Secondary, linked to a Savings account)
[TRANSACTION Table — Columns]
  - Acct_Num — VARCHAR(20) — Non-unique FK → ACCOUNT: an account has many transactions
  - Tran_Amount — DECIMAL(18,2) — Transaction amount in numbers (negative = debit)
  - Channel — VARCHAR(18) — Mode of transfer: ATM withdrawal, Cash Deposits, Online Shopping, Net banking, etc.
  - Area — VARCHAR(3) — State code where the transaction took place
  - Tran_date — DATE — Date on which the transaction occurred
[ACCT_RELATION Table — Columns]
  - Acct_Num — VARCHAR(20) — Primary Key : unique account number
  - Cust_Id — INT — FK → CUSTOMER: Customer identity for any account
  - Acct_type — VARCHAR(25) — Type: SAVINGS, FIXED DEPOSITS, CREDITCARD
  - Link_Acct — VARCHAR(20) — Parent account number: a FD is linked to its Savings account. Savings is the Link_Acct
[INTEREST Table — Columns]
  - Acct_type — VARCHAR(20) — Primary Key : Account type — SAVINGS, FIXED DEPOSITS, CREDITCARD
  - Rate — DECIMAL(18,2) — Rate of interest defined for each account type (e.g., 0.07 = 7%)
  - month — VARCHAR(2) — Month number (01–12) for which the rate applies
  - year — VARCHAR(4) — Year for which the rate applies (e.g., 2020, 2021)
[MESSAGE Table — Columns]
  - Event — VARCHAR(45) — Primary Key : Name of the upcoming bank event
  - Notice — VARCHAR(50) — Pre-defined notice message to be delivered to a customer when a sudden event occurs
  - Delivery_type — VARCHAR(9) — Mode of delivery: phone or e-mail
  - Date — DATE — Date of the event
'''


# ### Section 2 — Simple Joins & Aliases
# *Two-table queries · Table & Column aliases · Parent-Child · Row Selection*


# ========================================================
# Two-Table Query (Simple Join)
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 2 — Simple Joins & Aliases
# ========================================================

'''
[Definition]
  - The simplest form of a JOIN — retrieving data from two tables using a shared key column in the WHERE clause
  - Both table names are listed in FROM, separated by a comma
  - The WHERE clause specifies how the two tables are related (join condition)
[Example — Simple Two-Table Join with WHERE]
[Output Explanation]
  - Only rows where CUST_ID matches in both tables are returned
  - Because both tables have a column named CUST_ID , MySQL requires full qualification: CUSTOMER.CUST_ID and ACCOUNT.CUST_ID
  - Oliver (123001) appears twice — once for each account he holds
'''


# Example 1 — Two-Table Query (Simple Join)
sql = '''
-- Using full table names in WHERE clause (no aliases)
SELECT CUSTOMER.CUST_ID, ACCOUNT.CUST_ID, NAME, ACCT_NUM
FROM   CUSTOMER, ACCOUNT
WHERE  CUSTOMER.CUST_ID = ACCOUNT.CUST_ID;
'''


# ========================================================
# Table & Column Aliases
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 2 — Simple Joins & Aliases
# ========================================================

'''
[Why Aliases?]
  - When two joined tables share a column name (e.g., both have CUST_ID ), MySQL cannot tell which table the column comes from — you must qualify it
  - Table aliases shorten the table reference (e.g., CUSTOMER → BC, ACCOUNT → BA)
  - Column aliases rename output columns with more meaningful labels (e.g., Master_Cust_Id )
  - Aliases can also be given to an entire SELECT subquery when used as a derived table
[Example — With Table and Column Aliases]
[Types of Aliases]
  - Table alias — shortens table name for the query: FROM CUSTOMER BC or FROM CUSTOMER AS BC
  - Column alias — renames output column: SELECT BC.cust_id AS Master_Cust_Id
  - Derived table alias — alias for a subquery in FROM: FROM ( SELECT * FROM ACCOUNT ) BA
  NOTE: 💡 Table aliases simplify table references; column aliases make SELECT output columns more meaningful for reports and dashboards.
'''


# Example 1 — Table & Column Aliases
sql = '''
-- BC = alias for CUSTOMER, BA = alias for ACCOUNT
SELECT  BC.cust_id  AS  Master_Cust_Id,
        BA.cust_id  AS  Account_Cust_Id,
        Name        AS  Customer_Name,
        Acct_Num    AS  Account_Number
FROM    CUSTOMER BC,
        ACCOUNT  BA
WHERE   BC.CUST_ID = BA.CUST_ID;
'''


# ========================================================
# Parent–Child Relationship Queries
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 2 — Simple Joins & Aliases
# ========================================================

'''
[Concept]
  - The same table is referenced multiple times in a single SELECT query to establish parent–child (hierarchical) relationships
  - First reference acts as the parent ; second reference acts as the child
  - Useful for finding hierarchical data and relationships between two records in the same table
[ACCT_RELATION Table — Key Concept]
  - Acct_Num holds all accounts (SAVINGS, FIXED DEPOSITS, CREDITCARD)
  - Link_Acct stores the parent account number — for SAVINGS it is empty; for FD/CC it points to the linked Savings account
  - Goal: display Primary Account alongside its Secondary Account(s) side-by-side
[Example — Parent-Child Query on ACCT_RELATION]
[Output Explanation]
  - Result shows each SAVINGS account paired with its FIXED DEPOSITS or CREDITCARD child accounts
  - FIXED DEPOSITS and Credit card are confirmed as child accounts of the parent SAVINGS account
  - Rows where Link_Acct is NULL (SAVINGS accounts with no parent) are not returned — because nothing matches them as a child
'''


# Example 1 — Parent–Child Relationship Queries
sql = '''
-- AR1 = parent alias, AR2 = child alias (same table, two roles)
SELECT AR1.Acct_Num   AS Primary_Account,
       AR1.Acct_Type  AS Primary_Acct_Type,
       AR2.Acct_Num   AS Secondary_Account,
       AR2.Acct_Type  AS Secondary_Acct_Type
FROM   ACCT_RELATION AR1,
       ACCT_RELATION AR2
WHERE  AR1.Acct_Num = AR2.Link_Acct;
'''


# ========================================================
# Joins with Row Selection Criteria (Derived Tables)
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 2 — Simple Joins & Aliases
# ========================================================

'''
[Concept]
  - Rows returned from a SELECT query can act as a temporary (derived) table and be joined with any other physical table
  - The subquery appears inside the FROM clause and is given an alias
[Example 1 — Subquery as Derived Table]
[Example 2 — Derived Table Joined with Physical Table]
[Example 3 — Composite Joining Key with Business Condition]
  NOTE: 💡 Composite joining key : when multiple columns together define the relationship between tables. Here Acct_Num + Balance + Acct_type collectively form the join condition.
'''


# Example 1 — Joins with Row Selection Criteria (Derived Tables)
sql = '''
-- The inner SELECT acts as a temporary table aliased as BA
SELECT BA.Acct_num, BA.Balance
FROM ( SELECT * FROM ACCOUNT ) BA;
'''


# Example 2 — Joins with Row Selection Criteria (Derived Tables)
sql = '''
-- TRANSACTION subquery result (AT) joined with physical ACCOUNT table (BA)
SELECT BA.Acct_Num,
       BA.Acct_Type,
       AT.Tran_amount
FROM   ACCOUNT BA,
       ( SELECT * FROM TRANSACTION ) AT
WHERE  BA.Acct_Num = AT.Acct_Num;
'''


# Example 3 — Joins with Row Selection Criteria (Derived Tables)
sql = '''
-- Multiple columns form a composite join key
-- Finds DEPOSIT accounts where balance exceeds the transaction amount
SELECT BA.Acct_Num, BA.Acct_type, BA.Balance, TR.Tran_Amount
FROM   ACCOUNT BA
JOIN   TRANSACTION TR
ON ( BA.Acct_Num = TR.Acct_Num
     AND BA.Balance > ABS(TR.Tran_Amount)
     AND BA.Acct_type LIKE '%DEPOSIT%' );
'''


# ### Section 3 — Join Types
# *Natural · Equi · Non-Equi · Self · INNER · LEFT · RIGHT · FULL OUTER · CROSS*


# ========================================================
# Natural Join
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 3 — Join Types
# ========================================================

'''
[Definition]
  - A NATURAL JOIN maps rows implicitly using all common column names between the two tables defined in the FROM clause
  - Best used when you need to join on all common columns and retrieve the full column set from both tables
  - The developer does not need to specify the joining column(s) — MySQL identifies them automatically
[Example — NATURAL JOIN between CUSTOMER and ACCOUNT]
[Output Explanation]
  - NATURAL JOIN implicitly joins on CUST_ID — the common column
  - Output includes all columns from both tables (CUST_ID appears only once)
  - Result is equivalent to an INNER JOIN on CUST_ID
  NOTE: 💡 Natural joins take all key columns of the first table and then try to match them with the other table's columns.
[Restrictions on Natural Joins]
  - Requires curated (unique, clean) data in the common columns — duplicates cause too many rows without meaningful relationships
  - High chance of returning excess rows if duplicate values exist in joining key columns
  - Cannot handle NULL values in joining key columns — NULL ≠ NULL in implicit matching, so those rows are silently dropped
[Example — NATURAL JOIN across Three Tables]
'''


# Example 1 — Natural Join
sql = '''
-- MySQL automatically detects CUST_ID as the common column
SELECT * FROM CUSTOMER NATURAL JOIN ACCOUNT;
'''


# Example 2 — Natural Join
sql = '''
-- CUST_ID links CUSTOMER→ACCOUNT; ACCT_NUM links ACCOUNT→TRANSACTION
SELECT * FROM CUSTOMER
NATURAL JOIN ACCOUNT
NATURAL JOIN TRANSACTION;
'''


# ========================================================
# Queries with Three or More Tables
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 3 — Join Types
# ========================================================

'''
[Concept]
  - SELECT statements can join three or more tables to understand complex relationships between business entities
  - Each additional table requires at least one additional ON condition
  - Rule: for N tables , you need at least N−1 join conditions
[Common Key Columns in the Bank Schema]
  - CUST_ID — common key between CUSTOMER ↔ ACCOUNT
  - ACCT_NUM — common key between ACCOUNT ↔ TRANSACTION
'''


# ========================================================
# Equi-Join (INNER JOIN with = operator)
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 3 — Join Types
# ========================================================

'''
[Definition]
  - Like NATURAL JOIN, the EQUI-JOIN matches rows using common key columns — but the joining columns are explicitly specified
  - Equi-Join is also called INNER JOIN and uses the equal ( = ) operator in the ON or WHERE clause
[Advantages over Natural Join]
  - Efficiently handles NULL values — use IFNULL() to replace NULLs before comparison
  - Assigns default values by replacing NULL values in joining key columns, ensuring records are not dropped from output
[Example — Equi-Join with NULL handling using IFNULL]
[Example — Equi-Join using USING clause]
  NOTE: 💡 USING (column) is a cleaner syntax for EQUI-JOIN — it identifies the common joining key column in both tables and produces all matching rows. The output column appears only once (no duplicate key column).
'''


# Example 1 — Equi-Join (INNER JOIN with = operator)
sql = '''
-- IFNULL replaces NULL Balance with 0 so comparison doesn't drop the row
SELECT BA.Acct_Num, BA.Acct_type, BA.Balance, TR.Tran_Amount
FROM   ACCOUNT BA
JOIN   TRANSACTION TR
WHERE  BA.Acct_Num = TR.Acct_Num
   AND IFNULL(BA.BALANCE, 0) = TR.Tran_Amount;
'''


# Example 2 — Equi-Join (INNER JOIN with = operator)
sql = '''
-- USING clause replaces the WHERE + equal operator approach
SELECT cust_id, Name, Acct_Num
FROM   CUSTOMER
JOIN   ACCOUNT
USING (CUST_ID);
'''


# ========================================================
# Non-Equi Join
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 3 — Join Types
# ========================================================

'''
[Definition]
  - A Non-Equi Join uses comparison operators other than = to join tables: > , < , <> , NOT , BETWEEN , LIKE
  - Filters records in one table and maps the remaining rows across the other table's rows
  - Widely used for creating different dimensional reports and range-based lookups
[Example — Non-Equi Join: Privileged Interest Rate (> 7%)]
[Output Explanation]
  - Bank decided to provide a privileged interest rate of 8% to Savings and Fixed Deposit account holders
  - NOT LIKE '%CARDS%' filters out Credit Card accounts (they are not eligible)
  - Interest_type column shows "PRIVILEGED" for all qualifying accounts
'''


# Example 1 — Non-Equi Join
sql = '''
-- Find accounts eligible for privileged interest rate (> 7%)
-- Excludes CREDIT CARD accounts
SELECT AC.Acct_Num, AC.Acct_type,
       IR.Rate     Modified_rate,
       IR.Acct_type Interest_type
FROM   ACCOUNT AC
JOIN   INTEREST IR
WHERE  IR.RATE > 0.07
  AND  AC.Acct_Type NOT LIKE '%CARDS%';
'''


# ========================================================
# Self Join
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 3 — Join Types
# ========================================================

'''
[Definition]
  - A SELF JOIN joins a table to itself using two different aliases
  - Applied when meaningful hierarchical or comparative data exists within the same table
  - Used to compare rows within the same table side-by-side
[Example — Side-by-Side Current vs Previous Month Transactions]
[Output Explanation]
  - T1 and T2 both point to the same TRANSACTION table — this is the Self Join
  - The T1.Tran_date > T2.Tran_date condition ensures T1 is always the more recent transaction
  - Result: comparative current vs previous month details from one single TRANSACTION table
'''


# Example 1 — Self Join
sql = '''
-- T1 = current month (later date), T2 = previous month (earlier date)
-- Both T1 and T2 refer to the same TRANSACTION table
SELECT T1.Acct_Num          AS Account,
       T1.Tran_date         AS current_month,
       T1.Tran_Amount       AS Latest_transaction,
       T2.Tran_date         AS previous_month,
       T2.Tran_Amount       AS Previous_transaction
FROM   TRANSACTION T1
JOIN   TRANSACTION T2
ON     T1.Acct_Num = T2.Acct_Num
   AND  T1.Tran_date > T2.Tran_date;
'''


# ### Section 4 — Outer Joins & CROSS JOIN
# *INNER JOIN · LEFT JOIN · RIGHT JOIN · FULL OUTER JOIN · CROSS JOIN*


# ========================================================
# INNER JOIN
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 4 — Outer Joins & CROSS JOIN
# ========================================================

'''
[Definition]
  - The INNER JOIN is the default type of join — it selects only matching rows in both tables using the common joining column
  - It represents the intersection of two tables (rows that exist in both)
  - Non-matching rows from either table are excluded
TABLE A 
 TABLE B 
 MATCH 
 INNER JOIN = Intersection only
[Syntax]
[Example — Customer and Account Details]
[Output Explanation]
  - Only records where cust_id exists in both CUSTOMER and ACCOUNT are returned
  - A customer registered in CUSTOMER but with no account in ACCOUNT table will not appear
  - Oliver (123001) appears twice — he has two accounts (SAVINGS and FIXED DEPOSITS)
'''


# Example 1 — INNER JOIN
sql = '''
SELECT column_name(s)
FROM   table1
INNER JOIN table2
ON     table1.column_name = table2.column_name;
'''


# Example 2 — INNER JOIN
sql = '''
-- Returns ONLY customers who have at least one account
SELECT BC.cust_id, BC.name, BA.Acct_Num, BA.Balance
FROM   CUSTOMER BC
INNER JOIN ACCOUNT BA
ON     BC.cust_id = BA.cust_id;
'''


# ========================================================
# LEFT JOIN (Left Outer Join)
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 4 — Outer Joins & CROSS JOIN
# ========================================================

'''
[Definition]
  - The LEFT JOIN returns:
 
 All rows from the left table (even with no match in the right table) 
 Matching rows from the right table where the join condition is met 
 Where no match exists in the right table — right-table columns appear as NULL
TABLE A 
 TABLE B 
 LEFT JOIN = All of A + Matching B
[Syntax]
[Example — All Accounts, Even Those With No Transactions]
[Output Explanation]
  - LEFT JOIN extracts matching records from both tables on ACCOUNT_NUMBER
  - For accounts with no transactions (e.g., account 4000-1956-2900), all right-table columns (Tran_Account, Tran_Amount, Channel) appear as NULL
  - This is useful for finding dormant accounts — accounts that exist but have never been used
'''


# Example 1 — LEFT JOIN (Left Outer Join)
sql = '''
SELECT [Column List]
FROM   [Table 1] LEFT OUTER JOIN [Table 2]
ON     [Table 1 Column] = [Table 2 Column]
WHERE  [Condition];
-- Note: the word OUTER is optional — LEFT JOIN is also valid
'''


# Example 2 — LEFT JOIN (Left Outer Join)
sql = '''
-- Shows ALL accounts (left table); NULLs appear where no transaction exists
SELECT BA.Acct_Num, BA.Balance,
       BT.Acct_Num AS Tran_Account,
       BT.Tran_Amount, BT.Channel
FROM   ACCOUNT BA
LEFT JOIN TRANSACTION BT
ON     BA.Acct_Num = BT.Acct_Num
ORDER BY 1;
'''


# ========================================================
# RIGHT JOIN (Right Outer Join)
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 4 — Outer Joins & CROSS JOIN
# ========================================================

'''
[Definition]
  - The RIGHT JOIN returns:
 
 All rows from the right table (even with no match in the left table) 
 Matching rows from the left table where the join condition is met 
 Where no match exists in the left table — left-table columns appear as NULL
TABLE A 
 TABLE B 
 RIGHT JOIN = Matching A + All of B
[Syntax]
[Example — Transactions for Expired/Inactive Accounts]
[Output Explanation]
  - All transactions are returned — even those whose account no longer exists in ACCOUNT table
  - For transactions with no matching account, BA.Acct_Num and BA.Balance show as NULL
  - Useful for catching pending/orphaned credit card transactions on expired accounts
'''


# Example 1 — RIGHT JOIN (Right Outer Join)
sql = '''
SELECT [Column List]
FROM   [Table 1] RIGHT OUTER JOIN [Table 2]
ON     [Table 1 Column] = [Table 2 Column]
WHERE  [Condition];
-- Note: the word OUTER is optional — RIGHT JOIN is also valid
'''


# Example 2 — RIGHT JOIN (Right Outer Join)
sql = '''
-- Finds transactions that exist in TRANSACTION but have no matching ACCOUNT
-- Typical case: credit card account expired but transactions still pending
SELECT BA.Acct_Num, BA.Balance,
       BT.Acct_Num AS Tran_Account,
       BT.Tran_Amount, BT.Channel
FROM   ACCOUNT BA
RIGHT JOIN TRANSACTION BT
ON     BA.Acct_Num = BT.Acct_Num;
'''


# ========================================================
# FULL OUTER JOIN
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 4 — Outer Joins & CROSS JOIN
# ========================================================

'''
[Definition]
  - A FULL OUTER JOIN combines the results of both LEFT JOIN and RIGHT JOIN
  - Returns: all rows from the left table + all rows from the right table + matched rows (with NULLs where no match exists on either side)
  - MySQL does not support FULL OUTER JOIN directly — it is simulated using UNION of a LEFT JOIN and a RIGHT JOIN
TABLE A 
 TABLE B 
 FULL OUTER = All rows from both
[Example — FULL OUTER JOIN using UNION]
[Output Explanation]
  - LEFT JOIN result: all active accounts with their transactions (NULL where no transaction)
  - RIGHT JOIN result: all transactions including those whose accounts have expired (NULL for account details)
  - UNION merges the two result sets without duplicates
  - Purpose: get a complete view of all accounts and all transactions to identify data quality issues
  NOTE: ⚠️ MySQL does NOT natively support FULL OUTER JOIN. Always simulate it using: LEFT JOIN UNION RIGHT JOIN.
'''


# Example 1 — FULL OUTER JOIN
sql = '''
-- Part 1: All accounts + their transactions (LEFT JOIN)
SELECT BA.Acct_Num, BT.Acct_Num AS Tran_Account, BT.Tran_Amount
FROM   ACCOUNT BA
LEFT JOIN TRANSACTION BT
ON     BA.Acct_Num = BT.Acct_Num

UNION

-- Part 2: All transactions + their accounts (RIGHT JOIN)
SELECT BA.Acct_Num, BT.Acct_Num AS Tran_Account, BT.Tran_Amount
FROM   ACCOUNT BA
RIGHT JOIN TRANSACTION BT
ON     BA.Acct_Num = BT.Acct_Num;
'''


# ========================================================
# CROSS JOIN
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 4 — Outer Joins & CROSS JOIN
# ========================================================

'''
[Definition]
  - A CROSS JOIN produces the Cartesian product of two tables — every row from the left table is combined with every row from the right table
  - No ON or WHERE condition is needed — all combinations are returned
  - If Table A has M rows and Table B has N rows, the result has M × N rows
[Example — Send ALL Bank Notifications to ALL Customers]
[Output Explanation]
  - Every customer is paired with every message — mimicking a broadcast notification system
  - If there are 8 customers and 5 messages, the result has 8 × 5 = 40 rows
  - Business use: blast all bank notices (lockdown, withdrawal limits, etc.) to all customers simultaneously
  NOTE: ⚠️ CROSS JOINs on large tables can return billions of rows. Use only when a Cartesian product is genuinely required.
[Variation — Implicit Cartesian Product (no JOIN keyword)]
  - This is the implicit form of a Cartesian product — listing two tables with a comma and no WHERE join condition
  - Equivalent in result to writing CUSTOMER CROSS JOIN ACCOUNT
  - This is how accidental Cartesian products happen — forgetting the WHERE condition in a two-table query produces this silently
'''


# Example 1 — CROSS JOIN
sql = '''
-- Each customer paired with every message in the MESSAGE table
SELECT BC.Cust_id, BC.Name, MG.NOTICE
FROM   CUSTOMER BC
CROSS JOIN MESSAGE MG;
'''


# Example 2 — CROSS JOIN
sql = '''
-- Returns ALL combinations of CUSTOMER x ACCOUNT rows
-- No WHERE condition = Cartesian Product (same result as CROSS JOIN)
SELECT * FROM CUSTOMER, ACCOUNT;
'''


# ========================================================
# JOIN Multiple Tables
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 4 — Outer Joins & CROSS JOIN
# ========================================================

'''
[Concept]
  - Complex reports that need customer details, account info, and transactions in one query require multi-table JOINs
  - Different JOIN types can be mixed in a single query (e.g., INNER JOIN for required data, LEFT JOIN for optional data)
  - There is no maximum limit on the number of tables — expert SQL writers commonly join 20–30 tables in production
[Example — CUSTOMER + ACCOUNT + TRANSACTION (INNER + LEFT JOIN)]
[Output Explanation]
  - INNER JOIN on CUSTOMER–ACCOUNT: ensures only customers who actually have accounts appear
  - LEFT JOIN on ACCOUNT–TRANSACTION: all accounts shown even if they have no transactions (those rows get NULL in Tran_Amount and Channel)
  - Mixed JOIN types in one query is the standard pattern for real-world reports
'''


# Example 1 — JOIN Multiple Tables
sql = '''
-- INNER JOIN ensures only customers with accounts are included
-- LEFT JOIN includes accounts even if no transactions exist yet
SELECT BC.cust_id,  BC.Name,     BC.Address,
       BA.Acct_Num,  BA.Balance,
       BT.Tran_Amount, BT.Channel
FROM       CUSTOMER BC
INNER JOIN ACCOUNT BA     ON BA.cust_id  = BC.cust_id
LEFT JOIN  TRANSACTION BT ON BA.Acct_Num = BT.Acct_Num;
'''


# ### Section 5 — SQL Considerations for Multiple Queries
# *Qualified names · Wildcard * · Multi-join rules · Oracle (+) operator*


# ========================================================
# Qualified Column Names
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 5 — SQL Considerations for Multiple Queries
# ========================================================

'''
[Definition]
  - Qualified names — table names and column names that are unambiguous and unique within the database schema
  - Data architects and Business Analysts use qualified names to design clear models and maintain lineage of the business flow
  - Qualified names are standards established by Data Management and Governance authorities and banking regulators
[Example]
  NOTE: 💡 When two joined tables share a column name (e.g., both have CUST_ID ), the column becomes ambiguous . Use qualified references like CUSTOMER.CUST_ID or table aliases like BC.CUST_ID .
'''


# Example 1 — Qualified Column Names
sql = '''
-- CUSTOMER is a qualified table name — unambiguous in this schema
-- Cust_Id and Name are qualified column names — unique within CUSTOMER
SELECT Cust_Id, Name, Address FROM CUSTOMER;
'''


# ========================================================
# All Column Selection — Wildcard *
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 5 — SQL Considerations for Multiple Queries
# ========================================================

'''
[Concept]
  - Any RDBMS (including MySQL) allows tables to have more than 250 columns , depending on the size of individual columns
  - For wide tables with many columns, the wildcard * selects all columns at once
  - Real-world example: a TRANSACTION table can have 50+ columns because modern payments happen through many modes (UPI, ATM, POS, IVR, etc.)
  NOTE: ⚠️ Using SELECT * in production is generally discouraged — it retrieves all columns including those you may not need, which impacts performance.
'''


# Example 1 — All Column Selection — Wildcard *
sql = '''
-- Select ALL columns from CUSTOMER
SELECT * FROM CUSTOMER;

-- Select ALL columns from CUSTOMER × ACCOUNT join
SELECT * FROM CUSTOMER NATURAL JOIN ACCOUNT;
'''


# ========================================================
# Rules for Multi-Join Queries
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 5 — SQL Considerations for Multiple Queries
# ========================================================

'''
[Key Rules]
  - N−1 Rule: For N tables joined in a query, you need at least (N − 1) join conditions 
 
 4 tables joined → at least 3 join conditions required
  - Preferred: unique column values in the driving (left/first) table when using INNER JOIN — avoids cross-distribution of rows
[Understanding Cardinality in the Bank Schema]
  - CUST_ID in CUSTOMER — Unique (PK) — One identity per customer
  - CUST_ID in ACCOUNT — Repeated (FK) — A customer can have multiple accounts
  - ACCT_NUM in ACCOUNT — Unique (PK) — Each account has one number
  - ACCT_NUM in TRANSACTION — Repeated (FK) — An account can have many transactions
  NOTE: 💡 Always join from the unique-key side to the foreign-key side to get predictable one-to-many expansion of rows, not a Cartesian explosion.
'''


# ========================================================
# Join Notation using (+) Operator — Oracle Non-ANSI
# 4 — Multiple Table Queries & JOINs
# SECTION: Section 5 — SQL Considerations for Multiple Queries
# ========================================================

'''
[Definition]
  - The (+) operator is a Non-ANSI, Oracle-specific notation for performing LEFT and RIGHT outer joins in the WHERE clause
  - Not supported in MySQL — only in Oracle RDBMS
  - Developers should be familiar with it when reading legacy Oracle SQL code
[LEFT JOIN using (+)]
[RIGHT JOIN using (+)]
  NOTE: ⚠️ If the (+) operator is omitted, the query silently converts to an INNER JOIN. Developers familiar with Oracle code must be careful when migrating to MySQL ANSI syntax.
[Oracle (+) vs MySQL ANSI equivalent]
  - WHERE A.col = B.col(+) in Oracle → FROM A LEFT JOIN B ON A.col = B.col in MySQL
  - WHERE (+)A.col = B.col in Oracle → FROM A RIGHT JOIN B ON A.col = B.col in MySQL
'''


# Example 1 — Join Notation using (+) Operator — Oracle Non-ANSI
sql = '''
-- (+) on RIGHT side = LEFT JOIN in Oracle
-- The table with (+) is the optional (right) side
SELECT BA.Acct_Num, BA.Balance_Amount,
       AT.Tran_Amount, AT.Channel
FROM   ACCOUNT    BA,
       TRANSACTION AT
WHERE  BA.Acct_Num = AT.Account_Number(+);
'''


# Example 2 — Join Notation using (+) Operator — Oracle Non-ANSI
sql = '''
-- (+) on LEFT side = RIGHT JOIN in Oracle
SELECT BA.Acct_Num, BA.Balance_Amount,
       AT.Tran_Amount, AT.Channel
FROM   ACCOUNT    BA,
       TRANSACTION AT
WHERE  (+)BA.Acct_Num = AT.Account_Number
  AND  BA.ACCOUNT_STATUS = 'ACTIVE';
'''


# ---

# ## Session 5 — Subqueries & Query Expressions

# *Subqueries · EXISTS / IN · ANY / ALL · Nested & Correlated · WITH Clause*


# ### Section 1 — Database Schema (Bank_Inventory)
# *Tables used throughout Session 5 examples*


# ========================================================
# E-R Diagram — Bank_Inventory Schema
# 5 — Subqueries & Query Expressions
# SECTION: Section 1 — Database Schema (Bank_Inventory)
# ========================================================

'''
[Table: INVENTORY]
  - Product VARCHAR(15) — Bank products purchased from vendor (e.g. Plastic Visa debit/credit cards)
  - Quantity INT — Quantity purchased from vendor
  - Purchase_cost REAL — Purchase cost of product from vendor
  - Month INT — Month during which inventory is maintained
[Table: PROFIT_LOSS]
  - Branch VARCHAR(15) — Bank branch across different locations
  - Banker SMALLINT — Salesperson (banker)
  - Product VARCHAR(15) — Product details maintained with banker at branches
  - Cost INT — Purchase cost + service charges + maintenance charges at branch
  - Revenue INT — Revenue generated from selling the product
  - Estimated_Profit INT — Expected profit (may not equal actual calculated profit)
  - Month SMALLINT — Month of the record
  NOTE: ℹ️ The INVENTORY and PROFIT_LOSS tables are linked on the Product column. All SQL in this session uses the Bank_Inventory database. The Account, Transaction, Customer, and Message tables from previous sessions are also referenced in subquery examples.
'''


# ### Section 2 — Introduction to Subqueries
# *Definition · Types · Benefits*


# ========================================================
# What is a Subquery?
# 5 — Subqueries & Query Expressions
# SECTION: Section 2 — Introduction to Subqueries
# ========================================================

'''
[Definition]
  - A subquery is a SELECT query nested inside another (main) query
  - Like JOINs, subqueries require common key columns to connect with the main query
  - A subquery is also called a virtual table — it wraps an independent piece of business logic
  - Subqueries execute independently and share their results with the main query, reducing overall complexity
  NOTE: 💡 Think of a subquery as a "pre-computed answer" that the main query uses. The database runs the inner query first, then feeds its result to the outer query.
[Where Can Subqueries Be Written?]
  - SELECT clause — as a scalar derived column value
  - FROM clause — as a derived table (must be aliased)
  - WHERE clause — most common: using IN, EXISTS, ANY, ALL, =, <, >
  - HAVING clause — to filter grouped results dynamically
'''


# ========================================================
# Types of Subqueries
# 5 — Subqueries & Query Expressions
# SECTION: Section 2 — Introduction to Subqueries
# ========================================================

'''
[Classification by Return Type]
  - Single Row Subquery — Returns a single scalar value; fed to the main query through =, <, >
  - Multiple Row Subquery — Returns multiple rows; used with IN, ANY, ALL, EXISTS
  - Multiple Column Subquery — Returns one or more columns; matched against outer query columns
  - Correlated Subquery — Depends on the outer query for each row it processes; re-executes for every outer row
  - Nested Subquery — A subquery placed inside another subquery (A → B → C…)
  NOTE: ⚠️ Exam Trap: A correlated subquery is NOT independent — it references a column from the outer query inside its WHERE clause (e.g. WHERE T.Acct_Num = A.Acct_Num ). An independent subquery runs once; a correlated one runs once per outer row.
'''


# ========================================================
# Benefits of Subqueries
# 5 — Subqueries & Query Expressions
# SECTION: Section 2 — Introduction to Subqueries
# ========================================================

'''
[Key Benefits]
  - Separates complex business logic from the main query — easier to read and maintain
  - Easier to debug an individual subquery than a large multi-table JOIN
  - When used correctly, subqueries improve query performance
  - Can be placed in SELECT, FROM, WHERE, or HAVING — highly flexible
'''


# ### Section 3 — Subqueries in the WHERE Clause
# *IN · = (Scalar) · EXISTS · ANY · ALL*


# ========================================================
# Subquery in WHERE — Using IN
# 5 — Subqueries & Query Expressions
# SECTION: Section 3 — Subqueries in the WHERE Clause
# ========================================================

'''
[Operators Available]
  - Multi-row operators: IN, EXISTS, ANY, ALL — compare against multiple rows returned by subquery
  - Single-row operators: =, <, >, <=, >= — compare against a single scalar value from subquery
[How IN Works with a Subquery]
  - The subquery executes first and independently , returning a list of values
  - The main query then checks each of its rows: if the key column is IN that list, the row is included
  - Use IN when the main query must search all rows returned by the subquery
[Example — Find accounts that have ATM withdrawal transactions]
  OUTPUT: Result 
 Acct_Num | Balance | Acct_type | Acct_status 
 4000-1956-3456 | 200000 | SAVINGS | ACTIVE 
 4000-1956-5102 | 300000 | SAVINGS | ACTIVE
[Execution Flow]
  - Step 1 — Inner query runs: fetches all Acct_Num from TRANSACTION where Channel = 'ATM withdrawal'
  - Step 2 — Outer query runs: checks if each ACCOUNT's Acct_Num is in that list
  - Step 3 — Only matching accounts are returned
'''


# Example 1 — Subquery in WHERE — Using IN
sql = '''
SELECT A.Acct_Num, A.Balance, A.Acct_type, A.Acct_status
FROM ACCOUNT A
WHERE A.Acct_Num IN
    (SELECT T.Acct_Num
     FROM   TRANSACTION T
     WHERE  T.Channel = 'ATM withdrawal');
'''


# ========================================================
# Subquery Comparison Test (Scalar / Single-Row)
# 5 — Subqueries & Query Expressions
# SECTION: Section 3 — Subqueries in the WHERE Clause
# ========================================================

'''
[Concept]
  - Subquery results are dynamic — the developer does not hardcode the input value
  - The subquery returns a single (scalar) value that is used in the WHERE condition
  - Use single-row operators (=, <, >) when the subquery returns exactly one value
[Example — Find transactions on the most recent holiday]
  OUTPUT: Result (subquery returns scalar: 2020-04-24) 
 Acct_Num | Tran_Amount | Tran_Date 
 4000-1956-2001 | -3000.00 | 2020-04-24 
 4000-1956-5102 | -6500.00 | 2020-04-24 
 5000-1700-9911 | 2000.00 | 2020-04-24
  NOTE: 💡 The = operator requires the subquery to return exactly one row . Using MAX() or MIN() guarantees this. If the subquery could return multiple rows, use IN instead.
'''


# Example 1 — Subquery Comparison Test (Scalar / Single-Row)
sql = '''
SELECT Acct_Num, Tran_Amount, Tran_Date
FROM   TRANSACTION
WHERE  Tran_Date = (SELECT MAX(event_dt)
                    FROM   MESSAGE
                    WHERE  Event = 'Holiday');
'''


# ========================================================
# Set Membership Test — IN with Multiple Rows
# 5 — Subqueries & Query Expressions
# SECTION: Section 3 — Subqueries in the WHERE Clause
# ========================================================

'''
[Concept]
  - IN operator performs a multi-row operation — subquery returns a list and main query checks membership
  - The subquery and main query must share the same data type on the matching column
  - Values returned by subquery drive which rows the outer query returns
[Example — Get account details for accounts with ATM withdrawals]
  NOTE: ℹ️ Multiple values are provided to the main query through the IN list. The outer query only executes for accounts whose Acct_Num appears in the subquery result set.
'''


# Example 1 — Set Membership Test — IN with Multiple Rows
sql = '''
SELECT A.Acct_Num, A.Balance, A.Acct_type, A.Acct_status
FROM   ACCOUNT A
WHERE  A.Acct_Num IN
       (SELECT Acct_Num
        FROM   TRANSACTION
        WHERE  Channel = 'ATM withdrawal');
'''


# ========================================================
# Subquery Existence Test — EXISTS
# 5 — Subqueries & Query Expressions
# SECTION: Section 3 — Subqueries in the WHERE Clause
# ========================================================

'''
[Concept]
  - EXISTS returns TRUE (1) if the subquery produces at least one row, FALSE (0) otherwise
  - The subquery is re-executed for each row of the main query — it is a correlated subquery by nature
  - Common key columns connect the subquery to the outer query
  - Inside the subquery, a constant such as 'yes' is typically selected — the actual value doesn't matter, only whether rows exist
[Example — Return all accounts that have at least one transaction]
  OUTPUT: Result — All 10 accounts that have transactions 
 Acct_Num | Balance | acct_type | acct_status 
 4000-1956-3456 | 200000 | SAVINGS | ACTIVE 
 4000-1956-2001 | 400000 | SAVINGS | ACTIVE 
 5000-1700-6091 | 7500000 | FIXED DEPOSITS | ACTIVE 
 … (7 more rows)
[How EXISTS Works]
  - For every account A, MySQL runs the inner query with that account's Acct_Num
  - If any transaction row exists for that account → EXISTS = TRUE → account is included
  - If no matching transaction → EXISTS = FALSE → account is excluded
'''


# Example 1 — Subquery Existence Test — EXISTS
sql = '''
SELECT A.Acct_Num, A.Balance, A.acct_type, A.acct_status
FROM   ACCOUNT A
WHERE  EXISTS (SELECT 'yes'
               FROM   TRANSACTION T
               WHERE  T.Acct_Num = A.Acct_Num);
'''


# ========================================================
# Quantified Test — ANY Operator
# 5 — Subqueries & Query Expressions
# SECTION: Section 3 — Subqueries in the WHERE Clause
# ========================================================

'''
[Concept]
  - Quantified test = "validating many records" — the subquery returns multiple rows and the operator walks through all of them
  - ANY — the condition is TRUE if it holds for at least one value in the subquery result set
  - Used with range operators: > ANY , < ANY
  - > ANY effectively means "greater than the minimum value in the subquery list"
[Example — Get all transactions after ANY holiday]
  OUTPUT: Subquery returns holidays: 2020-02-19, 2020-03-16, 2020-04-24 
 ANY picks the earliest (2020-02-19) → returns all transactions after Feb 19 
 Acct_Num | Tran_Date 
 4000-1956-2001 | 2020-03-23 
 4000-1956-2001 | 2020-04-24 
 4000-1956-2001 | 2020-04-26 
 4000-1956-2001 | 2020-03-15
  NOTE: ANY vs IN — Key Difference 
 
 ANY with > — returns all transactions after any holiday (range check, 4 rows above) 
 IN — returns only transactions on a holiday (exact match, only 1 row: 2020-04-24) 
 Replacing ANY with IN dramatically reduces results and changes the query meaning
'''


# Example 1 — Quantified Test — ANY Operator
sql = '''
SELECT Acct_Num, Tran_Date
FROM   TRANSACTION
WHERE  Acct_Num = '4000-1956-2001'
  AND  Tran_Date > ANY
       (SELECT Event_dt
        FROM   Message
        WHERE  event = 'Holiday');
'''


# ========================================================
# Quantified Test — ALL Operator
# 5 — Subqueries & Query Expressions
# SECTION: Section 3 — Subqueries in the WHERE Clause
# ========================================================

'''
[Concept]
  - ALL — the condition must hold for every single value in the subquery result
  - > ALL means "greater than the maximum value" in the subquery list
  - < ALL means "less than the minimum value" in the subquery list
  - ALL is stricter than ANY — far fewer rows typically qualify
[Example 1 — < ALL: Transactions BEFORE all holidays]
  OUTPUT: Result — transactions before the earliest holiday (2020-02-19) 
 Acct_Num | Tran_Date 
 4000-1956-2001 | 2020-02-14 
 4000-1956-2001 | 2020-01-19
[Example 2 — > ALL: Transactions AFTER all holidays]
  OUTPUT: Result — only transaction after the latest holiday (2020-04-24) 
 Acct_Num | Tran_Date 
 4000-1956-2001 | 2020-04-26
'''


# Example 1 — Quantified Test — ALL Operator
sql = '''
SELECT Acct_Num, Tran_Date
FROM   TRANSACTION
WHERE  Acct_Num = '4000-1956-2001'
  AND  Tran_Date < ALL
       (SELECT Event_dt
        FROM   MESSAGE
        WHERE  event = 'Holiday');
'''


# Example 2 — Quantified Test — ALL Operator
sql = '''
SELECT Acct_Num, Tran_Date
FROM   TRANSACTION
WHERE  Acct_Num = '4000-1956-2001'
  AND  Tran_Date > ALL
       (SELECT Event_dt
        FROM   MESSAGE
        WHERE  event = 'Holiday');
'''


# ### Section 4 — Outer References & FROM Clause Subqueries
# *Derived tables · Filtering before joining*


# ========================================================
# Outer References — Subquery in FROM Clause (Derived Table)
# 5 — Subqueries & Query Expressions
# SECTION: Section 4 — Outer References & FROM Clause Subqueries
# ========================================================

'''
[Concept]
  - A subquery placed in the FROM clause acts as a derived table (temporary virtual table)
  - It executes independently, then its result is referenced by the main query through an alias
  - Benefits over referencing the full table:
 
 Only selected rows and columns are exposed to the outer query — leaner join 
 Complex filtering logic is isolated from the main query
[Example — Join accounts with transactions over 23,000]
  OUTPUT: Result — accounts that had large transactions 
 Acct_Num | Tran_Amount 
 5000-1700-6091 | 40000.00 
 4000-1956-9977 | 50000.00
[Execution Flow]
  - Step 1 — Subquery (aliased Sub_T ) runs first: filters TRANSACTION rows where amount > 23000
  - Step 2 — Main query joins ACCOUNT with Sub_T on matching Acct_Num
'''


# Example 1 — Outer References — Subquery in FROM Clause (Derived Table)
sql = '''
SELECT A.Acct_Num, Sub_T.Tran_Amount
FROM   ACCOUNT A,
       (SELECT Acct_Num, Tran_Amount
        FROM   TRANSACTION
        WHERE  Tran_amount > 23000) Sub_T
WHERE  A.Acct_Num = Sub_T.Acct_Num;
'''


# ========================================================
# Subquery in FROM Clause — JOIN with Derived Table
# 5 — Subqueries & Query Expressions
# SECTION: Section 4 — Outer References & FROM Clause Subqueries
# ========================================================

'''
[Concept]
  - A FROM-clause subquery acts like a view table derived from conditions
  - It can be used inline with JOINs — the derived table is treated as a regular table in the join
[Example — Retrieve account details for transactions on holidays]
  OUTPUT: Result — holiday transactions with account info 
 Acct_Num | Tran_Amount | Tran_Date 
 4000-1956-2001 | -3000.00 | 2020-04-24 
 5000-1700-6091 | 40000.00 | 2020-02-19 
 4000-1956-5102 | -6500.00 | 2020-04-24 
 5000-1700-9911 | 2000.00 | 2020-04-24
[Execution Flow]
  - Step 1 — Inner subquery (aliased Tran ) joins Transaction and Message to find holiday transactions
  - Step 2 — Outer query joins ACCOUNT with Tran on Acct_Num to attach account metadata
'''


# Example 1 — Subquery in FROM Clause — JOIN with Derived Table
sql = '''
SELECT A.Acct_Num, Tran.Tran_Amount, Tran.Tran_Date
FROM   ACCOUNT A
JOIN (SELECT Acct_Num, Tran_Amount, Tran_Date
      FROM   Transaction, Message
      WHERE  Tran_Date = Event_dt
        AND  event = 'Holiday') Tran
ON  Tran.Acct_Num = A.Acct_Num;
'''


# ### Section 5 — Nested Subqueries
# *Subquery within a subquery · Execution order · IN and JOIN nesting*


# ========================================================
# Nested Subqueries — Overview
# 5 — Subqueries & Query Expressions
# SECTION: Section 5 — Nested Subqueries
# ========================================================

'''
[Definition]
  - A subquery that is embedded inside another subquery — nesting can be many levels deep
  - Any SELECT query supports multiple levels of nesting (A contains B, B contains C, etc.)
  - Each nested subquery executes independently and passes its result up to the next level
[Execution Order]
  - MySQL executes the innermost (lowest-level) subquery first
  - Its result is passed to the next-level subquery, and so on upward
  - The outermost (main) query executes last using all accumulated intermediate results
  NOTE: ℹ️ Memory aid: Think of Russian nesting dolls — you open from the innermost outward. Subquery-C runs first → gives result to B → B gives result to A → A gives result to main query.
'''


# ========================================================
# Nested Subqueries with JOIN
# 5 — Subqueries & Query Expressions
# SECTION: Section 5 — Nested Subqueries
# ========================================================

'''
[Scenario]
  - The main query JOINs the ACCOUNT table with a subquery called Tran_Evnt
  - Tran_Evnt itself JOINs the TRANSACTION table with a deeper subquery called Evnt
  - Evnt is the innermost: it pulls Event and Event_dt from the MESSAGE table
[Example — Account details with holiday transaction info (2-level JOIN nesting)]
  OUTPUT: Result 
 Cust_id | Acct_Num | Balance | Tran_Amount | Event 
 123002 | 4000-1956-2001 | 400000 | -3000.00 | Holiday 
 123004 | 5000-1700-6091 | 7500000 | 40000.00 | Holiday 
 123005 | 4000-1956-5102 | 300000 | -6500.00 | Holiday 
 123009 | 5000-1700-9911 | 2000 | 2000.00 | Holiday
[What Each Level Contributes]
  - Evnt (innermost) — Message table: Event name + Event date
  - Tran_Evnt (middle) — TRANSACTION joined with Evnt: transactions on event days
  - Main query — ACCOUNT joined with Tran_Evnt: adds customer and balance info
  NOTE: 💡 Unlike IN-based nesting, JOIN-based nesting can bring columns from all levels into the final result (see Cust_id, Balance, AND Event all appearing).
'''


# Example 1 — Nested Subqueries with JOIN
sql = '''
SELECT Cust_id, A.Acct_Num, A.Balance,
       Tran_Evnt.Tran_Amount, Event
FROM   ACCOUNT A
JOIN (SELECT Acct_Num, Tran_Amount, Event
      FROM   TRANSACTION
      JOIN (SELECT Event, Event_dt
            FROM   Message) Evnt
      ON Tran_Date = Evnt.Event_dt) Tran_Evnt
ON  A.Acct_Num = Tran_Evnt.Acct_Num;
'''


# ========================================================
# Set Membership Test Using Nested Subqueries (IN)
# 5 — Subqueries & Query Expressions
# SECTION: Section 5 — Nested Subqueries
# ========================================================

'''
[Concept]
  - A chain of IN-based subqueries where each level filters records using values from the level below
  - Innermost subquery executes first; its result is referenced by IN in the next level; and so on up
  - Limitation: Unlike JOIN nesting, IN-based nesting can only return columns from the outermost main query table
[Example — Get transaction details for customers with positive-balance accounts]
[Execution Flow]
  - Step 1 — Innermost: all Cust_Id values from CUSTOMER table
  - Step 2 — Middle: ACCOUNT rows where Cust_Id is in that set AND Balance > 0 → returns Acct_Num list
  - Step 3 — Outer: TRANSACTION rows where Acct_Num is in that Acct_Num list
  NOTE: ⚠️ The final result only shows TRANSACTION columns. IN-based nested subqueries cannot pull columns from inner subquery tables (unlike JOIN nesting).
'''


# Example 1 — Set Membership Test Using Nested Subqueries (IN)
sql = '''
SELECT Acct_Num, Tran_Amount, Channel, Tran_date
FROM   TRANSACTION
WHERE  Acct_Num IN
       (SELECT Acct_Num
        FROM   ACCOUNT
        WHERE  Balance > 0
          AND  Cust_Id IN
               (SELECT Cust_Id
                FROM   CUSTOMER));
'''


# ========================================================
# Set Comparison Using Nested Subqueries (IN + >)
# 5 — Subqueries & Query Expressions
# SECTION: Section 5 — Nested Subqueries
# ========================================================

'''
[Concept]
  - Combines IN (set membership) and comparison operators (>, <) across nested levels
  - The deepest subquery returns a scalar using MAX() — required when the comparison operator expects a single value
[Example — Find customers who made transactions after the most recent holiday]
  OUTPUT: Result — customers who transacted after the last holiday (2020-04-24) 
 Cust_Id | Name | Address | State | Phone 
 123002 | George | 194-6, New Brighton | MN | 189761700 
 123005 | Jacob | 325-7, Mission Dist | SFO | 1897637000
[Why MAX() is Used Here]
  - The > operator requires a scalar (single) value
  - Without MAX(), the subquery could return multiple holiday dates, causing an error
  - MAX() collapses multiple dates to the single latest date → safe for > comparison
'''


# Example 1 — Set Comparison Using Nested Subqueries (IN + >)
sql = '''
SELECT *
FROM   CUSTOMER
WHERE  Cust_Id IN
       (SELECT Cust_Id
        FROM   ACCOUNT
        WHERE  Acct_Num IN
               (SELECT Acct_Num
                FROM   TRANSACTION
                WHERE  Tran_Date >
                       (SELECT MAX(Event_dt)
                        FROM   Message)));
'''


# ### Section 6 — Advanced Subquery Topics
# *WITH Clause · HAVING · Correlated · Scalar · Subquery vs JOIN · Row-Valued · Query Expressions*


# ========================================================
# Subqueries with the WITH Clause (CTE)
# 5 — Subqueries & Query Expressions
# SECTION: Section 6 — Advanced Subquery Topics
# ========================================================

'''
[Concept]
  - A subquery written in the WITH clause plays a factoring role — it is defined once and reused multiple times
  - Once a WITH clause subquery executes, its result is cached and referenced by alias anywhere in the main query
  - Avoids repeating the same subquery in multiple places — critical for complex queries
  - Also known as a Common Table Expression (CTE)
[Example — Assign interest rates to accounts by account type]
  OUTPUT: Result — each account gets its interest rate 
 Acct_num | Acct_type | rate 
 4000-1956-3456 | SAVINGS | 0.04 
 5000-1700-3456 | FIXED DEPOSITS | 0.07 
 4000-1956-2001 | SAVINGS | 0.04 
 … (more rows)
[Key Points]
  - I_RATE acts as a re-usable dataset — can be JOINed or referenced multiple times in the main query
  - SAVINGS accounts get rate 0.04; FIXED DEPOSITS get 0.07
  - Use WITH when the same subquery logic must appear more than once in the query
'''


# Example 1 — Subqueries with the WITH Clause (CTE)
sql = '''
WITH I_RATE AS
     (SELECT Acct_type, rate
      FROM   Interest)
SELECT A.Acct_num, I_RATE.Acct_type, I_RATE.rate
FROM   ACCOUNT A
JOIN   I_RATE
ON     A.Acct_type = I_RATE.Acct_type;
'''


# ========================================================
# Subqueries in the HAVING Clause
# 5 — Subqueries & Query Expressions
# SECTION: Section 6 — Advanced Subquery Topics
# ========================================================

'''
[Concept]
  - HAVING filters grouped results of the main query
  - A subquery in HAVING returns derived values dynamically — no hardcoded threshold needed
  - Allows comparing group-level aggregates against aggregates from another dataset
[Example — Find branches with above-average estimated profit]
  OUTPUT: Result — branches/products with profit above the bank-wide average 
 Branch | Product | Profit 
 Delhi | SuperSave | 20050070 
 Delhi | SmartSav | 30050070 
 Hyd | SmartSav | 60050224 
 Banglr | SmartSav | 30000154 
 Hyd | BusiCard | 35110140
[How It Works]
  - Subquery executes first: computes AVG(estimated_profit) across ALL rows in Profit_Loss
  - Main query groups by Branch and Product, then HAVING filters out groups below the average
'''


# Example 1 — Subqueries in the HAVING Clause
sql = '''
SELECT Branch, Product, SUM(Estimated_profit) AS Profit
FROM   Profit_Loss
GROUP BY Branch, Product
HAVING SUM(Estimated_profit) >
       (SELECT AVG(estimated_profit)
        FROM   Profit_Loss);
'''


# ========================================================
# Correlated Subqueries in the HAVING Clause
# 5 — Subqueries & Query Expressions
# SECTION: Section 6 — Advanced Subquery Topics
# ========================================================

'''
[Concept]
  - The HAVING subquery can correlate with a non-grouping field from the main query
  - The subquery is re-executed for each group produced by the outer query — it is not independent
  - Enables comparing branch-level profit for a specific product against the company-wide average for that same product
[Example — Branches where each product's profit exceeds that product's company average]
  OUTPUT: Result — correlated: per-product company average used as threshold 
 Branch | Product | Profit 
 Delhi | SmartSav | 30050070 
 Delhi | EasyCash | 10050077 
 Hyd | SmartSav | 60050224 
 Banglr | SmartSav | 30000154 
 Hyd | BusiCard | 35110140
[Why This Is Different from the Non-Correlated Version]
  - Non-correlated (previous slide): compares every branch against a single bank-wide average
  - Correlated: for SmartSav, compares each branch's SmartSav profit against SmartSav's average across all branches — a much more targeted comparison
  - The subquery re-executes for each (Branch, Product) group with that product's value fed in
'''


# Example 1 — Correlated Subqueries in the HAVING Clause
sql = '''
SELECT Branch, P1.Product, SUM(Estimated_profit) AS Profit
FROM   PROFIT_LOSS P1
GROUP BY Branch, P1.Product
HAVING SUM(Estimated_profit) >
       (SELECT AVG(Estimated_profit)
        FROM   PROFIT_LOSS P2
        WHERE  P2.Product = P1.Product);
'''


# ========================================================
# Scalar Valued Expression using Subquery
# 5 — Subqueries & Query Expressions
# SECTION: Section 6 — Advanced Subquery Topics
# ========================================================

'''
[Concept]
  - A scalar value = a single column value / single record (one dimension)
  - In a scalar valued expression, a subquery returning one row is placed inside the SELECT clause or CASE statement
  - The scalar subquery executes for every row returned by the main query (like a correlated subquery)
  - One dimension (single row) vs two dimensions (multiple rows and columns)
[Example — Label each transaction as HOLIDAY or WORKING DAY]
  OUTPUT: Result (scalar subquery returns 2020-04-24 — most recent holiday) 
 Acct_Num | tran_date | Event 
 4000-1956-2001 | 2020-04-24 | HOLIDAY 
 4000-1956-2001 | 2020-04-26 | WORKING DAY 
 4000-1956-5102 | 2020-04-24 | HOLIDAY 
 4000-1956-5102 | 2020-04-25 | WORKING DAY 
 5000-1700-9911 | 2020-04-24 | HOLIDAY
  NOTE: ℹ️ The scalar subquery SELECT MAX(Event_dt) FROM Message returns a single date (2020-04-24). Each transaction's Tran_Date is compared against that constant through CASE.
'''


# Example 1 — Scalar Valued Expression using Subquery
sql = '''
SELECT Acct_Num, tran_date,
       CASE WHEN Tran_Date =
            (SELECT MAX(Event_dt) FROM Message)
            THEN 'HOLIDAY'
            ELSE 'WORKING DAY'
       END AS Event
FROM   TRANSACTION
WHERE  Tran_Date > "2020-03-23";
'''


# ========================================================
# Subqueries vs JOINs
# 5 — Subqueries & Query Expressions
# SECTION: Section 6 — Advanced Subquery Topics
# ========================================================

'''
  NOTE: Subquery vs JOIN — Side-by-Side 
 Same result, two approaches 
 
 MySQL — Subquery Version 
 SELECT Acct_Num, Tran_Amount
 FROM TRANSACTION
 WHERE Tran_Date IN 
 ( SELECT Event_dt
 FROM Message
 WHERE Event_dt BETWEEN '2020-04-01' AND '2020-06-01' ); 
 
 
 MySQL — JOIN Version 
 SELECT Acct_Num, Tran_Amount
 FROM TRANSACTION, Message
 WHERE Tran_Date = Event_dt
 AND Event_dt BETWEEN '2020-04-01' AND '2020-06-01' ;
[Key Differences]
  - Subqueries separate complex logic from the main query; JOINs keep all logic in one place
  - Subqueries can be used alongside JOINs in many combinations
  - Calculations in a subquery return as a single derived value ; JOIN performs calculations in the SELECT
  - Subqueries allow pre-filtering before a table is exposed to the JOIN; JOINs filter automatically through ON/WHERE
  - IN-based subqueries cannot return columns from the subquery in the final output; JOINs can
'''


# ========================================================
# Row-Valued Expressions
# 5 — Subqueries & Query Expressions
# SECTION: Section 6 — Advanced Subquery Topics
# ========================================================

'''
[Definition]
  - A row-valued expression groups multiple column values together as a single unit
  - Two forms:
 
 A parenthesised list of scalars/column values: (col1, col2) 
 A subquery returning two or more columns
[Use Case 1 — INSERT with multiple rows]
[Use Case 2 — Equality comparison on multiple columns]
[Use Case 3 — Multi-column IN with subquery]
[Rules & Warnings]
  - Data types of matching columns must match between the row-valued expression and the subquery
  - NULL values are accepted in VALUES clause expressions
  - DEFAULT values defined at table level are not supported in a VALUES row expression
  - Single-column indexes become unused when columns are bundled in row-valued expressions with JOINs
  - For inserting thousands of rows, prefer file import methods over multi-row INSERT
'''


# Example 1 — Row-Valued Expressions
sql = '''
INSERT INTO CUSTOMER VALUES
(123009, 'Renee', '3305-1, San-Fran', 'SFO', 1677617700),
(123010, 'Holly', '3225-2, Concord',  'NJ',  1673547700);
'''


# Example 2 — Row-Valued Expressions
sql = '''
SELECT * FROM CUSTOMER
WHERE (Cust_Id, Address) = (123010, '3225-2, Concord');
'''


# Example 3 — Row-Valued Expressions
sql = '''
SELECT *
FROM   ACCOUNT
WHERE  (ACCT_NUM, BALANCE) IN
       (SELECT ACCT_NUM, TRAN_AMOUNT
        FROM   TRANSACTION);
'''


# ========================================================
# Query Expressions (Pattern Matching & Type Conversion)
# 5 — Subqueries & Query Expressions
# SECTION: Section 6 — Advanced Subquery Topics
# ========================================================

'''
[Definition]
  - Query expressions define search criteria on character patterns within strings
  - Used in WHERE clause conditions to filter rows on partial or phonetic matches
  - Analytics uses them to retrieve text at granular level — identifying partial text entries
[LIKE — Pattern Matching]
[SOUNDEX() — Same Pronunciation, Different Spelling]
[INSTR() — Find Position of Substring]
[REPLACE() — Substitute a Substring]
[CAST() & CONVERT() — Data Type Conversion]
  NOTE: ℹ️ CAST is ANSI-standard (portable across databases); CONVERT is used in MySQL and other commercial RDBMS. Both change the data type to one the system can interpret correctly (e.g. string to date for date comparisons).
'''


# Example 1 — Query Expressions (Pattern Matching & Type Conversion)
sql = '''
-- % wildcard: matches any string of characters
SELECT * FROM CUSTOMER WHERE Name LIKE 'Ja%';
-- Returns: Jack (123004), Jacob (123005)
'''


# Example 2 — Query Expressions (Pattern Matching & Type Conversion)
sql = '''
SELECT SOUNDEX('JACOB'), SOUNDEX('JAKOB');
-- Both return: J100 (same phonetic code)
'''


# Example 3 — Query Expressions (Pattern Matching & Type Conversion)
sql = '''
SELECT INSTR('Enterprise Data Analytics', 'Data');
-- Output: 12 (position where 'Data' starts)
'''


# Example 4 — Query Expressions (Pattern Matching & Type Conversion)
sql = '''
SELECT REPLACE('Enterprise Data Analytics', 'Data', 'Functional');
-- Output: 'Enterprise Functional Analytics'
'''


# Example 5 — Query Expressions (Pattern Matching & Type Conversion)
sql = '''
-- CAST: ANSI standard
SELECT CAST('2003-01-01' AS DATE);

-- CONVERT: MySQL / commercial RDBMS style
SELECT CONVERT('2003-01-01', DATE);
'''


# ---

# ## Session 6 — Window Functions, Normalization & Constraints

# *Window Functions · Normalization · ACID · Constraints · Data Integrity*


# ### Section 1 — Advanced Window / Analytical Functions
# *RANK · DENSE_RANK · PERCENT_RANK · LAG · LEAD · FIRST_VALUE · LAST_VALUE · NTILE · CUME_DIST*


# ========================================================
# Window Functions — Overview & Benefits
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 1 — Advanced Window / Analytical Functions
# ========================================================

'''
[Definition]
  - Many RDBMS provide Analytical (Window) functions to perform complex operations and evaluate results efficiently
  - Also called Windowing or OLAP (Online Analytical Processing) functions
  - They use the OVER() clause to calculate aggregate results on a group of rows based on a candidate key
  - The aggregate result produced from a group of rows is shared back to each row in the group — unlike GROUP BY which collapses rows
  - This is an advanced feature of GROUP BY: it shares aggregate results at row level
[Key Benefits]
  - Reduces the use of self-JOINs — analytical functions perform many self-join operations internally
  - Reporting shows comparison between current record entry vs. aggregate result
  - Build statistics on cumulative results rather than just aggregate results
  - More granular level of cost controlling — strategic reports through GROUP BY show overall performance, while window functions show row-level detail
[General OVER() Syntax]
[Window Function vs GROUP BY]
[GROUP BY]
  - Collapses rows into one row per group
  - Aggregate value shown once per group
  - Cannot see individual row details alongside
[Window Function (OVER)]
  - Preserves all rows in the result
  - Aggregate value shown alongside each individual row
  - Ideal for row-level comparison with group total
[Ranking Functions — 3 Types in MySQL]
  - RANK() — assigns rank; skips ranks for ties
  - DENSE_RANK() — assigns rank; does NOT skip ranks for ties
  - PERCENT_RANK() — assigns fractional rank (0 to 1) using formula: (rank − 1) / (rows − 1)
  NOTE: 💡 Assignment of rank always starts with 1 for every new partition.
'''


# Example 1 — Window Functions — Overview & Benefits
sql = '''
WINDOW_FUNCTION() OVER(
    [PARTITION BY column]   -- divide rows into groups
    [ORDER BY column ASC|DESC]  -- sort within each group
    [ROWS|RANGE BETWEEN ...]   -- optional frame clause
)
'''


# ========================================================
# RANK() Function
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 1 — Advanced Window / Analytical Functions
# ========================================================

'''
[Definition]
  - Displays the rank for each record based on the highest value of a desired column
  - Ranks are calculated on a group of rows divided by the corresponding candidate key (PARTITION BY)
  - Assigns the same rank for equal values , but skips subsequent ranks based on the count of ties
[Syntax]
[Example — Rank accounts by balance per customer]
  NOTE: ⚠ RANK() Skipping Rule: No. of ranks skipped = No. of ties in the same position. If 2 rows tie at rank-1, the next rank assigned is 3 (rank-2 is skipped).
'''


# Example 1 — RANK() Function
sql = '''
SELECT col1, col2, ...,
    RANK() OVER(PARTITION BY partition_col ORDER BY rank_col DESC) AS rank_alias
FROM table_name
WHERE condition;
'''


# Example 2 — RANK() Function
sql = '''
SELECT Cust_Id, Acct_Num, Acct_Type, Balance,
    RANK() OVER(PARTITION BY Cust_Id ORDER BY Balance DESC) AS Rank_of_balance_amount
FROM ACCOUNT
WHERE Cust_Id IN (123001, 123002);
'''


# ========================================================
# DENSE_RANK() Function
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 1 — Advanced Window / Analytical Functions
# ========================================================

'''
[Definition]
  - Displays the rank based on the highest value of a desired column, similar to RANK()
  - Key difference: preserves the next rank without skipping — no gaps in rank sequence
  - Tied rows still get the same rank, but the following row gets the very next integer
[Syntax]
[Example]
  NOTE: RANK() vs DENSE_RANK() — Side by Side 
 RANK() — Skips ranks on ties 
 
 Balance 7500000 → Rank 1 
 Balance 7500000 → Rank 1 (tied) 
 Balance 5000000 → Rank 3 (rank-2 is skipped because of the tie) 
 
 DENSE_RANK() — No skip on ties 
 
 Balance 7500000 → Dense_Rank 1 
 Balance 7500000 → Dense_Rank 1 (tied) 
 Balance 5000000 → Dense_Rank 2 (no gap — next consecutive rank assigned)
'''


# Example 1 — DENSE_RANK() Function
sql = '''
SELECT col1, col2, ...,
    DENSE_RANK() OVER(PARTITION BY partition_col ORDER BY rank_col DESC) AS dense_rank_alias
FROM table_name
WHERE condition;
'''


# Example 2 — DENSE_RANK() Function
sql = '''
SELECT Cust_Id, Acct_Num, Acct_type, Balance,
    DENSE_RANK() OVER(PARTITION BY Cust_Id ORDER BY Balance DESC) AS Dense_rank_of_balance
FROM ACCOUNT
WHERE Cust_Id = 123004;
'''


# ========================================================
# PERCENT_RANK() Function
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 1 — Advanced Window / Analytical Functions
# ========================================================

'''
[Definition]
  - Calculates the percentage rank of each row within its partition
  - Formula: (rank − 1) / (rows − 1)
  - All rows in a partition share a range of fractions from 0 to 1
  - First row always gets 0 ; last row always gets 1
  - Like RANK(), it also skips the rank percentage when duplicate values are identified
[Syntax]
[Key Behaviour]
  - Partitioned rows are in ascending order for PERCENT_RANK
  - If two rows share the same value → they get the same percent rank , and the next rank percentage is skipped (same skip logic as RANK)
  - Example: 4 rows with no ties → percent_ranks are 0, 0.333, 0.667, 1.0
'''


# Example 1 — PERCENT_RANK() Function
sql = '''
SELECT Cust_Id, Acct_Num, acct_type, Balance,
    PERCENT_RANK() OVER(PARTITION BY Cust_Id ORDER BY balance) AS Percent_rank_of_balance
FROM ACCOUNT
WHERE Cust_Id = 123004;
'''


# ========================================================
# LAG() & LEAD() Functions
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 1 — Advanced Window / Analytical Functions
# ========================================================

'''
[Definition]
  - In a normal SELECT query, records are interpreted serially
  - Sometimes there is a need to look back (LAG) or forward (LEAD) while retrieving the current record
  - LAG(col) — returns the value of col from the previous row in the result set
  - LEAD(col) — returns the value of col from the next row in the result set
[Syntax & Example]
[Output Explanation]
  - Each row shows its current balance, the previous row's balance , and the next row's balance
  - previous_balance is NULL for the first row — no prior record exists
  - next_balance is NULL for the last row — no further record exists
  NOTE: 💡 LAG and LEAD are powerful for trend analysis — comparing a sale today vs. yesterday, or a current stock price vs. the next day's price.
'''


# Example 1 — LAG() & LEAD() Functions
sql = '''
SELECT Cust_Id, Acct_Num, Acct_Type, Balance,
    LAG(Balance)  OVER(ORDER BY Balance) AS previous_balance,
    LEAD(Balance) OVER(ORDER BY Balance) AS next_balance
FROM Account
WHERE Cust_Id = 123004;
'''


# ========================================================
# FIRST_VALUE() Function
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 1 — Advanced Window / Analytical Functions
# ========================================================

'''
[Definition]
  - Analyzes the results of the OVER() analytical expression and returns the first value from the ordered set of rows
  - Can be used with ORDER BY only (no partition) or with PARTITION BY + ORDER BY
[Example 1 — With ORDER BY only (no partition)]
[Explanation — No Partition]
  - All rows ordered by Balance in OVER()
  - FIRST_VALUE picks the least balance from the ordered rows
  - That single least value is displayed across all rows in the output
[Example 2 — With PARTITION BY + ORDER BY]
[Explanation — With Partition]
  - All rows first partitioned into FIXED DEPOSITS and SAVINGS by Acct_Type
  - Within each partition, rows ordered by balance ascending
  - FIRST_VALUE applied to each partition independently — picks the least balance per partition type
  - That partition's least value is displayed across all rows within that partition
'''


# Example 1 — FIRST_VALUE() Function
sql = '''
-- Returns the least balance across all FIXED DEPOSITS and repeats it on every row
SELECT Cust_Id, Acct_Num, Acct_Type, Balance AS original_balance,
    FIRST_VALUE(Balance) OVER(ORDER BY Balance) AS Least_balance
FROM Account
WHERE acct_type = 'FIXED DEPOSITS';
'''


# Example 2 — FIRST_VALUE() Function
sql = '''
-- Returns the least balance per account type (partition)
SELECT Acct_Num, Acct_Type, Balance AS original_balance,
    FIRST_VALUE(Balance)
    OVER(PARTITION BY Acct_type ORDER BY balance) AS Least_balance
FROM Account
WHERE balance > 0;
'''


# ========================================================
# LAST_VALUE() Function
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 1 — Advanced Window / Analytical Functions
# ========================================================

'''
[Definition]
  - Returns the last value from an ordered set of rows defined by OVER()
  - Requires the RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING frame clause to correctly get the true last value — otherwise MySQL defaults to the current row as the frame end
[Example 1 — With ORDER BY + RANGE frame]
[Example 2 — With PARTITION BY + RANGE frame]
[Explanation — With Partition]
  - Rows first partitioned by Acct_Type (FIXED DEPOSITS / SAVINGS)
  - Within each partition, rows ordered by Balance; full range frame used
  - LAST_VALUE picks the highest balance from each partition independently and repeats it across all rows in that partition
  NOTE: ⚠ Without RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING , LAST_VALUE will return the current row's value instead of the true last — MySQL's default frame ends at the current row.
'''


# Example 1 — LAST_VALUE() Function
sql = '''
SELECT Acct_Num, Acct_Type, Balance AS original_balance,
    LAST_VALUE(Balance)
    OVER(ORDER BY Balance
         RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_original_value
FROM ACCOUNT
WHERE Acct_type = 'FIXED DEPOSITS';
'''


# Example 2 — LAST_VALUE() Function
sql = '''
SELECT Acct_Num, Acct_Type, Balance AS original_balance,
    LAST_VALUE(Balance)
    OVER(PARTITION BY ACCT_TYPE ORDER BY Balance
         RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS part_last_value
FROM ACCOUNT
WHERE balance > 0;
'''


# ========================================================
# NTILE() Function — Buckets
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 1 — Advanced Window / Analytical Functions
# ========================================================

'''
[Definition]
  - NTILE(n) splits the total records into a predefined number of buckets (n)
  - Rows are divided as equally as possible; the last bucket receives any leftover rows
  - The developer specifies the number of buckets — e.g., NTILE(3) creates 3 buckets
[Example 1 — Without partition (full table bucketing)]
[Example 2 — With PARTITION BY (bucket within each group)]
'''


# Example 1 — NTILE() Function — Buckets
sql = '''
SELECT Acct_Num, Acct_Type, Balance AS original_balance,
    NTILE(3) OVER(ORDER BY Balance) AS sav_bucket
FROM ACCOUNT
WHERE Acct_type = 'SAVINGS' AND balance > 0;
'''


# Example 2 — NTILE() Function — Buckets
sql = '''
SELECT Acct_Num, Acct_Type, Balance AS original_balance,
    NTILE(2) OVER(PARTITION BY ACCT_TYPE ORDER BY Balance) AS bucket
FROM ACCOUNT
WHERE balance > 0;
'''


# ========================================================
# CUME_DIST() — Cumulative Distribution
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 1 — Advanced Window / Analytical Functions
# ========================================================

'''
[Definition]
  - Distribution of records = the percentage a record occupies in the total record set
  - Cumulative distribution = the cumulative percentage of records from the first row to the current row, out of the total result
  - Returns a value between 0 and 1; unlike PERCENT_RANK, the first row is never 0
[Example 1 — Without partition]
[Explanation — No Partition]
  - 4 FIXED DEPOSIT rows → each row occupies 25% of total
  - Row 1: cumulative dist = 25% (0.25)
  - Rows 2 & 3 have the same balance → both get 75% (0.75); row 4 gets 100% (1.0)
  - If rows 2 & 3 had different values: row 2 = 50%, row 3 = 75%
[Example 2 — With PARTITION BY]
[Explanation — With Partition]
  - Cumulative distribution calculated independently for each partition : FIXED DEPOSITS and SAVINGS
  - Each partition restarts its cumulative count from scratch
'''


# Example 1 — CUME_DIST() — Cumulative Distribution
sql = '''
SELECT Acct_Num, Acct_Type, Balance AS original_balance,
    CUME_DIST() OVER(ORDER BY Balance) AS cum_distribution
FROM ACCOUNT
WHERE acct_type = 'FIXED DEPOSITS';
'''


# Example 2 — CUME_DIST() — Cumulative Distribution
sql = '''
SELECT Acct_Num, Acct_Type, Balance AS original_balance,
    CUME_DIST() OVER(PARTITION BY ACCT_TYPE ORDER BY Balance) AS Part_Cume_dist
FROM ACCOUNT
WHERE balance > 0;
'''


# ========================================================
# Aggregate Functions with Window Functions
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 1 — Advanced Window / Analytical Functions
# ========================================================

'''
[Concept]
  - Standard grouping functions (SUM, AVG, MIN, MAX, COUNT) can be used inside window functions to retrieve aggregate results while comparing against each row
  - This is the key use case: show both the individual row detail and the group aggregate in the same query
[Example — SUM with OVER(PARTITION BY)]
[Other aggregate functions usable with OVER()]
  - AVG(col) OVER(PARTITION BY ...) — running average per group
  - MIN(col) OVER(PARTITION BY ...) — group minimum per row
  - MAX(col) OVER(PARTITION BY ...) — group maximum per row
  NOTE: ℹ Analytical functions are widely used in organizations because they reduce the number of calls to the same table — especially useful when SELF JOINs would otherwise be needed. Performance is high due to less CPU utilization for row mapping.
'''


# Example 1 — Aggregate Functions with Window Functions
sql = '''
SELECT Cust_Id, Acct_Num, Acct_Type, Balance,
    SUM(Balance) OVER(PARTITION BY Cust_Id) AS customer_level_balance
FROM ACCOUNT
WHERE CUST_ID IN (123001, 123002, 123004);
'''


# ### Section 2 — Cross-Tab & Recursive Queries
# *CASE-based pivoting · WITH RECURSIVE*


# ========================================================
# Cross-Tab and Relational Tables
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 2 — Cross-Tab & Recursive Queries
# ========================================================

'''
[Definition]
  - Cross tabulation of a relational database displays columns as rows and rows as columns (pivot-like structure)
  - A cross-table is a multi-dimensional structure that pivots rows vertically and columns horizontally
  - Used to display strategic reports with summarized data , trend reports with aggregate results
  - Can display grand totals for columns, rows, or the entire measure; also supports subtotals
[Syntax — CASE-based pivot (count transactions by channel per month)]
'''


# Example 1 — Cross-Tab and Relational Tables
sql = '''
SELECT MONTHNAME(T.Tran_Date) AS "Month",
    COUNT(CASE WHEN T.Channel = 'ATM Withdrawal'  THEN 1 END) AS ATM_transaction,
    COUNT(CASE WHEN T.Channel = 'UPI transfer'    THEN 1 END) AS UPI_transaction,
    COUNT(CASE WHEN T.Channel = 'Net banking'     THEN 1 END) AS net_banking,
    COUNT(CASE WHEN T.Channel = 'Bankers cheque'  THEN 1 END) AS bankers_cheque,
    COUNT(CASE WHEN T.Channel = 'ECS transfer'   THEN 1 END) AS ECS_transfer,
    COUNT(CASE WHEN T.Channel = 'Cash Deposit'   THEN 1 END) AS Cash_deposit
FROM Transaction T
GROUP BY MONTH(T.Tran_Date);
'''


# ========================================================
# Recursive Query Expressions
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 2 — Cross-Tab & Recursive Queries
# ========================================================

'''
[Definition]
  - Used to report hierarchical structured data (family trees, org charts, bill of materials)
  - Follows a chain process of identifying relationships between relevant columns
  - Defined with a sub-query using the RECURSIVE clause inside a CTE ( WITH )
  - The query iterates between the main (anchor) query and the sub-query a predefined number of times
  - Must have a terminating condition to stop recursion
[Setup — Create hierarchical table]
[Recursive Query]
[How It Works]
  - Anchor query : selects the root row — GEFF (Parent_Name IS NULL). This is the starting point
  - UNION ALL : joins the CTE result back to the original table — finding children of current rows
  - The recursion keeps running until no more children are found (natural termination)
  - CONCAT builds the hierarchy path: GEFF → GEFF,MARK → GEFF,MARK,CHARLIE etc.
  NOTE: ⚠ Always ensure a terminating condition exists (like IS NULL for root, or a depth limit). Without it, a recursive query can run infinitely and crash the server.
'''


# Example 1 — Recursive Query Expressions
sql = '''
CREATE TABLE CUSTOMER_HOUSEHOLD (
    Cust_Id     INT,
    NAME        VARCHAR(20),
    PARENT_NAME VARCHAR(20)
);

INSERT INTO CUSTOMER_HOUSEHOLD VALUES
(123000, 'GEFF',    NULL   ),   -- root (no parent)
(123001, 'MARK',    'GEFF' ),
(123002, 'CHARLIE', 'MARK' ),
(123003, 'CRISTY',  'MARK' ),
(123004, 'SARAH',   'GEFF' ),
(123005, 'ROBERT',  'SARAH'),
(123006, 'ANDY',    'SARAH');
'''


# Example 2 — Recursive Query Expressions
sql = '''
WITH RECURSIVE Family (NAME, PARENT_NAME, Hierarchy) AS (
    -- Anchor query: start from root (no parent)
    SELECT Name, Parent_name, CAST(Name AS CHAR(200))
    FROM   CUSTOMER_HOUSEHOLD
    WHERE  Parent_Name IS NULL

    UNION ALL

    -- Recursive part: join back to find children of each row
    SELECT ch.Name, ch.Parent_Name, CONCAT(cf.Hierarchy, ',', ch.name)
    FROM   Family cf
    JOIN   CUSTOMER_HOUSEHOLD ch
    ON     cf.name = ch.parent_name
)
SELECT * FROM Family ORDER BY Hierarchy;
'''


# ### Section 3 — Data Integrity
# *Row integrity · Column integrity · Referential integrity · ACID Properties*


# ========================================================
# What is Data Integrity?
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 3 — Data Integrity
# ========================================================

'''
[Definition]
  - According to the data management and governance community: Integrity of data ensures an appropriate lineage of business entities in the data flow process
  - Data Integrity ensures smooth business flow and is the key aspect of design of data flow processes
  - It ensures consistency of data through the entire project lifecycle — data must be relevant across the business
[Why Data Integrity Matters]
  - Receive accurate data without flaws — loss of data costs the organization
  - Consistency of data flow across business processes — no entities stuck due to invalid/irrelevant data
  - Data generated should be reliable within business units — consistent when shared across units
[Consequences of Loss of Data Integrity]
  - Audit penalty by data governance
  - Costs associated with unused data maintenance (billions in additional storage)
  - Additional RAM consumption by SQL programs running on bad data
  - Purchase of additional disk space (standalone or cloud)
  - Analytics show inappropriate results
  - Quality control becomes an overhead
  - Inappropriate decision making from multiple strategic reports with poor data quality
'''


# ========================================================
# Classification of Data Integrity
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 3 — Data Integrity
# ========================================================

'''
[Three Types]
  - 1. Row Level Integrity — each row referenced by unique values; avoids conflicts with other rows; unique identifier = Primary Key
  - 2. Column Level Integrity — every column holds a business meaning; data stored must adhere to the same format, data type, size, and range of possible values
  - 3. Referential Integrity — ensures consistency of records between two related tables through FOREIGN KEY and PRIMARY KEY relationships
[Row Level Integrity — Example]
[Column Level Integrity — Example]
[Referential Integrity — Define Foreign Key]
[Referential Integrity Rules]
  - Foreign Key (MUL) — accepts duplicate values, but values must already exist in the parent column (EQUIPMENT)
  - Cannot INSERT or UPDATE a record in the child table for which no record exists in the parent table
  - Fix : insert in the parent table first, then insert in the child table
  - Cannot DELETE a parent record that is referenced by a child's foreign key (unless CASCADE is set)
'''


# Example 1 — Classification of Data Integrity
sql = '''
-- CUSTOMER table uses Cust_Id as unique identifier (Primary Key)
SELECT * FROM CUSTOMER WHERE Cust_Id = 123001;
'''


# Example 2 — Classification of Data Integrity
sql = '''
-- MODEL column is INT; inserting 'Nineteen' (string) violates column integrity
INSERT INTO EQUIPMENT VALUES ('MAC03', 'SPINNING', 'Nineteen');  -- FAILS

-- Correct: match the column's data type
INSERT INTO EQUIPMENT VALUES ('MAC03', 'SPINNING', 2019);         -- OK
'''


# Example 3 — Classification of Data Integrity
sql = '''
ALTER TABLE LEASE
ADD FOREIGN KEY (MACHINE_ID)
REFERENCES EQUIPMENT (MACHINE_ID);
'''


# ========================================================
# ACID Properties
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 3 — Data Integrity
# ========================================================

'''
[What is a Transaction?]
  - A transaction is a single logical unit of work which acts on database contents
  - The database state is in tandem with every transaction to ensure data integrity
  - Transaction processing follows four standard properties (ACID) to ensure smooth flow
[A — Atomicity]
  - Complete 100% or retain original status — all-or-nothing
  - Example: A debits $1000 and B gets credited $1000. If any step fails, both are reversed — no partial transaction
[C — Consistency]
  - Ensures data is not leaked in any case of success or failure
  - Example: A debits $2000 to B, but B is credited only $1000 — $1000 is lost. This transaction is a success but not consistent
  - Database application must ensure transformation rules are consistent without data loss
[I — Isolation]
  - Every transaction is individual, secured, and hidden from other transactions
  - Transactions are serialized to avoid conflicts like double-spending
  - Example: Edward has $5000, gives two cheques of $3000 and $2700 — isolation prevents both from clearing simultaneously (total would exceed balance)
[D — Durability]
  - Data should be persistent before and after a transaction
  - Example: Edward swipes $2000 on Amazon; network goes down; money debited but order not fulfilled. Durability ensures the transaction can either succeed fully or be reversed
  - Database maintains state of data before and after every transaction
  NOTE: ACID — Quick Reference 
 A — Atomicity 
 All or Nothing — no partial commits allowed If any part of a transaction fails, the entire transaction is rolled back 
 C — Consistency 
 No data leakage — transformation rules are always enforced Every transaction must leave the database in a valid, consistent state 
 I — Isolation 
 Transactions don't interfere with each other Serialized execution — concurrent transactions see each other as if run sequentially 
 D — Durability 
 Committed data is permanent — survives system failures and crashes Database maintains before/after state of every transaction
'''


# ### Section 4 — Normalization
# *Functional Dependency · 1NF · 2NF · 3NF · BCNF*


# ========================================================
# Functional Dependency
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 4 — Normalization
# ========================================================

'''
[Definition]
  - All non-key columns of a table are said to be dependent on the Primary Key , which uniquely identifies each row
  - Example: CUSTOMER(Cust_Id, Name, Address, State, Telephone) — Cust_Id is PK; all other columns are functionally dependent on Cust_Id
'''


# ========================================================
# First Normal Form (1NF)
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 4 — Normalization
# ========================================================

'''
[Four Rules for 1NF]
  - A column/attribute must consist of scalar atomic values (no multi-valued or composite attributes)
  - All values in a column must have the same business meaning
  - All columns must have unique names
  - The order of rows and columns does not matter
[Problem before 1NF]
  - A bank branch table stores multiple IFSC codes (phone numbers, branches) in a single column — multi-valued
  - This makes building relationships between rows and columns difficult
[1NF Resolution]
  - Decompose the multi-valued column — place each value in a separate row
  - Result: each cell contains one atomic value
'''


# Example 1 — First Normal Form (1NF)
sql = '''
-- Before 1NF: multi-valued in one column
SELECT * FROM ALL_BANKS;

-- After 1NF: multi-values placed in different rows
SELECT * FROM BANKS;
'''


# ========================================================
# Second Normal Form (2NF)
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 4 — Normalization
# ========================================================

'''
[Rules for 2NF]
  - Must already be in 1NF
  - All non-key & independent attributes must be fully functionally dependent on the primary key
  - Eliminates partial dependencies — no non-key column should depend on only part of a composite key
[Problem before 2NF (Equipment_Lease table)]
  - Redundancy : Every new invoice repeats Machine Name, Machine Id, Model Number
  - Dependency : Invoice columns are made dependent on machine columns — too much coupling
  - Composite key: [MACHINE_ID, INVOICE]; columns like Lease_date, Lease_expiry, Quantity, Price are only partially dependent
[2NF Resolution]
  - Split the table into two tables : one for EQUIPMENT, one for LEASE/INVOICE
  - Split the composite key into two separate primary keys
  - Make non-key columns fully dependent on their respective primary keys
  - Then add referential integrity through FOREIGN KEY relationship
'''


# ========================================================
# Third Normal Form (3NF)
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 4 — Normalization
# ========================================================

'''
[Rules for 3NF]
  - Must already be in 2NF
  - No transitive dependency should exist — non-prime attributes must not depend on other non-prime attributes
  - Transitive dependency: A depends on B, B depends on C → A transitively depends on C
[Problem — ACCOUNT_TRANSACTION table before 3NF]
  - Tran_amount, Cheque_No, Pay_purpose → depend on Tran_id
  - Tran_id → depends on Account_Number
  - Account_Number → depends on Cust_id
  - All non-prime attributes are transitively dependent on the super key (Cust_ID) — violates 3NF
[3NF Resolution]
  - Split ACCOUNT_TRANSACTION into two: ACCOUNT and TRANSACTION
  - Eliminate transitive dependency of Tran_amount, Cheque_No, Pay_purpose on Cust_Id
  - Each table now has non-key columns directly dependent on their own primary key
'''


# ========================================================
# Boyce-Codd Normal Form (BCNF)
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 4 — Normalization
# ========================================================

'''
[Rules for BCNF]
  - Must already be in 3NF
  - Resolves problems related to redundancy of data that appeared in 3NF
  - A 3NF table is split into DIMENSION and FACT tables
  - 3NF issue arises when multiple sub-transactions appear for a single transaction
[Dimension Table]
  - Contains break-up details of a transaction
  - Example: A cheque for education is split into fees, tax, cess — all are dimensions of one transaction
[Fact Table]
  - Contains high-level records — unique entries
  - Example: Cheque Number and its corresponding account number
  NOTE: Normalization — Quick Reference Table 
 
 1NF — Atomic values in all columns; no multi-valued attributes 
 2NF — 1NF + all non-key attributes fully depend on the entire primary key (no partial dependency) 
 3NF — 2NF + no transitive dependency (non-key attributes don't depend on other non-key attributes) 
 4NF — BCNF + no multi-valued dependency 
 5NF — 4NF + no join dependency; joins are lossless
'''


# ### Section 5 — Constraints on Relations
# *NOT NULL · DEFAULT · CHECK · UNIQUE · PRIMARY KEY · FOREIGN KEY · CASCADE · DEFERRED*


# ========================================================
# Constraints — Overview
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 5 — Constraints on Relations
# ========================================================

'''
[Definition]
  - SQL Constraints are rules used to limit the type of data that can go into a column or table
  - Ensure the accuracy and integrity of the data inside the column/table
[Column Level Constraints]
  - Limits data in a single column
  - Includes: NOT NULL, DEFAULT, CHECK, UNIQUE, PRIMARY KEY
[Table Level Constraints]
  - Limits the complete table dataset across multiple columns
  - Includes: FOREIGN KEY, composite PRIMARY KEY, table-level CHECK
'''


# ========================================================
# NOT NULL Constraint
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 5 — Constraints on Relations
# ========================================================

'''
[Definition]
  - Restricts a column from having a NULL value
  - After applying NOT NULL, you cannot pass a null value into that column
[Syntax]
[Effect]
  - IFSC_CODE's NULL property changes from "YES" to "NO" — the field must not be blank
'''


# Example 1 — NOT NULL Constraint
sql = '''
-- Add NOT NULL to an existing column
ALTER TABLE BANKS MODIFY IFSC_CODE VARCHAR(35) NOT NULL;

-- This will fail — IFSC_CODE cannot be NULL
INSERT INTO BANKS VALUES ('HDFC', 'HYDERABAD', 'KOTHAPET', NULL);
'''


# ========================================================
# CHECK Constraint
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 5 — Constraints on Relations
# ========================================================

'''
[Definition]
  - Conditionally validates column values before insertion of a record
  - Prevents any unwanted entry that doesn't meet the defined condition
[Syntax & Example]
'''


# Example 1 — CHECK Constraint
sql = '''
-- Ensure transaction amount never exceeds 2,000,000
ALTER TABLE TRANSACTION ADD CHECK (ABS(Tran_Amount) < 2000000);

-- This will FAIL — 2,000,009 exceeds the limit
INSERT INTO TRANSACTION VALUES
('5000-1700-5001', 'T99305', 'CHQ0022', 'Cash Withdraw', 2000009);
'''


# ========================================================
# UNIQUE Constraint
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 5 — Constraints on Relations
# ========================================================

'''
[Definition]
  - Ensures a column will only have unique values — no duplicates allowed
  - Combined with NOT NULL, prevents both NULL and duplicate values
[Syntax]
'''


# Example 1 — UNIQUE Constraint
sql = '''
ALTER TABLE BANKS ADD UNIQUE (IFSC_CODE);

-- This will FAIL — HDFC0000145 already exists in BANKS
INSERT INTO BANKS VALUES ('HDFC', 'HYDERABAD', 'ABIDS', 'HDFC0000145');
'''


# ========================================================
# PRIMARY KEY Constraint
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 5 — Constraints on Relations
# ========================================================

'''
[Definition]
  - Defined on a column and uniquely identifies each record in a table
  - A Primary Key by default creates an Index on the column — used for fast record search based on conditions
  - Implicitly enforces both NOT NULL and UNIQUE
[Syntax]
'''


# Example 1 — PRIMARY KEY Constraint
sql = '''
ALTER TABLE ACCOUNT ADD PRIMARY KEY (Account_Number);

-- This will FAIL — Account_Number 4000-1956-2001 already exists
INSERT INTO ACCOUNT VALUES (123002, '4000-1956-2001', 'SAVINGS', 950000);
'''


# ### Section 6 — Referential Integrity & CASCADE
# *FK rules · ON UPDATE CASCADE · ON DELETE CASCADE · Cyclic references · Deferred constraints*


# ========================================================
# Referential Integrity — Rules & Problems
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 6 — Referential Integrity & CASCADE
# ========================================================

'''
[Recap — Foreign Key Rules]
  - Foreign key constraints always reference a primary or unique key in the parent table
  - A foreign key value assigned NULL doesn't reference any primary key
  - If a foreign key has a valid value, it must have an associated value in the primary key
[DML Restrictions due to Referential Integrity]
  - Enforcing referential integrity causes limitations on DML operations (INSERT, DELETE, UPDATE) on referenced tables
  - Decreases performance — SQL engine must check both the table being updated and all referenced tables
  - Overhead when exporting tables between databases — foreign keys must be disabled, then re-enabled
  - Re-enabling foreign keys may lose data integrity as it won't scan appropriately
[Update Foreign Key — What Happens?]
  NOTE: ⚠ Delete of a child table record does NOT affect the parent table. But delete of a parent record referenced by a child's FK will fail — unless CASCADE is configured.
'''


# Example 1 — Referential Integrity — Rules & Problems
sql = '''
-- FAILS: MAC09 does not exist in EQUIPMENT (parent table)
UPDATE LEASE SET MACHINE_ID = 'MAC09' WHERE MACHINE_ID = 'MAC01';

-- FAILS: Updating Primary Key in parent when child FK references it
UPDATE EQUIPMENT SET MACHINE_ID = 'MAC09' WHERE MACHINE_ID = 'MAC01';

-- FAILS: Deleting parent record referenced by child FK
DELETE FROM EQUIPMENT WHERE MACHINE_ID = 'MAC01';
'''


# ========================================================
# CASCADE — ON UPDATE & ON DELETE
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 6 — Referential Integrity & CASCADE
# ========================================================

'''
[What is CASCADE?]
  - To overwrite DML rules on referential integrity fields, CASCADE is issued on the table having the foreign key column
  - Changes to parent table records are automatically reflected in child table
  - Two types: ON UPDATE CASCADE and ON DELETE CASCADE
[ON UPDATE CASCADE — Setup]
[ON DELETE CASCADE — Setup]
[Referential Cycles]
  - In a parent-child relationship, if the PK of the child table references the PK of the parent, and the PK of the parent references the PK of the child — they form a loop of referential integrity constraints
  - Example: ACCT_LOCKER (Acct_Num PK) ↔ BANK_LOCKER (Safe_box PK) — each references the other
'''


# Example 1 — CASCADE — ON UPDATE & ON DELETE
sql = '''
-- Drop existing FK, re-add with CASCADE
ALTER TABLE LEASE DROP FOREIGN KEY lease_ibfk_1;
ALTER TABLE LEASE ADD FOREIGN KEY (MACHINE_ID)
    REFERENCES EQUIPMENT (MACHINE_ID)
    ON UPDATE CASCADE;

-- Now this works: LEASE.MACHINE_ID auto-updated from MAC01 → MAC09
UPDATE EQUIPMENT SET MACHINE_ID = 'MAC09' WHERE MACHINE_ID = 'MAC01';
'''


# Example 2 — CASCADE — ON UPDATE & ON DELETE
sql = '''
ALTER TABLE LEASE DROP FOREIGN KEY lease_ibfk_1;
ALTER TABLE LEASE ADD FOREIGN KEY (MACHINE_ID)
    REFERENCES EQUIPMENT (MACHINE_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE;

-- Deleting MAC02 from EQUIPMENT auto-deletes all LEASE rows for MAC02
DELETE FROM EQUIPMENT WHERE MACHINE_ID = 'MAC02';
SELECT COUNT(*) FROM LEASE WHERE MACHINE_ID = 'MAC02';  -- returns 0
'''


# ========================================================
# Deferred Constraints
# 6 — Window Functions, Normalization & Constraints
# SECTION: Section 6 — Referential Integrity & CASCADE
# ========================================================

'''
[Definition]
  - During large volume transactions involving multiple dependencies, constraints can make it difficult to process data efficiently
  - Deferred constraints allow overriding such restrictions temporarily
  - Default status is NOT DEFERRED — constraints are checked immediately at each statement
[Two Types of DEFERRABLE]
  - INITIALLY IMMEDIATE : updates records directly onto database (checked at end of each statement)
  - INITIALLY DEFERRED : does NOT update records directly; keeps them in logs and commits onto database later (checked at end of transaction)
[Syntax]
[Primary Use Case]
  - Cyclic Foreign Keys — inserting a record in one table expects the record to be present in another table (which in turn expects the first)
  - Without DEFERRED, neither table can be populated first
  - DEFERRED allows both inserts to succeed; constraints are validated only at commit time
  NOTE: 💡 DEFERRED constraints are primarily used to handle circular foreign key dependencies — a situation that cannot be resolved with standard immediate constraint checking.
'''


# Example 1 — Deferred Constraints
sql = '''
-- Define a deferrable FK constraint
ALTER TABLE ACCOUNT_TRANSACTIONS
ADD CONSTRAINT ACCOUNT_tran_init_imm
FOREIGN KEY (Acct_Num) REFERENCES ACCOUNT(Account_NUMBER)
DEFERRABLE INITIALLY IMMEDIATE;

-- Alter session to deferred mode (allows cyclic FK inserts)
ALTER SESSION SET CONSTRAINTS = DEFERRED;

-- Now cyclic inserts work (both tables reference each other)
INSERT INTO ACCOUNT_Locker VALUES ('4000-1956-2900', 999102);
INSERT INTO Bank_Locker   VALUES (999102, 'DELHI', '4000-1956-2900');
'''


# ---

# ## Session 7 — Transactions, Isolation, Locking & Views

# *Transactions · Isolation · Savepoints · Locking · Views*


# ### Section 1 — Transaction Processing
# *START TRANSACTION · COMMIT · ROLLBACK · SET TRANSACTION*


# ========================================================
# What is a Transaction?
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 1 — Transaction Processing
# ========================================================

'''
[Definition]
  - A transaction is a process of executing multiple DML statements sequentially to achieve a final task
  - DML operations (INSERT, DELETE, UPDATE, SELECT) within a transaction ensure data integrity
  - In online applications, transactions happen concurrently on the database — ensuring data is accurate, reliable, and without loss
  - Large organizations like banks perform millions of transactions per minute — all processed through DML statements
[ACID Recap in Transaction Context]
  - Atomicity : Transaction fulfilled 100% or rolled back entirely — e.g., ordering a Pizza: choose item → insert order → payment. If customer cancels at any stage, all DML operations are rolled back
  - Consistency : On database crash or network failure, SQL engine replays transactions from the doublewrite buffer to recover original state
  - Isolation : Concurrent transactions are kept in a queue — one executes after another. E.g., ATM withdrawal and internet transfer at same second — database queues them and checks balance sufficiency for each
  - Durability : Committed changes are permanent and survive system failures
[Real-world Transaction — ATM Withdrawal]
  - Step 1: SELECT — Check bank balance
  - Step 2: INSERT — Record withdrawal in Transaction table
  - Step 3: UPDATE — Deduct withdrawn amount from account balance
  - Step 4: INSERT — Calculate and record service charge (0.2% of withdrawn amount)
  - Step 5: UPDATE — Deduct service charge from account balance
  - Step 6: COMMIT — Finalize the transaction
'''


# ========================================================
# Transaction Model — Full Example
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 1 — Transaction Processing
# ========================================================

'''
[Complete ATM Withdrawal Transaction]
[Transaction Summary]
  - COMMIT — ensures the transaction is fulfilled; changes are permanently written to physical data files and made visible to other users
  - ROLLBACK — if the customer ignores/cancels the withdrawal at any stage, all DML operations above are reversed; original balance is retained
  NOTE: 💡 A transaction is atomic : the ATM withdrawal of money and the service charge deduction are treated as one indivisible unit — either both succeed or neither does.
'''


# Example 1 — Transaction Model — Full Example
sql = '''
START TRANSACTION;

-- Step 1: Check bank balance
SELECT Balance FROM ACCOUNT
WHERE Acct_Num = '4000-1956-2001';

-- Step 2: Record the withdrawal in Transaction table
INSERT INTO Transaction VALUES
('4000-1956-2001', -2300.00, 'ATM Withdrawal', 'CA', NOW());

-- Step 3: Update balance after withdrawal
UPDATE ACCOUNT
SET   balance = balance - 2300
WHERE Acct_Num = '4000-1956-2001';

-- Step 4: Record service charge (0.2% of withdrawn amount)
INSERT INTO Transaction VALUES
('4000-1956-2001', -2300.00 * 0.02, 'ATM Withdrawal', 'CA', CURRENT_DATE());

-- Step 5: Deduct service charge from balance
UPDATE ACCOUNT
SET   balance = balance - 2300 * 0.02
WHERE Acct_Num = '4000-1956-2001';

-- Step 6: Commit — make changes permanent
COMMIT;
'''


# ========================================================
# COMMIT & ROLLBACK
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 1 — Transaction Processing
# ========================================================

'''
[COMMIT]
  - Ends the current transaction
  - Permanently saves transaction-effected changes to the physical data files and makes them visible to other users
  - After COMMIT, the current transaction exits and all savepoints within it disappear
  - There is no "undo" after COMMIT — the changes are final
[COMMIT Example — Delete inactive accounts]
[ROLLBACK]
  - In a running transaction that is not yet physically committed , ROLLBACK undoes all transactional changes and retains the original status of the data
  - Very useful during interactive operations when users want to cancel modifications
[ROLLBACK Example]
  NOTE: ⚠ ROLLBACK only works before COMMIT. Once a transaction is committed, the changes cannot be undone — there is no "undo" option in the database.
'''


# Example 1 — COMMIT & ROLLBACK
sql = '''
-- Verify rows to delete first
SELECT * FROM ACCOUNT
WHERE Acct_status = 'INACTIVE'
AND  (balance = 0 OR balance IS NULL);

-- Delete and commit
DELETE FROM ACCOUNT
WHERE Acct_status = 'INACTIVE'
AND  (balance = 0 OR balance IS NULL);

COMMIT;
'''


# Example 2 — COMMIT & ROLLBACK
sql = '''
-- Delete a record (within an uncommitted transaction)
DELETE FROM CUSTOMER WHERE CUST_ID = 123006;

-- Oops! Undo the delete — customer 123006 is restored
ROLLBACK;

-- Verify: 123006 is back
SELECT * FROM CUSTOMER;
'''


# ========================================================
# SET TRANSACTION
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 1 — Transaction Processing
# ========================================================

'''
[What SET TRANSACTION Does]
  - Wraps DML statements within a transaction boundary
  - Separates execution of DML statements from those of other concurrent transactions
  - Inter-locks the underlying affected records to prevent concurrent modification
[How Isolation is Achieved]
  - Data integrity requires each transaction to know the latest value of a record even if multiple transactions affect it simultaneously
  - Achieved by: restricting other transactions from working on the same records until the first completes
  - And by: maintaining a queue — other transactions wait until the first transaction commits
[Isolation Example]
  - At 9:00 AM: Transaction-1 starts updating Account 123456; expected to complete by 9:05 AM
  - At 9:02 AM: Transaction-2 also tries to update Account 123456
  - Transaction-2 will not have access to Account 123456 until 9:05 AM — it waits in queue
  - After 9:05 AM: Transaction-2 proceeds and executes
  NOTE: ℹ MySQL handles ISOLATION internally — users don't need to manage it. However, users can manually alter isolation levels to modify constraints and tune the trade-off between data integrity and performance.
'''


# ### Section 2 — Isolation Levels
# *REPEATABLE READ · READ COMMITTED · READ ONLY · READ WRITE*


# ========================================================
# Isolation — Overview & Classification
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 2 — Isolation Levels
# ========================================================

'''
[Classification of Isolation Levels]
  - REPEATABLE READ — acquires a table-level lock ; other instances cannot UPDATE, INSERT, or DELETE on the locked table while Transaction-1 is running (even on different rows)
  - READ COMMITTED — acquires a record-level lock ; only the specific record(s) being modified are locked; other records and inserts in the same table are allowed by other sessions
  - SERIALIZABLE — the strictest level; transactions are fully serialized (not covered in practice examples in this deck)
[Transaction Modifiers (same instance)]
  - READ WRITE (default) — any DML statement is allowed in the current instance
  - READ ONLY — only SELECT is allowed; UPDATE/INSERT/DELETE throws an error
  NOTE: 💡 Pre-requisite for all isolation practice sessions: Disable Auto-commit in MySQL Workbench — otherwise each statement auto-commits and isolation effects cannot be observed.
'''


# ========================================================
# REPEATABLE READ — Table-Level Lock
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 2 — Isolation Levels
# ========================================================

'''
[Behaviour]
  - When Instance-1 executes an UPDATE within a REPEATABLE READ transaction, a table-level lock is acquired on the entire table
  - This lock affects ALL records in the table — not just the row being updated
  - Instance-2 cannot UPDATE, INSERT, or even SELECT with modification intent on any row in the same table — it keeps running/waiting
[Instance-1 — Set REPEATABLE READ]
[Instance-2 — Experiences the Lock]
  NOTE: ⚠ REPEATABLE READ locks the entire table . Even modifying a completely different row in Instance-2 is blocked until Instance-1 COMMITs or ROLLBACKs.
'''


# Example 1 — REPEATABLE READ — Table-Level Lock
sql = '''
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- Check balance
SELECT Balance FROM ACCOUNT
WHERE Acct_Num = '4000-1956-2001';

-- This UPDATE acquires a TABLE-LEVEL LOCK
UPDATE ACCOUNT
SET   balance = balance - 2300
WHERE Acct_Num = '4000-1956-2001';

-- Verify updated balance
SELECT Balance FROM ACCOUNT
WHERE Acct_Num = '4000-1956-2001';
'''


# Example 2 — REPEATABLE READ — Table-Level Lock
sql = '''
-- Try to update a DIFFERENT record — still blocked!
UPDATE ACCOUNT
SET   balance = balance - 1500
WHERE Acct_Num = '4000-1956-5698';  -- different account, still waits

-- Try to insert a new record — also blocked!
INSERT INTO ACCOUNT
VALUES (123001, '4000-1956-9999', 'SAVINGS', 69000, 'ACTIVE', 'P');
-- Status: RUNNING / WAITING — lock acquired by Instance-1
'''


# ========================================================
# READ COMMITTED — Record-Level Lock
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 2 — Isolation Levels
# ========================================================

'''
[Behaviour]
  - When Instance-1 executes an UPDATE within a READ COMMITTED transaction, a record-level lock is acquired — only on the specific record(s) being modified
  - Instance-2 can INSERT new records into the same table (lock is only on existing modified rows, not the whole table)
  - Instance-2 cannot update the same specific record that Instance-1 has locked
[Instance-1 — Set READ COMMITTED]
[Instance-2 — Only Partially Blocked]
  NOTE: REPEATABLE READ vs READ COMMITTED 
 REPEATABLE READ 
 
 Acquires a table-level lock 
 ALL rows in the table are locked — not just the modified row 
 No INSERT, UPDATE, or DELETE allowed from any other session until commit 
 Stricter — highest integrity, lowest concurrency 
 
 READ COMMITTED 
 
 Acquires a record-level lock only on the modified rows 
 Only the specific rows being modified are locked 
 INSERT of new records from other sessions is allowed 
 More flexible — higher concurrency, lower integrity overhead
'''


# Example 1 — READ COMMITTED — Record-Level Lock
sql = '''
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

SELECT Balance FROM ACCOUNT
WHERE Acct_Num = '4000-1956-2001';

-- Record-level lock on Acct_Num '4000-1956-2001' only
UPDATE ACCOUNT
SET   balance = balance - 2300
WHERE Acct_Num = '4000-1956-2001';
'''


# Example 2 — READ COMMITTED — Record-Level Lock
sql = '''
-- SELECT on different account — works fine
SELECT Balance FROM ACCOUNT
WHERE Acct_Num = '4000-1956-5698';

-- INSERT new record — SUCCEEDS (not blocked by record-level lock)
INSERT INTO ACCOUNT
VALUES ('4000-1956-9999', 'SAVINGS', 69000, 'ACTIVE', 'P');
-- Success! Instance-1's lock is only on the row it modified
'''


# ========================================================
# READ / WRITE Transaction Modifiers
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 2 — Isolation Levels
# ========================================================

'''
[Two Modifiers]
  - READ WRITE (default) — any DML statement (SELECT, INSERT, UPDATE, DELETE) is allowed in the current instance
  - READ ONLY — only SELECT is permitted; any UPDATE/INSERT/DELETE throws the error: "Cannot execute statement in a READ ONLY transaction"
[SET TRANSACTION READ WRITE (default)]
[SET TRANSACTION READ ONLY]
[Altering Modifiers Mid-Session]
  - Modifiers set at instance level using SET SESSION TRANSACTION can be altered, but do not affect the current running transaction
  - The new modifier takes effect only from the next transaction
'''


# Example 1 — READ / WRITE Transaction Modifiers
sql = '''
SET TRANSACTION READ WRITE;   -- default; all DML allowed

SELECT Balance FROM ACCOUNT WHERE Acct_Num = '4000-1956-2001';

UPDATE ACCOUNT                -- executes successfully
SET   balance = balance - 2300
WHERE Acct_Num = '4000-1956-2001';
'''


# Example 2 — READ / WRITE Transaction Modifiers
sql = '''
SET TRANSACTION READ ONLY;

SELECT Balance FROM ACCOUNT WHERE Acct_Num = '4000-1956-2001';  -- OK

UPDATE ACCOUNT                -- ERROR: READ ONLY transaction
SET   balance = balance - 2300
WHERE Acct_Num = '4000-1956-2001';
'''


# Example 3 — READ / WRITE Transaction Modifiers
sql = '''
SET SESSION TRANSACTION READ WRITE;  -- current mode

START TRANSACTION;

SET SESSION TRANSACTION READ ONLY;   -- effective from NEXT transaction only

-- This DML still executes (current transaction is READ WRITE)
UPDATE ACCOUNT
SET   balance = balance - 2300
WHERE Acct_Num = '4000-1956-2001';

COMMIT;   -- end current transaction

-- Second transaction: now READ ONLY kicks in
START TRANSACTION;
UPDATE ACCOUNT SET balance = balance - 2300
WHERE Acct_Num = '4000-1956-2001';   -- ERROR here
'''


# ### Section 3 — SAVEPOINT & RELEASE SAVEPOINT
# *Partial rollback within a transaction*


# ========================================================
# SAVEPOINT
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 3 — SAVEPOINT & RELEASE SAVEPOINT
# ========================================================

'''
[Definition]
  - So far, ROLLBACK was applied to the entire transaction . SAVEPOINT enables partial rollback
  - SAVEPOINT marks a portion of a transaction with a unique identifier/label
  - These checkpoints are later referred to by ROLLBACK to undo only a portion of the transaction
  - Very useful for error recovery in database applications without losing the entire transaction
[Syntax]
[Example — Partial Rollback with SAVEPOINTs]
[How SAVEPOINT + ROLLBACK TO Works]
  - Before any delete: SAVEPOINT customer_1 is set
  - After deleting 123004: SAVEPOINT customer_2 is set — this captures the state "only 123004 deleted"
  - ROLLBACK TO customer_2 — undoes everything after customer_2 (deletes of 123003 and 123002 are reversed)
  - COMMIT — permanently applies the state at customer_2 (only 123004 deleted); all savepoints disappear
  NOTE: ⚠ Upon COMMIT , all savepoints defined within the transaction are permanently lost . You cannot ROLLBACK TO them after committing.
'''


# Example 1 — SAVEPOINT
sql = '''
SAVEPOINT label_name;       -- mark a checkpoint
ROLLBACK TO label_name;     -- undo back to that checkpoint
'''


# Example 2 — SAVEPOINT
sql = '''
-- Initial data check
SELECT * FROM CUSTOMER
WHERE CUST_ID IN (123002, 123003, 123004);

START TRANSACTION;

SAVEPOINT customer_1;                -- checkpoint before any delete
DELETE FROM CUSTOMER WHERE CUST_ID = 123004;

SAVEPOINT customer_2;                -- checkpoint after deleting 123004
DELETE FROM CUSTOMER WHERE CUST_ID = 123003;

SAVEPOINT customer_3;                -- checkpoint after deleting 123003
DELETE FROM CUSTOMER WHERE CUST_ID = 123002;

-- Rollback to customer_2: undoes deletion of 123003 and 123002
-- Only deletion of 123004 (done before customer_2) is kept
ROLLBACK TO customer_2;

COMMIT;   -- all savepoints are lost after commit

-- Result: 123004 is deleted; 123002 and 123003 still exist
SELECT * FROM CUSTOMER
WHERE CUST_ID IN (123002, 123003, 123004);
'''


# ========================================================
# RELEASE SAVEPOINT
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 3 — SAVEPOINT & RELEASE SAVEPOINT
# ========================================================

'''
[Definition]
  - Savepoints can be deleted from within a transaction without affecting the transaction itself
  - Once a savepoint is released, you can no longer ROLLBACK TO it — attempting to do so throws an error
  - ROLLBACK TO savepoints that were created before the released one still work
[Example — Release and Attempt ROLLBACK]
  NOTE: 💡 Think of RELEASE SAVEPOINT as erasing a bookmark — the pages still exist, but you can no longer jump back to that specific page marker.
'''


# Example 1 — RELEASE SAVEPOINT
sql = '''
START TRANSACTION;

SAVEPOINT customer_1;
DELETE FROM CUSTOMER WHERE CUST_ID = 123007;

SAVEPOINT customer_2;
DELETE FROM CUSTOMER WHERE CUST_ID = 123006;

SAVEPOINT customer_3;
DELETE FROM CUSTOMER WHERE CUST_ID = 123005;

-- Release customer_2 — it is now gone
RELEASE SAVEPOINT customer_2;

ROLLBACK TO customer_2;  -- ERROR: savepoint customer_2 does not exist
ROLLBACK TO customer_3;  -- ERROR: customer_2 was between 1 and 3; customer_3 may still exist

-- This ROLLBACK works — customer_1 exists and was before the released savepoint
ROLLBACK TO customer_1;  -- restores state before ALL three deletes
'''


# ### Section 4 — Locking
# *Locking Levels · Shared Locks · Exclusive Locks*


# ========================================================
# Locks — Overview
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 4 — Locking
# ========================================================

'''
[Definition]
  - Locks are acquired by user transactions in a session
  - SQL Engine locks objects when a transaction begins DML statements on each record
  - To ensure data integrity, DML statements acquire explicit locks on data records or tables
  - Multiple users in an integrated environment can see changes applied by each other only after commit
  - After transactions complete, locks are released
[Lock Hierarchy]
  - Locks can be acquired at different levels for different transaction purposes
  - Higher-level locks (table) are broader; lower-level locks (row/record) are more precise
'''


# ========================================================
# Locking Levels
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 4 — Locking
# ========================================================

'''
[Row Level — RID (Row ID)]
  - Row-ID is a unique address of an individual record in a table
  - DML statements isolate records from other transactions using this row-id
  - The row-id is locked, then the DML operation is performed
[Table Level]
  - A transaction with DML statements locks the entire table and its corresponding indexes
  - More reliable in batch processing with high volume data — restricts users from accessing tables; prevents performance degradation when taking data snapshots
[Key Level]
  - Indexes are generated by default when a Primary Key is created
  - Locks are acquired on these index keys
[Memory-Level Locks]
[Page Lock]
  - A page = 8 KB unit used by a data file or index
  - Lock is acquired at the page level — affects all rows in that 8 KB page
[Extent Lock]
  - An extent = 8 contiguous data pages (64 KB)
  - Lock is acquired at the extent level — coarser than page lock
[Database Lock]
  - The entire database is locked
  - Used for maintenance purposes only — never for normal transactions
'''


# ========================================================
# Shared Locks (S) — Read Locks
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 4 — Locking
# ========================================================

'''
[Definition]
  - Shared lock is an initial lock acquired by a SELECT statement to lock rows before applying next DML statements
  - Useful to avoid deadlocks when multiple transactions use the same DML statements
  - Multiple transactions can acquire multiple shared locks (S) simultaneously on the same records — they don't block each other
[Syntax — LOCK IN SHARE MODE]
[Shared Lock + UPDATE (within same session)]
  NOTE: ⚠ When Session-1 escalates from a shared lock to an exclusive lock (through UPDATE), Session-2's shared lock request on the same record is put in the queue — it must wait.
'''


# Example 1 — Shared Locks (S) — Read Locks
sql = '''
-- Instance 1: Acquire shared lock
START TRANSACTION;
SELECT * FROM ACCOUNT
WHERE Acct_Num = '4000-1956-2001'
LOCK IN SHARE MODE;

-- Instance 2: Also acquires shared lock on same record — no conflict
START TRANSACTION;
SELECT * FROM ACCOUNT
WHERE Acct_Num = '4000-1956-2001'
LOCK IN SHARE MODE;  -- succeeds — shared locks are compatible with each other
'''


# Example 2 — Shared Locks (S) — Read Locks
sql = '''
-- Session 1: Select with shared lock, then update
START TRANSACTION;
SELECT * FROM ACCOUNT
WHERE Acct_Num = '4000-1956-2001' LOCK IN SHARE MODE;

UPDATE ACCOUNT
SET   balance = balance - balance * 0.04
WHERE Acct_Num = '4000-1956-2001';  -- triggers escalation to exclusive lock

-- Session 2: tries to get shared lock on same record
START TRANSACTION;
SELECT * FROM ACCOUNT
WHERE Acct_Num = '4000-1956-2001' LOCK IN SHARE MODE;
-- Session 2 WAITS — it is in Queue until Session 1 COMMITs/ROLLBACKs
'''


# ========================================================
# Exclusive Locks (X) — Write Locks
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 4 — Locking
# ========================================================

'''
[Definition]
  - Exclusive locks are acquired by DELETE, INSERT, and UPDATE statements — any DML that modifies data
  - Data cannot be modified by two DML statements simultaneously — one transaction must wait
  - Mandatorily acquired by any modifying DML statement by default when executed
  - Cannot be shared with any other transaction — all others must wait until the first DML transaction completes and commits
[Critical Rule]
  - Once an Exclusive lock (X) is acquired: other transactions gain NEITHER Shared (S) NOR Exclusive (X) locks on the same records — they all wait
[Multi-Session Exclusive Lock Scenario]
  NOTE: Shared (S) vs Exclusive (X) Locks 
 Shared Lock (S) — Read Lock 
 
 Acquired by SELECT … LOCK IN SHARE MODE 
 Multiple sessions can hold S lock on the same record simultaneously 
 Compatible with other S locks — they coexist without conflict 
 Not compatible with an X lock on the same record — S lock waits if X is present 
 
 Exclusive Lock (X) — Write Lock 
 
 Acquired automatically by INSERT, UPDATE, DELETE statements 
 Only one session can hold an X lock on a record at a time 
 Incompatible with both S and X locks from other sessions 
 All other sessions must wait until the X lock is released (through COMMIT or ROLLBACK)
'''


# Example 1 — Exclusive Locks (X) — Write Locks
sql = '''
-- Session 1: acquires Shared lock, then Exclusive lock (via UPDATE)
START TRANSACTION;
SELECT * FROM ACCOUNT WHERE Acct_Num = '4000-1956-2001' LOCK IN SHARE MODE;
UPDATE ACCOUNT SET balance = balance - balance * 0.04
WHERE Acct_Num = '4000-1956-2001';   -- ← X lock acquired here

-- Session 2: acquires Shared lock, then tries Exclusive lock — WAITS
START TRANSACTION;
SELECT * FROM ACCOUNT WHERE Acct_Num = '4000-1956-2001' LOCK IN SHARE MODE;
UPDATE ACCOUNT SET balance = balance - balance * 0.04
WHERE Acct_Num = '4000-1956-2001';   -- ← WAITING for Session-1 to release X lock

-- Session 3: acquires NEITHER S nor X lock — WAITS
START TRANSACTION;
SELECT * FROM ACCOUNT WHERE Acct_Num = '4000-1956-2001' LOCK IN SHARE MODE;
UPDATE ACCOUNT SET balance = balance - balance * 0.04
WHERE Acct_Num = '4000-1956-2001';   -- ← also WAITING
'''


# ### Section 5 — Views & Virtual Tables
# *Simple · Complex · Inline · Materialized · Horizontal · Vertical · Group · Joined · CHECK OPTION*


# ========================================================
# Views — Overview
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 5 — Views & Virtual Tables
# ========================================================

'''
[What is a Virtual Table?]
  - A virtual table is a derived form of data from physical database tables
  - Logically represented using physical data — does not store any data itself
  - A virtual table is a construct of record sets that are not actual tables; they are referenced in SQL statements like normal tables
  - Otherwise called Views — stored as database objects in MySQL's information_schema and can be retrieved without rewriting the query
[What is a View?]
  - A view is a database object created using a SELECT query with complex logic
  - Views are the logical representation of physical data
  - Behave like physical tables — usable in any part of SQL queries
  - DML operations can be performed on base tables through views
  - Stored in the data dictionary — retrieved easily at any time
[Advantages of Views]
  - Stored queries that are reused — accessible by multiple users in different sessions
  - High scalability — one view serves many queries
  - Hide confidential columns (SSN, date of birth, address, telephone)
  - Avoid direct access to physical data — protects against hackers in downstream web applications
  - Materialized views useful in centralized environments where many users access large batch data
  - Simplify complex queries — views absorb joins and conditions so the parent query stays clean
[Disadvantages of Views]
  - When a base table is dropped, its associated view becomes obsolete
  - Queries using views are slightly slower — SQL engine performs semantic checking of the view each time
  - Views created using aggregate functions are restricted in WHERE clauses
  - Materialized views store physical data → redundant data → additional storage for MViews and Logs
  - Views are inefficient with remote database tables — high I/O between local and remote
[How RDBMS Handles Views — Before/After Images]
  - Views reflect committed data only — uncommitted updates are NOT visible through the view
  - When a base table is being updated: RDBMS maintains before-image (pre-update snapshot) and after-image (post-update)
  - SELECTs during update show the before-image — consistent read
  - After-image is written to disk after COMMIT; before-image is then deleted
  - This maintains overhead of multiple before-images for concurrent users to ensure data integrity
  NOTE: ℹ Views are stored in the data dictionary: SELECT * FROM ALL_VIEWS WHERE view_name IN ('SIMPLE_VIEW', 'COMPLX_VIEW');
'''


# ========================================================
# Simple View
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 5 — Views & Virtual Tables
# ========================================================

'''
[Definition]
  - Created with a SELECT query written using a single table
  - DML operations (INSERT, UPDATE, DELETE) are easily performed — just like working directly on the table
[Syntax]
'''


# Example 1 — Simple View
sql = '''
CREATE VIEW Simple_view AS
SELECT * FROM CUSTOMER;
'''


# ========================================================
# Complex View
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 5 — Views & Virtual Tables
# ========================================================

'''
[Definition]
  - Created using a SELECT query written with multiple tables using JOINs, subqueries, WITH clauses , and conditional filters
[Syntax]
[Usage in Queries]
'''


# Example 1 — Complex View
sql = '''
CREATE VIEW Complex_view AS
SELECT c.Cust_Id, a.ACCOUNT
FROM  CUSTOMER c
JOIN  ACCOUNT a
WHERE c.Cust_Id = a.Cust_Id
AND   a.balance > 300000;
'''


# Example 2 — Complex View
sql = '''
-- Complex_view handles the JOIN + filter; parent query stays simple
SELECT   CA_vw.Cust_Id, bat.Acct_Num,
         bat.Tran_Amount, CA_vw.balance
FROM     Transaction bat
JOIN     Complex_view CA_vw
ON       bat.Acct_Num = CA_vw.Acct_Num;
'''


# ========================================================
# Inline View
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 5 — Views & Virtual Tables
# ========================================================

'''
[Definition]
  - A subquery is called an Inline View if and only if it is used in the FROM clause of a SELECT query
  - NOT stored in any data dictionary — dynamically defined in queries each time
[Syntax]
'''


# Example 1 — Inline View
sql = '''
SELECT * FROM (
    SELECT c.Cust_Id, ba.ACCOUNT
    FROM   CUSTOMER c
    JOIN   ACCOUNT ba
    WHERE  c.Cust_Id = ba.Cust_Id
    AND    ba.balance > 300000
) AS inline_result;
'''


# ========================================================
# Materialized View (Oracle)
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 5 — Views & Virtual Tables
# ========================================================

'''
[Definition]
  - Unlike normal views, Materialized Views store the results of complex SQL queries physically
  - Also called Snapshots of database tables
  - Very useful when the SQL engine takes too long to execute complex query logic on every call
  - Refreshed with new data at scheduled intervals
  - Mostly used in data marts — repositories of summarized historical data for a specific business unit (e.g., the sales department)
[Create and Refresh (Oracle)]
[Complete Refresh]
  - Truncates the entire materialized view data first
  - Reloads from scratch using the full underlying query
  - Slower — time = full query execution + data reload
  - Method code: 'C'
[Fast Refresh]
  - Uses a materialized view log — captures history of changes on the base table
  - Loads only delta (changed) records — not the full dataset
  - Faster — only changed data is transferred
  - Requires a log to be created on the base table first
  - Method code: 'F'
'''


# Example 1 — Materialized View (Oracle)
sql = '''
-- Create materialized view (no data yet)
CREATE MATERIALIZED VIEW mview_account AS
SELECT * FROM ACCOUNT WHERE Balance > 500000;

-- Refresh explicitly to load / update data
EXECUTE dbms_mview.refresh('mview_account');

SELECT * FROM mview_account;
'''


# Example 2 — Materialized View (Oracle)
sql = '''
-- COMPLETE REFRESH
CREATE MATERIALIZED VIEW REFRESH COMPLETE mview_account_RC AS
SELECT * FROM ACCOUNT WHERE Balance > 500000;
EXECUTE dbms_mview.refresh(list => 'mview_account_RC', method => 'C');

-- FAST REFRESH (requires log on base table first)
CREATE MATERIALIZED VIEW fastrefresh_log ON ACCOUNT WITH SEQUENCE;
CREATE MATERIALIZED VIEW REFRESH FAST mview_account_RFast AS
SELECT * FROM ACCOUNT WHERE Balance > 500000;
EXECUTE dbms_mview.refresh(list => 'mview_account_RFast', method => 'F');
'''


# ========================================================
# Horizontal View
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 5 — Views & Virtual Tables
# ========================================================

'''
[Definition]
  - A Horizontal view dynamically represents data without awareness of the specific columns
  - Uses wildcard (*) — does not need to know the number of columns or their data types
  - Base tables are explicitly defined in the view, but column details are left dynamic
  - Any changes to column names or data types do not affect view creation
[Syntax]
'''


# Example 1 — Horizontal View
sql = '''
-- Wildcard "*" references all columns dynamically
CREATE VIEW Horizontal_view AS
SELECT ba.*
FROM  ACCOUNT
WHERE balance > 99999;
'''


# ========================================================
# Vertical View
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 5 — Views & Virtual Tables
# ========================================================

'''
[Definition]
  - Built with predefined, explicitly named columns
  - Changes to column data types do not affect the view unless they are type-cast or system functions are applied
  - If column names in the base table change, the view must be updated accordingly — otherwise throws an error
[Syntax]
  NOTE: Horizontal vs Vertical View — Side by Side 
 Horizontal View 
 
 Columns selected through wildcard * — dynamic, unknown at definition time 
 Execution plan is recalculated each time the view is accessed (columns not cached) 
 Easy maintenance — no view update required when columns are added or renamed 
 User has access to all columns in the base table 
 User can apply any data type conversions on the returned columns 
 
 Vertical View 
 
 Columns explicitly named at definition — static, fixed at creation time 
 Execution plan is cached — faster repeated access when columns are stable 
 Maintenance required when column names in the base table change 
 Sensitive columns can be hidden by simply not including them 
 Data type conversions are allowed unless incompatible with internal functions in the view
'''


# Example 1 — Vertical View
sql = '''
CREATE VIEW Vertical_view AS
SELECT Cust_Id, Acct_Num, Balance, Acct_Type, Acct_status, Relation
FROM  ACCOUNT;
'''


# ========================================================
# Row-Column Subset View
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 5 — Views & Virtual Tables
# ========================================================

'''
[Definition]
  - Represents a subset of records AND a subset of columns — filters rows and hides columns simultaneously
[Syntax]
'''


# Example 1 — Row-Column Subset View
sql = '''
CREATE VIEW Subset_view AS
SELECT Cust_Id, Acct_Num, Balance     -- only 3 of the columns
FROM  ACCOUNT
WHERE Balance > 700000;              -- only high-balance records
'''


# ========================================================
# Group View (Grouped View)
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 5 — Views & Virtual Tables
# ========================================================

'''
[Definition]
  - Created using a SELECT query with grouping (aggregate) functions applied on multiple rows of data
  - Displays aggregate results only — individual rows are collapsed
[Syntax]
  NOTE: ⚠ Views created using aggregate functions are restricted in WHERE clauses of external queries — use HAVING for group-level filtering inside the view.
'''


# Example 1 — Group View (Grouped View)
sql = '''
CREATE VIEW Grouping_view (Acct_Num, total_transaction) AS
SELECT Acct_Num, SUM(Tran_Amount)
FROM  Transaction
GROUP BY Acct_Num;
'''


# ========================================================
# Joined View
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 5 — Views & Virtual Tables
# ========================================================

'''
[Definition]
  - Represents data from more than one base table joined using key columns
  - The underlying query can have JOINs or subqueries on base tables
  - From the view user's perspective, data from multiple tables appears as a single unified entity
[Syntax]
'''


# Example 1 — Joined View
sql = '''
CREATE VIEW Joined_view AS
SELECT c.Cust_Id, c.Name, a.Acct_Num,
       a.Acct_Type, a.Balance, c.telephone
FROM  ACCOUNT a
JOIN  CUSTOMER c
ON    a.Cust_Id = c.Cust_Id;
'''


# ========================================================
# WITH CHECK OPTION
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 5 — Views & Virtual Tables
# ========================================================

'''
[Definition]
  - Simple views can be queried and allow DML operations
  - WITH CHECK OPTION restricts users from performing DML operations that would violate the view's WHERE condition
  - Without CHECK OPTION, you can INSERT records that don't satisfy the view's filter — they insert into the base table but are invisible through the view
[Example — View with CHECK OPTION]
[LOCAL CHECK OPTION]
  - Validates only this view's own WHERE condition
  - Ignores conditions of any parent/dependent views in the chain
  - Example: local_view on top of normal_view with LOCAL — only local_view's condition is enforced; normal_view's condition can be bypassed
[CASCADED CHECK OPTION]
  - Validates all conditions of every view in the entire chain
  - Parent view conditions cannot be bypassed
  - Example: cascaded_view on top of normal_view with CASCADED — both conditions must be satisfied before INSERT succeeds
[LOCAL CHECK Example]
[CASCADED CHECK Example]
  NOTE: LOCAL vs CASCADED — Decision Rule 
 
 LOCAL : Only my own WHERE condition matters — parent view conditions are ignored (bypassable) 
 CASCADED : All conditions in the entire view chain must be satisfied — parent view conditions cannot be bypassed 
 Use CASCADED when strict data integrity across the view hierarchy is required 
 Use LOCAL when only the immediate view's rules should be enforced
'''


# Example 1 — WITH CHECK OPTION
sql = '''
CREATE VIEW View_with_Check AS
SELECT * FROM ACCOUNT
WHERE Balance > 5000
WITH CHECK OPTION;

-- FAILS: balance 4000 violates the view's WHERE Balance > 5000
INSERT INTO View_with_Check VALUES
(123001, '4000-7843-3002', 'SAVINGS', 4000, 'ACTIVE', 'P');
'''


# Example 2 — WITH CHECK OPTION
sql = '''
-- normal_view: balance >= 80000 (no check option — bypassable)
CREATE VIEW normal_view AS
SELECT * FROM ACCOUNT WHERE Balance >= 80000;

-- local_view: balance <= 90000, LOCAL only validates THIS condition
CREATE VIEW local_view AS
SELECT * FROM normal_view
WHERE Balance <= 90000
WITH LOCAL CHECK OPTION;

-- Insert balance=65000: bypasses normal_view condition (no check there)
-- local_view only checks its own: 65000 <= 90000 → SUCCEEDS
INSERT INTO local_view VALUES
(123001, '6500-3823-4032', 'SAVINGS', 65000, 'ACTIVE', 'P');
'''


# Example 3 — WITH CHECK OPTION
sql = '''
-- normal_view: balance >= 80000
CREATE VIEW normal_view AS
SELECT * FROM ACCOUNT WHERE Balance >= 80000;

-- cascaded_view: balance <= 90000, CASCADED checks BOTH conditions
CREATE VIEW cascaded_view AS
SELECT * FROM normal_view
WHERE Balance <= 90000
WITH CASCADED CHECK OPTION;

-- Insert balance=70000: FAILS — violates normal_view's >= 80000 condition
INSERT INTO cascaded_view VALUES
(123001, '5000-1253-4312', 'SAVINGS', 70000, 'ACTIVE', 'P');
-- Only records with balance BETWEEN 80000 AND 90000 are accepted
'''


# ========================================================
# DROP VIEW
# 7 — Transactions, Isolation, Locking & Views
# SECTION: Section 5 — Views & Virtual Tables
# ========================================================

'''
[Definition]
  - Any type of view can be dropped without affecting the base table data
  - Dropping a view only removes the view definition from the data dictionary
[Syntax]
'''


# Example 1 — DROP VIEW
sql = '''
DROP VIEW view_name;
'''
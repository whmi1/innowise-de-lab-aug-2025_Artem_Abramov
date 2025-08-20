--Task 1: Insert 2 new employees into table Employees

INSERT INTO 
    employees(
        firstname,
        lastname,
        department,
        salary
    )
VALUES
    (
        'Gosha',
        'Dudar',
        'IT',
        52000.00
    ),
    (
        'Steve',
        'Jobs',
        'Head',
        1000000.00
    );

--Task 2: Select all employees from the table
SELECT 
    * 
FROM 
    employees
ORDER BY
    employeeid;

--Task 3: Select only FirstName and LastName from 'IT' employees
SELECT
    firstname,
    lastname
FROM
    employees
WHERE
    department = 'IT';

--Task 4: Update 'Alice Smith's Salary to 65000.00
UPDATE
    employees
SET
    salary = 65000.00
WHERE
    firstname = 'Alice'
    AND lastname = 'Smith';

--Task 5: Delete employee, whose last name is 'Prince'
ALTER TABLE
    employeeprojects
ADD CONSTRAINT
    employeeid_delition
FOREIGN KEY (employeeid) REFERENCES employees(employeeid)
ON DELETE CASCADE;
    
DELETE FROM 
    employees 
WHERE 
    lastname = 'Prince';

--Task 6: Check all chenges using SELECT * FROM Employees
SELECT 
    * 
FROM 
    employees;

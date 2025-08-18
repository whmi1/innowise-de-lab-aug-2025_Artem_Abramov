--Task 1: Create new table named Departments with next columns:
CREATE TABLE 
    Departments(
        DepartmentID SERIAL PRIMARY KEY,
        DepartmentName VARCHAR(50) UNIQUE NOT NULL,
        Location VARCHAR(50)
    );

--Task 2: Edit Employees table by inserting new column named Email(VARCHAR(100))
ALTER TABLE 
    employees 
ADD COLUMN 
    Email VARCHAR(100);

--Task 3: Add UNIQUE constraint to the Email column, pre-filling it with any values
ALTER TABLE 
    employees
ADD CONSTRAINT
    Email UNIQUE (email);

UPDATE employees SET email = 'luna.wraith92@frostmail.net' WHERE employeeid = 1;
UPDATE employees SET email = 'dexter.qubit@neonbyte.org' WHERE employeeid = 2;
UPDATE employees SET email = 'ivy.zephyr@cloudhaven.io' WHERE employeeid = 3;
UPDATE employees SET email = 'niko.shadowfax@glimmerhub.com' WHERE employeeid = 4;
UPDATE employees SET email = 'talia.ember@pixelforge.dev' WHERE employeeid = 5;
UPDATE employees SET email = 'jax.orbitron@cybernest.co' WHERE employeeid = 6;
UPDATE employees SET email = 'soren.echo@phantomlane.xyz' WHERE employeeid = 7;

SELECT * FROM employees;

--Task 4: Rename Location column in Departments table into OfficeLocation
ALTER TABLE
    departments
RENAME COLUMN
    location to officelocation;

SELECT * FROM departments;


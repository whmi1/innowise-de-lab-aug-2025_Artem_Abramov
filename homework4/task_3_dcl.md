--All images are in "images_for_3_task" directory

--Task 1: Create new user PostgreSQL (role) with name 'hr_user' and simple password
CREATE USER 
    hr_user 
WITH PASSWORD 
    '12345678';

--Task 2: Allow hr_user do SELECT in the Employees table
CREATE ROLE selection_role;

GRANT
    SELECT
ON  
    employees
TO
    selection_role;

GRANT
    selection_role
TO
    hr_user;

--Task 3: Test: In a new session, connect as hr_user and try to execute SELECT * FROM Employees;. (Should work).

--All images are in "images_for_3_task" directory

--Task 4: As hr_user, try running INSERT command to add a new employee to the Employees table (Shouldn't work)

--All images are in "images_for_3_task" directory

--Task 5: As administrator, allow hr_user run commands INSERT and UPDATE the Employees table
GRANT INSERT, UPDATE ON employees TO selection_role;

GRANT selection_role TO hr_user;

--Task 6: Test: As hr_user, try to execute INSERT and UPDATE on employee. (This should work now).

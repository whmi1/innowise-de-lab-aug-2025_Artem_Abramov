--Task 1: Grow Salary all employees in 'HR' department on 10 % 
UPDATE
    employees
SET
    salary = salary * 1.1
WHERE
    department = 'HR';

--Task 2: Update the Department of any employee with a Salary above 70000.00 to 'Senior IT'.
UPDATE
    employees
SET
    department = 'Senior IT'
WHERE
    employeeid = (
        SELECT 
            employeeid
        FROM
            employees
        WHERE
            salary > 70000.00 AND department = 'IT'
        LIMIT 1
    );

--Task 3: Delete all employees who are not assigned to any project in the EmployeeProjects table.

DELETE FROM
    employees e
WHERE
    e.employeeid NOT IN (
        SELECT 
            ep.employeeid
        FROM
            employeeprojects ep
        GROUP BY
            ep.employeeid
    );

SELECT * FROM employeeprojects;

/*
    Task 4: Insert a new project and assign it to two existing employees with a certain 
    number of HoursWorked in EmployeeProjects, all in one BEGIN/COMMIT block.
*/
BEGIN;

    INSERT INTO
        projects(projectname, budget, startdate, enddate)
    VALUES
        ('Database Development', 100000.00, '2024-03-01', '2024-09-15');
    
    SELECT * FROM projects;

    SAVEPOINT project_added;

    INSERT INTO
        employeeprojects(employeeid, projectid, hoursworked)
    VALUES 
        (1, 4, 100),
        (3, 4, 80);

    SELECT * FROM employeeprojects;

COMMIT;

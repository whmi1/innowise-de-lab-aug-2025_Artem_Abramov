--Task 1: Find the ProjectName of all projects in which 'Bob Johnson' has worked for more than 150 hours.
SELECT
    projectname
FROM
    projects
WHERE
    projectid IN (
        SELECT
            projectid
        FROM
            employeeprojects
        WHERE
            employeeid = 2
    );

--Task 2: Increase the budget of all projects by 10% if at least one IT employee is assigned to them.
UPDATE 
    projects
SET
    budget = budget * 1.1
WHERE
    projectid IN (
        SELECT DISTINCT
            ep.projectid
        FROM
            employeeprojects ep
        JOIN
            employees e ON ep.employeeid = e.employeeid
        WHERE
            e.department = 'IT'
            AND ep.projectid IS NOT NULL
    )
    AND budget IS NOT NULL;

SELECT * FROM projects;

--Task 3: For any project that does not yet have an EndDate (EndDate IS NULL), set the EndDate to one year after its StartDate.
INSERT INTO
    projects(projectname, budget, startdate, enddate)
VALUES
    ('AI Testing', 52000.00, '2025-01-01', NULL);

UPDATE
    projects
SET
    enddate = startdate + INTERVAL '1 YEAR'
WHERE
    enddate IS NULL;

SELECT * FROM projects;

/*
    Task 4: Insert a new employee and immediately assign them to the 'Website Redesign' project with 80 hours worked, 
    all within a single transaction. Use the RETURNING clause to retrieve the EmployeeID of the newly inserted employee.
*/
BEGIN;

WITH new_employee AS (
    INSERT INTO
        employees(firstname, lastname, department, salary, email)
    VALUES
        ('LeBron', 'James', 'IT', 65000.00, 'lebronjames@gmail.com')
    RETURNING 
        employeeid
),

project_info AS (
    SELECT 
        projectid
    FROM
        projects
    WHERE
        projectname = 'Wbsite Redesign'
    LIMIT 1
)

INSERT INTO
    employeeprojects(employeeid, projectid, hoursworked)
SELECT
    ne.employeeid,
    pi.projectid,
    80
FROM
    new_employee ne,
    project_info pi;

COMMIT;

SELECT * FROM employees;
SELECT * FROM employeeprojects;

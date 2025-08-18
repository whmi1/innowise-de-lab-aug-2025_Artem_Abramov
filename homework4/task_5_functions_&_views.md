--Task 1: Create a PostgreSQL function named CalculateAnnualBonus that takes employee_id and Salary as input and returns the calculated bonus amount (10% of Salary) for that employee. Use PL/pgSQL for the function body.
CREATE OR REPLACE FUNCTION calculate_annual_bonus(
    employeeid INTEGER,
    salary DECIMAL
)
RETURNS DECIMAL
LANGUAGE plpgsql
AS $$
DECLARE
    discounted_salary DECIMAL;
BEGIN
    IF employeeid < 0 OR salary < 0 THEN
        RETURN 0;
    ELSE
        discounted_salary := salary * 0.1;
        RETURN discounted_salary;
    END IF;
END;
$$;

--Task 2: Use this function with SELECT to see a potential bonus for each employee.
SELECT
    employeeid,
    firstname,
    lastname,
    salary,
    calculate_annual_bonus(employeeid, salary)
FROM
    employees;

--Task 3: View (View): Create a view named IT_Department_View that shows EmployeeID, FirstName, LastName, and Salary for employees in the 'IT' department only.
CREATE OR REPLACE VIEW IT_Department_View AS
SELECT
    employeeid AS Employee_ID,
    firstname AS FirstName,
    lastname AS LastName,
    salary AS Salary
FROM
    employees
WHERE
    department = 'IT';

--Task 4: Select data from IT_Department_View

SELECT * FROM IT_Department_View;



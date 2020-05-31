-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/1fASd9
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

DROP TABLE IF EXISTS "employees" CASCADE;

CREATE TABLE "employees" (
    "emp_no" Int   NOT NULL,
    "emp_title_id" varchar(30)   NOT NULL,
    "birth_date" date   NOT NULL,
    "first_name" varchar(30)   NOT NULL,
    "last_name" varchar(30)   NOT NULL,
    "sex" varchar(1)   NOT NULL,
    "hire_date" date   NOT NULL,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "emp_no"
     )
);

DROP TABLE IF EXISTS "dept_emps" CASCADE;

CREATE TABLE "dept_emps" (
    "emp_no" int   NOT NULL,
    "dept_no" varchar(10)   NOT NULL
);

DROP TABLE IF EXISTS "dept_manager" CASCADE;

CREATE TABLE "dept_manager" (
    "dept_no" varchar(30)   NOT NULL,
    "emp_no" Int   NOT NULL
);

DROP TABLE IF EXISTS "salaries" CASCADE;

CREATE TABLE "salaries" (
    "emp_no" int   NOT NULL,
    "salary" int   NOT NULL
);

DROP TABLE IF EXISTS "titles" CASCADE;

CREATE TABLE "titles" (
    "title_id" varchar(10)   NOT NULL,
    "title" varchar(20)   NOT NULL,
    CONSTRAINT "pk_titles" PRIMARY KEY (
        "title_id"
     )
);

DROP TABLE IF EXISTS "departments" CASCADE;

CREATE TABLE "departments" (
    "dept_no" varchar(10)   NOT NULL,
    "dept_name" varchar(20)   NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_no"
     )
);

ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_title_id" FOREIGN KEY("employee_title_id")
REFERENCES "titles" ("title_id");

ALTER TABLE "dept_emps" ADD CONSTRAINT "fk_dept_emps_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_emps" ADD CONSTRAINT "fk_dept_emps_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

SELECT * FROM employees;
SELECT * FROM departments;
SELECT * FROM dept_manager;
SELECT * FROM dept_emps;
SELECT * FROM salaries;
SELECT * FROM titles;

-- 1. List the following details of each employee: employee number, last name, first name, sex, and salary.

SELECT employees.emp_no, employees.first_name, employees.last_name, employees.sex, salaries.salary

FROM employees

INNER JOIN salaries ON

employees.emp_no=salaries.emp_no;

-- 2. List first name, last name, and hire date for employees who were hired in 1986.

SELECT * FROM employees;

SELECT first_name, last_name, hire_date

FROM employees

WHERE 

EXTRACT(YEAR FROM hire_date) = '1986';

-- 3. List the manager of each department with the following information: department number, department name, 
--the manager's employee number, last name, first name.

SELECT * FROM employees;
SELECT * FROM dept_manager;
SELECT * FROM departments;

SELECT d.dept_no, d.dept_name, e.emp_no, e.last_name, e.first_name

FROM dept_manager AS dm
 
INNER JOIN employees AS e

ON dm.emp_no=e.emp_no

INNER JOIN departments AS d

ON dm.dept_no = d.dept_no;



-- 4. List the department of each employee with the following information: employee number, last name, 
-- first name, and department name. 

SELECT * FROM employees;
SELECT * FROM titles;
SELECT * FROM departments;

SELECT 
e.emp_no, e.last_name, e.first_name, 
dn.dept_name

FROM
dept_emps as de

INNER JOIN  employees AS e
ON de.emp_no = e.emp_no

INNER JOIN departments AS  dn
ON de.dept_no=dn.dept_no

ORDER BY
e.last_name, e.first_name, 
dn.dept_name
;

-- 5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

SELECT * FROM employees;

SELECT first_name, last_name, sex

FROM employees

WHERE first_name = 'Hercules' and upper (last_name) like 'B%';

-- 6. List all employees in the Sales department, including their employee number, 
-- last name, first name, and department name.

SELECT 
e.emp_no, e.first_name, e.last_name,
dn.dept_name

FROM
dept_emps as de

INNER JOIN  employees AS e
ON de.emp_no = e.emp_no

INNER JOIN departments AS  dn
ON de.dept_no=dn.dept_no

WHERE dn.dept_name = 'Sales'

ORDER BY
e.emp_no, e.first_name, e.last_name,
dn.dept_name
;




-- 7. List all employees in the Sales and Development departments, including their employee number, 
-- last name, first name, and department name.


SELECT 
e.emp_no, e.first_name, e.last_name,
dn.dept_name

FROM
dept_emps as de

INNER JOIN  employees AS e
ON de.emp_no = e.emp_no

INNER JOIN departments AS  dn
ON de.dept_no=dn.dept_no

WHERE dn.dept_name = 'Sales' OR dn.dept_name = 'Development'

ORDER BY
e.emp_no, e.first_name, e.last_name,
dn.dept_name
;
--8. In descending order, list the frequency count of employee last names, 
--- i.e., how many employees share each last name.

SELECT last_name, COUNT (last_name) 

FROM employees

GROUP BY last_name

ORDER BY COUNT (last_name) DESC;



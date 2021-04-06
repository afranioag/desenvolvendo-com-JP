DECLARE 
--criando o retorno
    TYPE employee_model IS RECORD( v_hire_date OEHR_EMPLOYEES.HIRE_DATE%TYPE)
    v_employee employee_model;
BEGIN
    SELECT HIRE_DATE 
    INTO v_employee.v_hire_date
    FROM OEHR_EMPLOYEES emp
    WHERE emp.EMPLOYEE_ID = 101;

    DBMS_OUTPUT.PUT_LINE('Last_name'||' '||v_employee.v_hire_date);
END
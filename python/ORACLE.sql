DECLARE 
    v_hire_date OEHR_EMPLOYEES.HIRE_DATE%TYPE;
    v_years NUMBER;

BEGIN
    SELECT MIN(HIRE_DATE)
    INTO v_hire_date
    FROM OEHR_EMPLOYEES;

    v_years := floor(months_between(SYSDATE, v_hire_date)/12);

    IF v_years > 25 THEN
        DBMS_OUTPUT.PUT_LINE('Apto');
    ELSE
       DBMS_OUTPUT.PUT_LINE('Inapto');
    END IF; 
END



DECLARE 
    v_hire_date OEHR_EMPLOYEES.HIRE_DATE%TYPE;
    v_years NUMBER;
    v_saida VARCHAR2(6);
BEGIN
    SELECT MIN(HIRE_DATE)
    INTO v_hire_date
    FROM OEHR_EMPLOYEES;

    v_years := floor(months_between(SYSDATE, v_hire_date)/12);

    IF v_years > 25 THEN
        v_saida := 'Apto';
    ELSE
        v_saida := 'Inapto';
    END IF;

    DBMS_OUTPUT.PUT_LINE(v_saida);
END

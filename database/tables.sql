CREATE TABLE USERS_BIKE1 (
    USER_ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    FIRST_NAME VARCHAR2(50) NOT NULL,
    LAST_NAME VARCHAR2(50),
    CPF VARCHAR2(14) UNIQUE NOT NULL,
    EMAIL VARCHAR2(100) UNIQUE NOT NULL,
    PASSWORD VARCHAR2(100) NOT NULL
);

CREATE SEQUENCE USER_BIKE1_ID_SEQ START WITH 1 INCREMENT BY 1;

CREATE TABLE BIKES_CH (
    BIKE_ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    USER_ID NUMBER,
    BIKE_TYPE_ID NUMBER,
    BRAND VARCHAR2(50) NOT NULL,
    SERIAL_NUMBER VARCHAR2(50) NOT NULL,
    YEAR NUMBER NOT NULL,
    VALUE NUMBER NOT NULL,
    ADDITIONAL_MODIFICATIONS CLOB,
    FOREIGN KEY (USER_ID) REFERENCES USERS_BIKE(USER_ID),
);

CREATE SEQUENCE BIKE_ID_SEQ START WITH 1 INCREMENT BY 1;
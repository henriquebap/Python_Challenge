SELECT
    COUNT(*)
FROM
    USER_SEQUENCES
WHERE
    SEQUENCE_NAME = 'USER_BIKE5_ID_SEQ';

DROP SEQUENCE USER_BIKE5_ID_SEQ;

DECLARE
    SEQUENCE_EXISTS NUMBER;
BEGIN
    SELECT
        COUNT(*) INTO SEQUENCE_EXISTS
    FROM
        USER_SEQUENCES
    WHERE
        SEQUENCE_NAME = 'USER_BIKE5_ID_SEQ';
    IF SEQUENCE_EXISTS = 0 THEN
        EXECUTE IMMEDIATE 'CREATE SEQUENCE USER_BIKE5_ID_SEQ
            START WITH 1
            INCREMENT BY 1
            NOMAXVALUE
            NOCYCLE';
    END IF;
END;
/

CREATE TABLE "USERS_BIKE5"(
    ID NUMBER(10) DEFAULT USER_BIKE5_ID_SEQ.NEXTVAL PRIMARY KEY,
    NAME VARCHAR2(50 CHAR) NOT NULL,
    LAST_NAME VARCHAR2(50 CHAR),
    CPF CHAR(14) UNIQUE NOT NULL,
    EMAIL VARCHAR2(100 CHAR) UNIQUE NOT NULL,
    PASSWORD VARCHAR2(100 CHAR) NOT NULL
);

DESCRIBE USERS_BIKE5

DECLARE
    SEQUENCE_EXISTS NUMBER;
BEGIN
    SELECT
        COUNT(*) INTO SEQUENCE_EXISTS
    FROM
        USER_SEQUENCES
    WHERE
        SEQUENCE_NAME = 'USER_BIKE5_ID_SEQ';
    IF SEQUENCE_EXISTS = 0 THEN
        EXECUTE IMMEDIATE 'CREATE SEQUENCE USER_BIKE5_ID_SEQ
            START WITH 1
            INCREMENT BY 1
            NOMAXVALUE
            NOCYCLE';
    ELSE
        DBMS_OUTPUT.PUT_LINE('Sequence USER_BIKE5_ID_SEQ already exists.');
    END IF;
END;
/

CREATE SEQUENCE BIKE_CH3_ID_SEQ START WITH 1 INCREMENT BY 1 NOMAXVALUE NOCYCLE;

CREATE TABLE "BIKES_CH4"(
    ID NUMBER(10) DEFAULT BIKE_CH3_ID_SEQ.NEXTVAL PRIMARY KEY,
    BRAND VARCHAR2(50 CHAR) NOT NULL,
    SERIAL_NUMBER VARCHAR2(50 CHAR) NOT NULL,
    YEAR INTEGER NOT NULL,
    VALUE NUMBER(10, 2) DEFAULT 0 NOT NULL,
    ADDITIONAL_MODIFICATIONS CLOB,
    USER_ID INTEGER,
    FOREIGN KEY (USER_ID) REFERENCES "USERS_BIKE5"(ID)
);

SELECT
    COUNT(*)
FROM
    USER_SEQUENCES
WHERE
    SEQUENCE_NAME = 'IMG_PRED_ID_SEQ';

DROP SEQUENCE IMG_PRED_ID_SEQ;

DECLARE
    SEQUENCE_EXISTS NUMBER;
BEGIN
    SELECT
        COUNT(*) INTO SEQUENCE_EXISTS
    FROM
        USER_SEQUENCES
    WHERE
        SEQUENCE_NAME = 'IMG_PRED_ID_SEQ';
    IF SEQUENCE_EXISTS = 0 THEN
        EXECUTE IMMEDIATE 'CREATE SEQUENCE IMG_PRED_ID_SEQ
            START WITH 1
            INCREMENT BY 1
            NOMAXVALUE
            NOCYCLE';
    END IF;
END;
/

CREATE TABLE "IMAGE_PREDICTIONS" (
    ID NUMBER(10) DEFAULT IMG_PRED_ID_SEQ.NEXTVAL PRIMARY KEY,
    IMAGE_PATH VARCHAR2(255 CHAR),
    PREDICTION_IMAGE_PATH VARCHAR2(255 CHAR),
    PREDICTED_CLASS VARCHAR2(50 CHAR),
    CONFIDENCE NUMBER(5, 2),
    BIKE_ID INTEGER,
    FOREIGN KEY (BIKE_ID) REFERENCES "BIKES_CH4" (ID)
);
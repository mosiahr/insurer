CREATE USER POSTGRES_USER;

CREATE DATABASE POSTGRES_DB;
GRANT ALL PRIVILEGES ON DATABASE POSTGRES_DB TO POSTGRES_USER;

--CREATE DATABASE myApp_test;
--GRANT ALL PRIVILEGES ON DATABASE myApp_test TO myUser;
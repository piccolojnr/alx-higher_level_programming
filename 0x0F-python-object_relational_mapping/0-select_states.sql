-- Active: 1704681884983@@mysql-320d010-rahimdaud246-8d4e.a.aivencloud.com@21332@defaultdb
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas'), ('New York'), ('Nevada');

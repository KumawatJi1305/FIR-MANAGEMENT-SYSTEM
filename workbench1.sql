CREATE DATABASE fir_hns;

USE fir_hns;

CREATE TABLE all_firs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(255),
    complaint TEXT,
    status VARCHAR(20) DEFAULT 'Pending',
    date DATE
);

SELECT * FROM all_firs;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    address TEXT
);

ALTER TABLE all_firs
ADD user_id INT,
ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(user_id);

CREATE TABLE admin_login (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(255)
);
select * from all_firs;
select name from all_firs where status = 'pending';

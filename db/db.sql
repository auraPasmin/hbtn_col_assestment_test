CREATE DATABASE IF NOT EXISTS proyect_db;
CREATE USER IF NOT EXISTS 'proyect_user'@'localhost' IDENTIFIED BY 'proyect_user_pass@';
GRANT ALL PRIVILEGES ON proyect_db.* TO 'proyect_user'@'localhost';
GRANT SELECT ON performance_schema.* TO 'proyect_user'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE order(
order_id INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY (order_id )
);

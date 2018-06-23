create database store

USE store

create table category (
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(30) NOT NULL,
PRIMARY KEY (id)
);

create table product (
id INT NOT NULL AUTO_INCREMENT,
title VARCHAR(30) NOT NULL,
descrip VARCHAR(30) NOT NULL,
price INT NOT NULL,
img_url VARCHAR(255) NOT NULL,
category INT,
favorite VARCHAR(30),
PRIMARY KEY(id),
FOREIGN KEY (category) REFERENCES category(id)
);



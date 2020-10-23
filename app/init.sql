CREATE DATABASE cv_data;
use cv_data;

CREATE TABLE app_user (
    id INT UNIQUE PRIMARY KEY NOT NULL,
    hash VARCHAR(255) NOT NULL
);
CREATE SCHEMA cv_data;
USE cv_data;

CREATE TABLE user_table (
  user_id int UNIQUE PRIMARY KEY NOT NULL,
  user_hash varchar(255) NOT NULL
);

CREATE TABLE student_table (
  student_id int UNIQUE PRIMARY KEY NOT NULL,
  student_name varchar(128) NOT NULL,
  student_phone varchar(16) UNIQUE NOT NULL,
  student_email varchar(128) UNIQUE NOT NULL,
  student_dob date NOT NULL,
  student_branch varchar(128) NOT NULL,
  student_minor varchar(128) NOT NULL,
  student_year int NOT NULL
);

ALTER TABLE student_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);
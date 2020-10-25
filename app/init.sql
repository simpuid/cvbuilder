CREATE SCHEMA cv_data;
USE cv_data;

CREATE TABLE user_table (
  user_id int UNIQUE PRIMARY KEY NOT NULL,
  user_hash varchar(256) NOT NULL
);

CREATE TABLE student_table (
  student_id int UNIQUE PRIMARY KEY NOT NULL,
  student_name varchar(256) NOT NULL,
  student_phone int UNIQUE NOT NULL,
  student_email varchar(256) UNIQUE NOT NULL,
  student_dob date NOT NULL,
  student_branch varchar(256) NOT NULL,
  student_minor varchar(256) NOT NULL,
  student_year int NOT NULL
);

CREATE TABLE tenth_table (
  student_id int UNIQUE PRIMARY KEY NOT NULL,
  tenth_school_name varchar(256) NOT NULL ,
  tenth_cgpa float NOT NULL ,
  tenth_board varchar(256) NOT NULL ,
  tenth_year int NOT NULL
);

CREATE TABLE twelfth_table (
  student_id int UNIQUE PRIMARY KEY NOT NULL,
  twelfth_school_name varchar(256),
  twelfth_cgpa float NOT NULL,
  twelfth_board varchar(256) NOT NULL,
  twelfth_year int NOT NULL
);

CREATE TABLE skill_table (
  student_id int NOT NULL,
  skill_name varchar(255) NOT NULL,
  PRIMARY KEY (student_id, skill_name)
);

ALTER TABLE student_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE tenth_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE twelfth_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE skill_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);
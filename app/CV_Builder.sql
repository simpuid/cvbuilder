CREATE SCHEMA cv_data;
USE cv_data;

CREATE TABLE student_table (
  student_id int UNIQUE PRIMARY KEY NOT NULL,
  student_name varchar(128) NOT NULL,
  student_phone int UNIQUE NOT NULL,
  student_email varchar(128) UNIQUE NOT NULL,
  student_dob date NOT NULL,
  student_branch varchar(128) NOT NULL,
  student_minor varchar(128) NOT NULL,
  student_year int NOT NULL
);

CREATE TABLE user_table (
  user_id int UNIQUE PRIMARY KEY NOT NULL,
  user_hash varchar(255) NOT NULL
);

CREATE TABLE professor_table (
  professor_id int UNIQUE PRIMARY KEY NOT NULL,
  professor_name varchar(255) NOT NULL,
  professor_department varchar(255),
  professor_email varchar(255) UNIQUE NOT NULL,
  professor_phone varchar(255) UNIQUE NOT NULL
);

CREATE TABLE project_table (
  project_id int UNIQUE PRIMARY KEY NOT NULL,
  project_title varchar(255) NOT NULL,
  project_description varchar(255),
  project_start_date date,
  project_end_date date
);

CREATE TABLE tenth_table (
  student_id int UNIQUE PRIMARY KEY NOT NULL,
  tenth_school_name varchar(128) NOT NULL ,
  tenth_cgpa float NOT NULL ,
  tenth_board varchar(128) NOT NULL ,
  tenth_year int NOT NULL
);

CREATE TABLE twelfth_table (
  student_id int UNIQUE PRIMARY KEY NOT NULL,
  twelfth_school_name varchar(255),
  twelfth_cgpa float NOT NULL,
  twelfth_board varchar(255),
  twelfth_year int
);

CREATE TABLE reference_table (
  student_id int NOT NULL,
  professor_id int NOT NULL,
  PRIMARY KEY (student_id, professor_id)
);

CREATE TABLE project_student_relation_table (
  project_id int NOT NULL,
  student_id int NOT NULL,
  PRIMARY KEY (project_id, student_id)
);

CREATE TABLE project_professor_relation_table (
  project_id int NOT NULL,
  professor_id int NOT NULL,
  PRIMARY KEY (project_id, professor_id)
);

CREATE TABLE sgpa_table (
  student_id int NOT NULL,
  semester int NOT NULL,
  sgpa float,
  PRIMARY KEY (student_id, semester)
);

CREATE TABLE internship_table (
  student_id int NOT NULL,
  internship_start_date date NOT NULL,
  internship_end_date date NOT NULL,
  internship_organization varchar(255),
  internship_designation varchar(255),
  internship_description varchar(255),
  PRIMARY KEY (student_id, internship_start_date, internship_end_date)
);

CREATE TABLE extra_curricular_table (
  student_id int NOT NULL,
  extra_curricular_title varchar(255) NOT NULL,
  extra_curricular_start_date date NOT NULL,
  extra_curricular_end_date date NOT NULL,
  extra_curricular_description varchar(255),
  PRIMARY KEY (student_id, extra_curricular_title, extra_curricular_start_date, extra_curricular_end_date)
);

CREATE TABLE skill_table (
  student_id int NOT NULL,
  skill_name varchar(255) NOT NULL,
  PRIMARY KEY (student_id, skill_name)
);

CREATE TABLE language_table (
  student_id int NOT NULL,
  language_name varchar(255) NOT NULL,
  writing boolean,
  reading boolean,
  speaking boolean,
  PRIMARY KEY (student_id, language_name)
);

CREATE TABLE achievement_table (
  student_id int NOT NULL,
  achievement_description varchar(255) NOT NULL,
  PRIMARY KEY (student_id, achievement_description)
);

ALTER TABLE student_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE tenth_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE twelfth_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE reference_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE reference_table ADD FOREIGN KEY (professor_id) REFERENCES professor_table (professor_id);

ALTER TABLE project_student_relation_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE project_student_relation_table ADD FOREIGN KEY (project_id) REFERENCES project_table (project_id);

ALTER TABLE project_professor_relation_table ADD FOREIGN KEY (professor_id) REFERENCES professor_table (professor_id);

ALTER TABLE project_professor_relation_table ADD FOREIGN KEY (project_id) REFERENCES project_table (project_id);

ALTER TABLE sgpa_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE internship_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE extra_curricular_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE skill_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE language_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE achievement_table ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);
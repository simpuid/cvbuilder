CREATE TABLE project_table (
  project_id int UNIQUE PRIMARY KEY NOT NULL,
  project_title varchar(255) NOT NULL,
  project_description varchar(255),
  project_start_date date,
  project_end_date date
);


CREATE TABLE project_professor_relation_table (
  project_id int NOT NULL,
  professor_id int NOT NULL,
  PRIMARY KEY (project_id, professor_id)
);

ALTER TABLE project_professor_relation_table ADD FOREIGN KEY (professor_id) REFERENCES professor_table (professor_id);

ALTER TABLE project_professor_relation_table ADD FOREIGN KEY (project_id) REFERENCES project_table (project_id);

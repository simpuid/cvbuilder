CREATE SCHEMA cv_data;
USE cv_data;

CREATE TABLE `student_table` (
  `student_id` int UNIQUE PRIMARY KEY NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` varchar(255) UNIQUE NOT NULL,
  `email` varchar(255) UNIQUE NOT NULL,
  `dob` date,
  `branch` varchar(255),
  `minor` varchar(255),
  `year` int
);

CREATE TABLE `credential_table` (
  `student_id` int UNIQUE PRIMARY KEY NOT NULL,
  `hash` varchar(255) NOT NULL
);

CREATE TABLE `professor_table` (
  `professor_id` int UNIQUE PRIMARY KEY NOT NULL,
  `name` varchar(255) NOT NULL,
  `department` varchar(255),
  `email` varchar(255) UNIQUE NOT NULL,
  `phone` varchar(255) UNIQUE NOT NULL
);

CREATE TABLE `project_table` (
  `project_id` int UNIQUE PRIMARY KEY NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` varchar(255),
  `start_date` date,
  `end_date` date
);

CREATE TABLE `tenth_table` (
  `student_id` int UNIQUE PRIMARY KEY NOT NULL,
  `school_name` varchar(255),
  `cgpa` float NOT NULL,
  `board` varchar(255),
  `year` int
);

CREATE TABLE `twelfth_table` (
  `student_id` int UNIQUE PRIMARY KEY NOT NULL,
  `school_name` varchar(255),
  `cgpa` float NOT NULL,
  `board` varchar(255),
  `year` int
);

CREATE TABLE `reference_table` (
  `student_id` int NOT NULL,
  `professor_id` int NOT NULL,
  PRIMARY KEY (`student_id`, `professor_id`)
);

CREATE TABLE `project_student_relation_table` (
  `project_id` int NOT NULL,
  `student_id` int NOT NULL,
  PRIMARY KEY (`project_id`, `student_id`)
);

CREATE TABLE `project_professor_relation_table` (
  `project_id` int NOT NULL,
  `professor_id` int NOT NULL,
  PRIMARY KEY (`project_id`, `professor_id`)
);

CREATE TABLE `sgpa_table` (
  `student_id` int NOT NULL,
  `semester` int NOT NULL,
  `sgpa` float,
  PRIMARY KEY (`student_id`, `semester`)
);

CREATE TABLE `internship_table` (
  `student_id` int NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `organization` varchar(255),
  `designation` varchar(255),
  `description` varchar(255),
  PRIMARY KEY (`student_id`, `start_date`, `end_date`)
);

CREATE TABLE `extra_curricular_table` (
  `student_id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `description` varchar(255),
  PRIMARY KEY (`student_id`, `title`, `start_date`, `end_date`)
);

CREATE TABLE `skill_table` (
  `student_id` int NOT NULL,
  `skill` varchar(255) NOT NULL,
  PRIMARY KEY (`student_id`, `skill`)
);

CREATE TABLE `language_table` (
  `student_id` int NOT NULL,
  `language` varchar(255) NOT NULL,
  `writing` boolean,
  `reading` boolean,
  `speaking` boolean,
  PRIMARY KEY (`student_id`, `language`)
);

CREATE TABLE `achievement_table` (
  `student_id` int NOT NULL,
  `achievement` varchar(255) NOT NULL,
  PRIMARY KEY (`student_id`, `achievement`)
);

ALTER TABLE `student_table` ADD FOREIGN KEY (`student_id`) REFERENCES `credential_table` (`student_id`);

ALTER TABLE `tenth_table` ADD FOREIGN KEY (`student_id`) REFERENCES `credential_table` (`student_id`);

ALTER TABLE `twelfth_table` ADD FOREIGN KEY (`student_id`) REFERENCES `credential_table` (`student_id`);

ALTER TABLE `reference_table` ADD FOREIGN KEY (`student_id`) REFERENCES `credential_table` (`student_id`);

ALTER TABLE `reference_table` ADD FOREIGN KEY (`professor_id`) REFERENCES `professor_table` (`professor_id`);

ALTER TABLE `project_student_relation_table` ADD FOREIGN KEY (`student_id`) REFERENCES `credential_table` (`student_id`);

ALTER TABLE `project_student_relation_table` ADD FOREIGN KEY (`project_id`) REFERENCES `project_table` (`project_id`);

ALTER TABLE `project_professor_relation_table` ADD FOREIGN KEY (`professor_id`) REFERENCES `professor_table` (`professor_id`);

ALTER TABLE `project_professor_relation_table` ADD FOREIGN KEY (`project_id`) REFERENCES `project_table` (`project_id`);

ALTER TABLE `sgpa_table` ADD FOREIGN KEY (`student_id`) REFERENCES `credential_table` (`student_id`);

ALTER TABLE `internship_table` ADD FOREIGN KEY (`student_id`) REFERENCES `credential_table` (`student_id`);

ALTER TABLE `extra_curricular_table` ADD FOREIGN KEY (`student_id`) REFERENCES `credential_table` (`student_id`);

ALTER TABLE `skill_table` ADD FOREIGN KEY (`student_id`) REFERENCES `credential_table` (`student_id`);

ALTER TABLE `language_table` ADD FOREIGN KEY (`student_id`) REFERENCES `credential_table` (`student_id`);

ALTER TABLE `achievement_table` ADD FOREIGN KEY (`student_id`) REFERENCES `credential_table` (`student_id`);
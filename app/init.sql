CREATE SCHEMA cv_data;
USE cv_data;

CREATE TABLE user_table
(
    user_id   int UNIQUE PRIMARY KEY NOT NULL,
    user_hash varchar(256)           NOT NULL
);

CREATE TABLE student_table
(
    student_id     int UNIQUE PRIMARY KEY NOT NULL,
    student_name   varchar(256)           NOT NULL,
    student_phone  int UNIQUE             NOT NULL,
    student_email  varchar(256) UNIQUE    NOT NULL,
    student_dob    date                   NOT NULL,
    student_branch varchar(256)           NOT NULL,
    student_minor  varchar(256)           NOT NULL,
    student_year   int                    NOT NULL
);

CREATE TABLE tenth_table
(
    student_id        int UNIQUE PRIMARY KEY NOT NULL,
    tenth_school_name varchar(256)           NOT NULL,
    tenth_cgpa        float                  NOT NULL,
    tenth_board       varchar(256)           NOT NULL,
    tenth_year        int                    NOT NULL
);

CREATE TABLE twelfth_table
(
    student_id          int UNIQUE PRIMARY KEY NOT NULL,
    twelfth_school_name varchar(256)           NOT NULL,
    twelfth_cgpa        float                  NOT NULL,
    twelfth_board       varchar(256)           NOT NULL,
    twelfth_year        int                    NOT NULL
);

CREATE TABLE skill_table
(
    student_id int          NOT NULL,
    skill_name varchar(255) NOT NULL,
    PRIMARY KEY (student_id, skill_name)
);

CREATE TABLE professor_table
(
    professor_email      varchar(255) UNIQUE PRIMARY KEY NOT NULL,
    professor_name       varchar(255)                    NOT NULL,
    professor_department varchar(255),
    professor_phone      varchar(255) UNIQUE             NOT NULL
);

CREATE TABLE achievement_table
(
    student_id              int          NOT NULL,
    achievement_description varchar(512) NOT NULL,
    PRIMARY KEY (student_id, achievement_description)
);

CREATE TABLE language_table
(
    student_id    int          NOT NULL,
    language_name varchar(128) NOT NULL,
    speaking      boolean,
    reading       boolean,
    writing       boolean,
    PRIMARY KEY (student_id, language_name)
);

CREATE TABLE extra_curricular_table
(
    student_id                   int          NOT NULL,
    extra_curricular_title       varchar(128) NOT NULL,
    extra_curricular_start_date  date         NOT NULL,
    extra_curricular_end_date    date         NOT NULL,
    extra_curricular_description varchar(512),
    PRIMARY KEY (student_id, extra_curricular_title, extra_curricular_start_date, extra_curricular_end_date)
);

CREATE TABLE internship_table
(
    student_id              int          NOT NULL,
    internship_start_date   date         NOT NULL,
    internship_end_date     date         NOT NULL,
    internship_organization varchar(255) NOT NULL,
    internship_designation  varchar(255) NOT NULL,
    internship_description  varchar(512),
    PRIMARY KEY (student_id, internship_start_date, internship_end_date)
);

CREATE TABLE sgpa_table
(
    student_id    int   NOT NULL,
    sgpa_semester int   NOT NULL,
    sgpa_value    float NOT NULL,
    PRIMARY KEY (student_id, sgpa_semester)
);

CREATE TABLE reference_table
(
    student_id      int          NOT NULL,
    professor_email varchar(255) NOT NULL,
    PRIMARY KEY (student_id, professor_email)
);

ALTER TABLE student_table
    ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE tenth_table
    ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE twelfth_table
    ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE skill_table
    ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE achievement_table
    ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE language_table
    ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE extra_curricular_table
    ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE internship_table
    ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE sgpa_table
    ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE reference_table
    ADD FOREIGN KEY (student_id) REFERENCES user_table (user_id);

ALTER TABLE reference_table
    ADD FOREIGN KEY (professor_email) REFERENCES professor_table (professor_email);

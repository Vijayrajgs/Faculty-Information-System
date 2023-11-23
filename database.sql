show databases;

create database miniProject;
use miniProject;

CREATE TABLE IF NOT EXISTS `admin` (
    `admin_id` INT NOT NULL AUTO_INCREMENT,
    `adm_username` VARCHAR(30) NOT NULL,
    `adm_password` VARCHAR(30) NOT NULL,
    PRIMARY KEY(`admin_id`)
);

INSERT INTO `admin` (`adm_username`, `adm_password`) VALUES ('admin', 'admin@123');

CREATE TABLE IF NOT EXISTS `schedule` (
    `sched_id` int NOT NULL,    
    `timehr` varchar(20) DEFAULT NULL,
    `days` varchar(20) DEFAULT NULL,
    `teach_id` int DEFAULT NULL,
    `yls_id` int DEFAULT NULL,
    `schoolyear` varchar(20) DEFAULT NULL,
    `room` varchar(20) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `students` (
    `stud_id` INT NOT NULL AUTO_INCREMENT,  
    `stud_no` VARCHAR(12) DEFAULT NULL,
    `stud_fname` VARCHAR(200) DEFAULT NULL,
    `stud_mname` VARCHAR(200) DEFAULT NULL,
    `stud_lname` VARCHAR(200) DEFAULT NULL,
    `stud_gender` VARCHAR(200) DEFAULT NULL,
    `stud_age` VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (`stud_id`)
) AUTO_INCREMENT = 1;

INSERT INTO `students` (`stud_no`, `stud_fname`, `stud_mname`, `stud_lname`, `stud_gender`, `stud_age`)
VALUES
    ('080-123-456', 'Vijayraj ', NULL, 'G', 'Male', '20'),
    ('080-789-123', 'Vishal', NULL, 'S', 'Male', '21'),
    ('123-456', 'Jessica', 'L', 'Cortez', 'Female', '22');

CREATE TABLE IF NOT EXISTS `student_year_level` (
	`syl_id`  int NOT NULL,
	`stud_id` int DEFAULT NULL,
	`year_id` int DEFAULT NULL,
	`schoolyear` varchar(20) DEFAULT NULL
);

INSERT INTO `student_year_level` (`syl_id`, `stud_id`, `year_id`, `schoolyear`) VALUES
(4, 3, 5, '2021-2025'),
(5, 1, 4, '2021-2025'),
(6, 2, 4, '2020-2024');

CREATE TABLE IF NOT EXISTS `subjects` (
    `subj_id`  int NOT NULL,
    `subj_code` varchar(200) DEFAULT NULL,
    `subj_name` varchar(200) DEFAULT NULL,
    `units` varchar(12) DEFAULT NULL
);


INSERT INTO `subjects` (`subj_id`, `subj_code`, `subj_name`, `units`) VALUES
(1, 'UE21CS341A', 'Software Engineering', '4'),
(2, 'UE21CS342AA2', 'Data Analytics', '4'),
(3, 'UE21CS351A', 'Database Management System', '4'),
(4, 'UE21CS141A', 'Python for Computational Problem Solving', '5');


CREATE TABLE IF NOT EXISTS `faculties` (
	`faculty_id` int NOT NULL,
	`faculty_no` varchar(12) DEFAULT NULL,
	`faculty_fname` varchar(200) DEFAULT NULL,
	`faculty_mname` varchar(200) DEFAULT NULL,
	`faculty_lname` varchar(200) DEFAULT NULL,
	`faculty_gender` varchar(200) DEFAULT NULL,
	`faculty_degree` varchar(200) DEFAULT NULL,
    `faculty_masteral` varchar(200) DEFAULT NULL
);

INSERT INTO `faculties` (`faculty_id`, `faculty_no`, `faculty_fname`, `faculty_mname`, `faculty_lname`, `faculty_gender`, `faculty_degree`, `faculty_masteral`) VALUES
(1, '12-3213-321', 'Charu ', NULL, 'Kathuria', 'Female', 'PhD', ''),
(2, '23-3213-321', 'Mannar', NULL, "Mannan", 'Male', 'PhD', '');

CREATE TABLE IF NOT EXISTS `year_level` (
	`year_id` int NOT NULL,
	`year_level` varchar(200) DEFAULT NULL,
	`section` varchar(12) DEFAULT NULL
);

INSERT INTO `year_level` (`year_id`, `year_level`, `section`) VALUES
(4, '1st yr', 'A'),
(5, '2nd yr', 'A');

CREATE TABLE IF NOT EXISTS `year_level_subject` (
	`yls_id` int NOT NULL,
	`year_id` int DEFAULT NULL,
	`subj_id` int DEFAULT NULL
);

INSERT INTO `year_level_subject` (`yls_id`, `year_id`, `subj_id`) VALUES
(10, 4, 1),
(11, 4, 2),
(12, 4, 3);

ALTER TABLE `schedule` ADD PRIMARY KEY (`sched_id`), ADD KEY `teach_id` (`teach_id`), ADD KEY `yls_id` (`yls_id`);

ALTER TABLE `student_year_level` ADD PRIMARY KEY (`syl_id`), ADD KEY `stud_id` (`stud_id`,`year_id`), ADD KEY `year_id` (`year_id`);

ALTER TABLE `subjects` ADD PRIMARY KEY (`subj_id`);

ALTER TABLE `faculties` ADD PRIMARY KEY (`faculty_id`);

ALTER TABLE `year_level` ADD PRIMARY KEY (`year_id`);

ALTER TABLE `year_level_subject` ADD PRIMARY KEY (`yls_id`), ADD KEY `year_id` (`year_id`,`subj_id`), ADD KEY `subj_id` (`subj_id`);

ALTER TABLE `schedule`
ADD CONSTRAINT `schedule_ibfk_1` FOREIGN KEY (`teach_id`) REFERENCES `faculties` (`faculty_id`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD CONSTRAINT `schedule_ibfk_2` FOREIGN KEY (`yls_id`) REFERENCES `year_level_subject` (`yls_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `student_year_level`
ADD CONSTRAINT `student_year_level_ibfk_1` FOREIGN KEY (`stud_id`) REFERENCES `students` (`stud_id`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD CONSTRAINT `student_year_level_ibfk_2` FOREIGN KEY (`year_id`) REFERENCES `year_level` (`year_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `year_level_subject`
ADD CONSTRAINT `year_level_subject_ibfk_1` FOREIGN KEY (`subj_id`) REFERENCES `subjects` (`subj_id`) ON DELETE CASCADE ON UPDATE CASCADE,
ADD CONSTRAINT `year_level_subject_ibfk_2` FOREIGN KEY (`year_id`) REFERENCES `year_level` (`year_id`) ON DELETE CASCADE ON UPDATE CASCADE;

show tables;

DESC admin;
SELECT * FROM admin;

DESC schedule;

DESC student_year_level;
SELECT * FROM student_year_level;

DESC students;
SELECT * FROM students;

DESC subjects;
SELECT * FROM subjects;

DESC faculties;
SELECT * FROM faculties;

DESC year_level;
SELECT * FROM year_level;

DESC  year_level_subject;
SELECT * FROM year_level_subject;

use miniProject;


select * from schedule;
desc schedule;

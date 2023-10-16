show databases;

CREATE TABLE IF NOT EXISTS `admin` (
    `admin_id` INT NOT NULL AUTO_INCREMENT,
    `adm_username` VARCHAR(30) NOT NULL,
    `adm_password` VARCHAR(30) NOT NULL,
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
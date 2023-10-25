-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    Student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_student VARCHAR(120) UNIQUE NOT NULL,
    code_group VARCHAR(5), --NOT NULL
    address_s VARCHAR(150),
    email VARCHAR(120),
    n_tel VARCHAR(20)
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    name_teacher VARCHAR(120) NOT NULL,
    address_t VARCHAR(150),
    email VARCHAR(120),
    n_tel VARCHAR(20)

);


-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    code_group VARCHAR(5) UNIQUE NOT NULL,
    name_group VARCHAR(120) NOT NULL

);



-- Table: disciplines
DROP TABLE IF EXISTS disciplines;
CREATE TABLE disciplines (
    discip INTEGER UNIQUE NOT NULL,
    teacher INTEGER ,
    name_discipline VARCHAR(120) NOT NULL

);

-- Table: ritings
DROP TABLE IF EXISTS ritings;
CREATE TABLE ritings (
    stud_id INTEGER NOT NULL,
    discip INTEGER,
    riting INTEGER,
    teacher INTEGER,
    date_r VARCHAR(10) NOT NULL,
    FOREIGN KEY (stud_id) REFERENCES students (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);
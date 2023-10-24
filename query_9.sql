SELECT d.name_discipline
FROM students s
JOIN ritings r ON s.student_id = r.stud_id
JOIN disciplines d ON r.discip = d.discip
WHERE s.name_student = 'Венедикт Ярош';
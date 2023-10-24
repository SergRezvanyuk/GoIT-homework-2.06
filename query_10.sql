SELECT d.name_discipline
FROM students s
JOIN ritings r ON s.student_id = r.stud_id
JOIN disciplines d ON r.discip = d.discip
JOIN teachers t ON d.teacher = t.teacher_id
WHERE s.name_student = 'Федір Яремко' AND t.name_teacher = 'Демид Негода';
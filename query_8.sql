SELECT t.name_teacher, AVG(r.riting) AS avg_riting
FROM teachers t
JOIN disciplines d ON t.teacher_id = r.teacher
JOIN ritings r ON d.discip = r.discip
GROUP BY t.name_teacher;
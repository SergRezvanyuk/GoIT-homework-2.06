SELECT s.name_student, AVG(r.riting) AS avg_riting
FROM students s
JOIN ritings r ON s.student_id = r.stud_id
GROUP BY s.name_student
ORDER BY avg_riting DESC
LIMIT 5;
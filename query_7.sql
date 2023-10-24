SELECT s.name_student, r.riting
FROM students s
JOIN groups g ON s.code_group = g.code_group
JOIN ritings r ON s.student_id = r.stud_id
JOIN disciplines d ON r.discip = d.discip
WHERE g.name_group = 'Маркетинг' AND d.name_discipline = 'Математичний аналіз';
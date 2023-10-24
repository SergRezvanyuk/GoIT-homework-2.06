SELECT s.name_student
FROM students s
JOIN groups g ON s.code_group = g.code_group
WHERE g.name_group = 'Менеджмент';
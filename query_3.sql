SELECT g.name_group, AVG(r.riting) AS avg_riting
FROM groups g
JOIN students s ON g.code_group = s.code_group
JOIN ritings r ON s.student_id = r.stud_id
JOIN disciplines d ON r.discip = d.discip
WHERE d.name_discipline = 'Інформаційний маркетинг та менеджмент'
GROUP BY g.name_group;
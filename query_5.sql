SELECT d.name_discipline
FROM disciplines d
JOIN teachers t ON d.teacher = t.teacher_id
WHERE t.name_teacher = 'Демид Негода';
-- Write a script that lists all records of a table.

-- using the SELECT, FROM, WHERE, ORDER BY keyword.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

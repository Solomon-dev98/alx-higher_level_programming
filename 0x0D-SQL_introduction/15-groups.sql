 -- A script that lists the number of records with the same score.

 -- using SELECT,FROM, GROUP BY and ORDER BY with DESC.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

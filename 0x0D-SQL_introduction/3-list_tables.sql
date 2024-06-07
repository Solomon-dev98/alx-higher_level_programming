-- a script that lists all the tables of a database.

-- SELECT TABLE NAME
SELECT TABLE_NAME

-- use the specified database;
FROM information_schema.TABLES

-- The condition to match the specified database
WHERE TABLE_SCHEMA = DATABASE();

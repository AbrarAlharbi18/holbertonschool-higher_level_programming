-- creates a table and inserts rows of data into it
-- creates a table
CREATE TABLE IF NOT EXISTS second_table (
	id INT, name VARCHAR(256), score INT
	);
-- inserts a row of data into the newly created table
INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10);
-- inserts another row of data
INSERT INTO second_table (id, name, score)
VALUES (2, 'Alex', 3);
-- inserts another row of data
INSERT INTO second_table (id, name, score)
VALUES (3, 'Bob', 14);
-- inserts another row of data
INSERT INTO second_table (id, name, score)
VALUES (4, 'George', 8);

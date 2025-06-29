-- mysql script that creates a table with a unique column
-- Create command is used to create the table and UNIQUE constrain is enforced
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);

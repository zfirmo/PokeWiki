CREATE TABLE IF NOT EXISTS pokemon(
	pokemon_id SERIAL PRIMARY KEY,
	pokemon_num INT,
	name VARCHAR(50) NOT NULL,
	generation_id INT,
	height DECIMAL(5,2),
	weight DECIMAL(6,2),
	
	CONSTRAINT fk_generation_id 
		FOREIGN KEY (generation_id) 
		REFERENCES generation(generation_id)
)

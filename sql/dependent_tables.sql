CREATE TABLE base_stats(
	pokemon_id INT PRIMARY KEY,
	hp INT NOT NULL,
	attack INT NOT NULL,
	defense INT NOT NULL, 
	sp_attack INT NOT NULL,
	sp_defense INT NOT NULL,
	speed INT NOT NULL,

	CONSTRAINT fk_pokemon_id FOREIGN KEY (pokemon_id) 
	REFERENCES pokemon(pokemon_id)
	ON DELETE CASCADE

)

CREATE TABLE evolution(
	from_pokemon_id INT,
	to_pokemon_id INT,
	evolution_type VARCHAR(50),
	evolution_value VARCHAR(50),

	PRIMARY KEY (from_pokemon_id,to_pokemon_id),

	CONSTRAINT fk_from_pokemon FOREIGN KEY (from_pokemon_id)
	REFERENCES pokemon(pokemon_id),
	CONSTRAINT fk_to_pokemon FOREIGN KEY (to_pokemon_id)
	REFERENCES pokemon(pokemon_id)
	
)
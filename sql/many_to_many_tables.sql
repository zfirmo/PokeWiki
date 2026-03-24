CREATE TABLE pokemon_type(
	pokemon_id INT,
	type_id INT,
	PRIMARY KEY (pokemon_id,type_id)

	CONSTRAINT fk_pokemon_id FOREIGN KEY (pokemon_id) 
	REFERENCES pokemon(pokemon_id)
	ON DELETE CASCADE,
	
	CONSTRAINT fk_type_id FOREIGN KEY (type_id) 
	REFERENCES type(type_id)
	ON DELETE CASCADE
)

CREATE TABLE pokemon_ability(
	pokemon_id INT,
	ability_id INT,
	is_hidden BOOL,
	PRIMARY KEY (pokemon_id,ability_id),

	CONSTRAINT fk_pokemon_id FOREIGN KEY (pokemon_id) 
	REFERENCES pokemon(pokemon_id)
	ON DELETE CASCADE,
	
	CONSTRAINT fk_ability_id FOREIGN KEY (ability_id) 
	REFERENCES ability(ability_id)
	ON DELETE CASCADE
)

CREATE TABLE pokemon_egg_group(
	pokemon_id INT,
	egg_group_id INT,
	PRIMARY KEY (pokemon_id,egg_group_id),

	CONSTRAINT fk_pokemon_id FOREIGN KEY (pokemon_id) 
	REFERENCES pokemon(pokemon_id)
	ON DELETE CASCADE,
	
	CONSTRAINT fk_egg_group_id FOREIGN KEY (egg_group_id) 
	REFERENCES egg_group(egg_group_id)
	ON DELETE CASCADE
)
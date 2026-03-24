CREATE TABLE IF NOT EXISTS type(
	type_id SERIAL PRIMARY KEY,
	name VARCHAR(20)
)
-- @block 

CREATE TABLE IF NOT EXISTS ability(
	ability_id SERIAL PRIMARY KEY,
	name VARCHAR(50)
)

-- @block

CREATE TABLE IF NOT EXISTS egg_group(
	egg_group_id SERIAL PRIMARY KEY,
	name VARCHAR(25)
)

-- @block

CREATE TABLE IF NOT EXISTS generation(
	generation_id SERIAL PRIMARY KEY,
	name VARCHAR(25)
)
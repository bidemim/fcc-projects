CREATE DATABASE universe;
\c universe
CREATE TABLE IF NOT EXISTS

galaxy(
  galaxy_id SERIAL PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  diameter_in_light_years INT,
  star_count_in_million INT NOT NULL,
  shape VARCHAR(20),
  galaxy_type TEXT,
  is_active BOOLEAN,
  description TEXT, 
  has_active_galactic_nucleus BOOLEAN
  );


CREATE TABLE star(
  star_id SERIAL PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  constellation TEXT,

  age_in_millions_of_years NUMERIC,
  distance_from_earth
  star_description TEXT,
  star_types
  is_spherical BOOLEAN,
  galaxy_id FOREIGN KEY
);

CREATE TABLE moon(
  moon_id SERIAL PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  moon_description TEXT,
  has_life BOOLEAN,
  is_spherical BOOLEAN,
  moon_types
  distance_from_planet
  parent_planet 
);

CREATE TABLE planet(
  planet_id SERIAL PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  planet_types 
  has_life BOOLEAN,
  age_in_millions_of_years,
  distance_from_earth
);

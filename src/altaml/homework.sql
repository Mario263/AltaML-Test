CREATE TABLE pets(
    id INT PRIMARY KEY, 
    pet_type VARCHAR(20) NOT NULL,
    curr_name VARCHAR(20) NULL,
    age INT NOT NULL,
    favorite_food VARCHAR(20) NULL,
    speech_count INT NOT NULL
);

CREATE TABLE pet_name_hist(
    id INT PRIMARY KEY,
    pet_id INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    name_pos INT NOT NULL,
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);

INSERT INTO pets (
    id, 
    pet_type, 
    curr_name, 
    age, 
    favorite_food, 
    speech_count)
    VALUES (
        1, 
        'Cat', 
        'Katherine', 
        5, 
        'Fish',
        4
        );

INSERT INTO pets (
    id, 
    pet_type, 
    curr_name, 
    age, 
    favorite_food, 
    speech_count
    ) VALUES (
        2, 
        'Dog', 
        'Snoopy', 
        6, 
        'Kennel Max',
        4
        );

-- ## History        

INSERT INTO pet_name_hist(
    id, 
    pet_id,
    name,
    name_pos
) VALUES (
    1,
    1,
    'Katherine',
    1

);

INSERT INTO pet_name_hist(
    id, 
    pet_id,
    name,
    name_pos
) VALUES (
    2,
    2,
    'Snoopy',
    1
);
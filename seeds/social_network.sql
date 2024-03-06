
-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them 
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email_address VARCHAR(255),
    username VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, email_address) VALUES ('Dipa', 'rite2dipa@yahoo.com');
INSERT INTO users (username, email_address) VALUES ('Dalloway', 'dalloway@gmail.com');


DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them 
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    contents VARCHAR(255),
    no_of_views INTEGER,
    user_id INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, contents, no_of_views, user_id) VALUES ('Dipas todays post', 'Its snowing', 5, 1);
INSERT INTO posts (title, contents, no_of_views, user_id) VALUES ('Dalloway post', 'I am having a coffee', 1, 2);

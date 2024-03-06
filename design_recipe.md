Two Tables Design Recipe Template



1. Extract nouns from the user stories or specification

# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.


Nouns:

user_accounts, email_address, username, 

posts, user_account,title, contents,views


2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

|----------------------------------------------------------|
|Record        | 	            Properties                 |
|user   	   |    id,email_address, username             |
|posts         |   id, title, contents,views               |
|----------------------------------------------------------|

# Name of the first table (always plural): users

Column names: email_address, username

# Name of the second table (always plural): posts

Column names: title, contents,views


3. Decide the column types
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

Table: users
id: SERIAL
email_address : text
username : text


Table: posts
id: SERIAL
title : text
content : text
no_of_views : int

4. Decide on The Tables Relationship
Most of the time, you'll be using a one-to-many relationship, and will need a foreign key on one of the two tables.

To decide on which one, answer these two questions:

Can one user have many posts? (YES)
Can one post have many user? (NO)

You'll then be able to say that:

users has many posts
And on the other side, [B] belongs to [A]
In that case, the foreign key is in the table posts

Replace the relevant bits in this example with your own:

# EXAMPLE

5. Write the SQL

-- file: social_network.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username text,
  email_address text
);

-- Then the table with the foreign key second.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  no_of_views int

-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_post foreign key(user_id) references 
  users(id)
);

6. Create the tables
psql -h 127.0.0.1 social_network < social_network.sql








# python-learning

Some really random and un-organized Python scripts used to get familiar with the language a little bit.

Assumes a local MySQL database, here are the relevant statements to get it setup:

create a new empty database called "python_learning"
    
    CREATE DATABASE pythen_learning;

create a user named "learner" with a password of "python"
    
    CREATE USER 'learner'@'localhost' IDENTIFIED BY 'python';

give read/write privileges to our "learner" user on anything in our "python_learning" database
    
    GRANT ALL PRIVILEGES ON python_learning.* TO learner@localhost WITH GRANT OPTION;

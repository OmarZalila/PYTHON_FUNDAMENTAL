SELECT * FROM mydb.users;

INSERT INTO users (first_name , last_name , email)
VALUES('omar','zalila','omar@gmail.com'),('mouheb','benmansoura','mouheb@gmail.com'),('nader','khammassi','nader@gmail.com');

select * From mydb.users
WHERE email  LIKE "o%";

select * from mydb.users
ORDER BY id DESC
LIMIT 1;

UPDATE mydb.users 
SET last_name = "is pancake"
where id = 3 ;

DELETE FROM mydb.users WHERE id=2;

SELECT first_name FROM mydb.users;

SELECT first_name From mydb.users
ORDER BY first_name DESC;

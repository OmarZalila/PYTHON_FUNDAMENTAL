SELECT * FROM dojos;
INSERT INTO dojos(name)
VALUES ('omar'),('mouheb'),('nader');

DELETE FROM dojos WHERE id < 4;

INSERT INTO ninjas(name)
VALUES ('omar'),('mouheb'),('nader');

SELECT * FROM ninjas;

SELECT * From ninjas 
LIMIT 3;

SELECT * FROM ninjas
ORDER BY dojo_id DESC
LIMIT 3;

SELECT * FROM ninjas
ORDER BY dojo_id DESC
LIMIT 1;

INSERT INTO ninjas(first_name , last_name , age , dojo_id)
VALUES ('hamza','bedoui',25,4),('houssem','hedhli',26,4),('adam','laarif',28,4);

INSERT INTO ninjas(first_name , last_name , age , dojo_id)
VALUES ('joe','doe',18,5),('jane','smith',19,5),('steven','boe',25,5);

INSERT INTO ninjas(first_name , last_name , age , dojo_id)
VALUES ('jessika','bernard',20,6),('keven','bryne',30,6),('roben','diaz',35,6);

SELECT * FROM dojos
JOIN ninjas ON dojos.id=ninjas.dojo_id
WHERE ninjas.id=21;

SELECT * FROM dojos
JOIN ninjas ON dojos.id=ninjas.dojo_id;





SELECT name FROM category;
SELECT name as genero FROM category;
SELECT COUNT(*) as número_filas FROM actor;

SELECT
title as titulo,
rental_duration as duracion_alquiler,
rental_rate as precio_alquiler
FROM film WHERE film_id = 5;

SELECT * FROM film ORDER BY length ASC;

SELECT * FROM film 
WHERE length < 50 and rental_rate = 4.99;

SELECT * FROM payment
WHERE payment_date BETWEEN '2007-04-10' AND '2007-04-18' ORDER BY amount DESC;

SELECT * FROM payment
WHERE payment_date BETWEEN  '2007-04-10' AND '2007-04-18'
AND staff_id = 2 AND amount > 7.00;

SELECT count(*) FROM payment
WHERE payment_date BETWEEN  '2007-04-10' AND '2007-04-18'
AND staff_id = 2 AND amount > 7.00;
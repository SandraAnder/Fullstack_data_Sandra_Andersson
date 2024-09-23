SELECT * FROM chess;

SELECT DISTINCT(winner) FROM chess;

SELECT DISTINCT(victory_status) FROM chess;


SELECT DISTINCT(opening_eco) FROM chess;

SELECT COUNT(*) FROM chess;

SELECT
	winner,
	COUNT(winner) AS winner_count
FROM
	chess
GROUP BY
	winner
ORDER BY
	winner_count;


SELECT
	opening_name,
	COUNT(opening_name) AS name
FROM
	chess
GROUP BY
	opening_name
ORDER BY name DESC
LIMIT 10;


SELECT
	white_id AS name_w,
	MAX(white_rating) AS rating_w,
FROM
	chess
GROUP BY name_w
ORDER BY rating_w DESC
LIMIT 5;



SELECT
	black_id AS name_b,
	MAX(black_rating) AS rating_b,
FROM
	chess
GROUP BY name_b
ORDER BY rating_b DESC
LIMIT 5;
	


desc;
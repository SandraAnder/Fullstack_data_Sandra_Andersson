desc;

SELECT
	*
FROM
	information_schema.schemata;

CREATE SCHEMA IF NOT EXISTS marts;

CREATE TABLE IF NOT EXISTS marts.content_view_time AS 
(
SELECT
	Videotitel,
	"Publiceringstid för video" AS Publiceringstid,
	Visningar,
	"Visningstid (timmar)" AS Visningstid_timmar,
	Exponeringar,
	Prenumeranter,
	"Klickfrekvens för exponeringar (%)" AS "Klickfrekvens_exponering_%"
FROM
	innehall.tabelldata
ORDER BY
	"Visningstid (timmar)" DESC OFFSET 1);

CREATE TABLE IF NOT EXISTS marts.views_per_date AS (
SELECT
	STRFTIME('%Y-%m-%d',
	Datum) AS Datum,
	Visningar
FROM
	innehall.totalt);


CREATE TABLE IF NOT EXISTS marts.content_gender_viewers AS (
SELECT 
    "Tittarnas ålder" AS "Kön",
    "Visningar (%)" AS "Visningar_%",
    "Genomsnittlig visningslängd",
    "Genomsnittlig procent som har visats (%)" AS "Genomsnittlig_%_visat",
    "Visningstid (timmar) (%)" AS "Visningstid_timmar_%"
FROM 
    tittare.tabelldata_kon
ORDER BY
    "Kön");


CREATE TABLE IF NOT EXISTS marts.content_age_viewers AS (
SELECT 
    "Tittarnas kön" AS "Ålder",
    "Visningar (%)" AS "Visningar_%",
    "Genomsnittlig visningslängd",
    "Genomsnittlig procent som har visats (%)" AS "Genomsnittlig_%_visat",
    "Visningstid (timmar) (%)" AS "Visningstid_timmar_%"
FROM 
    tittare.tabelldata_alder);


CREATE TABLE IF NOT EXISTS marts.content_top_15_viewed AS (
SELECT
	 "Videotitel" AS Titel,
	 "Visningar" AS Antal_visningar
FROM
	innehall.tabelldata);



SELECT
	*
FROM
	information_schema.tables
WHERE
	table_schema = 'marts';


SELECT
	*
FROM
	marts.content_view_time;


SELECT
	*
FROM
	marts.views_per_date;

SELECT
	*
FROM
	marts.content_gender_viewers;

SELECT
	*
FROM
	marts.content_age_viewers;


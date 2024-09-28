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



CREATE TABLE IF NOT EXISTS marts.content_viewer_geografy AS (
SELECT 
	Geografi, 
	Visningar,
	"Genomsnittlig visningslängd"
FROM 
	geografi.tabelldata
ORDER BY 
	"Visningar" DESC);

CREATE TABLE IF NOT EXISTS marts.op_system_views AS (
SELECT 
    Operativsystem,
    SUM(Visningar) AS Totala_visningar
FROM 
    operativsystem.diagramdata
GROUP BY 
    Operativsystem
ORDER BY 
    Totala_visningar DESC);


CREATE TABLE IF NOT EXISTS marts.subscribers AS (
SELECT 
        "Prenumerationskälla",
        SUM(Prenumeranter) AS Totala_prenumeranter,
        SUM("Nya prenumeranter") AS Totala_nya_prenumeranter,
        SUM("Förlorade prenumeranter") AS Totala_förlorade_prenumeranter
    FROM 
        prenumerationskalla.tabelldata
    GROUP BY 
        "Prenumerationskälla");


CREATE TABLE IF NOT EXISTS marts.subs_source AS (
SELECT 
	"Prenumerationskälla", 
	SUM(Prenumeranter) AS Totala_prenum 
FROM 
	prenumerationskalla.diagramdata
GROUP BY "Prenumerationskälla");


CREATE TABLE IF NOT EXISTS marts.content_10_latest_vid AS (
WITH video_table AS (SELECT * FROM innehall.tabelldata),
     video_diagram AS (SELECT * FROM innehall.diagramdata)
SELECT 
    DISTINCT(vtab."Videotitel"),
    vtab."Publiceringstid för video",
    vtab.visningar AS totala_visningar,
    vtab."Visningstid (timmar)",
    vtab.Prenumeranter,
FROM
    video_table AS vtab
LEFT JOIN video_diagram AS vdia
ON vtab."Publiceringstid för video" = vdia."Publiceringstid för video"
WHERE 
    STRPTIME(vtab."Publiceringstid för video", '%b %d, %Y') >= STRPTIME('2024-01-01', '%Y-%m-%d') -- här omvandlas det till en datumsträng för att kunna sortera på år och ta bort de äldre videorna
ORDER BY (STRPTIME(vtab."Publiceringstid för video", '%b %d, %Y'), totala_visningar) DESC LIMIT 10);




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

SELECT
	*
FROM
	marts.content_top_15_viewed;

SELECT
	*
FROM
	marts.content_viewer_geografy;

SELECT
	*
FROM
	marts.op_system_views;

SELECT
	*
FROM
	marts.subscribers;

SELECT
	*
FROM
	marts.subs_source;

SELECT
	*
FROM
	marts.content_10_latest_vid;
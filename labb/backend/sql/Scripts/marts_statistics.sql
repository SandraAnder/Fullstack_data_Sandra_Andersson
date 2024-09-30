
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



SELECT
	*
FROM
	information_schema.tables
WHERE
	table_schema = 'marts';

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
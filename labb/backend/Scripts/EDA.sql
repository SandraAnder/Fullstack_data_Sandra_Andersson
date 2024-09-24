desc;


WITH date_table AS (SELECT * FROM datum.tabelldata OFFSET 1),
	 date_total AS (SELECT * FROM datum.totalt)
SELECT
	STRFTIME('%Y-%m-%d', tot.datum),
	tot.visningar,
	tab.visningar,
	tab."visningstid (timmar)"
FROM
	date_total as tot
LEFT JOIN date_table as tab
ON tot.datum = tab.datum;


SELECT
	Enhetstyp,
	COUNT(*) AS total_rows,
	SUM(Visningar) AS total_visningar
FROM
	enhetstyp.diagramdata
GROUP BY
	Enhetstyp;


SELECT
	* EXCLUDE (Innehåll)
FROM
	innehall.tabelldata
ORDER BY
	"visningstid (timmar)" DESC;


SELECT * FROM innehall.tabelldata;






desc;

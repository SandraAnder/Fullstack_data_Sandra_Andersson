desc;


WITH date_table AS (SELECT * FROM datum.tabelldata OFFSET 1),
	 date_total AS (SELECT * FROM datum.totalt)
SELECT
	STRFTIME('%Y-%m-%d', tot.datum),
	tot.visningar,
	tab.visningar,
	tab."visningstid (timmar)",
	tab."Genomsnittlig visningslängd"
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

-- Tittar på kön och hur dessa tittar på innehållet
SELECT 
    "Tittarnas ålder",
    "Visningar (%)",
    "Genomsnittlig visningslängd",
    "Genomsnittlig procent som har visats (%)",
    "Visningstid (timmar) (%)"
FROM 
    tittare.tabelldata_kon;

   -- Tittar på åldersgrupper och hur dessa tittar på innehållet
   SELECT 
    "Tittarnas kön",
    "Visningar (%)",
    "Genomsnittlig visningslängd",
    "Genomsnittlig procent som har visats (%)",
    "Visningstid (timmar) (%)"
FROM 
    tittare.tabelldata_alder;



-- Vilka är de mest populära/mest sedda videorna top 15
SELECT * FROM innehall.tabelldata;

SELECT 
	Videotitel,
	Visningar
FROM innehall.tabelldata
ORDER BY Visningar DESC LIMIT 15;
   
   


desc;


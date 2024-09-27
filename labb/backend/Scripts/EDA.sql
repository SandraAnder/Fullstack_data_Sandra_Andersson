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
-- ovan är Kokchuns exempel



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
   
  
-- Var finns tittarna
SELECT
	Geografi,
	COUNT(Geografi)
FROM
	geografi.diagramdata
GROUP BY Geografi;


-- Vilka operativsyststem och visningar
SELECT 
	DISTINCT(Operativsystem),
	Visningar
FROM 
	operativsystem.diagramdata;


-- Prenumeranter 
SELECT 
	DISTINCT(*)
FROM 
	prenumerationskalla.tabelldata;

-- Prenumerationskälla
SELECT 
	DISTINCT(Prenumerationskälla), 
	Prenumeranter 
FROM 
	prenumerationskalla.diagramdata;


-- De tio senaste videorna
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
ORDER BY (STRPTIME(vtab."Publiceringstid för video", '%b %d, %Y'), totala_visningar) DESC LIMIT 10; --Konverterar till ännu en datumsträng för att kunna sortera ordentligt på månad och på så sätt få fram de senaste videorna



desc;


# Lab overview - the data driven youtuber

I denna labben skapas en dashboard för att undersöka och reda i en youtube-sidas statistik och trafik.
Koden är uppdelad i olika filer för att hålla koden så ren och enkel att förstå som möjligt.

Först rensas och ordnas csv filer med information som sedan utgör en databas. 
Där görs en EDA för att undersöka datan och sedan plockas intressant information ut genom sql-queries.
Några exempel på sådan som gjorts i denna labben är:

### EDA.sql
- Vad är skillnaden mellan män och kvinnor i tittarstatistik
- Vilka åldersgrupper engageras i materialet och hur stor är genomsnittstiden de tittar
- Vilka är de 15 mest sedda videorna
- Vilka operativsystem är vanligast
- Vart finns tittarna geografiskt
- Prenumeranter och källa

### marts_content.sql
Här görs vår koppling mellan databasen och dashboard. Vi skapar nya tabeller (om de inte redan finns) i marts som vi sedan kan koppla ihop med våra KPI:er/grafer

### graphs.py
Alla grafer finns här enkelt att anropa

### kpi.py
Jag skapar klasser och funktioner som jag kan stoppa in mina kpi:er i för att enkellt anropa de via min dashboard.py

### style.css
Här skapas utseendet på min dashboard, färger, typsnitt, design, flervalsboxar osv fixas här

### dashboard.py
Mina KPI:er, grafer, färger anropas och sätts ihop till en snygg och förståelig dashboard



## :eyeglasses:


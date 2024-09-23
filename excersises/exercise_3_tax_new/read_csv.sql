CREATE TABLE tax07 AS
SELECT *
FROM read_csv_auto('../../data/Leverantorsfaktura202407.csv', types={'Organisationsnummer': 'VARCHAR'});

CREATE TABLE tax08 AS
SELECT *
FROM read_csv_auto('../../data/Leverantorsfaktura202408.csv', types={'Organisationsnummer': 'VARCHAR'});
ALTER PROCEDURE [dbo].[SuddivisioneTutti] @scelta int, @prov1 float, @prov2 float, @prov3 float
AS
IF @scelta = 1
	BEGIN
		-- Totale Ordini
		SELECT FORMAT(SUM(SubTotal), 'c') AS [Totale Ordini]
			FROM Sales.SalesOrderHeader
	END

IF @scelta = 2
-- Totale Ordini suddivisi tra Venditori ed Online
	BEGIN
		DECLARE @online float, @offline float
		SET @online = 0		--init
		SET @offline = 0

		SELECT @online = SUM(SubTotal)
		FROM Sales.SalesOrderHeader
		WHERE SalesPersonID IS NULL

		SELECT @offline = SUM(SubTotal)
		FROM Sales.SalesOrderHeader
		WHERE SalesPersonID IS NOT NULL

		PRINT 'Fatturato vendite online: ' + FORMAT(@online, 'c')
		PRINT 'Fatturato vendite in persona: ' + FORMAT(@offline, 'c')
	END

IF @scelta = 3
	BEGIN
		-- Totale Ordini suddivisi per singolo venditore
		SELECT Person.LastName [Venditore],
				SUM(SalesOrderHeader.SubTotal) AS [Totale Ordini]
			FROM Sales.SalesOrderHeader
			INNER JOIN Person.Person
				ON SalesOrderHeader.SalesPersonID = Person.BusinessEntityID
			GROUP BY  Person.LastName 
			ORDER BY [Totale Ordini] DESC
	END

IF @scelta = 4
	BEGIN
		-- Totale Ordini suddivisi per singolo venditore con %
		SELECT Person.LastName [Venditore],
				FORMAT(SUM(SalesOrderHeader.SubTotal), 'c') AS [Totale Ordini],
				100 * SUM(SalesOrderHeader.SubTotal) / (
						SELECT SUM(SalesOrderHeader.SubTotal)
						FROM Sales.SalesOrderHeader
						WHERE OnlineOrderFlag = 0
				) AS [Totale Ordini Percentuale]
			FROM Sales.SalesOrderHeader
			INNER JOIN Person.Person
				ON SalesOrderHeader.SalesPersonID = Person.BusinessEntityID
			GROUP BY  Person.LastName 
			ORDER BY [Totale Ordini Percentuale] DESC
	END

IF @scelta = 5
	-- Totale Ordini suddivisi per singolo venditore con provv.
	BEGIN
		SELECT Person.LastName [Venditore],
			FORMAT(SUM(SalesOrderHeader.SubTotal), 'c') AS [Totale Ordini],
			(100 * SUM(SalesOrderHeader.SubTotal) / (
					SELECT SUM(SalesOrderHeader.SubTotal)
					FROM Sales.SalesOrderHeader
					WHERE OnlineOrderFlag = 0
			)) AS [Totale Ordini Percentuale],

			FORMAT(
				CASE
					WHEN SUM([SalesOrderHeader].SubTotal) < 5000000
						THEN SUM(SalesOrderHeader.SubTotal) * @prov1
					WHEN SUM(SalesOrderHeader.SubTotal) BETWEEN 5000000 AND 10000000
						THEN SUM(SalesOrderHeader.SubTotal) * @prov2
					ELSE SUM(SalesOrderHeader.SubTotal) * @prov3
				END
			, 'c') AS [Provvigione]
			
		FROM Sales.SalesOrderHeader
		INNER JOIN Person.Person
			ON SalesOrderHeader.SalesPersonID = Person.BusinessEntityID
		GROUP BY  Person.LastName
		ORDER BY [Totale Ordini Percentuale] DESC
	END




-- Totale Ordini suddivisi per singolo venditore con provv. Parametrica





IF @scelta = 6
	BEGIN
		-- Salvataggio in tabella


		INSERT INTO [dbo].[Provvigioni] (
						cognome,
						totale_vendite,
						percentuale_vendite,
						provvigione
						)

			SELECT Person.LastName AS [Venditore],
				SUM(SalesOrderHeader.SubTotal) AS [Totale Ordini],
				(100 * SUM(SalesOrderHeader.SubTotal) / (
						SELECT SUM(SalesOrderHeader.SubTotal)
						FROM Sales.SalesOrderHeader
						WHERE OnlineOrderFlag = 0
				)) AS [Totale Ordini Percentuale],

				CASE
					WHEN SUM([SalesOrderHeader].SubTotal) < 5000000
						THEN SUM(SalesOrderHeader.SubTotal) * @prov1
					WHEN SUM(SalesOrderHeader.SubTotal) BETWEEN 5000000 AND 10000000
						THEN SUM(SalesOrderHeader.SubTotal) * @prov2
					ELSE SUM(SalesOrderHeader.SubTotal) * @prov3
				END
				AS [Provvigione]

			FROM Sales.SalesOrderHeader
			INNER JOIN Person.Person ON SalesOrderHeader.SalesPersonID = Person.BusinessEntityID
			GROUP BY  Person.LastName
	END



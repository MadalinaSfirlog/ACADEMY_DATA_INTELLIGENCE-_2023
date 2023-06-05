SELECT *
FROM [Purchasing].[PurchaseOrderDetail]


SELECT *
FROM [Production].[Product]


-- 1. Numeri totale lucchetti ordinati
SELECT sum(Purchasing.PurchaseOrderDetail.OrderQty) as Totale_Lucchetti
    FROM [Production].[Product] 
     INNER JOIN [Purchasing].[PurchaseOrderDetail] on [Production].[Product].ProductID = [Purchasing].[PurchaseOrderDetail].ProductID
       WHERE [Production].[Product].Name LIKE'%Lock%'


-- 2. Il volume d'affari per categoria di prodotto
SELECT sum(LineTotal) as Totale_Ricavi, left([Production].[Product].ProductNumber,2) AS Nominativi
   FROM [Purchasing].[PurchaseOrderDetail]
    INNER JOIN [Production].[Product] on [Production].[Product].ProductID = [Purchasing].[PurchaseOrderDetail].ProductID
       GROUP BY left([Production].[Product].ProductNumber,2)
	      ORDER BY Nominativi ASC

-- 3. Idenfiticare quanto è stata la massima vendita 
WITH cte_query
AS
(SELECT sum(LineTotal) as Totale_Ricavi, left([Production].[Product].ProductNumber,2) AS Nominativi
   FROM [Purchasing].[PurchaseOrderDetail]
    INNER JOIN [Production].[Product] on [Production].[Product].ProductID = [Purchasing].[PurchaseOrderDetail].ProductID
       GROUP BY left([Production].[Product].ProductNumber,2))

SELECT MAX(Totale_Ricavi) as Max_Vendita
FROM cte_query




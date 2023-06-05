-- if / else in T-SQL
DECLARE @scelta int;
SET @scelta = 1;

IF @scelta = 1
BEGIN
    
    DECLARE @Total_Customers int;
    SET @Total_Customers = 0;

    SELECT @Total_Customers = COUNT(CustomerID)
    FROM Sales.SalesOrderHeader;

    PRINT 'Numero totale di clienti: ' + CAST(@Total_Customers AS varchar(10));
END
ELSE
BEGIN
    PRINT 'La scelta non corrisponde';
END

IF @scelta = 2
BEGIN
    
    DECLARE @Total_Revenue int;
    SET @Total_Revenue = 0;

    SELECT @Total_Revenue = SUM(SubTotal)
    FROM Sales.SalesOrderHeader;

    PRINT 'Il fatturato totale è: ' + CAST(@Total_Revenue AS varchar(10));
END
ELSE
BEGIN
    PRINT 'La scelta non corrisponde';
END




--Create a stored Procedure for Total Customers 
CREATE PROCEDURE TotalCustomers
AS
DECLARE @scelta int;
SET @scelta = 1;

IF @scelta = 1
BEGIN

    DECLARE @Total_Customers int;
    SET @Total_Customers = 0;

    SELECT @Total_Customers = COUNT(CustomerID)
    FROM Sales.SalesOrderHeader;

    PRINT 'Numero totale di clienti: ' + CAST(@Total_Customers AS varchar(10));
END
ELSE
BEGIN
    PRINT 'La scelta non corrisponde';
END


EXEC TotalCustomers


-- Create a stored procedure for Total Revenue 
CREATE PROCEDURE TotalRevenue
AS
DECLARE @scelta int;
SET @scelta = 2;

IF @scelta = 2
BEGIN
    
    DECLARE @Total_Revenue int;
    SET @Total_Revenue = 0;

    SELECT @Total_Revenue = SUM(SubTotal)
    FROM Sales.SalesOrderHeader;

    PRINT 'Il fatturato totale è: ' + CAST(@Total_Revenue AS varchar(10));
END
ELSE
BEGIN
    PRINT 'La scelta non corrisponde';
END

EXEC TotalRevenue











-- create two variables which contains integer numbers
DECLARE  @num1 int; 
DECLARE @num2 int; 
SET @num1 = 10;
SET @num2 = 20; 

SELECT @num1 + @num2 as Total_Nums
SELECT @num2 - @num1 as Total_Nums



-- another example 
-- nchar = dati a stringa fissa ( da 1 a 4000)
-- nvarchar = dati a stringa variabile ( da 1 a 4000)
DECLARE  @first_Name nvarchar (100);  
DECLARE @last_Name nvarchar (100); 
DECLARE @fullName as nvarchar (200)
SET @first_Name = 'Jhon'; 
SET @last_Name = 'Smith'; 
SET @fullName = CONCAT(@first_Name, ' ' , @last_Name)



-- use variables in SELECT 
SELECT @first_Name as FirstName, @last_Name as LastName, @fullName as FullName;  


-- variables with case_when 
DECLARE  @first_variable int; 
DECLARE @second_variable int; 
SET @first_variable = 10;
SET @second_variable = 20; 

SELECT @first_variable + @second_variable as Total_Variables,
       Case 
	      When @first_variable > @second_variable Then 'the result is not corect' 
	      Else 'the result is corect' 
	   End As Final_Description; 


-- declare two variables and pass in the firstname and lastname of the top 1 customer
SELECT TOP 1 FirstName, LastName 
FROM [Person].[Person]

DECLARE  @first_Name nvarchar (100);
DECLARE @last_Name nvarchar (100); 

SELECT TOP 1 @first_Name = FirstName, @last_Name = LastName 
FROM [Person].[Person]

SELECT @first_Name as First_Name, @last_Name as Last_Name
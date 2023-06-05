                                           -- SQL PROGRAM ACADEMY

-- how to change email 
UPDATE [Person].[EmailAddress]
   SET [EmailAddress] = 'roberto0@europa.com'
   WHERE [EmailAddressID] = 3

SELECT EmailAddress
FROM [Person].[EmailAddress]
WHERE [EmailAddressID] = 3

-- how to change all dates 
UPDATE [Person].[EmailAddress]
SET [ModifiedDate] = '19/04/2023'

-- change a part of an email
UPDATE [Person].[EmailAddress]
SET [EmailAddress] = REPLACE(EmailAddress, 'adventure-works', 'europa')

-- check how many emails are there in the table [Person].[EmailAddress]
SELECT count (EmailAddress) AS EMAIL
FROM [Person].[EmailAddress]

-- delete a row
 DELETE FROM [Person].[EmailAddress]
 WHERE [BusinessEntityID] = 9

 -- concatenate FirstName and LastName from the table [Person].[Person] in a new column 
 SELECT FirstName, LastName, FirstName + ' ' + LastName as Concatenate_Name
 FROM [Person].[Person]

--return back just the 3 letters of the LastName in table [Person].[Person]
SELECT SUBSTRING (LastName, 1, 3) as Three_First_Letters
FROM [Person].[Person]

-- using left 
SELECT LEFT(LastName, 3) as Three_First_Letters
FROM [Person].[Person]

-- delete one of the tables from the db 
DROP TABLE [Sales].[PersonCreditCard]

-- add a new column 
ALTER TABLE dbo.Clienti ADD telefono varchar(15)

-- delete a column 
ALTER TABLE dbo.Clienti DROP COLUMN telefono

-- Create a new table Authors 
CREATE TABLE musica.dbo.Authors(
    [id] int primary key,
	[Nome] varchar(50), 
	[Cognome] varchar(50)
)

-- Create a new table Brani in relation with table Authors in the same db Musica 
CREATE TABLE musica.dbo.Brani(
    [id_brano] int primary key identity(10,10),
	[Titolo] varchar(50), 
	[id_autore] int, 
	[durata in secondi] int default 240, 
	foreign key ([id_autore]) references Musica.dbo.Authors(id)
	on delete set null 
	on update cascade
)

INSERT INTO musica.dbo.Authors 
VALUES 
(01, 'Gianna', 'Nannini'),
(02, 'Marco', 'Mengoni'),
(03, 'Tiziano', 'Ferro');


INSERT INTO musica.dbo.Brani
VALUES 
('Sole', 01, 250),
('Farfalla', 02, 260),
('Mare', 03, 290);

select * 
from musica.dbo.Authors

select * 
from musica.dbo.Brani


-- select data in common
SELECT [dbo].[Authors].[Nome] AS 'Nome_Artista',
       [dbo].[Authors].[Cognome] AS 'Cognome_Artista',
       [dbo].[Brani].[Titolo] AS 'Nome_Brano' 
      
    FROM  dbo.Brani
	  INNER JOIN dbo.Authors   
		  ON [dbo].[Brani].[id_autore] = [dbo].[Authors]. [id]



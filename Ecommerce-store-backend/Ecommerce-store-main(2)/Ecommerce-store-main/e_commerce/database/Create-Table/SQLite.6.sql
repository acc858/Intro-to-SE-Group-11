 CREATE TABLE "Users" (
  "First_Name" TEXT NOT NULL,
  "Last_Name" TEXT NOT NULL,
  "Username" TEXT NOT NULL,
  "Password" TEXT NOT NULL,
  "User_ID" INTEGER NOT NULL,
  PRIMARY KEY("USER_ID")
  );
  
  CREATE TABLE "Payment_Info" (
  "Payment_ID" INTEGER NOT NULL,
  "User_ID" INTEGER NOT NULL,
  "Payment_Type" TEXT NOT NULL,
  "Card_Number" INTEGER NOT NULL,
  "CVV" INTEGER NOT NULL,
  "Address_Line_1" TEXT NOT NULL,
  "Address_Line_2" TEXT NOT NULL,
  "City" TEXT NOT NULL,
  "State" TEXT NOT NULL,
  "Zip_Code" INTEGER NOT NULL,
  "Phone_Number" INTEGER NOT NULL,
  PRIMARY KEY("Payment_ID")
  );
  
  CREATE TABLE "Shipping_Info" (
  "Shipping_ID" INTEGER NOT NULL,
  "User_ID" INTEGER NOT NULL,
  "Address_Line_1" TEXT NOT NULL,
  "Address_Line_2" TEXT NOT NULL,
  "City" TEXT NOT NULL,
  "State" TEXT NOT NULL,
  "Zip_Code" INTEGER NOT NULL,
  "Phone_Number" INTEGER NOT NULL,
  PRIMARY KEY("Shipping_ID")
  );
   
 
 CREATE TABLE User_History (
  ISBN INTEGER NOT NULL,
  Title varchar(50),
  Author varchar(50),
  Year int(4),
  Genre varchar(50),
  User_ID INTEGER NOT NULL,
  Quantity INTEGER NOT NULL,
  Price INTEGER NOT NULL
  );

CREATE TABLE Cart (
  ISBN INTEGER NOT NULL,
  Title varchar(50),
  Author varchar(50),
  Year int(4),
  Genre varchar(50),
  User_ID INTEGER NOT NULL,
  Quantity INTEGER NOT NULL,
  Price INTEGER NOT NULL
  );
 
 CREATE TABLE Inventory (
  ISBN INTEGER NOT NULL,
  Title varchar(50),
  Author varchar(50),
  Year int(4),
  Genre varchar(50),
  Quantity INT,
  Price INT,
  PRIMARY KEY(ISBN)
  );

INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
(101, 'First Book', 'George Orwell', '1949', 'Dystopian', 100, 15);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
(102, 'Mockingbird', 'Harper Lee', '1960', 'Southern Gothic', 100, 25);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
(103, 'The Color Purple', 'Alice Walker', '1982', 'Epistolary', 100, 20);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
(104, 'Beloved', 'Toni Morrison', '1987', 'American Literature', 100, 15);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
(105, 'Misery', 'Stephen King', '1987', 'Psychological Horror', 100, 30);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
(106, 'Gilead', 'Marilynne Robinson', '2004', 'Novel', 100, 20);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
(107, 'The Road', 'Cormac McCarthy', '2006', 'Post apocalyptic fiction', 100, 25);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
(108, 'Build', 'Lois McCarthy', '2008', 'Sci-fi', 100, 20);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
(109, '8-bit Zeta', 'Devin Neal', '2016', 'Legend', 100, 50);
INSERT INTO Inventory (ISBN, Title, Author, Year, Genre, Quantity, Price) VALUES
(110, 'Life Jacket', 'Devin Neal', '2020', 'Comic', 3, 20);
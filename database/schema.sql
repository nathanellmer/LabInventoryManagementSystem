-- schema to define the database tables

-- Users table
CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserName TEXT NOT NULL UNIQUE,
    UserEmail TEXT NOT NULL UNIQUE,
    UserOffice TEXT NOT NULL
);

-- Suppliers table
CREATE TABLE Suppliers (
    SupplierID INTEGER PRIMARY KEY AUTOINCREMENT,
    SupplierName TEXT NOT NULL UNIQUE,
    SupplierWebsite TEXT NOT NULL,
    SupplierAddressL1 TEXT NOT NULL,
    SupplierAddressL2 TEXT NOT NULL,
    SupplierPostcode TEXT NOT NULL,
    SupplierPhone TEXT NOT NULL,
    SupplierEmail TEXT NOT NULL
);

-- Grant codes table
CREATE TABLE GrantCodes (
    GrantCodeID INTEGER PRIMARY KEY AUTOINCREMENT,
    GrantCodeName TEXT NOT NULL,
    GrantCodeOwner TEXT NOT NULL
);

-- Locations table
CREATE TABLE StorageLocations (
    LocationID INTEGER PRIMARY KEY AUTOINCREMENT,
    LocationName TEXT NOT NULL UNIQUE
);

-- Items table
CREATE TABLE Items (
    ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    ItemName TEXT NOT NULL,
    ItemSupplier INTEGER NOT NULL,
    ItemRef TEXT NOT NULL UNIQUE,
    ItemDescription TEXT NOT NULL,
    ItemSize TEXT NOT NULL,
    ItemQuantity INTEGER NOT NULL,
    ItemStorageLocation INTEGER NOT NULL,
    ItemUnitCost DECIMAL(15, 2) DEFAULT 0.00,
    ItemWebsite TEXT NOT NULL,
    ItemReorderFlag BOOLEAN NOT NULL DEFAULT FALSE,
    ItemOriginator INTEGER NOT NULL,
    ItemCategory TEXT NOT NULL,
    ItemNotes TEXT,
    ItemQuartzyRef TEXT DEFAULT NULL,
    ItemGHS1 BOOLEAN NOT NULL DEFAULT FALSE,
    ItemGHS2 BOOLEAN NOT NULL DEFAULT FALSE,
    ItemGHS3 BOOLEAN NOT NULL DEFAULT FALSE,
    ItemGHS4 BOOLEAN NOT NULL DEFAULT FALSE,
    ItemGHS5 BOOLEAN NOT NULL DEFAULT FALSE,
    ItemGHS6 BOOLEAN NOT NULL DEFAULT FALSE,
    ItemGHS7 BOOLEAN NOT NULL DEFAULT FALSE,
    ItemGHS8 BOOLEAN NOT NULL DEFAULT FALSE,
    ItemGHS9 BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (ItemSupplier) REFERENCES Suppliers(SupplierID),
    FOREIGN KEY (ItemStorageLocation) REFERENCES StorageLocations(LocationID),
    FOREIGN KEY (ItemOriginator) REFERENCES Users(UserID)
);

-- -- Institutions table
-- CREATE TABLE Institutions (
--     InstitutionID INTEGER PRIMARY KEY AUTOINCREMENT,
--     InstitutionName TEXT NOT NULL,
--     AssocCategoryID INTEGER NOT NULL,
--     FOREIGN KEY (AssocCategoryID) REFERENCES Categories(CategoryID)
-- );

-- -- Banks table
-- CREATE TABLE Banks (
--     BankID INTEGER PRIMARY KEY AUTOINCREMENT,
--     BankName TEXT NOT NULL
-- );

-- -- Accounts table
-- CREATE TABLE Accounts (
--     AccountID INTEGER PRIMARY KEY AUTOINCREMENT,
--     AccountName TEXT NOT NULL,
--     AssocBankID INTEGER NOT NULL,
--     AccountStartDate DATE NOT NULL,
--     AccountEndDate DATE NOT NULL,
--     AccountType TEXT NOT NULL,
--     AccountBalance DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
--     FOREIGN KEY (AssocBankID) REFERENCES Banks(BankID)
-- );

-- -- Transactions table
-- CREATE TABLE Transactions (
--     TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
--     TransactionAccountID INTEGER NOT NULL,
--     TransactionDate DATE NOT NULL,
--     TransactionOutInstitutionID INTEGER,
--     TransactionOutAccountID INTEGER,
--     TransactionAmountDebit DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
--     TransactionAmountCredit DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
--     FOREIGN KEY (TransactionAccountID) REFERENCES Banks(BankID),
--     FOREIGN KEY (TransactionOutInstitutionID) REFERENCES Institutions(InstitutionID),
--     FOREIGN KEY (TransactionOutAccountID) REFERENCES Banks(BankID)
-- );


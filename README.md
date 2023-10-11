# InventoryManagementSystem
## Python Assignment for APU
### Yap Zhu Sheng TP073670
### Ho Yan Xun TP073669

Sure! Here's a documentation for the provided code:

# PPE Inventory Management System Documentation

## Introduction

The PPE (Personal Protective Equipment) Inventory Management System is a Python-based program designed to manage the inventory of PPE items, suppliers, hospitals, and user accounts. It allows users to perform various tasks such as adding, deleting, searching, and modifying user accounts, managing suppliers and hospitals, and tracking PPE inventory transactions.

## Table of Contents

1. [Initialization](#initialization)
   - [initCheck](#initcheck)
   - [initialization](#initialization)
   - [supplierInitialize](#supplierinitialize)
   - [hospitalInitialize](#hospitalinitialize)

2. [File Operations](#file-operations)
   - [readFile](#readfile)
   - [writeToFile](#writetofile)

3. [User Management](#user-management)
   - [manageUsers](#manageusers)
   - [addUser](#adduser)
   - [delUser](#deluser)
   - [searchUser](#searchuser)
   - [modifyUser](#modifyuser)
   - [listUsers](#listusers)

4. [Main Menu](#main-menu)
   - [mainMenu](#mainmenu)
   - [loginMenu](#loginmenu)

5. [Inventory Management](#inventory-management)
   - [inventoryInit](#inventoryinit)
   - [inventory](#inventory)
   - [lessThan25](#lessthan25)
   - [receiveItems](#receiveitems)
   - [doesItemExists](#doesitemexists)
   - [distributeItems](#distributeitems)
   - [search](#search)
   - [history](#history)
   - [transactionBetweenTimePeriod](#transactionbetweentimeperiod)
   - [convStrToDT](#convstrtodt)
   - [addTransaction](#addtransaction)

6. [Supplier Management](#supplier-management)
   - [supplier](#supplier)
   - [addDistribution](#adddistribution)
   - [listStock](#liststock)
   - [listHospitals](#listhospitals)
   - [listSuppliers](#listsuppliers)

7. [Main Functionality](#main-functionality)
   - [main](#main)

## Initialization

### initCheck

The `initCheck` function checks if the program is running for the first time by detecting the existence of specific files (`users.txt`, `suppliers.txt`, and `hospitals.txt`). If these files do not exist, the program proceeds with the initialization process.

### initialization

The `initialization` function creates the `users.txt` file, prompting the user to create an admin account and enter supplier and hospital details.

### supplierInitialize

The `supplierInitialize` function initializes the `suppliers.txt` file, allowing the user to enter supplier codes, names, and contact numbers.

### hospitalInitialize

The `hospitalInitialize` function initializes the `hospitals.txt` file, allowing the user to enter hospital codes and names.

## File Operations

### readFile

The `readFile` function reads the content of a specified file and returns it as a list.

### writeToFile

The `writeToFile` function writes data to a specified file.

## User Management

### manageUsers

The `manageUsers` function provides an admin panel for user management, allowing operations such as adding, deleting, searching, modifying users, and listing all users.

### addUser

The `addUser` function adds a new user with a specified user type (Admin or Staff).

### delUser

The `delUser` function deletes a user, excluding the admin performing the operation.

### searchUser

The `searchUser` function searches for a user based on their userID.

### modifyUser

The `modifyUser` function allows the modification of user details such as user type and password.

### listUsers

The `listUsers` function lists all users with their details.

## Main Menu

### mainMenu

The `mainMenu` function presents the main menu options for the PPE Inventory Management System, including inventory, suppliers, hospitals, user management, and logging out.

### loginMenu

The `loginMenu` function handles user login, checking the validity of user credentials.

## Inventory Management

### inventoryInit

The `inventoryInit` function initializes the `ppe.txt` file, allowing the user to enter PPE item codes, names, and supplier codes.

### inventory

The `inventory` function provides options for checking stock, receiving items, distributing items, viewing transaction history, searching transaction details, and quitting.

### lessThan25

The `lessThan25` function provides a reminder for items with a quantity less than 25 boxes.

### receiveItems

The `receiveItems` function handles the process of receiving items into the inventory.

### doesItemExists

The `doesItemExists` function checks whether a specified item exists in the inventory.

### distributeItems

The `distributeItems` function handles the process of distributing items to hospitals.

### search

The `search` function allows the user to search for transaction details of a specific item.

### history

The `history` function provides options to view transaction history, distribution history, and transactions within a specified time period.

### transactionBetweenTimePeriod

The `transactionBetweenTimePeriod` function filters transactions based on a specified time period.

### convStrToDT

The `convStrToDT` function converts a string date to a datetime object.

### addTransaction

The `addTransaction` function adds a transaction record to the `transaction.txt` file.

## Supplier Management

### supplier

The `supplier` function provides options for listing supplier details, changing supplier names, changing supplier contact numbers, and quitting.

### addDistribution

The `addDistribution` function adds a distribution record to the `distribution.txt` file.

### listStock

The `listStock` function lists PPE items along with their codes and quantities.

### listHospitals

The `listHospitals` function lists hospitals along with their codes and names.

### listSuppliers

The `listSuppliers` function lists suppliers along with their codes, names, and contact numbers.

## Main Functionality

### main

The `main` function serves as the entry point to the program, initiating the check for program initialization and presenting the user with login and main menu options.

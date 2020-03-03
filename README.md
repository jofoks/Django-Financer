# Django Personal Financer

### ABOUT:  
This is a website based personal financial tool. It is built on a website firstly to build some experience buidling websites and secondly for some of its features. This website will give an oversight over the personal finance essentials to get a good grasp on your current finacial situation.

### FEATURES:   
* Web based UI
* Python 3
* ING CSV file reader/parser
* SQLiteDB and tools
* Charts and Graphs/ visualisations
* Highlight section about the certain transactions
* Outstanding debt/ auto tithe and gift tracker
* Reoccuring transaction payment tracker
* Optional auto payment reminders
* Envelope system and tracker
* Manual entries
* Some verification tracking
* Save a list of contacts with their Account information
* Tax calculator

### USES:   
* Store financial transactions
* Sort them by personalized filters
* Oversee outstanding payments
* General oversight of your financials
* Recognzing patterns in spending and income
* Tithe/ gift/ recursive payment tracking
* Month's transactions oversight

### PURPOSE:    
    To get a firm understanding on your financial situation, to recognize spending patterns and to be timely and integrous about debts.

### MODULES:

## DOCUMENTATION
***

### VENV Modules: {bin, inlude, lib}    
* Django
* Django pylint
* Python3

### APPS:   
* Transactions  **::TESTED::**
* Categories    **::TESTED::**
* Envelopes     **::TESTED::**
    * income allocations
    * fixed charges
    * (fixed income?)
* Debt          **::TESTED::**
* Address       **::TESTED::**
* BankAcount    **::TESTED::**
* Contacts      **::TESTED::**
    * General
    * Address
    * Bank Account
* TAX?

### APPS:   
#### TRANSACTION:
* Date	
* Name	
* Account	            # User's bank account
* Counterparty	        # Optional. Integrated Contacts Menu
* Amount	
* type	
* Description

#### CONTACT:                
**General:**                    
* First Name                
* Last Name                 
* Email           
* Bank Account          

#### BANK ACCOUNT:
**Subclasses:**
* NL Account
    * Name
    * IBAN
* US Account
    * Address (APP)
    * Routing Number
    * Account Number
    * Choice (Checking/Savings)

**main:**
* bankAccount
    Choose from account types
    Prompt that model
    return that model to account

#### DEBT:
* Name
* Description
* Amount
* Creditor (Contact)
* Due Date 'Balkable'
* Start Date (current time default)

#### ENVELOPE:
* Name
* Description
* Income Fraction (%)



### URLS/ PAGES:

|    URL                             | Name                  | Description                                               |
| ------------------------------------|:----------------------:|------------------------------------------------------------:|
|    #website.com/                    | Reel                   | Future Feature: a representative page on what this website |has to offer
|    website.com/login                | Login                  | Initial prompted page to authorize access to all urls stated |below
|    website.com/home                 | overview               | Oversight page over highlight information about all |catagories

|    website.com/view/visuals         | Graphs                 | Displaying a number of interactive graphs|
|    website.com/view/transactions    | Totals                 | An overview of the complete database of transactions|
|    website.com/view/envelopes       | Distributions          | A hub viewing the preset distribution of the monthly cashflow|
|    website.com/view/debts           | Debts                  | Displaying outstanding debts and payments? of the debts |
            

### TODOS:  
#### GENERAL:    
* create user home interface
* create widgets
* csv uploader

#### BY PAGES:   
**LOGIN:**  
* prompt this page if user is not logged in on any url
* create an admin url that routs you to the home page (or the requested page)

#### HOME:   
* Sketch the layout
* preset the areas information will come
* build a base template for the overlay on every page
* Create pulldown menu's and top options in base:
    * Views
    * Settings
    * Logout -> login
    * Home

(for now)
        



                                            


# Django Personal Financer

### New Look!
Check out this video!

<a href="http://www.youtube.com/watch?feature=player_embedded&v=FXEApZXXkAI
" target="_blank"><img src="http://img.youtube.com/vi/FXEApZXXkAI/0.jpg" 
alt="Youtube GUI video" width="240" height="180" border="10" /></a>

Design by Studio Festein

Backend, CSS, HTML, JS by Joram Millenaar

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
* django-address      0.2.1  
* django-crispy-forms 1.8.1  

## DOCUMENTATION
skip this if you're not me, this is just for my own sanity
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
* Create a form? and/or view
* Create website home post template (alternating right and left)
* add an Update and Detail view/url for all the apps
* Do some style synergizing

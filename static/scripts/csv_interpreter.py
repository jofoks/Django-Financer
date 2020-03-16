import pandas as pds
import json
from transaction.models import Transaction
from DJ_Financer.settings import BASE_DIR
import os
import datetime
  
def catch_errors(func):
    def func_wrapper(*args, **kwargs):
        try:
           return func(*args, **kwargs)
        except Exception as e:
            return e
    return func_wrapper

@catch_errors
def handle_file(user, csv):
  ''' Question: 
        - When are there too many functions?
        - Do I put these functions inside function?
        - Do I pass arguments in inner functions?
        - Do I chain these functions or call them sequencially
        - Assert or if statements?'''
  def get_DataFrame():
    try: return pds.read_csv(csv)
    except:raise TypeError('Could not read CSV file')

  def get_header_map(DF):
    '''find headers and if all required headers are present:
        return a dictionary of the header and its name'''
    def solve_headers():
      dct_gen = ((key, values) for key, values in header_keys.items())
      try: header = next(headers)
      except StopIteration:
        if checklist_verified():
          return checklist
      if not header_in_json(header, dct_gen):
          print(f'Skippedd header: {header}')
      return solve_headers()
      
    def header_in_json(header, dct_gen):
      try: key, keywords = next(dct_gen)
      except StopIteration:
        return False
      if is_in_list(header, keywords):
        header_string = " ".join(header)
        checklist[key] = header_string
        return True
      return header_in_json(header, dct_gen)

    def is_in_list(header, keywords):
      for keyword in keywords:
        for word in header:
          if word in keyword:
            return True
      return False

    def checklist_verified():
      missing_items = [key for key, value in checklist.items() if not value]
      if missing_items:
        raise ValueError(f"Invalid CSV File")
      return True

    checklist = {
      "types": False,
      "amount": False,
      "date": False,
      "name": False,
      "description": False,
      "counterparty": False,
      "account": False,
    }

    headers = list(DF)
    assert len(headers) < 16, 'Too many columns'
    headers = (i.lower().split(' ') for i in headers)
    return solve_headers()

  def format_amount(row):
    amount = row[header_map["amount"]]
    us_amount = float(amount.replace(',','.')) ### debit? and detect , or .
    if credit_debit_keyword:
      debit_credit = row[credit_debit_keyword].lower()
      if debit_credit in header_keys['identifier']['debit']:
        us_amount = -us_amount
      elif debit_credit in header_keys['identifier']['credit']:
        us_amount = us_amount
      else:
        raise ValueError(f"Unknown debit/credit value: '{debit_credit}'")
    return us_amount

  def format_date(raw):
    s = str(raw)
    date = datetime.date(year=int(s[0:4]), month=int(s[4:6]), day=int(s[6:8])) 
    return date

  def get_debitCredit():
      identifiers = header_keys['identifier']['amount']
      keyword = [kw for kw in identifiers if kw in csv_DF.columns]
      if len(keyword) == 0:
        return None
      return keyword[0]
        
  def populate_transactions():
    for index, row in csv_DF.iterrows():
      us_amount = format_amount(row=row)
      date = format_date(row[header_map["date"]])
      Transaction.objects.create(
        kind= row[header_map["types"]],
        amount= us_amount,
        date= date,
        name= row[header_map["name"]],
        description= row[header_map["description"]],
        counterparty= row[header_map["counterparty"]],
        account= row[header_map["account"]],
        owner= user
      )

  assert csv.content_type in ('text/csv', 'text/tsv'), 'Not a csv or tsv file'
  assert csv.size < 10*10**7, 'File is too big'
  with open(os.path.join(BASE_DIR, 'static/scripts/csv_identifiers.json'), 'r') as js:
    header_keys = json.load(js)
  csv_DF = get_DataFrame()
  header_map = get_header_map(csv_DF)
  csv_DF.columns = [i.lower() for i in csv_DF.columns]
  credit_debit_keyword = get_debitCredit()
  populate_transactions()

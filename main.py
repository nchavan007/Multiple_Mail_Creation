#!/usr/bin/python3.6

import json
from mail import sendmail
from openpyxl import load_workbook

with open("Mail_Config", "r") as file:
  MailDetails = json.load(file)
DetailsXl = MailDetails["Path_XL"]
subject =  MailDetails["DefaultSubject"]
message = ""

main_workbook = load_workbook(filename=DetailsXl)
main_sheet = main_workbook.active
for row in main_sheet.iter_rows(min_row=2, values_only=True):
  message = f"""

  test message for application {row[0]}
  
  """
  
  sendmail(Title=subject, receiver_email=row[1], msg=message)

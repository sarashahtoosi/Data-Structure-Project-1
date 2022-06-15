import os
import csv
from datetime import datetime
from datetime import date
from bidi.algorithm import get_display
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np

my_file = open("result.txt", "w")

# -------------- FAZE 1 -------------- #
§
# 3

list_file_names = ['people', 'accounts', 'calls', 'cars',
                   'ownerships', 'phones', 'transactions', 'relationships', 'homes']

# 4 convert csv files to excel

if not os.path.isdir('excel'):
    os.mkdir('excel')

for row in list_file_names:

    # Reading the csv file
    df_new = pd.read_csv(row + '.csv')

    # saving xlsx file
    GFG = pd.ExcelWriter(r'excel/' + row + '.xlsx')  # pylint: disable=abstract-class-instantiated

    df_new.to_excel(GFG, index=False)

    GFG.save()

# 5 convert excel files to html

if not os.path.isdir('html'):
    os.mkdir('html')

for row in list_file_names:

    df = pd.read_excel(r'excel/'+ row +'.xlsx')

    df.to_html(r'html/' + row + '.html')

# -------------- FAZE 2 -------------- #

WORK_SEARCH = get_display("بندر")
WORK_SEARCH2 = get_display("گمرک")

my_file.write("start faze 2 - " + datetime.now().strftime('%H:%M:%S') + "\n")

# 8

peoplecsv = csv.DictReader(open('people.csv', encoding='utf-8'))

list_A = []

for row in peoplecsv:

    if get_display(row['work']).__contains__(WORK_SEARCH) or get_display(row['work']).__contains__(WORK_SEARCH2):

        list_A.append(row['ssn'])

# 9

list_B = []

ownershipscsv = csv.DictReader(open('ownerships.csv', encoding='utf-8'))

DATE_NOW = datetime.now().date()

for row in ownershipscsv:
    if list_A.__contains__(row['from']):

        table_row_date = row['date']  # 2020-02-02

        row_date = date(int(table_row_date[:4]), int(
            table_row_date[5:7]), int(table_row_date[8:10]))

        dates_difference = relativedelta(DATE_NOW, row_date).years

        if dates_difference < 3:

            if not list_B.__contains__(row['from']):
                list_B.append(row['from'])

# 10

list_C = []

relationshipscsv = csv.DictReader(
    open('relationships.csv', encoding='utf-8'))

for row in relationshipscsv:
    if list_A.__contains__(row['from']):

        if row['relation'] == 'PARENT' or row['relation'] == 'OFFSPRING' or row['relation'] == 'SILIBING' or row['relation'] == 'SPOUSE':

            if not list_C.__contains__(row['to']):
                list_C.append(row['to'])

# 11

list_D = []

ownershipscsv = csv.DictReader(open('ownerships.csv', encoding='utf-8'))

for row in ownershipscsv:
    if list_C.__contains__(row['from']):

        table_row_date = row['date']

        row_date = date(int(table_row_date[:4]), int(
            table_row_date[5:7]), int(table_row_date[8:10]))
        dates_difference = relativedelta(DATE_NOW, row_date).years

        if dates_difference < 3:

            if not list_D.__contains__(row['from']):
                list_D.append(row['from'])

# 12

list_E = []

relationshipscsv = csv.DictReader(
    open('relationships.csv', encoding='utf-8'))

for row in relationshipscsv:
    if list_D.__contains__(row['to']):

        if not list_E.__contains__(row['from']):
            list_E.append(row['from'])


# 13

for row in list_E:
    if not list_B.__contains__(row):
        list_B.append(row)

# 14

Faze2_ssn = list_B

peoplecsv = csv.DictReader(open('people.csv', encoding='utf-8'))

my_file.write("نام" + " | " + "نام خانوادگی" + " | " + 'کد ملی' +
              " | " + 'تاریخ تولد' + " | " + 'شهر' + " | " + 'شغل' + "\n")

count = 0

for row in peoplecsv:
    if Faze2_ssn.__contains__(row['ssn']):

        count += 1

        my_file.write(row['first_name'] + " | " + row['last_name'] + " | " + row['ssn'] +
                      " | " + row['birthday'] + " | " + row['city'] + " | " + row['work'] + "\n")

my_file.write("تعداد مظنونین : " + str(count) + "\n")

my_file.write("end faze 2 - " + datetime.now().strftime('%H:%M:%S') + "\n")
my_file.write("------------------------------\n")


# -------------- FAZE 3 -------------- #


my_file.write("start faze 3 - " + datetime.now().strftime('%H:%M:%S') + "\n")

# 17

list_F = []

accountscsv = csv.DictReader(open('accounts.csv', encoding='utf-8'))

for row in accountscsv:
    if Faze2_ssn.__contains__(row['ssn']):

        list_F.append(row['account_id'])

# 18

list_ssn_ghachaghchi_ha = []

peoplecsv = csv.DictReader(open('people.csv', encoding='utf-8'))

for row in peoplecsv:
    if get_display(row['work']).__contains__(get_display('قاچاقچی')):

        list_ssn_ghachaghchi_ha.append(row['ssn'])

# 19

list_hesab_ghachaghchi_ha = []

accountscsv = csv.DictReader(open('accounts.csv', encoding='utf-8'))

for row in accountscsv:

    if list_ssn_ghachaghchi_ha.__contains__(row['ssn']):

        list_hesab_ghachaghchi_ha.append(row['account_id'])

# 20

list_G = []

transactionscsv = csv.DictReader(open('transactions.csv', encoding='utf-8'))

for row in transactionscsv:
    if list_F.__contains__(row['to']) and list_hesab_ghachaghchi_ha.__contains__(row['from']):

        list_G.append(row['to'])

# 21

list_H = []

for row in list_G:

    if not list_H.__contains__(row):

        current_account_count = list_G.count(row)

        if 6 > current_account_count > 1:

            list_H.append(row)

# 22

list_I = []

accountscsv = csv.DictReader(open('accounts.csv', encoding='utf-8'))

for row in accountscsv:

    if list_H.__contains__(row['account_id']):

        if not list_I.__contains__(row['ssn']):
            list_I.append(row['ssn'])

# 23

Faze3_ssn = list_I

peoplecsv = csv.DictReader(open('people.csv', encoding='utf-8'))

count = 0

my_file.write("نام" + " | " + "نام خانوادگی" + "\n")

for row in peoplecsv:
    if Faze3_ssn.__contains__(row['ssn']):

        count += 1

        my_file.write(row['first_name'] + " | " + row['last_name'] + "\n")

my_file.write("تعداد مظنونین : " + str(count) + "\n")

my_file.write("end faze 3 - " + datetime.now().strftime('%H:%M:%S') + "\n")
my_file.write("------------------------------\n")

# -------------- FAZE 4 -------------- #

my_file.write("start faze 4 - " + datetime.now().strftime('%H:%M:%S') + "\n")

# 26

list_J = []

phonescsv = csv.DictReader(open('phones.csv', encoding='utf-8'))

for row in phonescsv:
    if Faze3_ssn.__contains__(row['ssn']):

        list_J.append(row['number'])

# 27

list_shomare_ghachaghchi_ha = []

phonescsv = csv.DictReader(open('phones.csv', encoding='utf-8'))

for row in phonescsv:

    if list_ssn_ghachaghchi_ha.__contains__(row['ssn']):

        list_shomare_ghachaghchi_ha.append(row['number'])

# 28

list_K = []

callscsv = csv.DictReader(open('calls.csv', encoding='utf-8'))

for row in callscsv:
    if list_J.__contains__(row['from']) or list_J.__contains__(row['to']):

        x = ""

        if list_J.__contains__(row['from']):

            if list_shomare_ghachaghchi_ha.__contains__(row['to']):

                x = row['from']
        else:

            if list_shomare_ghachaghchi_ha.__contains__(row['from']):

                x = row['to']

        if not list_K.__contains__(x):
            list_K.append(x)

# 29

list_L = []

phonescsv = csv.DictReader(open('phones.csv', encoding='utf-8'))

for row in phonescsv:
    if list_K.__contains__(row['number']):

        list_L.append(row['ssn'])

# 30

Faze4_ssn = list_L

peoplecsv = csv.DictReader(open('people.csv', encoding='utf-8'))

count = 0

my_file.write("نام" + " | " + "نام خانوادگی" + "\n")

for row in peoplecsv:
    if Faze4_ssn.__contains__(row['ssn']):

        count += 1

        my_file.write(row['first_name'] + " | " + row['last_name'] + "\n")

my_file.write("تعداد مظنونین : " + str(count) + "\n")

my_file.write("end faze 4 - " + datetime.now().strftime('%H:%M:%S') + "\n")
my_file.write("------------------------------\n")
my_file.write("The End")

# -------------- END --------------
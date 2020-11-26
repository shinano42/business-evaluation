import sys
import csv
from faker import Faker
from random import randint, uniform

num = int(sys.argv[1]) * 10
not_accept_num = 1000 - num
is_test_data =  sys.argv[2].lower() in ['true', '1', 't', 'y', 'yes', 'yeah'] if len(sys.argv) >= 3 else False

print(is_test_data)
fake = Faker()
fieldnames = ["Id", "result", "Name", "AgeOfEstablishment", "Fund", "NumberOfEmployees", "AverageIncome", "OfficerAverageIncome", "RateOfTurnover", "Sales", "ProfitRatio"]


if (is_test_data == False):
    with open('train.csv', 'w', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        
        for i in range(num):
            income = randint(70,500)
            company = {
                "Id": i+1,
                "result": "Yes",
                "Name": fake.company(),
                "AgeOfEstablishment": randint(0,200),
                "Fund": randint(100,100000),
                "NumberOfEmployees": randint(3,100000),
                "AverageIncome": income,
                "OfficerAverageIncome": income + 150,
                "RateOfTurnover": round(uniform(0, 1), 2),
                "Sales": randint(500,100000),
                "ProfitRatio": randint(10,100)/100

            }
            csvwriter.writerow(company)
        for i in range(not_accept_num):
            income = randint(70,300)
            company = {
                "Id": 1000 - not_accept_num + (i +1),
                "result": "No",
                "Name": fake.company(),
                "AgeOfEstablishment": randint(0,50),
                "Fund": randint(100,10000),
                "NumberOfEmployees": randint(3,1000),
                "AverageIncome": income,
                "OfficerAverageIncome": income + 100,
                "RateOfTurnover": randint(25,100)/100,
                "Sales": randint(100,10000),
                "ProfitRatio": randint(10,70)/100
            }
            csvwriter.writerow(company)
        
else:
    with open('test.csv', 'w', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        for i in range(1000):
            income = randint(70,500)
            company = {
                "Id": i+1,
                "Name": fake.company(),
                "AgeOfEstablishment": randint(0,200),
                "Fund": randint(50,100000),
                "NumberOfEmployees": randint(3,100000),
                "AverageIncome": income,
                "OfficerAverageIncome": income + 150,
                "RateOfTurnover": round(uniform(0, 1), 2),
                "Sales": randint(500,100000),
                "ProfitRatio": randint(0,100)/100

            }
            csvwriter.writerow(company)
 
csvfile.close()
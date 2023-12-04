import requests
import json
import csv
import xlsxwriter
from bs4 import BeautifulSoup

r = requests.get('https://www.nobroker.in/property/rent/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NjMzODIzLCJsb24iOjc3LjYwMzQ4OTQsInBsYWNlSWQiOiJDaElKMDYtLVk5WVZyanNSZzkxeUFoVG4wQmsiLCJwbGFjZU5hbWUiOiJSaWNobW9uZCBUb3duIiwic2hvd01hcCI6ZmFsc2V9LHsibGF0IjoxMi45NTY5OTExLCJsb24iOjc3LjYwMjc3MzIsInBsYWNlSWQiOiJDaElKTTJKakZOSVZyanNSaEpRellHeTU0Z1kiLCJwbGFjZU5hbWUiOiJMYW5nZm9yZCBUb3duLCBTaGFudGkgTmFnYXIiLCJzaG93TWFwIjpmYWxzZX0seyJsYXQiOjEyLjk2Mzg0NzcsImxvbiI6NzcuNTk4NDc1OCwicGxhY2VJZCI6IkNoSUp5WFNrUE5jVnJqc1I5eUlCVkUtUENabyIsInBsYWNlTmFtZSI6Ikxhbmdmb3JkIEdhcmRlbnMiLCJzaG93TWFwIjpmYWxzZX1d&radius=2.0&sharedAccomodation=0&type=BHK2&city=bangalore&locality=Richmond%20Town&isMetro=false')

website='www.nobroker.in'

print(r)
soup = BeautifulSoup(r.content, 'html.parser')

excel = xlsxwriter.Workbook("data.xlsx")
sheet = excel.add_worksheet("sheet1")

sheet.write(0,0,'#')
sheet.write(0,1,'Property')
sheet.write(0,2,'Rent')
sheet.write(0,3,'Deposit')
sheet.write(0,4,'Link')






title_results = soup.find_all('a', class_="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full")
rent_results = soup.find_all(id="minimumRent")  
deposit_results = soup.find_all(id="roomType")
for x in range(len(title_results)):
    sheet.write(x+1,0,str(x))
    sheet.write(x+1,1,title_results[x].text)
    sheet.write(x+1,2,rent_results[x].text)
    sheet.write(x+1,3,deposit_results[x].text)
    sheet.write(x+1,4,website+title_results[x].get('href'))

excel.close()

#<div class="bg-white rounded-4 bg-clip-padding overflow-hidden mx-0.5p tp:border-b-0 shadow-defaultCardShadow tp:shadow-cardShadow tp:mt-0.5p  my-1.2p   tp:mx-0 tp:mb:1p
#						hover:cursor-pointer nb__2_XSE"

# py nobroker.py




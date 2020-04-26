#!python3
import sys
from lxml import etree



xmlname = sys.argv[1]
# xmlname = 'FoodServiceData_fourth.xml'

xml = etree.parse(xmlname)
xpath = '/foodservices/foodservice/inspections/inspection/Grade'
results = xml.xpath(xpath)
Grades = [result.text for result in results]

answer = {}
for grade in Grades:
    if grade == None:
        continue
    elif grade in answer.keys():
        answer[grade] += 1
    else:
        answer[grade] = 1
for grade in sorted(answer.keys()):
    print(grade+' ',answer[grade])


# if the grade is missing,then skip it
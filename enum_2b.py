#!python3
import sys
from lxml import etree



xmlname = sys.argv[1]
# xmlname = 'FoodServiceData_fourth.xml'

xml = etree.parse(xmlname)
xpath = '/foodservices/foodservice/TypeDescription'
results = xml.xpath(xpath)
tys = [result.text for result in results]
answer = {}
for td in tys:
    if td in answer.keys():
        answer[td] = answer[td] + 1
    else:
        answer[td] = 1
for td in sorted(answer.keys()):
    print(td+' '+str(answer[td]))

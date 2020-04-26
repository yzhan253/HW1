#!python3
import sys
import pandas as pd
import numpy as np
from lxml import etree

def xmlizer():
    data = sys.argv[1]
    output = sys.argv[2]
    # data = 'FoodServiceData.csv'
    # output = 'FoodServiceData_fourth.xml'
    df = pd.read_csv(data)
    df.replace(np.nan,'',inplace=True) 
    
    root = etree.Element("foodservices")
    EstablishmentID_list = df.EstablishmentID.drop_duplicates()
    for establishmentID in EstablishmentID_list[:5]:
        df_tmp = df.loc[df.EstablishmentID==establishmentID].iloc[0,:]
        foodservice = etree.SubElement(root,"foodservice")
        foodservice.set('id',str(establishmentID))
        etree.SubElement(foodservice,"Establishment").text = df_tmp["EstablishmentName"]
        etree.SubElement(foodservice,"Place").text = str(df_tmp["PlaceName"])
        etree.SubElement(foodservice,"Address").text = str(df_tmp["Address"])
        etree.SubElement(foodservice,"Address2").text = str(df_tmp["Address2"])
        etree.SubElement(foodservice,"City").text = str(df_tmp["City"])
        etree.SubElement(foodservice,"State").text = str(df_tmp["State"])
        etree.SubElement(foodservice,"Zip").text = str(df_tmp["Zip"])
        etree.SubElement(foodservice,"TypeDescription").text = str(df_tmp["TypeDescription"])
        etree.SubElement(foodservice,"Latitude").text = str(df_tmp["Latitude"])
        etree.SubElement(foodservice,"Longitude").text = str(df_tmp["Longitude"])
        inspections = etree.SubElement(foodservice,"inspections")
        for i in range(df.loc[df.EstablishmentID==establishmentID].shape[0]):
            df_tmp2 = df.loc[df.EstablishmentID==establishmentID].iloc[i,:]
            inspection = etree.SubElement(inspections,"inspection")
            inspection.set('id',str(df_tmp2['InspectionID']))
            etree.SubElement(inspection,"InspectionDate").text = str(df_tmp2['InspectionDate'])
            etree.SubElement(inspection,"Score").text = str(df_tmp2['Score'])
            etree.SubElement(inspection,"Grade").text = str(df_tmp2['Grade'])
            etree.SubElement(inspection,"NameSearch").text = str(df_tmp2['NameSearch'])
            etree.SubElement(inspection,"Intersection").text = str(df_tmp2['Intersection'])
    output_xml = etree.ElementTree(root)
    output_xml.write(output, pretty_print=True,encoding='utf8',xml_declaration=True)
if __name__ == '__main__':
    xmlizer()
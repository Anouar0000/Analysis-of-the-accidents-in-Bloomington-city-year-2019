from random import randrange
import pandas as pd

##########################convert damage estmated to number##################################

def convertData(Data1,feature):
    for i in range(len(Data1)):
        if ("UNDER" in str(Data1[feature][i])):
            Data1[feature][i] = 1000

        if ("TO" in str(Data1[feature][i])):
            datalist = Data1[feature][i].split(" ")
            Data1[feature][i] = int(datalist[2][1:])

        if ("OVER" in str(Data1[feature][i])):
            datalist = Data1[feature][i].split(" ")
            result = int(datalist[1][1:])
            Data1[feature][i] = randrange(result, result * 3)


###########################delet all blanc and none in data base ##############################

def cleanData(Data1):

    aaa = ['Master Record Number', 'Township', 'City', 'Collision Date', 'Collision Time', 'Vehicles Involved',
       'Number Injured', 'Roadway Class', 'Aggressive Driving?', 'Hit and Run?', 'Light Condition',
       'Weather Conditions', 'Surface Condition', 'Roadway Junction Type', 'Road Character', 'Roadway Surface',
       'Primary Factor', 'Damage Estimate', 'Traffic Control']

    nan_value = float("NaN")
    for i in aaa:
        Data1.replace("", nan_value, inplace=True)
        Data1.dropna(subset=[i], inplace=True)


################################corretion of dates############################################

def convertDate(Dataset,name):

    l=[]
    for i in range(len(Dataset[name])):
        try:
            print(type(Dataset[name][i]))

            if  len(Dataset[name][i])==8:
                l=Dataset[name][i].split("/")
                Dataset[name][i]="0"+l[0]+"/"+"0"+l[1]+"/"+l[2]

            if len(Dataset[name][i]) == 9:
                l=Dataset[name][i].split("/")

                if len(l[0])==2:
                    Dataset[name][i]=l[0]+"/"+"0"+l[1]+"/"+l[2]
                else:
                    Dataset[name][i]="0"+l[0] +"/"+ l[1] +"/" + l[2]
        except:
            continue

    Dataset[name] = pd.to_datetime(Dataset[name], format='%m/%d/%Y')

#########################################save DB############################################

def extractDataTocsv(Data1):

    name=input("enter data name : ")
    Data1.to_csv(r'.\''+name+'.csv', index=False, header=True)

def extractDataToXlsx(Data1):

    name = input("enter data name : ")
    Data1.to_excel(r'C:\Users\Anouar\Desktop\Dsen-A\S2\6-Projet BI\''+name+'.xlsx', index=False, header=True)

def convertFromCsvToXls():

    read_file = pd.read_csv(r'Path where the CSV file is stored\File name.csv')
    read_file.to_excel(r'Path to store the Excel file\File name.xlsx', index=None, header=True)

def __main__():

    ################################################select best feature######################
    Dataset = pd.read_csv(
        "city-of-bloomington-data/FirstData.csv")

    Data1 = Dataset.drop(
        ['Agency', 'Local Code', 'County', 'Trailers Involved', 'Number Dead', 'Number Deer', 'House Number',
         'Roadway Name', 'Roadway Suffix', 'Roadway Number', 'Roadway Interchange', 'Roadway Ramp', 'Roadway Id',
         'Intersecting Road', 'Intersecting Road Number', 'Mile Marker', 'Interchange', 'Corporate Limits?',
         'Property Type', 'Feet From', 'Direction', 'Latitude', 'Longitude', 'Traffic Control Devices?', 'Locality',
         'School Zone?', 'Rumble Strips?', 'Construction?', 'Construction Type', 'Type of Median',
         'Manner of Collision', 'Time Notified', 'Time Arrived', 'Investigation Complete?', 'Photos Taken?',
         'Unique Location Id', 'State Property Damage?', 'NARRATIVE'], axis=1)
    #

    convertData(Data1,"Damage Estimate")
    cleanData(Data1)
    convertDate(Data1,'Collision Date')
    #extractDataTocsv(Data1)
    extractDataToXlsx(Data1)

__main__()


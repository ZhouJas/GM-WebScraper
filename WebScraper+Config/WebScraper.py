from urllib.parse import urlparse
from urllib.parse import parse_qs
import requests
import json
import simplejson

# web request initialization
with open('./config.json') as f:
  configData = json.load(f)
url = configData['url']

payload=configData['payload']
headers = configData['headers']
siteurl = configData['siteurl']
imageurl = configData['imageurl']
print(headers)
response = requests.request("POST", url, headers=headers, data=payload)

parsedInfo = urlparse(url)
data = response.json()
output = {}
output['Trims'] = []
#output['Trims']['Colors'] = []

for i in data['modelMatrix']['bodyTypes']:
    for j in data['modelMatrix']['styleInformation']:
        for k in data['modelMatrix']['driveTypes']:
            output['Trims'].append({
                'id': "null",
                'Trim': j['trimName'],
                'Model': parse_qs(parsedInfo.query)['carline'][0],
                'Type': "SUV",#i['formattedConfig']
                'Year': parse_qs(parsedInfo.query)['modelyear'][0],
                'SiteURL': siteurl,
                'Colors': [],
                'ListPrice': j['baseMsrpValue'],
                'ListFinancing': [],
                'ListLeasing': [],
                "isAWD": (k['id'] == "AWD" or k['id'] == "4WD"),
                "is2WD": (k['id'] == "FWD" or k['id'] == "2WD" or k['id'] == "RWD"),
                "Engine": [
                    {
                        "Description": data['modelMatrix']['engine'][0]['description'],
                        "Displacement": "null",
                        "DisplacementUnit": "L",
                        "Features": "null"
                    }
                ],
                "FuelEco": "null",
                "FuelEcoUnit": "L/100km",
                "Summary": [],
                "Promotions": "null",
                "To60": "null",
                "To60Unit": "null",
                "Emission": "null",
                "EmissionUnit": "null",
                "FuelDelivery": "null",
                "Power": [
                    {
                        "Description": "0 horsepower",
                        "HorsePower": 0,
                        "HorsePowerUnit": "hp"
                    }
                ],
                "Torque": [
                    {
                        "Description": "0 lb-ft",
                        "Force": 0,
                        "ForceUnit": "lb-ft"
                    }
                ],
                "ElectricMotor": "null",
                "Battery": "null",
                "Brakes": {
                    "Description": "4-wheel antilock disc brakes",
                    "Type": "null",
                    "BrakeAssist": 1==0,
                    "Features": "null"
                },
                "Suspension": {
                    "Description": "Front MacPherson Strut, Rear Five-Link Independent",
                    "Front": "null",
                    "Rear": "null",
                    "Shocks": 1==0
                },
                "isAuto": 1==1,
                "isManual": 1==0,
                "Transmission": [
                    "null"
                ],
                "Wheels": {
                    "Description": "null",
                    "Options": "null"
                },
                "Steering": "null",
                "Exhaust": "null",
                "TractionControl": 1==1,
                "StabilityControl": 1==1,
                "Airbags": 0,
                "ParkDistanceControl": 1==0,
                "BlindSpotWarning": 1==0,
                "LaneDepartureWarning": 1==0,
                "LaneDepartureCorrection": 1==0,
                "CollisionWarning": 1==0,
                "CollisionAssist": 1==0,
                "Alarm": 1==0,
                "RearviewCamera": 1==0,
                "Seats": {
                    "Description": "Front Bucket Seats",
                    "Number": 5,
                    "Heated": 1==0,
                    "Adjustable": 1==1,
                    "Material": "null"
                },
                "SteeringWheel": {
                    "Description": "Leather-wrapped steering wheel",
                    "Heated": 1==0,
                    "Material": "null"
                },
                "ClimateControl": 1==0,
                "EntryAndStart": "null",
                "Lights": "Halogen headlamps",
                "Roof": {
                    "Description": "null",
                    "Sunroof": 1==0
                },
                "Mirrors": "null",
                "Doors": {
                    "Description": "4 doors",
                    "Number": 4
                },
                "Height": 0,
                "HeightUnit": "mm",
                "Length": 0,
                "LengthUnit": "mm",
                "Width": 0,
                "WidthUnit": "mm",
                "HeadRoomAverage": 0,
                "HeadRoomAverageUnit": "mm",
                "PassengerVolumne": 0,
                "PassengerVolumneUnit": "L",
                "TrunkVolume": 0,
                "TrunkVolumeUnit": "L",
                "FuelVol": 0,
                "FuelVolUnit": "L",
                "weight": 0,
                "WeightUnit": "kg",
                "AppleCarPlay": 1==1,
                "AndroidAuto": 1==1,
                "NavigationSystem": 1==0,
                "Bluetooth": 1==1,
                "RemoteStarter": 1==0,
                "USBPort": 1==0,
                "RemoteKeylessEntry": 1==0,
                "AuxInput": 1==1,
                "PowerDoorLocks": 1==0
            })

for i in data['config']['OPTIONS']['COLOR']['exterior']:
    for j in i['items']:
        colorcode = j['id']
        
        imgurl = imageurl.format(colorcode)
        for k in output['Trims']:
            k['Colors'].append({
                'Color': j['primaryName'],
                'ImageURL': imgurl
            })

with open('output.json', 'w') as outfile:
    json.dump(output, outfile)

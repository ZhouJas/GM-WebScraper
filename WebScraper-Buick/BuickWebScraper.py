from urllib.parse import urlparse
from urllib.parse import parse_qs
import requests
import json
import simplejson

# web request initialization

url = "https://www.buick.ca/byo-vc/services/retrieveConfiguration/buick/CA/en/na/404844?bodystyle=envision&carline=envision&modelyear=2020&postalCode=L1H8P7"

payload="{\"ss\":\"H4sIAAAAAAAAAH2PuwrCMBhGj00pIq76Ap07iBd0jL2k9YJSOxTB0U0c3XwdX1OTXqKC+A1Jzpf/Cgzh/sALLjjnK04oMd4Xd27yFOkLox5idNgjNoVCbMcFIik1KnlEyHyBSMczRLbTh8pyjcX0qUWtPsL3fdpiXhCXhSz1y208t46rerRRVV0Lpp0FNUlMmcYYNMlqvvzl6nFsoh7rDWZaC2YxC2bBFqCLJCQiJiVjxZqPz396AezqD9FoAQAA\"}"
headers = {
  'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
  'Content-Type': 'application/json; charset=utf-8',
  'Accept': '*/*',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'accept-language': 'en-CA,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5',
  'Cookie': 'TSa6897428027=08aac06b63ab2000293fbcaec2c673a5707fe8a5403a15381216805b982fa9a570d61984acb47a9b084131da131130000a980575152bf9d033e715e3de3bfd861c9ad70efaffd1b499a5002c916fd54dde4cdb81b6331bed00ecd24575113011; ipe.35282.pageViewedCount=5; ipe.35282.pageViewedDay=15; ipe_35282_fov=%7B%22numberOfVisits%22%3A1%2C%22sessionId%22%3A%22b9cb1dc4-be36-81b8-2959-60cf2cbafddd%22%2C%22expiry%22%3A%222021-02-15T04%3A04%3A30.838Z%22%2C%22lastVisit%22%3A%222021-01-16T04%3A29%3A26.810Z%22%7D; modelYear=2020; modelName=envision; bodystyle=envision; GMWP_location=country_code=CA,region_code=ON,city=TORONTO,county=,zip=M3H+M3M+M4B+M4C+M4E+M4G+M4H+M4J+M4K+M4L+M4M+M4N+M4P+M4R+M4S+M4T+M4V+M4W+M4X+M4Y+M5A+M5B+M5C+M5E+M5G+M5H+M5J+M5K+M5L+M5M+M5N+M5P+M5R+M5S+M5T+M5V+M5W+M5X+M6A+M6B+M6C+M6E+M6G+M6H+M6J+M6K+M6L+M6M+M6N+M6P+M6R+M6S+M7A+M7Y+M9M+M9N+M9P+M9W; ak_bmsc=48A291F5F6D0D63CA354C3C6DC7EDF8CB81A2C51056000000F6C02606AE12311~pl97jcJ3IzAT8O9RLQ6tcjnj86g046Y401gsRNjElPeEQAa/yVjg/FsPg68QlSgS/qywhoRREqERIKaBxZ1QIb6/q+e48YBrM7wAztjhZ+4FpDWLi4x5OiJZAt2ZjVlpPNg4tbLAzLzVW0KdW+qaCXSRqVVV2cjLXamodUA0/GyyJFbdVG4Pm+zso30OVvVsSkoPsu4IdOOSobe65WX8fBP+6pacArcxKyv5pSDK2G2z4=; bm_sv=D6CA0C93D92D52D22D6A376CD4D22EC3~5qNpbloD1xbTLWodNnCl/RuJR4YMNkNRwIso+jvhCr4BLPg9YIq+P8lHYZVEEpPV7rBRE+2TM0XVd30cZNfvX6CSeuGEanWi5oNQMF2eZ154U2X5ngPB7I+YwUiZcV6FdKtXABcTlhljZDKB9scfJw=='
}

response = requests.request("POST", url, headers=headers, data=payload)

parsedInfo = urlparse(url)
siteurl = "https://www.buick.ca/byo-vc/client/en/CA/buick/envision/2020/envision/trim"
colorcode = "GIR"
imageurl = f"https://cgi.buick.com/mmgprod-us/dynres/prove/image.gen?i=2020/4XU26/4XU26__1SP/{colorcode}_LTG_M3T_{colorcode}_HT5_IO6gmds2.jpg&v=deg01&std=true&country=US&removeCat="
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
        imageurl = f"https://cgi.buick.com/mmgprod-us/dynres/prove/image.gen?i=2020/4XU26/4XU26__1SP/{colorcode}_LTG_M3T_{colorcode}_HT5_IO6gmds2.jpg&v=deg01&std=true&country=US&removeCat="
        for k in output['Trims']:
            k['Colors'].append({
                'Color': j['primaryName'],
                'ImageURL': imageurl
            })

with open('dataBuick.json', 'w') as outfile:
    json.dump(output, outfile)

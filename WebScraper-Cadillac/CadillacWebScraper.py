from urllib.parse import urlparse
from urllib.parse import parse_qs
import requests
import json
import simplejson

# web request initialization

url = "https://www.cadillaccanada.ca/byo-vc/services/retrieveConfiguration/cadillac/CA/en/na/413287?bodystyle=escalade&carline=escalade&modelyear=2021&postalCode=L1H8P7"

payload="{\"ss\":\"H4sIAAAAAAAAAH2PPQ6CQBCFn4zBRlsvQG2iJqjtusBiwk8IYLiAsbP0AF7Di3kRa50BWbTxFbvvm53MvgEwB24F3OwM53SBoxWk9sOj6/P+4AuiKWhValCy24LSgp2pfZDeGFCZBox7BVL+ko8qA8XrGnTIj+xM9GKh0wzkeR76se4ibCrVsBt/atT1tb/1Xe3cAXi+BQlgQTIMwPkscIgBJJYFWciCLGZB1uoBmEAjQIgIBjESfD390xt0eoxBawEAAA==\"}"
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
  'Cookie': 'modelYear=2021; formData=undefined; ipe_s=68b75703-5e9d-28f0-8061-55b87f4b3ab5; IPE_LandingTime=1610773704376; ipe.35282.pageViewedCount=1; ipe.35282.pageViewedDay=16; modelName=escalade; bodystyle=escalade; firstEngagement=1; re-evaluation=true; TSa6897428027=08aac06b63ab200072120855104436de93a2fe0674f2087099dbfc5e15fa8fc4d758a1d917c0c8f8082636339f11300050d35c253de6c0c7e9aeadd6e654765cfd34d1df50b4f0e88c3871f0923d5cb94823339ada3dfdaaaa4d31f9423632af; ipe_35282_fov=%7B%22numberOfVisits%22%3A1%2C%22sessionId%22%3A%2268b75703-5e9d-28f0-8061-55b87f4b3ab5%22%2C%22expiry%22%3A%222021-02-15T05%3A08%3A24.381Z%22%2C%22lastVisit%22%3A%222021-01-16T05%3A09%3A40.001Z%22%7D; GMWP_location=country_code=CA,region_code=ON,city=TORONTO,county=,zip=M3H+M3M+M4B+M4C+M4E+M4G+M4H+M4J+M4K+M4L+M4M+M4N+M4P+M4R+M4S+M4T+M4V+M4W+M4X+M4Y+M5A+M5B+M5C+M5E+M5G+M5H+M5J+M5K+M5L+M5M+M5N+M5P+M5R+M5S+M5T+M5V+M5W+M5X+M6A+M6B+M6C+M6E+M6G+M6H+M6J+M6K+M6L+M6M+M6N+M6P+M6R+M6S+M7A+M7Y+M9M+M9N+M9P+M9W; ak_bmsc=22B8850ACF13E94D478A46E20ECB7BAEB81A2C50280C000036750260D2994F17~pl1BFsx1JiWCCbSDLd20Y4EyGUejQQi2VrIV6kUSTbLoFvkzZ0T4w2vhL+pfGb/0BEjNR7cTYnfhod2WMALMAeRkTXy6Nv5EHyT4nZwKb0pzcHrRFkIyewqDJquaonnt21SkJKGrmYF228/7RKdzZpypuI+Rvkg22v11uZvbt4gRn/h4L+lhhJQOrBD5o8fLKkLB9Qpclcc5VO5D1LFlUIh6Xw9v5FHWUre6cnj9LQT9Q='
}

response = requests.request("POST", url, headers=headers, data=payload)


parsedInfo = urlparse(url)
siteurl = "https://www.cadillaccanada.ca/byo-vc/client/en/CA/cadillac/escalade/2021/escalade/trim"
colorcode = "GBA"
imageurl = f"https://cgi.cadillac.com/mmgprod-us/dynres/prove/image.gen?i=2021/6K10706/6K10706__1SC/{colorcode}_L87_MQC_GU5_SMD_{colorcode}_A50_ATN_HGF_IOVgmds2.jpg&v=deg01&std=true&country=US&removeCat="
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
        
        imageurl = f"https://cgi.cadillac.com/mmgprod-us/dynres/prove/image.gen?i=2021/6K10706/6K10706__1SC/{colorcode}_L87_MQC_GU5_SMD_{colorcode}_A50_ATN_HGF_IOVgmds2.jpg&v=deg01&std=true&country=US&removeCat="
        for k in output['Trims']:
            k['Colors'].append({
                'Color': j['primaryName'],
                'ImageURL': imageurl
            })

with open('dataCadillac.json', 'w') as outfile:
    json.dump(output, outfile)

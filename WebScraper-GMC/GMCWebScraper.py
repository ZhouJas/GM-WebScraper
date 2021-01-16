from urllib.parse import urlparse
from urllib.parse import parse_qs
import requests
import json
import simplejson

# web request initialization

url = "https://www.gmccanada.ca/byo-vc/services/retrieveConfiguration/gmc/CA/en/na/412396?bodystyle=yukon&carline=yukon&modelyear=2021&postalCode=L1H8P7"

payload="{\"ss\":\"H4sIAAAAAAAAAH2QPW7CQBCFvzAJFUJUuYCVMhISP6Jd2cY24s+ClSx62pTpKHKOHCeXyCHSpg47sj0BIfGa3e9ptG/eAs/w8UV38UPn+EYndqh3xQ/vv5/f4UDVQ0Y7hyxnY2RVxkjmJ4jP10iZzAO6A+ImQyQfeqTY7JB4qnNL/xdErQESRRHts93XtNq7KtweG6/267SWZOwUnhrjpRnRNBvRLIOQeQFhUQNdzkCXNNBmBtrQQPsZaGODKs60RGP0ad3i1tUvTEjJyClYsGLNlhLPif/ad3UGUN2a1bcBAAA=\"}"
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
  'Cookie': 'modelYear=2021; formData=; ipe_s=80e2aa88-cad2-1631-7af7-53040f440982; IPE_LandingTime=1610767248179; ipe.35282.pageViewedDay=15; modelName=yukon; bodystyle=yukon; firstEngagement=1; BIGipServerpub-m-wpsegment10-wpx-443-pool=1592949514.64288.0000; re-evaluation=true; ipe.35282.pageViewedCount=2; BIGipServerpub-w-wpsegment10-wpx-443-pool=1733589514.64288.0000; TSa6897428027=08aac06b63ab20007deeb425a5c048cffdaa6a92aad42fa88ae7a0137cc311951f5e1cc658447e5708a2de0ea21130004cf2e8d159e416bb9bac649926ca5dba19c130fd6a56bec335db94a8e81dd19380e831fd86dc1a6e306e7500e6c1113e; ipe_35282_fov=%7B%22numberOfVisits%22%3A1%2C%22sessionId%22%3A%2280e2aa88-cad2-1631-7af7-53040f440982%22%2C%22expiry%22%3A%222021-02-15T03%3A20%3A48.188Z%22%2C%22lastVisit%22%3A%222021-01-16T03%3A46%3A58.574Z%22%7D; GMWP_location=country_code=CA,region_code=ON,city=TORONTO,county=,zip=M3H+M3M+M4B+M4C+M4E+M4G+M4H+M4J+M4K+M4L+M4M+M4N+M4P+M4R+M4S+M4T+M4V+M4W+M4X+M4Y+M5A+M5B+M5C+M5E+M5G+M5H+M5J+M5K+M5L+M5M+M5N+M5P+M5R+M5S+M5T+M5V+M5W+M5X+M6A+M6B+M6C+M6E+M6G+M6H+M6J+M6K+M6L+M6M+M6N+M6P+M6R+M6S+M7A+M7Y+M9M+M9N+M9P+M9W; ak_bmsc=CBC60D9D8B10B388F3E4BDD95E603DC91728BEADB0180000276202609D9BE979~pl46D56WhCd+qX0XzOm1Ow3CwWMY9DKCNWfe0eLkN5sXKbXKyy0sbZYzsSK6iBb7WgL2qJ71nsbQ5tt+c/ekJgVXIrYl6YUKe3kD33UImCagJcbEtk6oxDWDGRFOJV5QNz8uSne3GqnKVO7gqlsIhBwOZLFzw5aYs1kE8Uc9INQASFptf8P+1Tb94/9K2LzZAAbA/xDN71xq/6evJEMNlor1t6m8rmWBm94vpamxYp7QY='
}

response = requests.request("POST", url, headers=headers, data=payload)

parsedInfo = urlparse(url)
siteurl = "https://www.gmccanada.ca/byo-vc/client/en/CA/gmc/yukon/2021/yukon/trim"
colorcode = "GKZ"
imageurl = f"https://cgi.gmc.com/mmgprod-us/dynres/prove/image.gen?i=2021/TK10706/TK10706__5SA/{colorcode}_L87_MQC_GU5_RTL_XCI_{colorcode}_A50_H2X_ATN_IOTgmds2.jpg&v=deg01&std=true&country=US&removeCat="
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
        
        imageurl = f"https://cgi.gmc.com/mmgprod-us/dynres/prove/image.gen?i=2021/TK10706/TK10706__5SA/{colorcode}_L87_MQC_GU5_RTL_XCI_{colorcode}_A50_H2X_ATN_IOTgmds2.jpg&v=deg01&std=true&country=US&removeCat="
        for k in output['Trims']:
            k['Colors'].append({
                'Color': j['primaryName'],
                'ImageURL': imageurl
            })

with open('dataGMC.json', 'w') as outfile:
    json.dump(output, outfile)

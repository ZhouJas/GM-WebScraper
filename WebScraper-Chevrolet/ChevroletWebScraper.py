from urllib.parse import urlparse
from urllib.parse import parse_qs
import requests
import json
import simplejson

# web request initialization

url = "https://www.chevrolet.ca/byo-vc/services/toggleOptionData/chevrolet/CA/en/na/413687?bodystyle=corvette&carline=corvette&modelyear=2021&postalCode=L1H8P7"

payload="{\"rpo\":\"G8G\",\"ss\":\"H4sIAAAAAAAAAH2QPW7CUBCEP7yIBtLSULpKQeFIKFBaBhzAxjG4sOhpKTkAN8hBchduQwm72H5Aw0jvZ2ZHTzMP6MPpj052wdsf8KIQ01546/h/OuuBoYsESYEkxReSBgmSj3+Rcr5G4nGMhPkE+SlCZJFtVVvtdNsurwoqfCC+79O82BnOyiIs9dautUrXwWYWZWkteLp69aS53KM0fvkOJrXPhEHlvOdxFg3yIBbSEQvriJVzxEo6YmUdsdIurf7MJyMipsyJWZKQsmHHk+UdbjRwMZKMAQAA\"}"
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
  'Cookie': 'GMWP_location=country_code=CA,region_code=ON,city=TORONTO,county=,zip=M3H+M3M+M4B+M4C+M4E+M4G+M4H+M4J+M4K+M4L+M4M+M4N+M4P+M4R+M4S+M4T+M4V+M4W+M4X+M4Y+M5A+M5B+M5C+M5E+M5G+M5H+M5J+M5K+M5L+M5M+M5N+M5P+M5R+M5S+M5T+M5V+M5W+M5X+M6A+M6B+M6C+M6E+M6G+M6H+M6J+M6K+M6L+M6M+M6N+M6P+M6R+M6S+M7A+M7Y+M9M+M9N+M9P+M9W; bm_sv=B05ADF0BDC7CA17E9863998C15E807FC~VXuA6mglBQxr9nMmv04iCun4uJ/v5Awk7tP6B97T5FUIAqtFKjaFAADcCKhJ4omX5xkummzOH9v9ykqj59MMy+Bx0wKS+/5Zbm842BSvcBhu2BbfkY4Uc8q4iAK0JZ8Jo7uds26Ljs0VNLoI6KM6s+qvFUwvRwhidWo6aNwif7o=; TSa6897428027=08aac06b63ab2000da0a8f62c3ee2ce545553bedf5d8cf16a3c6614ac9406e727b1a6bdd8db8e7d40897f4f58f113000f8c08be6d0a6f631ca6857f4afc194d3bff1794f9240f52152a0c97b2c616eb52d450aa7f1ffbeaf09fc13e0921b3775; ak_bmsc=DC485E3BCDB2E3A8D521670EE7395EA3D194CC6DC5030000D5630260725A0529~plheiQGmsByI/CB5hqsR4E7ZP0miC9r+nHq/ncbeShaFBqmm9f1cuNNhcPzbCqKjTe6GULK+06Pj7urC/NO5UfO4XSNVWHSIVmtkSxkpXqV76rBJDOXz7QUT9CVXRcR/vfd738KXb+wjwqTVt3uuSh2wc7FU+IQkukNbhhs66RiNJQ9DMK05wGnrwaU7IbVSknXWhEpvkz8o0NR/1ENuG0Gruu+YcArOTMINBCXi6E/cA='
}

response = requests.request("POST", url, headers=headers, data=payload)

parsedInfo = urlparse(url)
siteurl = "https://www.chevrolet.ca/byo-vc/client/en/CA/chevrolet/corvette/2021/corvette/config"
colorcode = "GKZ"
imageurl = f"https://cgi.chevrolet.com/mmgprod-us/dynres/prove/image.gen?i=2021/1YC07/1YC07__1LT/{colorcode}_LT2_M1L_Q8P_XFN_{colorcode}_AQ9_HTA_IOS_719gmds2.jpg&v=deg01&std=true&country=US&removeCat="
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
                'Type': i['formattedConfig'],
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
        imageurl = f"https://cgi.chevrolet.com/mmgprod-us/dynres/prove/image.gen?i=2021/1YC07/1YC07__1LT/{colorcode}_LT2_M1L_Q8P_XFN_{colorcode}_AQ9_HTA_IOS_719gmds2.jpg&v=deg01&std=true&country=US&removeCat="
        for k in output['Trims']:
            k['Colors'].append({
                'Color': j['primaryName'],
                'ImageURL': imageurl
            })

with open('dataChevrolet.json', 'w') as outfile:
    json.dump(output, outfile)

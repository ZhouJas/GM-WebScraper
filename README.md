# GM WebScraper
 This is a Python 3.9 Webscraper created to aid my internship data-entry work regarding new vehicle data.
It autofills the provided template by mimicking the http request the car model customization page sends to the manufacturer's server,
thereby obtaining in response all required data for the cars and will create an output JSON with the required data.
* Included in the folders are the python script and a config setting to change which vehicle model data to obtain.
* Note that while the server sends most information in a consistant format there are some discrepencies so changing this link to other vehicle models may result in key errors (key-value pair does not exist).
* To change the vehicle, intercept the API call the desired vehicle customization page (in .py file as siteurl)is calling to the server through postman Interceptor, then add appropriate parameters to properly mimic http request in the config.json file. You must also change the imageURL or else the generated file will not have the image of the new vehicle. 
* The Cookie params have been removed for privacy but can be also obtained through PostMan.
* This page may be updated in the future, or not, depending on how much time is available.

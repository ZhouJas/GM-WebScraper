# GM WebScraper
 This is a Python 3.9 Webscraper created to aid my internship data-entry work.
It autofills the provided template by mimicking the http request the car model customization page sends to the manufacturer's server,
thereby obtaining in response all required data for the cars and will create an output JSON with the required data.
Included in the folders are the python script and their corresponding output file to a pre-defined link for the API call of a specific car model.
Note that while the server sends most information in a consistant format there are some discrepencies so changing this link to other vehicle models may result 
in key errors (key-value pair does not exist).
To change the vehicle, intercept the API call the desired GM vehicle customization page (in .py file as siteurl)is calling to the server through postman Interceptor, then add appropriate parameters to properly mimic http request. You must also change the imageURL or else the generated file will not have the image of the new vehicle. 
This page may be updated in the future, or not, depending on how much time is available.

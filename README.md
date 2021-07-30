# seoMentor Domain Back Order Tool
is the perfect tool for scheduling a purchase of expired domains.

Every Web Promoter want to get the best domain with the best link profile, history, etc.
After the research you find your self with few domains that u want to buy but they are still not released,
If you want to purchase them you should wait to the exac time they release and calculate the "Period of grace" from the expired date etc..
And in the end you need to purchase it.

seoMentor Domain back Order Tool takes the pain out while hunting expired domains.
All you need to to do is enter the domain, choose a Registration Period and the tool will whois the domain, calculate the date and shedule a buy for you!

# How its work? 

The tool working with 2 APIs

1. WhoisXMLAPI.com for gathering domain registry information.
2. Livedns.co.il API for purchase a domain
3. Schedule a Purchase on the expiry date and adds more 90 days (The time of grace of the Israeli domain registrar)


For now this tool available only with LiveDNS API so its mean its suitable now only to israeli users because livedns website has only hebrew lanaguge, but its working almost all kinds of tld.

If you are not reading hebrew language you can try to use livedns with google translate to control their web.

In the near feature i will develop the global version that will work with GoDaddy API.
but if you are a developer feel free that take the code and change the api to yours api, just keep the credit :)

# Getting Started

1. Open Account in Livedns.co.il and buy "Affiliate Credits"
2. In Livedns panel you have some blue square "Manage Contacts" or in hebrew (ניהול אנשי קשר) and open a new Contact.
3. Pay attention that you enter a valid details and only in english. if you already a livedns customer so keep your exist Contact.
4. after you create a Contact in the Contacts Control Management you will see Nic-Handle its will be something like "LD-SA12121-IL"
This nick handle will be the values of "AdminNicHandle", "TechnicalNicHandle", "ZoneNicHandle" in settings file.
5. Open Account in WhoisXMLAPI.com and generate whois api secret key, you will get free 500 whois requests per month.
6. Install Python 3.9.x on you machine and add it to PATH.
7. Download the script folder from here and save it on you desktop.
8. Open the setting file and and fill the empty values after "=".
for example: "RegistrantName = firstname%20lastname" if you write space do it with "%20".
the last line is "wxakey" is the key of they whoisapixml api key.
all the the values must to be filled. empty value make error.
9. open cmd/terminal and get inside the project folder with cd/ command.
11. install the requirements.txt with pip install -r requirements.txt
12. run the script with the command >> python3 main.py

The Tool working flow goes like this:

1. Enter Domain Name: (only name with tld, example: example.com)
2. Check if the domain is valid, if domain is invalid keep ask for another valid domain
3. Enter Registration Period: (only int numbers from 1 to 5)
4. Send request to whoisapi and get the info about the domain, if the domain is available for purchase now it will restart the program.
5. Validation Question before scheduling
6. Schedule
7. Purchase Succes, Done

Important things that you have to know:
The final time at which the purchase is scheduled is calculated according to the Registrar of Israeli Domains and only applies to domains with the suffix .il.




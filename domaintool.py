import requests
import time
import validators
from datetime import datetime
from datetime import timedelta
#ask which domain the user want to buy
def askfordomain():
    while True:
        ask = input("Enter domain: ")
        if validators.domain(ask):
            return ask
        else:
            print("This is not a domain")
# define a function that handle the setting and make setlist dict with all details
def getSettingsFromFile():
    settingsFile = 'settings.txt'
    f = open(settingsFile, 'r')
    fileContent = f.read()
    # define a dictionary
    setdict = {}
    # define for loop that run on the settings, split them to Key and Value and save them into Dict
    for line in fileContent.split('\n'):
        keyValue = line.split('=')
        key = keyValue[0].strip()
        value = keyValue[1].strip()
        setdict[key] = value
    # return the function the last value setdict and in fact getSettingsFromFile() function will return us dict list with our values
    return setdict
# define function that prepare the last url for http post request
def makelasturl(validDomain, getset):
    lastdiclist = getset
    UserName = lastdiclist['UserName']
    Password = lastdiclist['Password']
    RegistrantName = lastdiclist['RegistrantName']
    RegistrantEmail = lastdiclist['RegistrantEmail']
    RegistrantAddress = lastdiclist['RegistrantAddress']
    RegistrantCity = lastdiclist['RegistrantCity']
    RegistrantZipCode = lastdiclist['RegistrantZipCode']
    RegistrantCountry = lastdiclist['RegistrantCountry']
    RegistrantPhoneCountryCode = lastdiclist['RegistrantPhoneCountryCode']
    RegistrantPhoneCityCode = lastdiclist['RegistrantPhoneCityCode']
    RegistrantPhoneNumber = lastdiclist['RegistrantPhoneNumber']
    AdminNicHandle = lastdiclist['AdminNicHandle']
    TechnicalNicHandle = lastdiclist['TechnicalNicHandle']
    ZoneNicHandle = lastdiclist['ZoneNicHandle']
    NS1 = lastdiclist['NS1']
    NS2 = lastdiclist['NS2']
    NS3 = lastdiclist['NS3']
    url = f'https://domains.livedns.co.il/API/DomainsAPI.asmx/NewDomain?'
    lasturl = f'{url}UserName={UserName}&Password={Password}&DomainName={validDomain}RegistrantName={RegistrantName}&RegistrantEmail={RegistrantEmail}&RegistrantAddress={RegistrantAddress}&RegistrantCity={RegistrantCity}&RegistrantZipCode={RegistrantZipCode}&RegistrantCountry={RegistrantCountry}&RegistrantPhoneCountryCode={RegistrantPhoneCountryCode}&RegistrantPhoneCityCode={RegistrantPhoneCityCode}&RegisrantPhoneNumber={RegistrantPhoneNumber}&AdminNicHandle={AdminNicHandle}&TechnicalNicHandle={TechnicalNicHandle}&ZoneNicHandle={ZoneNicHandle}&NS1={NS1}&NS2={NS2}&NS3={NS3}'
    return lasturl
# define a function that make a url for request and send post request to get expiry date and convert the xml result to json
def getexpiresdate(validDomain, getset):
    lastdiclist = getset
    WhoApi = lastdiclist['wxakey']
    url = f'https://www.whoisxmlapi.com/whoisserver/WhoisService?'
    apiurl = f'{url}apiKey={WhoApi}&domainName={validDomain}&outputFormat=JSON&ignoreRawTexts=1'
    request = requests.get(apiurl)
    results = request.json()
    if 'expiresDate' in results['WhoisRecord']['registryData'].keys():
        edate = results['WhoisRecord']['registryData']['expiresDate']
        return edate
    elif 'dataError' in results['WhoisRecord']['registryData'].keys():
        print('domain is available for purchase now! restart the program')
        main()
# Define function that calulcate the date and add more 90 days and 1 second for last date and return the total seconds until the date purchase
def cpdate(validDate):
    date = validDate
    today = datetime.today()
    dt = datetime.strptime(date,'%d-%m-%Y')
    ddelay = timedelta(days=90, seconds=1)
    ldate = dt + ddelay
    print('This Domain will be Available at: ' + str(ldate))
    cdate = ldate - today
    tsec = (cdate.total_seconds())
    return tsec
# define the last function that buy the domain
def domainbuy(lurl):
    lurl = lurl
    request = requests.get(lurl)
    result = request.text
    return result
# define main function that make everything complete
def main():
    print("""
                                      $$\      $$\                       $$\                         
                                      $$$\    $$$ |                      $$ |                        
         $$$$$$$\  $$$$$$\   $$$$$$\  $$$$\  $$$$ | $$$$$$\  $$$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  
        $$  _____|$$  __$$\ $$  __$$\ $$\$$\$$ $$ |$$  __$$\ $$  __$$\ \_$$  _|  $$  __$$\ $$  __$$\ 
        \$$$$$$\  $$$$$$$$ |$$ /  $$ |$$ \$$$  $$ |$$$$$$$$ |$$ |  $$ |  $$ |    $$ /  $$ |$$ |  \__|
         \____$$\ $$   ____|$$ |  $$ |$$ |\$  /$$ |$$   ____|$$ |  $$ |  $$ |$$\ $$ |  $$ |$$ |      
        $$$$$$$  |\$$$$$$$\ \$$$$$$  |$$ | \_/ $$ |\$$$$$$$\ $$ |  $$ |  \$$$$  |\$$$$$$  |$$ |      
        \_______/  \_______| \______/ \__|     \__| \_______|\__|  \__|   \____/  \______/ \__|      
        
                ______                      _         _   _             _            
                |  _  \                    (_)       | | | |           | |           
                | | | |___  _ __ ___   __ _ _ _ __   | |_| |_   _ _ __ | |_ ___ _ __ 
                | | | / _ \| '_ ` _ \ / _` | | '_ \  |  _  | | | | '_ \| __/ _ \ '__|
                | |/ / (_) | | | | | | (_| | | | | | | | | | |_| | | | | ||  __/ |   
                |___/ \___/|_| |_| |_|\__,_|_|_| |_| \_| |_/\__,_|_| |_|\__\___|_|   
                                                                             
         """)
    print('Hello and Welcome to seoMentor Domain Back Order System')
    getset = getSettingsFromFile()
    validDomain = askfordomain()
    validDate = getexpiresdate(validDomain, getset)
    datesec = cpdate(validDate)
    lurl = makelasturl(validDomain, getset)
    vask = input(f'Are you want to Schedule Purchase? write "yes" or "not": ')
    if 'yes' in vask:
        print('Schedule a purchase, please dont close me.')
        d = datesec
        time.sleep(d)
        domainbuy(lurl)
        if 'Success' in domainbuy(lurl):
            print('Purchase Success')
        elif 'Specified domain is unavailable for registration' in domainbuy(lurl):
            print('Purchase failed, sending more request in 3 seconds')
            time.sleep(3)
            domainbuy(lurl)
    else:
        exit()
if __name__ == "__main__":
    main()

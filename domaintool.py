import requests
import time
from datetime import datetime
from datetime import timedelta
# set a variable for setting.txt
settingsFile = 'settings.txt'
# open the file in read mode
f = open(settingsFile, 'r')
#ask which domain the user want to buy
def askfordomain():
    ask = input('Which Domain You want to Hunt?: ')
    DomainName = ask
    return DomainName
# define a function that handle the setting and make setlist dict with all details
def getSettingsFromFile():
    # save settings value into fileContent variable
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
def makelasturl():
    lastdiclist = getSettingsFromFile()
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
    lasturl = f'{url}UserName={UserName}&Password={Password}&DomainName={askfordomain()}RegistrantName={RegistrantName}&RegistrantEmail={RegistrantEmail}&RegistrantAddress={RegistrantAddress}&RegistrantCity={RegistrantCity}&RegistrantZipCode={RegistrantZipCode}&RegistrantCountry={RegistrantCountry}&RegistrantPhoneCountryCode={RegistrantPhoneCountryCode}&RegistrantPhoneCityCode={RegistrantPhoneCityCode}&RegisrantPhoneNumber={RegistrantPhoneNumber}&AdminNicHandle={AdminNicHandle}&TechnicalNicHandle={TechnicalNicHandle}&ZoneNicHandle={ZoneNicHandle}&NS1={NS1}&NS2={NS2}&NS3={NS3}'
    return lasturl
# define a function that make a url for request and send post request to get expiry date and convert the xml result to json
def getexpiresdate():
    lastdiclist = getSettingsFromFile()
    WhoApi = lastdiclist['wxakey']
    url = f'https://www.whoisxmlapi.com/whoisserver/WhoisService?'
    apiurl = f'{url}apiKey={WhoApi}&domainName={askfordomain()}&outputFormat=JSON&ignoreRawTexts=1'
    request = requests.get(apiurl)
    results = request.json()
    if 'expiresDate' in results['WhoisRecord']['registryData'].keys():
        edate = results['WhoisRecord']['registryData']['expiresDate']
        return edate
    elif 'dataError' in results['WhoisRecord']['registryData'].keys():
        print('domain is available for purchase now! restart the program')
# Define function that calulcate the date and add more 90 days and 1 second for last date and return the total seconds until the date purchase
def cpdate():
    date = getexpiresdate()
    today = datetime.today()
    dt = datetime.strptime(date,'%d-%m-%Y')
    ddelay = timedelta(days=90, seconds=1)
    ldate = dt + ddelay
    cdate = ldate - today
    tsec = (cdate.total_seconds())
    return tsec
# define the last function that buy the domain
def domainbuy():
    lurl = makelasturl()
    request = requests.get(lurl)
    result = request.text
    return result
# define main function that make everything complete
def main():
    if True:
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
    getSettingsFromFile()
    makelasturl()
    askfordomain()
    getexpiresdate()
    print('This Domain will be Available at: ' + getexpiresdate())
    vask = input(f'Are you want to Schedule Purchase? write "yes" or "not"')
    if 'yes' in vask:
        d = cpdate()
        time.sleep(d)
        domainbuy()
        if 'Success' in domainbuy():
            print('Purchase Success')
        elif 'Specified domain is unavailable for registration' in domainbuy():
            print('Purchase failed, sending more request in 3 seconds')
            time.sleep(3)
            domainbuy()
    else:
        exit()
if __name__ == "__main__":
    main()

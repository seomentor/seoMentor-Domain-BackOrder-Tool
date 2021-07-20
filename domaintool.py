import requests
# Welcome Message
print('Hello and Welcome to seoMentor Domain Purchase Automation Tool')

# ask which domain he want to buy
domainBuy = input('Please Enter Domain Name: ')
def domaincheck(domainBuy):
    while '.co.il' not in domainBuy:
        domainBuy = str(input('please enter a valid input: '))
        if '.co.il' in domainBuy:
            print('Succes')
domaincheck(domainBuy)

# Validation Question Before Start Whois
qCheck = input('ARE YOU READY TO FUCK THEM ALL?!?!: Y/N')
def questioncheck(qCheck):
    while 'y' not in qCheck:
        qCheck = str(input('PLEASE SAY YES!!!: Y/N'))
    else:
        print('Start')
questioncheck(qCheck)

# Check the domain

# Gathering LiveDNS DATA
#now in test mode
UserName = 'sapirzuberismg@gmail.com'
Password = '32423432'
DomainName = 'admin.co.il'
RegistrationPeriod = '1'
RegistrantName = 'sapir'
RegistrantEmail = 'zuberi'
RegistrantAddress = 'avraham yafe 11'
RegistrantCity = 'holon'
RegistrantZipCode = '324234'
RegistrantCountry = 'IL'
RegistrantPhoneCountryCode = '972'
RegistrantPhoneCityCode = '03'
RegistrantPhoneNumber = '559282887'
AdminNicHandle = 'shay'
TechnicalNicHandle = 'adjkhas'
ZoneNicHandle = 'asdasd'
NS1 = 'asdasd'
NS2 = 'asdasd'
NS3 = 'asdasd'

url = f'https://domains.livedns.co.il/API/DomainsAPI.asmx/NewDomain?UserName={user}&Password=sapir0072k&DomainName={domain}&RegistrationPeriod=1&RegistrantName=sapir%20zuberi&RegistrantEmail=sapirzuberismg@gmail.com&RegistrantAddress=trompeldor%2018&RegistrantCity=hadera&RegistrantZipCode=3828022&RegistrantCountry=il&RegistrantPhoneCountryCode=972&RegistrantPhoneCityCode=055&RegistrantPhoneNumber=9807615&AdminNicHandle=LD-SZ4136-IL&TechnicalNicHandle=LD-SZ4136-IL&ZoneNicHandle=LD-SZ4136-IL&NS1=ns1.upress.io&NS2=ns2.upress.io&NS3=ns3.upress.io'

def buydomain():
    response = requests.post(url, data)
    pdata = response.json()
    print(response.status_code, response.reason, pdata)

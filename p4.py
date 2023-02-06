from bs4 import BeautifulSoup
# from lxml import etree
import requests
import re
from time import sleep
from datetime import date

def getVpn(lang):
    
   
    
    proxie={
        'http':'192.168.1.52:3000',
        'https':'192.168.1.52:3000'
    }
    
     # proxie can add in request.get('url',proxies)
     
    e=requests.get(f'https://www.vpngate.net/{lang}/')
    html=BeautifulSoup(e.content,"html.parser")


    # dom=etree.HTML(str(html))

    p=html.findAll('span')


    ii=0
    listt=[]
    listadd=[]

    for i in p:
            try:
            # print(i.text)
            # print(i)
            
                if i.text.find('opengw.net'):
                    ii=ii+1
                    # print(f"{ii} = > {i.text} ")
                    # print(p.index(i.text))
                    listt.append(i.text)
                    
                    
            except :
                print("cant ")
    # print(dom.xpath('//*[@id="vg_hosts_table_id"]/tbody/tr[3]/td[8]/p'))

    for i in listt:
        # if i.find('vpn'):
            # t=i.find('opengw.net')
            # print(i[t])
            try:
                found=re.search('vpn(.+?).opengw.net',i)
                f=re.search('opengw.net:(....+?)',i)
                ffff=re.search('opengw.net:(...+?)',i)
                foundd=''
                if found:
                    
                    foundd=found.group(1)
                    
                    
                if f:
                    
                    ff=f.group(1)
                    # print(ff)
                    print(f"vpn{foundd}.opengw.net:{ff}\n")
                    listadd.append("vpn"+foundd+".opengw.net:"+ff)
                
                
                # port3=ffff.group(1)
                # print(type(port3))
                
                # if port3=='990':
                #         fo=ffff
                #         print(fo)
                    
            except :
                print('')
    return listadd
            
def createOrremoveDate():
    with open('vpn.txt','w') as f:
        f.write('')
        f.close()
    

createOrremoveDate()

listt=['ja','en']
listdata=[]

# getVpn('en')


for i in listt:
    ii=getVpn(i)
    listdata.append(list(ii))
    sleep(3)
# print(listdata)

index=0    

# write to text 
for x in listdata:
    
        with open('vpn.txt','a') as f:
            f.write('\n\n\n export: '+str(date.today())+"  "+listt[index] )
            f.write('\n')
            ii=0
      
            for i in x:
                ii=ii+1
                x.pop(ii)
                f.write(i)
                f.write('\n')
        index=+1
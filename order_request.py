import json
import datetime


def extract_json(a):
    with open(str(a)) as f:
        return json.load(f)
data_order=extract_json("order.json")
data_order_request=extract_json("order_request.json")
data_company=extract_json("company.json")
l=[]
dic_company_city={}
for i in data_company:
    dic_company_city[i['id']]=i.get('city')


def get_stat_order_request(city,start_time,end_time):
    l1=[]
    temp_di={}
    for i in data_order_request:
        if(dic_company_city[i['cid']].lower() == city and start_time <= i['createdOn'] <= end_time ):
            temp_di[i['id']] =i.get('status')
            l1.append(i.get('status'))
    print(temp_di)
    
    return l1.count('submitted'),l1.count('unattended')
if __name__== "__main__":
    city=input("enter the city name:").lower()
    date = input("enter the date in yy/mm/date : ").split("/")
    y=int(date[0])
    m=int(date[1])
    d=int(date[2])
    
    start_time = datetime.datetime(y,m,d,int(0),int(0),int(0)).timestamp()
    end_time = datetime.datetime(y,m,d,23,59,59).timestamp()
    a,b =get_stat_order_request(city,int(start_time),int(end_time))
    print(f"no.of order requests submitted in  {city} on {date} is {a}" )
    print(f'no of order requests unattended in {city} on {date} is {a}')



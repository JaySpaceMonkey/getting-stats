import json
import datetime

def extract_json(a):
    with open(str(a)) as f:
        return json.load(f)


def has_city(i):
    if('city' in i.keys()):
        return True
    else:
        return False


def get_stat_order(city,start_time,end_time):
    temp_li=[]
    l1=[]
    temp_di={}
    reason_list=[]
    for i in data_order:
        if(has_city(i)):
            if(i['city'].lower() == city and start_time <= int(i['createdOn']) <= end_time):
                temp_li.append(i['status'])
                if(i['status']=='rejected'):
                    reason_list.append(i['cancelReason'])
        
    s= set(temp_li)
    for i in s:
        temp_di.update({str(i):temp_li.count(str(i))})
    temp_di['city']=city
    
    return temp_di,reason_list




if __name__== "__main__":
    city=input("enter the city name:").lower()
    date = input("enter the date in yy/mm/date : ").split("/")
    y=int(date[0])
    m=int(date[1])
    d=int(date[2])
    data_order=extract_json('order.json')
    data_company=extract_json('company.json')
    dic_company_city={}
    for i in data_company:
        dic_company_city[i['id']]=i.get('city')
    start_time = datetime.datetime(y,m,d,int(0),int(0),int(0)).timestamp()
    end_time = datetime.datetime(y,m,d,23,59,59).timestamp()
    l,r=get_stat_order(city,start_time,end_time)
    print(l)
    
    
    
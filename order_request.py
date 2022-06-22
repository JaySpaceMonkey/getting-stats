import json
import datetime
import argparse
import pandas as pd


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

def get_stat_order_request(city,pharma,start_time,end_time,avg):
    l1=[]
    temp_di={}
    for i in data_order_request:
        if(dic_company_city[i['cid']].lower() == city and pharma == i['cid']and start_time <= i['createdOn'] <= end_time ):
            temp_di[i['id']] =i.get('status')
            l1.append(i.get('status'))
    
    
    total_request_orders = len(l1)
    orders_attended = l1.count('submitted')
    business_lost = l1.count('unattended') * avg
    t ={'pharma_cid': pharma,'total':total_request_orders, 'attended' : orders_attended , 'lost': business_lost}
    
    return t
if __name__== "__main__":

    # city=input("enter the city name:").lower()
    # date = input("enter the date in yy/mm/date : ").split("/")
    avg_amt_lost= 500
    parser = argparse.ArgumentParser()

    parser.add_argument('--city', type = str ,required = True)
    parser.add_argument('--start_time', type = str ,required =True)
    parser.add_argument('--end_time', type = str )

    args = parser.parse_args()
    city = args.city
    date1 = args.start_time.split("/") 
    y, m, d = date1
    start_time = datetime.datetime(int(y),int(m),int(d),int(0),int(0),int(0)).timestamp()

    if(args.end_time):
        date2 = args.end_time.split("/")
        y,m,d = date2
        end_time = datetime.datetime(int(y),int(m),int(d),23,59,59).timestamp()
    else:
        date = args.start_time.split("/")
        y,m,d = date
        
        end_time = datetime.datetime(int(y),int(m),int(d),23,59,59).timestamp()
        
    lis_of_pharmas =[]
    for u in data_order_request:
        lis_of_pharmas.append(u['cid'])
    report =[]
    for pharma in lis_of_pharmas:
        report.append(get_stat_order_request(city,pharma,int(start_time),int(end_time),avg_amt_lost))
    #print(report)

    final_report = pd.DataFrame(report,columns =[ 'pharma_cid','total', 'attended', 'lost'])
    
    final_report.to_csv("report.csv")
    
    # print(f"no.of order requests submitted in  {city} on {date} is {a}" )
    # print(f'no of order requests unattended in {city} on {date} is {a}')



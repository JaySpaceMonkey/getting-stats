import json
import requests
from requests.structures import CaseInsensitiveDict
import argparse
import datetime

def get_from_payin(start,end):
    url = "https://api.pharmacyone.io/prod/rzp_transaction"
    headers = CaseInsensitiveDict()
    headers["session-token"] = "wantednote"
    skip = 0
    new_results = True
    while new_results:
        params_dict = {'skip' : str(skip), 'from' : str(start), 'to' : str(end)}
        response = requests.get(url, params=params_dict, headers=headers)
        
'''
#  get the data of(cid , amount , payment id , time )  


'''
#make network call to razorpay with(start , end)

def make_rp_out_call(start , end):
    razorpout_list = []
    skip = 0
    new_results = True
    url = "https://api.pharmacyone.io/prod/rzp_payout"
    headers = CaseInsensitiveDict()
    headers["session-token"] = "wantednote"
    while new_results: 
        params_dict = {'skip' : str(skip),'from' : str(start),'to' : str(end)}
        response = requests.get(url, params=params_dict, headers=headers)
        dict_data = response.json() 
        if 'data' in dict_data:
            new_results = dict_data.get("data").get("items", [])
        razorpout_list.extend(new_results)
        skip = int(skip) + 100
    razorpout_dict = {item['source']['notes']['id'] : item for item in razorpout_list if item.get('source') and item.get('source').get('notes') and item.get('source').get('notes').get('id')}
    for item in razorpout_dict:
        if razorpout_dict[item].get('source') and razorpout_dict[item].get('source').get('amount'):
            razorpout_dict[item]['source']['amount'] = (razorpout_dict[item].get('source').get('amount'))/100
    return razorpout_dict

# def make_network_call(start,end):
# amount in paise convert to rupees


# if in notes there is settlement then




#make network call to settlement 


#once getting the dict 

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_time",required=True)
    parser.add_argument("--end_time",required=True)
    
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

    print(make_rp_out_call(start_time , end_time))
    # d = razorpayout_dict(start , end)
    # for item in d:
    #     if(item['Cid'] and item['amount'])
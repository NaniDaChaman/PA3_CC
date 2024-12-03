import uuid
import json
import time
from kafka import KafkaProducer, KafkaConsumer
import numpy as np
from datetime import datetime,timedelta
import base64
import arima

try:
    consumer = KafkaConsumer(
        'controller',
        bootstrap_servers='172.16.2.137:30000',#could we try and init in
        #dynamically with env vars set by kubernetes
        auto_offset_reset='latest',
        enable_auto_commit=True,
        group_id=f'controller-group',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )
    print("Kafka consumer started, listening for inference results.")
    
 
except Exception as e : 
    print(f"Error making the Kafka consumer : {e}")

def discretize_consumer(consumer_horizon):
    arrivals_list=[]


start_time=None
n=0
arrival_list=[0]
forecast_list=[]
for message in consumer:
    data = message.value 
    time_now=datetime.fromisoformat(data['SentTime'])
    print("\nData from kafka : {data}\n")
    if n==0:
        start_time=time_now
    elif time_now>=start_time+timedelta(seconds=120):
        arrival_list.append(n)
        forecast_list=arima.get_prediction(arrival_list,10)
        print(f"\nnext 10 forecast is : \n{forecast_list}\n")
        #action=controller(forecast_list)
        n=0
        start_time=time_now
    else :
        n=n+1
    
    
        
    #arrivals_list.append(data['SentTime'])

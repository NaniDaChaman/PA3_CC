import numpy as np

def mmc(arrivals,queue,serving_time,time_horizon,servers):
    #there will be a part where we will load everything into the queue
    resp_time=[]
    for arr in arrivals : 
        jobs=np.ones(arr,1)@np.array([serving_time,1])
        #jobs=np.fill(arr,2,value=[serving_time,1])#check this function
        queue=queue+np.ones(queue.shape[0],1)@np.array([0,1])
        queue=np.concatenate(queue,jobs)#check this function

    #there will be a part where we will load stuff out of the queue and into the server
    return avg_response_time,queue_length
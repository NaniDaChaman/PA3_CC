import numpy as np

def mmc(arrivals,queue,serving_time,time_horizon,servers,time_delta):
    #there will be a part where we will load everything into the queue
    resp_time=[]
    for arr in arrivals : 
        #all of our arrivals are gonna be loaded into the queue for the time horizon
        jobs=np.ones(arr,1)@np.array([serving_time,1])
        #jobs=np.fill(arr,2,value=[serving_time,1])#check this function
        queue=queue+np.ones(queue.shape[0],1)@np.array([0,time_delta])
        queue=np.concatenate(queue,jobs)#check this function

    for i in time_horizon :
        #time_passed=min(time_delta,0) 
        temp=time_delta
        while temp>0:
            s_next=np.min_index(servers)#find the function for this
            temp=max(temp-servers[s_next],0)#find the function for this
            servers=servers-servers[s_next]
            #assume that it takes 1 second to load every server
            for s in servers:
                if s==0:
                    top=queue[0]
                    s=top[1]
                    resp_time.append(np.sum(top))
    #there will be a part where we will load stuff out of the queue and into the server
    avg_response_time=np.average(resp_time)
    queue_length=queue_length.shape[0]
    return avg_response_time,queue_length
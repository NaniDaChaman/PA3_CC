import numpy as np

def mmc(arrivals,queue,serving_time,time_horizon,servers,time_delta):
    #there will be a part where we will load everything into the queue
    resp_time=[0]
    for arr in arrivals : 
        #all of our arrivals are gonna be loaded into the queue for the time horizon
        if arr>0:
            init_job=np.array([serving_time,0])
            jobs_array=np.array([init_job]*int(arr))
            print(f"Jobs array looks like : {jobs_array} and dimensions are {np.array(jobs_array).shape}")
            #print(f"Jobs array first row: {jobs_array[0]}")
            jobs=jobs_array
            #print(f"Jobs for arrivals are {jobs}")
            queue=np.vstack((queue,jobs))
        #jobs=np.fill(arr,2,value=[serving_time,1])#check this function
        time_added_per=np.array([0,time_delta])
        time_added=np.array([time_added_per] * queue.shape[0])
        queue=queue+time_added
        #check this function
        #print(f"Updated queue is {queue}, queues dims are : {queue.shape}")#shape is a tuple

    for i in range(time_horizon) :
        #time_passed=min(time_delta,0) 
        print(f"\n\nAt {i}th time horizon is \n\n")
        print(f"\nServer is {servers}\n")
        #print(f"\nQueue is : {queue}\n")
        temp=time_delta
        while temp>0:
            s_next=np.argmin(servers)#find the function for this
            temp=max(temp-servers[s_next],0)#find the function for this
            servers=servers-servers[s_next]
            print(f"\nServer at temp are {servers}\n")
            #assume that it takes 1 second to load every server
            for i,s in enumerate(servers):
                if s==0:
                    if queue.size==0:
                        avg_response_time=np.average(resp_time)
                        queue_length=0
                        return avg_response_time,queue_length
                    top=queue[0]
                    #rint(top)
                    #print(f"Top is {top}")
                    servers[i]=queue[0,0]
                    resp_time.append(np.sum(top))
                    queue=np.delete(queue,0,axis=0)#what if queue is empty ?
    #there will be a part where we will load stuff out of the queue and into the server
    avg_response_time=np.average(resp_time)
    queue_length=queue.shape[0]
    return avg_response_time,queue_length

def test_mmc(c,scl,th,st):
    time_horizon=th
    arrivals=np.rint(np.random.exponential(scale=scl,size=time_horizon))
    print(f"\n\n Arrivals created : {arrivals}\n\n")
    queue=np.array([[0,0],[0,0]])
    serving_time=5#np.random.randint(1,st)
    print(f"\n\n Serving time created : {serving_time}\n\n")
    servers=np.random.randint(0,serving_time,c)
    print(f"\n\n Servers created : {servers}\n\n")
    time_delta=np.random.randint(scl,scl+10)
    print(f"\n\n Time delata is : {time_delta}\n\n")
    print()
    avg_rt,ql=mmc(arrivals,queue,serving_time,time_horizon,servers,time_delta)
    print(f'\n\nAverage Response Time is : {avg_rt}\n\nQueue Lenght is : {ql}\n\n')

def main():
    c=5
    scl=10
    th=50
    st=7
    test_mmc(c,scl,th,st)

if __name__ == '__main__':
    main()
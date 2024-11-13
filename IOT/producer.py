import os   # need this for popen
import time # for sleep
from kafka import KafkaProducer  # producer of events

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the producer
# (you will need to change this to your bootstrap server's IP addr)
producer = KafkaProducer (bootstrap_servers="10.82.35.234:30000", 
                                          acks=1)  # wait for leader to write to log

# say we send the contents 100 times after a sleep of 1 sec in between
for i in range (100):
    
    # get the output of the top command
    process = os.popen ("top -n 1 -b")

    # read the contents that we wish to send as topic content
    contents = process.read ()

    # send the contents under topic utilizations. Note that it expects
    # the contents in bytes so we convert it to bytes.
    #
    # Note that here I am not serializing the contents into JSON or anything
    # as such but just taking the output as received and sending it as bytes
    # You will need to modify it to send a JSON structure, say something
    # like <timestamp, contents of top>
    #
    producer.send ("utilizations", value=bytes (contents, 'ascii'))
    producer.flush ()   # try to empty the sending buffer

    # sleep a second
    time.sleep (1)

# we are done
producer.close ()
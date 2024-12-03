from kubernetes import client, config

try :
    config.load_incluster_config()
    print("Loaded local env")
except Exception as e:
    print(f"couldn't load local env :{e}")

try :
    config.load_incluster_config()
    print("Loaded remote env")
except Exception as e:
    print(f"couldn't load remote env :{e}")
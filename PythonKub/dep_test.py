# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Creates a deployment using AppsV1Api from file nginx-deployment.yaml.
"""

from os import path

import yaml

from kubernetes import client, config


def create_deployment():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), "nginx-deployment.yaml")) as f:
        dep = yaml.safe_load(f)#yaml thing not a kube thing
        k8s_apps_v1 = client.AppsV1Api()
        print("og replicas : ")
        print(dep['spec']['replicas'])
        dep['spec']['replicas']=3# you can set it up when it doesn't exist but you cant' change it
        #when it already exists might need to look into scale api
        print(f"changed replicas : {dep['spec']['replicas']}") #we can change a file stuff before 
        #deploying it 
        resp = k8s_apps_v1.create_namespaced_deployment(
            body=dep, namespace="team13")
        print(f"Deployment created. Status='{resp.metadata.name}'")
        return (resp.metadata.name,3)

def scale_deployment(name,replicas) :
    scale_request =client.V1ScaleSpec(replicas=replicas)
    client.patch_namespaced_deployment_scale("team13",name , scale_request)

if __name__ == '__main__':
    name='nginx-deployment'
    replicas=5
    try:
        create_deployment()
    except Exception as e:
        print(f"Creation exception : {e}")
    try:
        scale_deployment(name,replicas)
    except Exception as e:
        print(f"Creation exception : {e}")
    
    

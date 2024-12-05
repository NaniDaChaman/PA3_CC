from flask import Flask,jsonify,request,url_for,render_template,redirect,Response
import json
import deploy

app =Flask(__name__)
@app.route("/scale",methods=['POST'])
def scale_up():
    r=request
    response=json.loads(r.data)
    name=response['name']
    replicas=response['replicas']
    scale=deploy.scale_deployment(name,replicas)
    try :
        name_deployment=scale.metadata.name
        new_count=scale.spec.replicas
        old_count=scale.status.replicas
        data={"name":name_deployment,"old_count":old_count,"new_count":new_count}
        return jsonify(data)
    except Exception as e :
        print(f'Error occured when scaling the resource : {name}')
        print(e)
        return jsonify({}),500

@app.route("/scale_test/<string:name>/<int:replicas>",methods=['GET'])
def scale_up_test(name,replicas):
    #r=request
    #response=json.loads(r.data)
    #name=response['name']
    #replicas=response['replicas']
    response=deploy.test(name,replicas)
    data={'response':response}
    return jsonify(data),200

if __name__=="__main__":
    app.run(host = '0.0.0.0',port =5010)



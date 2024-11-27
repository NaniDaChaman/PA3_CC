from flask import Flask,jsonify,request,url_for,render_template,redirect,Response
import model as md
import numpy as np
#import cv2
#import jsonpickle


app= Flask(__name__)
@app.route("/get_pred/<filename>")
def get_pred(filename):
    prediction = md.model_pred(md.model_prob(filename))
    data={"Prediction" : prediction}
    return jsonify(data)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/handle_form",methods=["POST"])
def handle_form():
    #return "You did it"
    ufile=request.form['image']
    #print(ufile)
   
    #print(ufile.filename)
    
    return redirect(url_for("get_pred",filename=ufile))

# @app.route('/api/test', methods=['POST'])
# def test():
#     r = request
#     # convert string of image data to uint8
#     nparr = np.fromstring(r.data, np.uint8)
#     # decode image
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

#     # do some fancy processing here....

#     # build a response dict to send back to client
#     response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
#                 }
#     # encode response using jsonpickle
#     response_pickled = jsonpickle.encode(response)

#     return Response(response=response_pickled, status=200, mimetype="application/json")


if __name__=="__main__":
    md.load_model()
    #url_for("hello_world")
    app.run(host = '0.0.0.0',port =5000)
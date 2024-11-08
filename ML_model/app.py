from flask import Flask,jsonify,request,url_for,render_template,redirect
import model as md



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


if __name__=="__main__":
    md.load_model()
    #url_for("hello_world")
    app.run(host = '0.0.0.0',port =5000)
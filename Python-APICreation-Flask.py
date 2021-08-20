import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "WELCOME TO FLASK please use correct endpoint for ML
	example --  /ml/LR for linear and /ml/LOGIT for logistic"





@app.route('/ml/LR', methods=['GET'])
def home():
    ln = pkl.load(mdl.pkl)
	output = ln.predict(<>)
	print(output)


@app.route('/ml/LOGIT', methods=['GET'])
def home():
    logit = pkl.load(logisticregression.pkl)
	output = logit.predict(<>)
	print(output)




app.run()
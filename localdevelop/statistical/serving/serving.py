import joblib
import pandas as pd
import json
import numpy as np
from flask import Flask, jsonify, request

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = NpEncoder

@app.route("/", methods=['GET', 'POST'])
def call_home(request = request):
    print(request.values)
    return "SERVER IS RUNNING!"

@app.route("/modelo01", methods=['POST'])
def call_modelo01(request = request):
    print(request.values)

    json_ = request.json
    campos = pd.DataFrame(json_)

    if campos.shape[0] == 0:
        return "Dados de chamada da API estão incorretos.", 400

    for col in modelo01.independentcols:
        if col not in campos.columns:
            campos[col] = 0
    x = campos[modelo01.independentcols]

    prediction = modelo01.predict(x)
    predict_proba = modelo01.predict_proba(x)

    return jsonify({'prediction': list(prediction),
                    'proba': list(predict_proba)})

if __name__ == '__main__':
    modelo01 = joblib.load( '../../../datasets/statistical/modelo01.joblib')
    modelo02 = joblib.load( '../../../datasets/statistical/modelo02.joblib')
    # app.run(port=8080, host = '0.0.0.0')
    app.run(port=8080)
    # pass



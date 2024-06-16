from flask import Flask,request,jsonify
from google.cloud import bigquery
import os

app = Flask(__name__)

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-file.json"
# client = bigquery.Client()

# @app.route('/query',methods=['POST'])
# def query_bigquery():
#     query = request.json['query']
#     query_job = client.query(query)
#
#     results = query_job.result()
#     rows = [dict(row) for row in results]
#
#     return jsonify(rows)

@app.route("/")
def hello_world():
    return "Hello, World"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)

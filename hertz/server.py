import json
from flask import Flask, request, jsonify
from hertz import queries

app = Flask(__name__)

@app.route('/')
def index():
  return('GOOD')

@app.route('/health')
def healthCheck():
  return('OK')

# Main way in for data collection, receives a JSON-serialised hash of the daemon's
# collection method, but is currently not checked against a schema
@app.route('/api/v1.0/submit/<job_id>', methods=["POST"])
def submit(job_id):
  data_dict = request.get_data()
  data = json.loads(data_dict)
  queries.add_data(job_id,data)
  return "Thanks!"

# Currently this is a fucking mess. Returns an array of metrics with no keys
@app.route('/api/v1.0/results/<job_id>', methods=["GET"])
def results(job_id):
  data = queries.return_data(job_id)
  return str(data)



if __name__ == '__main__':
  app.run(debug=True)
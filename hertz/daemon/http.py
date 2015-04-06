import requests
import json
#
# hertz/daemon/http.py
#
# This submodule contains functions for communication with the management server via HTTP(S)
#

# submit() - Submits data to the master's API
#
# Arguments:
#   'job_id' [string] - Unique identifier of job data should be stored in
#   'data'   [dict]   - Key-value metric data

# Returns:
#   [boolean] - Success of submission
#
def submit(job_id,data):
  try:
    payload = json.dumps(data)
    url = 'http://localhost:5000'
    route = '/api/v1.0/submit/%s' % job_id
    submission = requests.post(url + route, data=payload)
    if submission.text == "Thanks!":
      print "Success!"
      return True
    else:
      print "Fail!"
      return False
  except requests.ConnectionError:
    print "Unable to connect to master server"

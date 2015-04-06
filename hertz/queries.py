from hertz.models import *

db.create_all()

def add_job(jobname):
  db.session.add(Job(jobname))
  db.session.commit()


def add_data(jobname,data):
  if type(data) is list:
    for datapoint in data:
      db.session.add(Data(jobname,datapoint))
  else:
    db.session.add(Data(jobname,data))

  db.session.commit()


def return_jobs():
  return Jobs.query.all()


def return_data(jobname):
  response = []
  dataset = Data.query.filter_by(job_id=jobname)
  for datapoint in dataset:
    response.append(datapoint)

  return response

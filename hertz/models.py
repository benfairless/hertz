from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
db = SQLAlchemy(app)


class Jobs(db.Model):
  id = db.Column(db.Integer)
  name = db.Column(db.String(80), primary_key=True)
  baseline = db.Column(db.Boolean)

  def __init__(self,name,baseline=False):
    self.name = name
    self.baseline = baseline

  def __repr__(self):
    return 'Job %s' % self.name


class Data(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  job_id = db.Column(db.String(80), db.ForeignKey('jobs.name'))
  hostname = db.Column(db.String(120))
  timestamp = db.Column(db.String(80))
  aggregate = db.Column(db.Integer)
  mem_swpd = db.Column(db.Integer)
  mem_free = db.Column(db.Integer)
  mem_buff = db.Column(db.Integer)
  mem_cache = db.Column(db.Integer)
  swap_in = db.Column(db.Integer)
  swap_out = db.Column(db.Integer)
  blocks_in = db.Column(db.Integer)
  blocks_out = db.Column(db.Integer)
  cpu_int = db.Column(db.Integer)
  cpu_cs = db.Column(db.Integer)
  cpu_usr = db.Column(db.Integer)
  cpu_sys = db.Column(db.Integer)
  cpu_idle = db.Column(db.Integer)
  cpu_wait = db.Column(db.Integer)
  proc_run = db.Column(db.Integer)
  proc_blk = db.Column(db.Integer)

  def __init__(self,job_id,data):
    self.job_id = job_id
    self.hostname = data['hostname']
    self.timestamp = data['time']
    self.aggregate = data['aggregate']
    self.mem_swpd = data['mem_swpd']
    self.mem_free = data['mem_free']
    self.mem_buff = data['mem_buff']
    self.mem_cache = data['mem_cache']
    self.swap_in = data['swap_in']
    self.swap_out = data['swap_out']
    self.blocks_in = data['blocks_in']
    self.blocks_out = data['blocks_out']
    self.cpu_int = data['cpu_int']
    self.cpu_cs = data['cpu_cs']
    self.cpu_usr = data['cpu_usr']
    self.cpu_sys = data['cpu_sys']
    self.cpu_idle = data['cpu_idle']
    self.cpu_wait = data['cpu_wait']
    self.proc_run = data['proc_run']
    self.proc_blk = data['proc_blk']

  def __repr__(self):
    return '%s %s %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i' % (
      self.hostname,
      self.timestamp,
      self.aggregate,
      self.mem_swpd,
      self.mem_free,
      self.mem_buff,
      self.mem_cache,
      self.swap_in,
      self.swap_out,
      self.blocks_in,
      self.blocks_out,
      self.cpu_int,
      self.cpu_cs,
      self.cpu_usr,
      self.cpu_sys,
      self.cpu_idle,
      self.cpu_wait,
      self.proc_run,
      self.proc_blk
    )
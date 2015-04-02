import sys
import os
import subprocess

# get() - Collect metrics from kernel via vmstat
#
# Arguments:
#   'aggregate' [integer] - The amount of seconds over which to collect data
#                           Defaults to 15
# Returns:
#   [dict] - All metrics collected within the aggregation period in key-value pairs
#
def get(aggregate=15):
  try:
    vmstat = subprocess.check_output(['vmstat','-S','K','-nt',str(aggregate),'2']).split('\n')[3].split()
    return {
        'hostname': os.environ['HOSTNAME'],
        'proc_run': int(vmstat[0]),
        'proc_blk': int(vmstat[1]),
        'mem_swpd': int(vmstat[2]),
        'mem_free': int(vmstat[3]),
        'mem_buff': int(vmstat[4]),
        'mem_cache': int(vmstat[5]),
        'swap_in': int(vmstat[6]),
        'swap_out': int(vmstat[7]),
        'blocks_in': int(vmstat[8]),
        'blocks_out': int(vmstat[9]),
        'cpu_int': int(vmstat[10]),
        'cpu_cs': int(vmstat[11]),
        'cpu_usr': int(vmstat[12]),
        'cpu_sys': int(vmstat[13]),
        'cpu_idle': int(vmstat[14]),
        'cpu_wait': int(vmstat[15]),
        'date': str(vmstat[17]),
        'time': str(vmstat[18]),
        'aggregate': aggregate,
      }
  except subprocess.CalledProcessError as e:
    print 'Unable to start vmstat. Command exited with status ' + str(e.returncode)
    sys.exit(1)
  except OSError as e:
    if e.errno == 2:
      print 'Unable to find vmstat binary in $PATH'
    else:
      print e.stderror
    sys.exit(1)


# buffered_get() - Creates a rate buffer by only outputting data collections at a specified rate
#
# Arguments:
#   output    [integer] - Time in seconds the buffer should hold on to data before releasing it
#                         Defaults to 60
#   aggregate [integer] - The amount of seconds in which an individual data collection should be performed
#                         Defaults to 15
#
# Returns:
#   [array] - Array of dict objects containing data collection
#
def buffered_get(time=60,aggregate=15):
  # If aggregate time is longer than specified output rate, output each collection
  if aggregate > time:
    total = 1
  else:
    total = time / aggregate

  count = 0
  buff = []
  while count < total:
    data.append(get(aggregate))
    count += 1

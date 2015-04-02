#!/usr/bin/env python
import sys
import os
import subprocess

# Collect metrics from kernel via vmstat
# poll is the amount of seconds over which to aggregate data
def collection(poll=10):
  try:
    data = subprocess.check_output(['vmstat','-S','K','-nt',str(poll),'2']).split('\n')[2].split()
    return {
        'proc_run': int(data[0]),
        'proc_blk': int(data[1]),
        'mem_swpd': int(data[2]),
        'mem_free': int(data[3]),
        'mem_buff': int(data[4]),
        'mem_cache': int(data[5]),
        'swap_in': int(data[6]),
        'swap_out': int(data[7]),
        'blocks_in': int(data[8]),
        'blocks_out': int(data[9]),
        'cpu_int': int(data[10]),
        'cpu_cs': int(data[11]),
        'cpu_usr': int(data[12]),
        'cpu_sys': int(data[13]),
        'cpu_idle': int(data[14]),
        'cpu_wait': int(data[15]),
        'date': str(data[17]),
        'time': str(data[18]),
        'poll_freq': poll,
      }
  except subprocess.CalledProcessError as e:
    print 'Unable to start vmstat. Command exited with status ' + str(e.returncode)
    sys.exit(1)
  except OSError as e:
    if e.errno == 2:
      print 'Unable to find vmstat binary in $PATH'
      sys.exit(1)
    else:
      print e.stderror
      sys.exit(1)




def tmpwrite():
  data = str(collection(15)) + '\n'
  with open('output.log','a',1) as fyle:
    fyle.write(data)

def main_loop():
  print "Starting monitoring..."
  while 1:
    tmpwrite()

if __name__ == '__main__':
  try:
    main_loop()
  except KeyboardInterrupt:
    print >> sys.stderr, '\nExiting by user request.\n'
    sys.exit(0)

#print collection(1)
#tmpwrite()
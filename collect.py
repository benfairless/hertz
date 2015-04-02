#!/usr/bin/env python
import sys
import os
import subprocess

# Collect metrics from kernel via vmstat
# poll is the amount of seconds over which to aggregate data
def collection(poll=10):
  try:
    vmstat = subprocess.check_output(['vmstat','-S','K','-nt',str(poll),'2']).split('\n')[3].split()
    return {
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
    # tmpwrite()
    print collection(5)

if __name__ == '__main__':
  try:
    main_loop()
  except KeyboardInterrupt:
    print >> sys.stderr, '\nExiting by user request.\n'
    sys.exit(0)

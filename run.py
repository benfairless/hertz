#!/usr/bin/env python
from hertz.daemon import collection
import ConfigParser

config = ConfigParser.SafeConfigParser()
config.read('hertzd.conf')
_buffer = config.get('Agent','buffer')

print collection.get(2)
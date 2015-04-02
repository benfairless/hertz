#!/usr/bin/env python
import sys
from hertz.daemon import collection

print collection.buffered_data(2)
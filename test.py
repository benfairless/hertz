#!/usr/bin/env python
from hertz.daemon import http, collection

while True:
  data = collection.get(15)
  http.submit('job1',data)
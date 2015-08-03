#!/usr/bin/env python
from epc.server import EPCServer

server = EPCServer(('localhost', 0))

@server.register_function
def echo(*a):
  return a

server.print_port()
server.serve_forever()

#!/usr/bin/env python3
from epc.server import EPCServer
import boto3
import botocore

server = EPCServer(('localhost', 0))
@server.register_function
def cfValidate(*template):
    ret = "Template Passed"
    session = boto3.Session(profile_name='dev', region_name='us-east-1')
    client = session.client('cloudformation')
    f = ''.join(template)
    try:
        client.validate_template(TemplateBody=f)
    except botocore.exceptions.ParamValidationError:
        ret = "Invalid Template Paramaters!"
    return ret

@server.register_function
def cfTest(*template):
    f = ''.join(template)
    return f

server.print_port()
server.serve_forever()

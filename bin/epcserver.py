#!/usr/bin/env python
from epc.server import EPCServer
from AwsConfigMFA import AwsConfigMFA
from boto import cloudformation

class AwsEl:
  """
  Class for doing specific tasks in AWS Boto that can be used in Emacs.
  """
  def __init__(self, profile):
    config = AwsConfigMFA()
    region = "us-east-1"
    r = config.get("profile %s" % profile, "region")
    if r != None:
      region = r
    creds = config.getTokenCredentials(profile)
    self.cf = cloudformation.connect_to_region(region,
                                               aws_access_key_id=creds['access_key'],
                                               aws_secret_access_key=creds['secret_key'],
                                               security_token = creds['session_token'])

  def getTemplate(self, name):
    d = self.cf.get_template(name)
    print d

  def validateTemplate(self, template):
    ret = "Template Passed"
    try:
      self.cf.validate_template(template)
    except Exception,e:
      ret = e.message
    return ret


if __name__ == "__main__":
  server = EPCServer(('localhost', 0))
  Aws = AwsEl('dev')
  @server.register_function
  def cfValidate(*template):
    f = ''.join(template)
    return Aws.validateTemplate(f)

  @server.register_function
  def cfTest(*template):
    f = ''.join(template)
    return f

  server.print_port()
  server.serve_forever()

  """
  #jfile = ''
  #with open('/home/thawes/src/sources/ansible-service-discovery/deploy/infra/cloudformation.json', 'r') as f:
  #  jfile = ' '.join(f.readlines())
  #
  #a = AwsEl('dev')
  #print a.validateTemplate(jfile)
  """

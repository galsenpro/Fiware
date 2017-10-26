#!/usr/bin/env python

#
# Copyright 2015 Telefonica Investigacion y Desarrollo, S.A.U
#
# This file is part of IoT orchestrator
#
# IoT orchestrator is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# IoT orchestrator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with IoT orchestrator. If not, see http://www.gnu.org/licenses/.
#
# For those usages not covered by this license please contact with
# iot_support at tid dot es
#
# Author: IoT team
#
import sys
import logging.config
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
sys.path.append("/var/env-orchestrator/lib/python2.6/site-packages/iotp-orchestrator")

from settings.common import LOGGING
from orchestrator.core.flow.Roles import Roles

try: logging.config.dictConfig(LOGGING)
except AttributeError: logging.basicConfig(level=logging.WARNING)


def main():

    print "This script set a XACML policy to a role in Access Control"
    print ""

    SCRIPT_NAME = sys.argv[0]
    NUM_ARGS_EXPECTED = 11

    if (len(sys.argv) - 1 < NUM_ARGS_EXPECTED):
        print "Usage: %s [args]" % SCRIPT_NAME
        print "Args: "
        print "  <KEYSTONE_PROTOCOL>             HTTP or HTTPS"
        print "  <KEYSTONE_HOST>                 Keystone HOSTNAME or IP"
        print "  <KEYSTONE_PORT>                 Keystone PORT"
        print "  <SERVICE_NAME>                  Service name"
        print "  <SERVICE_ADMIN_USER>            Service admin username"
        print "  <SERVICE_ADMIN_PASSWORD>        Service admin password"
        print "  <ROLE_NAME>                     Name of role"
        print "  <POLICY_FILE>                   Policy XACML file name"
        print "  <KEYPASS_PROTOCOL>              HTTP or HTTPS"
        print "  <KEYPASS_HOST>                  Keypass (or PEPProxy) HOSTNAME or IP"
        print "  <KEYPASS_PORT>                  Keypass (or PEPProxy) PORT"        
        print ""
        print "  Typical usage:"
        print "     %s http           \\" % SCRIPT_NAME
        print "                                 localhost      \\"
        print "                                 5000           \\"
        print "                                 smartcity      \\"
        print "                                 adm1           \\"
        print "                                 password       \\"
        print "                                 ServiceCustomer\\"
        print "                                 mypolicy.xml   \\"        
        print "                                 http           \\"
        print "                                 localhost      \\"
        print "                                 8080           \\"        
        print ""
        print "For bug reporting, please contact with:"
        print "<iot_support@tid.es>"
        return

    KEYSTONE_PROTOCOL = sys.argv[1]
    KEYSTONE_HOST = sys.argv[2]
    KEYSTONE_PORT = sys.argv[3]
    SERVICE_NAME = sys.argv[4]
    SERVICE_ADMIN_USER = sys.argv[5]
    SERVICE_ADMIN_PASSWORD = sys.argv[6]
    ROLE_NAME = sys.argv[7]
    POLICY_FILE_NAME = sys.argv[8]
    KEYPASS_PROTOCOL = sys.argv[9]
    KEYPASS_HOST = sys.argv[10]
    KEYPASS_PORT = sys.argv[11]    

    flow = Roles(KEYSTONE_PROTOCOL,
                 KEYSTONE_HOST,
                 KEYSTONE_PORT,
                 KEYPASS_PROTOCOL,
                 KEYPASS_HOST,
                 KEYPASS_PORT)                 

    flow.setPolicyRole(
        SERVICE_NAME,
        None,
        SERVICE_ADMIN_USER,
        SERVICE_ADMIN_PASSWORD,
        None,
        ROLE_NAME,
        None,
        POLICY_FILE_NAME)

if __name__ == '__main__':

    main()

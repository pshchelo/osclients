#!/usr/bin/env python                                                                                                                                              [5/65]

from novaclient import client as nova_client
from neutronclient import client as neutron_client
from keystoneclient import client as keystone_client
from glanceclient import client as glance_client
from swiftclient import client as swift_client
from ironicclient import client as ironic_client
from ceilometerclient import client as ceilometer_client
from heatclient import client as heat_client
from cinderclient import client as cinder_client

auth = {
    'os_username': 'admin',
    'os_tenant_name': 'admin',
    'os_password': 'admin',
    'os_auth_url': 'http://192.168.100.126:5000/v2.0'
}

def get_ironic(auth):
    return ironic_client.get_client(1, **auth)

def get_nova(auth):
    return nova_client.Client(2,
                              auth['os_username'],
                              auth['os_password'],
                              auth['os_tenant_name'],
                              auth['os_auth_url'])

def get_keystone(auth, version=2):
    if version == 3:
        pass
    else:
        pass

def get_neutron(auth):
    pass

def get_glance(auth):
    pass

def get_cinder(auth):
    pass

def get_heat(auth):
    pass
def get_ceilometer(auth):
    pass

def get_swift(auth):
    pass

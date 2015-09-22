#!/usr/bin/env python

import os

# later Juno onwards uses oslo_utils
try:
    from oslo_utils import importutils
# hack for early Juno and before
except ImportError:
    from oslo.utils import importutils

novaclient = importutils.try_import("novaclient")
if novaclient:
    from novaclient import client as nova_client

neutronclient = importutils.try_import("neutronclient")
if neutronclient:
    from neutronclient import client as neutron_client

keystoneclient = importutils.try_import("keystoneclient")
if keystoneclient:
    from keystoneclient.v2_0 import client as ks2client
    from keystoneclient.v3 import client as ks3client

glanceclient = importutils.try_import("glanceclient")
if glanceclient:
    from glanceclient import client as glance_client

swiftclient = importutils.try_import("swiftclient")
if swiftclient:
    from swiftclient import client as swift_client

ironicclient = importutils.try_import("ironicclient")
if ironicclient:
    from ironicclient import client as ironic_client

ceilometerclient = importutils.try_import("ceilometerclient")
if ceilometerclient:
    from ceilometerclient import client as ceilometer_client

heatclient = importutils.try_import("heatclient")
if heatclient:
    from heatclient import client as heat_client

cinderclient = importutils.try_import("cinderclient")
if cinderclient:
    from cinderclient import client as cinder_client

default_auth = {
    'os_username': os.environ.get('OS_USERNAME'),
    'os_tenant_name': os.environ.get('OS_TENANT_NAME'),
    'os_password': os.environ.get('OS_PASSWORD'),
    'os_auth_url': os.environ.get('OS_AUTH_URL')
}


class ClientNotFound(Exception):
    pass


class ClientNotImplemented(Exception):
    pass


def get_ironic(auth=default_auth):
    if not ironicclient:
        raise ClientNotFound
    return ironic_client.get_client(1, **auth)


def get_nova(auth=default_auth):
    if not novaclient:
        raise ClientNotFound
    return nova_client.Client(2,
                              auth['os_username'],
                              auth['os_password'],
                              auth['os_tenant_name'],
                              auth['os_auth_url'])


def get_keystone(auth=default_auth, version=2):
    if not keystoneclient:
        raise ClientNotFound
    if version == 3:
        auth_url = auth['os_auth_url'].replace('v2.0', 'v3')
        keystone_client = ks3client
    else:
        auth_url = auth['os_auth_url']
        keystone_client = ks2client
    kc = keystone_client.Client(username=auth['os_username'],
                                password=auth['os_password'],
                                project_name=auth['os_tenant_name'],
                                auth_url=auth_url,
                                endpoint=auth_url,
                                verify=False)
    kc.authenticate()
    return kc


def get_neutron(auth=default_auth):
    if not neutron_client:
        raise ClientNotFound
    else:
        raise ClientNotImplemented


def get_glance(auth=default_auth):
    if not glance_client:
        raise ClientNotFound
    else:
        raise ClientNotImplemented


def get_cinder(auth=default_auth):
    if not cinder_client:
        raise ClientNotFound
    else:
        raise ClientNotImplemented


def get_heat(auth=default_auth):
    if not heat_client:
        raise ClientNotFound
    else:
        raise ClientNotImplemented


def get_ceilometer(auth=default_auth):
    if not ceilometer_client:
        raise ClientNotFound
    else:
        raise ClientNotImplemented


def get_swift(auth=default_auth):
    if not swift_client:
        raise ClientNotFound
    else:
        raise ClientNotImplemented

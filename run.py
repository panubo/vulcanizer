#!/usr/bin/env python

import sys
from urlparse import urlparse
import click
import json
from etcd import Client, EtcdKeyNotFound, EtcdConnectionFailed


@click.command()
@click.option('--etcdctl-peers', default='http://127.0.0.1:4001', help="ETCD peers list", envvar='ETCDCTL_PEERS')
@click.option('--host', required=True, help="Virtual Host Server Name", envvar='VHOST_SERVER_NAME')
@click.option('--service-name', required=True, help="Service Name", envvar='SERVICE_NAME')
@click.option('--backend', required=False, help="Backend ID", envvar='BACKEND')
def main(etcdctl_peers, host, service_name, backend):
    etcd_url = urlparse(etcdctl_peers)
    etcd = Client(host=etcd_url.hostname, port=etcd_url.port)
    key = "/vulcand/frontends/%s/frontend" % service_name

    click.secho("Connecting to ECTD: %s" % etcdctl_peers, fg='green')
    try:
        etcd.read(key='/')
    except EtcdConnectionFailed:
        click.secho('ETCD Connection Failed', fg='red')
        sys.exit(99)

    click.secho("Writing key %s" % key, fg='green')
    try:
        value = etcd.read(key=key).value
    except EtcdKeyNotFound:
        value = '{}'

    j = json.loads(value)
    j['Route'] = "Host(`%s`) && PathRegexp(`/.*`)" % host
    j['Type'] = 'http'

    if backend:
        j['BackendId'] = backend

    # Write / Update Key
    try:
        etcd.write(key=key, value=json.dumps(j))
    except Exception as e:
        raise e  # TODO: Handle specific exceptions

    click.secho("All done.", fg='green')

if __name__ == '__main__':
    main()

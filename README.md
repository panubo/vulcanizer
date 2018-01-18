# Vulcanizer

[Vulcand](http://vulcand.io) frontend updater for [Etcd](https://github.com/coreos/etcd).

## Usage

```
docker run --rm -e ETCDCTL_PEERS=http://10.1.15.122:2379 vulcanizer --host foo --service-name foo-master
```

## TODO

Add support for:

- `VHOST_PRIMARY_NAME`
- `VHOST_SERVER_NAMES`
- `VHOST_SSL_CERTIFICATE`
- `VHOST_SSL_ONLY`

## Staus

Working as a proof of concept, however it is feature incomplete. 

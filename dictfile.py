router = { "ip": "10.1.1.1", "device_type": "ios"}
print ((router["device_type"]))
print ((router["ip"]))


cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.10',
    'username': 'test',
    'password': 'password',
    'port' : 8022,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}
print(type(router))
print ((cisco_881['host']))
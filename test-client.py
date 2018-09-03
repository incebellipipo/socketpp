#!/usr/bin/env python2

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 6751))
clientsocket.sendall(
'{\n'
'  "Event": "LIST_INTERFACES",\n'
'  "Payload": {\n'
'    "br-630b1454c1ee": {\n'
'      "broadcast_addr": "172.18.255.255",\n'
'      "dst_addr": "172.18.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.18.0.1",\n'
'      "mac_addr": "02:42:0c:f7:16:d3",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "br-630b1454c1ee",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "docker0": {\n'
'      "broadcast_addr": "172.17.255.255",\n'
'      "dst_addr": "172.17.0.1",\n'
'      "flags": ["UP", "BROADCAST", "MULTICAST"],\n'
'      "ip_addr": "172.17.0.1",\n'
'      "mac_addr": "02:42:96:db:b4:cc",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "docker0",\n'
'      "netmask_addr": "255.255.0.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "enp3s0": {\n'
'      "broadcast_addr": "192.168.1.255",\n'
'      "dst_addr": "192.168.1.3",\n'
'      "flags": ["UP", "BROADCAST", "RUNNING", "MULTICAST"],\n'
'      "ip_addr": "192.168.1.3",\n'
'      "mac_addr": "00:30:18:ce:a0:79",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "enp3s0",\n'
'      "netmask_addr": "255.255.255.0",\n'
'      "type": "ETHERNET"\n'
'    },\n'
'    "wlan0": {\n'
'      "broadcast_addr": "192.168.1.255",\n'
'      "dst_addr": "192.168.1.101",\n'
'      "flags": ["UP", "BROADCAST", "RUNNING", "MULTICAST"],\n'
'      "ip_addr": "192.168.1.101",\n'
'      "mac_addr": "bc:77:37:6b:bf:2a",\n'
'      "metric": 0,\n'
'      "mtu": 1500,\n'
'      "name": "wlan0",\n'
'      "netmask_addr": "255.255.255.0",\n'
'      "status": {\n'
'        "address": "bc:77:37:6b:bf:2a",\n'
'        "bitrate": "13Mb/s",\n'
'        "bssid": "64:66:b3:46:48:9e",\n'
'        "freq": "2452",\n'
'        "group_cipher": "TKIP",\n'
'        "id": "51",\n'
'        "ip_address": "192.168.1.101",\n'
'        "key_mgmt": "WPA2-PSK",\n'
'        "mode": "station",\n'
'        "pairwise_cipher": "CCMP",\n'
'        "ssid": "nm_test",\n'
'        "wpa_state": "COMPLETED"\n'
'      },\n'
'      "type": "WIRELESS"\n'
'    }\n'
'  },\n'
'  "ResponseMessage": "Interfaces successfully listed",\n'
'  "ResponseStatus": "Success"\n'
'}\n'
)

result = clientsocket.recv(4096)
print result
clientsocket.close()

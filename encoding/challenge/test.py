#!/usr/bin/env python3

from pwn import * # pip install pwntools
import json

import rot13
import hex
import b64
import bigint
import utf8

decode = {
    'rot13': rot13.decode,
    'hex': hex.decode,
    'base64': b64.decode,
    'bigint': bigint.decode,
    'utf-8': utf8.decode
}

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()
for i in range(100):

    if 'flag' in received:
        print(res["flag"])
        break

    e_type = received["type"]
    val = received["encoded"]

    print("Received type: ")
    print(e_type)
    print("Received encoded value: ")
    print(val)

    if e_type in decode:
        decoded = decode[e_type](val)
        print(decoded)
        to_send = {
        "decoded": decoded
        }
        json_send(to_send)
        received = json_recv()
    else:
        print(f'Error. Unknown type: {e_type}')


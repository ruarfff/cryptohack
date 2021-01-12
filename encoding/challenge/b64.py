import base64

def decode(s):
    base64_bytes = s.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return  message_bytes.decode('ascii')
    # return base64.b64encode(bytes.fromhex(s))


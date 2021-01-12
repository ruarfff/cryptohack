import struct

def decode(s):
    return bytes(s).decode('utf8')
    # struct.pack("b"*len(s),*s)
    # return struct.pack("b"*len(s),*s).decode('utf8')

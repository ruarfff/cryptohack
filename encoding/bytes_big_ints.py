#!/usr/bin/env python3

num = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

print(num.to_bytes(num.bit_length(), byteorder='big').decode("utf-8"))

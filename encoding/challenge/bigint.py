def decode(s):
    num = int(s.strip(), 0)
    print(num)

    text = num.to_bytes(num.bit_length(), byteorder='big').decode("utf-8")

    return text.replace('\x00','')



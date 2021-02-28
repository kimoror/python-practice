# https://vk.com/away.php?to=http%3A%2F%2Fwww.binaryconvert.com%2Fresult_unsigned_int.html%3Fdecimal%3D050052050056050048048056053053&cc_key=
def f22(num):
    a = (num & 0x0000001f) << 10
    b = (num & 0x00000020) << 26
    c = (num & 0x003FFFC0) << 9
    d = (num & 0x00C00000) >> 22
    e = (num & 0x01000000) >> 22
    f = (num & 0x3F000000) >> 22
    g = (num & 0xC0000000) >> 22
    return a | b | c | d | e | f | g

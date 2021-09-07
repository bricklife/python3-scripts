# ref. https://ja.wikipedia.org/wiki/%E5%B7%A1%E5%9B%9E%E5%86%97%E9%95%B7%E6%A4%9C%E6%9F%BB#CRC-32

crc_table = [0] * 256

def make_crc_table():
    for i in range(256):
        c = i
        for j in range(8):
            if c & 1:
                c = 0xEDB88320 ^ (c >> 1)
            else:
                c = c >> 1
        crc_table[i] = c

def crc32(buf):
    c = 0xFFFFFFFF
    l = len(buf)
    for i in range(l):
        c = crc_table[(c ^ buf[i]) & 0xFF] ^ (c >> 8)
    return c ^ 0xFFFFFFFF

if __name__ == "__main__":
    import sys
    make_crc_table()
    crc = crc32(sys.argv[1].encode())
    print('{:d} (0x{:08x})'.format(crc, crc))

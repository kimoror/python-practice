import struct


def get_list_links_list_items(length, link_list, size_link, original_binary, format_unpack):
    list_links = []

    for i in range(length):
        [item_link] = struct.unpack(format_unpack,
                                    original_binary[link_list + i * size_link: link_list + (i + 1) * size_link])
        list_links.append(item_link)

    return list_links


def f31(binary):
    def struct_a(offset):
        a1 = struct.unpack("< l", binary[offset:offset + 4])[0]
        offset += 4
        [size2] = struct.unpack("< L", binary[offset: offset + 4])
        offset += 4
        [address2] = struct.unpack("< L", binary[offset: offset + 4])
        offset += 4
        arr2 = get_list_links_list_items(size2, address2, 2, binary, '< H')
        a2 = []
        for i in range(size2):
            a2.append(struct_b(arr2[i]))
        # offset += 2
        [address3] = struct.unpack('< I', binary[offset: offset + 4])
        a3 = struct_c(address3)
        offset += 4
        return {
            'A1': a1,
            'A2': a2,
            'A3': a3,
        }

    def struct_b(offset):
        b1 = struct.unpack("< 7s", binary[offset: offset + 7])[0].decode('ascii')
        offset += 7
        b2 = struct.unpack("< H", binary[offset: offset + 2])[0]
        offset += 2
        return {
            'B1': b1,
            'B2': b2,
        }

    def struct_c(offset):
        res_d = struct_d(offset)
        c1 = res_d['structD']
        offset = res_d['offset']
        c2 = struct.unpack("< l", binary[offset:offset + 4])[0]
        offset += 4
        c3 = struct.unpack("< H", binary[offset:offset + 2])[0]
        offset += 2
        c4 = struct.unpack('< B', binary[offset: offset + 1])[0]
        offset += 1
        c5 = struct.unpack('< h', binary[offset: offset + 2])[0]
        offset += 2
        return {
            'C1': c1,
            'C2': c2,
            'C3': c3,
            'C4': c4,
            'C5': c5,
        }

    def struct_d(offset):
        d1 = struct.unpack('< L', binary[offset:offset + 4])[0]
        offset += 4
        d2 = list(struct.unpack('< 7b', binary[offset: offset + 1 * 7]))
        offset += 7
        [k] = struct.unpack('< L', binary[offset: offset + 4])
        offset += 4
        [offset1] = struct.unpack('< L', binary[offset: offset + 4])
        s = '<' + str(k) + 'l'
        d3 = list(struct.unpack(s, binary[offset1: offset1 + 4 * k]))
        offset += 4
        return {
            'structD': {
                'D1': d1,
                'D2': d2,
                'D3': d3,
            },
            'offset': offset
        }

    return struct_a(4)

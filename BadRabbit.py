def calc_rabbit_CRC(proc_name):
    """
    Quick and dirty implementation of BadRabbit's custom hashing algorithm in python
    
    :param proc_name: process name string to calculate its custom hash 
    :return: string of the custom
    """
    try:
        res_byte_array = bytearray([0x21, 0x43, 0x65, 0x87])
        proc_byte_array = bytearray(proc_name)
        j = 0
        while j < 3:
            i = 0
            while i < len(proc_name):
                place_to_replace = (i + j) % 4
                if proc_byte_array[i] != res_byte_array[place_to_replace]:
                    res_byte_array[place_to_replace] = (proc_byte_array[i] ^ res_byte_array[place_to_replace]) - 1
                else:
                    # fixing "byte underflow" case
                    res_byte_array[place_to_replace] = 0xff
                i += 1
            j += 1
        return binascii.hexlify(res_byte_array[::-1])
    except:
        pass

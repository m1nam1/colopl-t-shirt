'''
Colopl T-shirt

111000
111000
001010
110011

111000
111000
001110
101101

111000
111000
001110
010111

111000
111000
001110
101001
'''

def main():
    CO = '111000'\
         '111000'\
         '001010'\
         '110011'\

    LO = '111000'\
         '111000'\
         '001110'\
         '101101'\

    P = '111000'\
        '111000'\
        '001110'\
        '010111'\

    L = '111000'\
        '111000'\
        '001110'\
        '101001'\

    # bin
    COLOPL = CO + LO + P + L
    print (COLOPL)
    # 111000111000001010110011111000111000001110101101111000111000001110010111111000111000001110101001

    # bin to int
    colopl_int = int(COLOPL, 2)
    print ('int:', colopl_int)
    # int: 70411107086495060936066565033

    # int to hex
    colopl_hex = format(colopl_int, 'x')
    print ('hex:', colopl_hex)
    # hex: e382b3e383ade38397e383a9

    # hex to bytes
    colopl_bytes = bytes.fromhex(colopl_hex)
    print ('bytes:', colopl_bytes)
    # bytes: b'\xe3\x82\xb3\xe3\x83\xad\xe3\x83\x97\xe3\x83\xa9'

    # bytes to str
    colopl_str = colopl_bytes.decode('utf-8')
    print (colopl_str)
    # コロプラ

if __name__ == '__main__':
    main()

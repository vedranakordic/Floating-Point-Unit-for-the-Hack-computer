def float_bin(my_number, places = 1):

    my_whole, my_dec = str(my_number).split(".")
    my_whole = int(my_whole)
    res = (str(bin(my_whole))+".").replace('0b','')

    for x in range(places):
        my_dec = str('0.')+str(my_dec)
        temp = '%1.20f' %(float(my_dec)*2)
        my_whole, my_dec = temp.split(".")
        res += my_whole
    return res


def float_to_IEEE754_16bit(n) :

    sign = 0
    if n < 0 :
        sign = 1
        n = n * (-1)
    p = 10
    # zapis broja n u binarnoj reprezentaciji
    dec = float_bin (n, places = p)

    dotPlace = dec.find('.')
    onePlace = dec.find('1')
    # račuanje mantise
    if onePlace > dotPlace:
        dec = dec.replace(".","")
        onePlace -= 1
        dotPlace -= 1
    elif onePlace < dotPlace:
        dec = dec.replace(".","")
        dotPlace -= 1
    mantissa = dec[onePlace+1:]

    # računanje eksponenta
    exponent = dotPlace - onePlace
    exponent_bits = exponent + 15

    # pretvorba eksponenta u binarni zapis
    exponent_bits = bin(exponent_bits).replace("0b",'')

    mantissa = mantissa[0:10]

    # IEEE754 zapis
    final = str(sign) + exponent_bits.zfill(5) + mantissa
    return final





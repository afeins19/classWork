def decimal_to_binary(val):
    bin_val = []
    if val == 0:
        return 0

    if val == 1:
        return 1

    while val!=0:
        cur_bit = val % 2
        bin_val = [str(cur_bit)] + bin_val
        val = val // 2

    return ''.join(bin_val)

print(decimal_to_binary(46))
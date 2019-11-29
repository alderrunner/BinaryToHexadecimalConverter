table = [("0", "0000"), ("1", "0001"), ("2", "0010"), ("3", "0011"),
         ("4", "0100"), ("5", "0101"), ("6", "0110"), ("7", "0111"),
         ("8", "1000"), ("9", "1001"), ("A", "1010"), ("B", "1011"),
         ("C", "1100"), ("D", "1101"), ("E", "1110"), ("F", "1111")
         ]
binlist = []


def foursplit(binarynumber):
    if len(binarynumber) < 4:
        while len(binarynumber) != 4:
            binarynumber = "0" + binarynumber
        binlist.append(binarynumber)
    elif len(binarynumber) == 4:
        binlist.append(binarynumber)
    else:
        point = len(binarynumber) - 4
        pair = binarynumber[point:]
        binlist.append(pair)
        binarynumber = binarynumber[:point]
        foursplit(binarynumber)


def convert():
    hexnum = ""
    for num in binlist:
        for hexa in table:
            if hexa[1] == num:
                hexnum = hexnum + hexa[0]
    return hexnum


def alg():
    print("Enter the binary number to convert to hexadecimal:")
    inputbin = input()
    foursplit(inputbin)
    binlist.reverse()
    hexnum = convert()
    print(inputbin + " in hexadecimal is: " + hexnum)


alg()

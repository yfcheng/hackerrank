def encode(source):
    dest="";
    i = 0
    while i < len(source):
        runLength = 1;
        while (i + 1) < len(source) and source[i] == source[i+1]:
            runLength = runLength + 1
            i = i + 1
        dest += source[i]
        dest += str(runLength)
        i = i+1
    return dest

source = raw_input("")
print (encode(source))

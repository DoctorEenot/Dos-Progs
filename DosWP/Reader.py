def Read(FN):
    try:
        File = open(FN,'r')
    except:
        print('File doesn`t exist')
        return
    buf = []
    word = ''
    cont = list(File.readline())
    cont.remove('\n')
    for i in range(len(cont)):
        word = word+cont[i]
    buf.append(word)
    word = ''
    while cont:
        cont = list(File.readline())
        try:
            cont.remove('\n')
        except:
            pass
        for i in range(len(cont)):
            word = word+cont[i]
        buf.append(word)
        word = ''
    File.close()
    buf.remove('')
    return buf


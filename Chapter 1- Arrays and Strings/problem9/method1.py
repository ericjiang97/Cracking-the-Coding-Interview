def subString(s1,s2):
    begin = s1[0]
    for j in range(len(s1)):
        if(s2[j] == begin):
            if((str(s2[j:len(s2)])+str(s2[0:j]))==str(s1)):
                return True
    return False


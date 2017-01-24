def isNumber(s):
    if (1):
	status = 0
        l = len(s)
        i = 0
        while (i < l):
            if (s[i] == ' ' and status != 0):
                if (status == 5 or status == 8 or status == 9 or status == 10):
                    return False
                status = 7
                i += 1
                continue
            if (status == 0):
                if (s[i] >= '0' and s[i] <= '9'):
                    status = 4
                elif (s[i] == ' '):
                    status = 0
                elif (s[i] == '.'):
                    status = 8
                elif (s[i] == '-' or s[i] == '+'):
                    status = 9
                else :
                    return False
            elif (status == 9):
                if (s[i] >= '0' and s[i] <= '9'):
                    status = 4
                elif (s[i] == '.'):
                    status = 8
                else :
                    return False
            elif (status == 1):
                if (s[i] == '.'):
                    status = 3
                else:
                    return False
            elif (status == 2):
                if (s[i] >= '0' and s[i] <= '9'):
                    status = 3
                else:
                    return False
            elif (status == 3):
                if (s[i] >= '0' and s[i] <= '9'):
                    status = 3
                elif (s[i] == 'e' or s[i] == 'E'):
                    status = 5
                else:
                    return False
            elif (status == 4):
                if (s[i] >= '0' and s[i] <= '9'):
                    status = 4
                elif (s[i] == '.'):
                    status = 3
                elif (s[i] == 'e' or s[i] == 'E'):
                    status = 5
                else :
                    return False
            elif (status == 5):
                if (s[i] >= '0' and s[i] <= '9'):
                    status = 6
                elif (s[i] == '-' or s[i] == '+'):
                    status = 10
                else :
                    return False
            elif (status == 10):
                if (s[i] >= '0' and s[i] <= '9'):
                    status = 6
                else :
                    return False
            elif (status == 6):
                if (s[i] >= '0' and s[i] <= '9'):
                    status = 6
                else :
                    return False
            elif (status == 7):
                if (s[i] != ' '):
                    return False
            elif (status == 8):
                if (s[i] >= '0' and s[i] <= '9'):
                    status = 3
                else:
                    return False
            i+=1
        if (status == 5 or status == 0 or status == 8 or status == 9 or status == 10):
            return False
        else :
            return True

print(isNumber("00000000"))
print(isNumber("3"))
print(isNumber("abc"))
print(isNumber("1 a"))
print(isNumber("2e10"))
print(isNumber(" 0.0000 "))

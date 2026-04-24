from enum import Enum

class ErrorCodes(Enum):
    EACCES = 0
    ENODEV = 1
    ENOENT = 2

    def getErrorNum(self):
        return self.value

def example1(condition, string1, errno, input_data):
    p = None
    string2 = None
    message = [None] * 3
    i = 0
    if condition:
        p = [0]
        p[0] = 1
    try:
        p[1] = 0
    except Exception:
        pass 
    if condition or (string1 == string2):
        print("They are equal")

    message[ErrorCodes.EACCES.getErrorNum()] = "Permission denied"
    message[ErrorCodes.ENODEV.getErrorNum()] = "No such device"
    message[ErrorCodes.ENOENT.getErrorNum()] = "No such file or directory"

    error_num = errno.getErrorNum()
    if error_num in [0, 1, 2]:
        print(message[error_num])

    output = [''] * 100
    for i in range(101):
        try:
            output[i] = input_data[i]
            if input_data[i] == '\0':
                break
        except IndexError:
            break
    i = 0
    while True:
        try:
            output[i] = input_data[i]
            if input_data[i] == '\0':
                break
            i += 1
        except IndexError:
            break

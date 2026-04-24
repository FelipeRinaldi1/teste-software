def lookup(vector, key, n):
    low = 0
    high = n
    while low <= high:
        medium = (low + high) // 2
        if vector[medium] == key:
            return medium
        else:
            if vector[medium] < key:
                low = medium + 1
            else:
                high = medium - 1
    return -1

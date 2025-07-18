# Replace Elements with Greatest Element on Right Side

def replaceElements(self, arr):
    if len(arr) == 1:
        return [-1]

    max_value = -1
    for i in range(len(arr) - 1, -1, -1):
        temp = arr[i]
        arr[i] = max_value
        if temp > max_value:
            max_value = temp
        
    return arr

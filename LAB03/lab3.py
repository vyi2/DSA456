def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)
    
def linear_search(list, key, i = 0):
    if i == len(list):
        return -1
    if list[i] == key:
        return i
    return linear_search(list, key, i + 1)

def binary_search(list,key,lindex = 0, hindex = None):
    if hindex == None:
        hindex = len(list) - 1
    if hindex < lindex:
        return -1
    mindex = (lindex + hindex)//2
    if key == list[mindex]:
        return mindex
    elif key < list[mindex]:
        return binary_search(list,key,lindex,mindex - 1)
    else:
        return binary_search(list,key,mindex + 1, hindex)

def main(): 
    fac = factorial(5)
    print(fac)
    list = [1,2,3,4,5]
    key = 4
    mylist = linear_search(list,key)
    print(mylist)
    blist = [10,20,30,40,50,60,70,80,90,100]
    bkey = 80
    binlist = binary_search(blist,bkey)
    print(binlist)
    bkey = 40
    binlist = binary_search(blist,bkey)
    print(binlist)
    bkey = 10
    binlist = binary_search(blist,bkey)
    print(binlist)
    bkey = 100
    binlist = binary_search(blist,bkey)
    print(binlist)


main()
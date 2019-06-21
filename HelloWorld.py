def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in range(0, n, k):
        temp_string = string[i:i + k]
        u = []
        e = ''
        for j in temp_string:
            if j in e:
                continue
            else:
                e += j
        print (e)

string = input("Enter the string:")
k = int(input("Enter a factor of the string:"))
merge_the_tools(string,k)
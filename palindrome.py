def palindrome(num):
    temp=num
    rev=0
    while(num>0):
        n=num%10
        rev=rev*10+n
        num=num//10

    if rev==temp:
        print(rev,'=',temp)
        print("it is palindrome")
    else:
        print(rev,'!=',temp)
        print("it is not palindrome")
   


palindrome(12321)

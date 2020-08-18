while(1):
    num = int(input("enter no. to check prime or not"))
    if num>2:
        for i in range(2,num):
            if num%i==0:
                print(num,"is not prime")
                break
        else:
            print(num,"is prime")
    else:
        print(num,"is not prime")
     

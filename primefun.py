def check_prime(n):
    if n>1:
        for n in range(2,n):
            if n% 2 == 0:
                print("not prime")
                break
            else:
                print("prime")
    else:
        print("not prime")
a = check_prime(3)
print(a)
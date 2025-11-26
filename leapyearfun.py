def year(n):
    if(n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        print("is leap year")
    else:
        print("is not a leap yar")
year(2028)
string = "Gargee"
vowels = [ 'a','e','i' ,'o', 'u' ]
for char in string :
        if char.lower() in vowels:
            print("vowel:", char)
        else:
            print("consonants:", char)
def translate(phrase):
    translation  = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else: 
            translation = translation + letter
    return translation


print(translate(input("Input a phrase:")))


try:
    number = int(input("Enter a number"))
    print(number)

except:
    print("Invalid Input")
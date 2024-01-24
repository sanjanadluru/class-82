capitalLetters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerLetters='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'

def cipher(plaintext, n):
    global  capitalLetters, lowerLetters, numbers
    cipherText = ''

    for char in plaintext:
        if char in numbers:
            currentPosition = numbers.find(char)
            cipherText += numbers[(currentPosition + n ) % 10]
        # Check if 'char' is present in 'lowerLetters' list
        elif char in lowerLetters:
            # Get the current position of the 'char' in 'lowerLetters' list
            currentPosition = lowerLetters.find(char)
            cipherText += lowerLetters[(currentPosition + n ) % 26]
          
        # Check if 'char' is present in 'capitalLetters' list
        elif char in capitalLetters:
            # Get the current position of the 'char' in 'capitalLetters' list
            currentPosition = capitalLetters.find(char)
            cipherText += capitalLetters[(currentPosition + n ) % 26]
          
            # Calculate the character using formula : numbers[(currentPosition + n ) % 26] and add it to cipherText
             
        else:
            cipherText += char
    
    return cipherText
        

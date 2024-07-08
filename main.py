import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

while True :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    def caesar(direction, text, shift) :
        change_text = ""
        if direction == "decode" :
            shift *= -1
        for i in text :
            if i not in alphabet :
                change_text += i
            else :
                position = alphabet.index(i) + shift
                if position > 25 or position < 0 :
                    position = position % 26
                change_text += alphabet[position]
        print(f"The {direction} text is {change_text}")
        
    caesar(direction, text, shift)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no" :
        print("Goodbye")
        break
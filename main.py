from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceaser(word, switch):
    password = ""
    if direction == "encode":
      for _ in range(len(word)):
        password += alphabet[(alphabet.index(word[_]) + switch) % 26]
      print(f"The encoded text is: {password}")
    elif direction == "decode":
      for _ in range(len(word)):
        password += alphabet[(alphabet.index(word[_]) - switch) % 26]
      print(f"The decoded text is: {password}")
  

      
    
repeat = True
while repeat:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceaser(text,shift)
  answer = input("Would you like to type again?: yes or no\n").lower()
  if answer == "no":
    print("Good bye!")
    repeat = False
    
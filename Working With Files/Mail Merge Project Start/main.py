#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    


PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names:
    items = names.readlines()
with open("./Input/Letters/starting_letter.txt") as letters:
    p_letter = letters.read()
    for item in items:
        name = item.strip()
        new_letter = p_letter.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode= "w") as completed_letter:
            completed_letter.write(new_letter)




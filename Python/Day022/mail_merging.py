PLACEHOLDER = "[name]"

with open("./Day22/input/names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Day22/input/letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Day22/output/ready_to_send/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
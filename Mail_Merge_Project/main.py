#!/usr/bin/python3

with open("./Input/Letters/starting_letter.txt",
          'r', encoding='utf-8') as start:
    content = start.read()
    with open("./Input/Names/invited_names.txt",
              'r', encoding='utf-8') as names:
        for name in names.readlines():
            name = name.strip()
            with open(f"./Output/ReadyToSend/letter_to_{name}.txt",
                      'w', encoding='utf-8') as mail:
                message = content.replace("[name]", name)
                mail.write(message)

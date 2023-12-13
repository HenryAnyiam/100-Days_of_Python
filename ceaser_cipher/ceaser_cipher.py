#!/us/bin/python3
"""ceaser cipher encryption"""


logo = __import__("ceaser_art").logo


alphabets = [chr(i) for i in range(97, 123)]
numbers = [i for i in range(0, 26)]
alphanum = {key : val for key, val in zip(alphabets, numbers)}


def encrypt(message, shift, command):
    """encrypt or decrypt a message by shiting it with
    the given shift values.
    When encrypting, you shift the values forward
    When decrypting, you shift the values backward
    """
    newmessage = ""
    message = message.lower()
    try:
        shift = int(shift)
    except ValueError:
        return message
    for i in message:
        if i not in alphanum:
            newmessage += i
        else:
            curr = alphanum[i]
            if command == "encode":
                index = (25 + shift + curr) % 25
            else:
                index = ((25 + curr) - shift) % 25
            newmessage += alphabets[index]
    return newmessage

def encodeOrdecode(command):
    text = input("Type your message: ").lower()
    shift = input("Type the shift number: ")
    cipher = encrypt(text, shift, command)
    print(f"Your {command}d message is {cipher}")


def ceaser_cipher():
    """main ceaser cipher"""
    stop = False
    while not stop:
        print("Type 'encode' to encypt. Type 'decode' to decrypt, Type 'exit' to exit")
        command = input("").lower()
        if (command == 'encode') or (command == 'decode'):
            encodeOrdecode(command)
        elif command == 'exit':
            stop = True
        else:
            print("You've entered and incorrect command")


if __name__ == "__main__":
    print(logo)
    ceaser_cipher()
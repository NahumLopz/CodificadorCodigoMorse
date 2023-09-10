
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': ' '
}

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in morse_dict:
            morse_code.append(morse_dict[char])
        else:
            morse_code.append(char)
    return ' '.join(morse_code)


with open('entrada.txt', 'r') as file:
    text = file.read()
    morse_text = text_to_morse(text)

with open('salida.txt', 'w') as file:
    file.write(morse_text)

print("El contenido del archivo se ha convertido a código Morse y se ha guardado en 'salida.txt'.")
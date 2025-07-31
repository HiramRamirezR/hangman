# if the letter is incorrect, add a part to the body and reduce one attempt
# if the letter has already been entered, show an error message
# start the game with 6 attempts

import random

# list of words
words = [
    "gato", "perro", "casa", "flor", "sol", "luna", "mar", "agua", "pato", "río",
    "nube", "tren", "pan", "luz", "cielo", "amor", "rojo", "azul", "verde", "ratón",
    "nieve", "rey", "reina", "piedra", "tigre", "pez", "león", "oso", "mono", "arroz",
    "playa", "juguete", "silla", "mesa", "carro", "ventana", "fruta", "bici", "yogur",
    "globo", "delfín", "cebra", "goma", "manzana", "pera", "lago", "barco", "zorro",
    "pájaro", "niño", "niña", "dado", "dedo", "cama", "camión", "ratón", "lápiz",
    "tierra", "sola", "papel", "cuchara", "bomba", "abeja", "limón", "bota", "rana",
    "conejo", "caballo", "cabra", "pollo", "grillo", "pluma", "estrella", "sandía",
    "naranja", "melón", "chicle", "mango", "bailar", "cantar", "saltar", "comer",
    "leer", "escribir", "parque", "jirafa", "plato", "sopa", "agua", "foca", "sapo",
    "nido", "caracol", "abeja", "botella", "pelota", "cuadro", "reloj", "zapato",
    "playa", "helado", "bruja", "banda", "circo"
]

word = random.choice(words)

letters = []
attempts = 6
spaces = ["_"] * len(word)

print(f"Let's start the game.\nYour word has {len(word)} letters.\n")
print(person[0])
print(f"{spaces}\n")


while attempts > 0:

    letter = input(f"Enter a letter. You have {attempts} attempts left.\n")

    if letter in letters:
        print(f"\n-------------------------------------\nYou have already entered the letter '{letter}'.")
        print(f"{spaces}\n")
        continue

    # add the letter to the list
    letters.append(letter)

    # check if the letter is in the word
    if letter in word:
        # replace the "_" with the letter in the word
        for i, char in enumerate(word):
            if char == letter:
                spaces[i] = letter
        print("\n-------------------------------------\nWell done, keep going! \n")

    else:
        print(f"\n-------------------------------------\nThe letter '{letter}' is not in the word.")
        attempts -= 1

    print(person[6 - attempts])
    print(f"{spaces}\n")

    if "_" not in spaces:
        print("Congratulations! You have guessed the word correctly.")
        break

if attempts == 0:
    print(f"Game over. The word was '{word}'.")

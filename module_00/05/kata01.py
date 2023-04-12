languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

# iterar sobre un diccionario
# en este caso n el el key y lenguages[n] es el contenido del key
for n in languages:
    print(n, "was created by", languages[n])

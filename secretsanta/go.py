from random import shuffle
names = ('emil jeff joey alan a3qz shab hoag'.split())
shuffle(names)
for i in range(0, len(names)):
    #print(i, names[i], "->", names[(i + 1) % len(names)])
    with open(f'{names[i]}/index.html', 'w+') as f:
        f.write("""<body>
    <h1>A very wolfrat secret santa</h1><br/>
    <h3>You will buy for </h3><h2>""" + names[(i + 1) % len(names)] + "</h2>\n</body>")

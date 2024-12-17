from random import shuffle

names = ('emil jeff joey alan a3qz shab hoag'.split())
last_year_names = ('a3qz emil alan joey jeff shab hoag'.split())
last_year_buys = {}
last_year_gets = {}
for i in range(0, len(names)):
    last_year_buys[names[i]] = names[(i + 1) % len(names)] 
    last_year_gets[names[(i + 1) % len(names)]] = names[i]

failed = True
while failed:
    shuffle(names)
    mapping = {}
    failed = False
    for i in range(0, len(names)):
        newname = names[(i + 1) % len(names)]
        if last_year_buys[names[i]] == newname or last_year_gets[names[i]] == newname:
            failed = True
for i in range(0, len(names)):
    with open(f'{names[i]}/index.html', 'w+') as f:
        f.write("""<body>
    <h1>A very wolfrat secret santa</h1><br/>
    <h3>You will buy for </h3><h2>""" + names[(i + 1) % len(names)] + "</h2>\n</body>")

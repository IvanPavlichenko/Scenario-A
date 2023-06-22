print("Hello salama")
for i in range(1, 10 + 1):
    print(i)

x = int(input("Давай ка число мне тут напиши, я тебе таблицу умножения до этого чилса сделаю: "))

for r in range(1, x + 1):
    for e in range(1, x + 1):
        print(r, "*", e, "=", r * e)
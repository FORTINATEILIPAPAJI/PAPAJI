stroka = "прИВет. как Дела"
s = []
print(stroka.split("."))
for i in stroka.split("."):
    i = i.lstrip().capitalize()
    s.append(i)
print(". ".join(s) + ".")

print(*list("UTRI"), "ughcv", "hf", sep="\t")
print("ughcv", "hf", *list("UTRI"), sep="\t")
print(1, end="\n")

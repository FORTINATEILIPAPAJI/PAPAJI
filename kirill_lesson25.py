# dictionary {} dict() - это как список, у которого индексы элементов мы задаём вручную
# x = {key1: value1, key2: value2, ...}
# ключ в словаре может быть только неизменяемым объектом, например: int, float, str, tuple
# чтобы создать пустое множество, мы обязательно используем функцию set()
# print(type({}))
#print(type(set()))
processor = {"LGA1155": {"i3 2100 series", "i5 2300 series", "i7 2600 series"},
             "LGA 775": {"Pentium dual-core", "core 2 duo series", "core 2 quad series"}}
print(processor)
processor["am3/am3+"] = ["athlon || x2 series", "FX 8000 series", "FX 4300 series"]
print(processor)
processor["am3/am3+"].append("FX 6000 series")

#EmuPedia 1 ссылка
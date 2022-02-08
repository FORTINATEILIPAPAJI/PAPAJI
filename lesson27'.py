processor = {"LGA1155": {"i3 2100 series", "i5 2300 series", "i7 2600 series"},
             "LGA 775": {"Pentium dual-core", "core 2 duo series", "core 2 quad series"}}
# del - инструкция, которая удаляет ключ с его значениями
del processor['LGA 775']
print(processor)
processor["am3/am3+"] = ["athlon || x2 series", "FX 8000 series", "FX 4300 series"]
processor["am3/am3+"].append("FX 6000 series")
# .pop(x, y) - возвращает удаляемый ключ (с его значением),иначе возвращает y (если он вообще указан)
print(processor.pop('LGA 775',None))
print(processor)
if "Top Sborka ZA 100 Rublei" not in processor:
    print("SPASIBO CHTO NE DABAVIL!")
# .get(x,y) - возвращает значение по указаному ключу x, иначе возвращает y (если он вообще указан)к
print(processor.get("Top Sborka ZA 100 Rublei",None))
# метод .keys - возвращает ключи словаря
print(tuple(processor.keys()))

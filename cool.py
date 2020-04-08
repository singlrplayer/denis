"""sergeiev denis 5-A claas"""
rectangle={"a":123,"d":321,"e":446,"c":543}
l=rectangle["e"]+rectangle["a"]+rectangle["d"]+rectangle["c"]
print(l)
g=0#перыметр
for key in rectangle:
    g=g+rectangle[key]
print(g)

name=input("")
i=0
a=""
while i < len(name):
    if name[i] not in a:
        a+=name[i]
        print(f"{name[i]}:{name.count(name[i])}")
    i+=1
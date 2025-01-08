# for nth consonant replace in alphabetical order
coso_list = 'bcdfghjklmnpqrstvwxyz'
conso_list = list(coso_list)

message = "codeSignal"
message = list(message)
n=3
k=0
for m in range(len(message)):
    if message[m].lower() in conso_list:
        temp = message[m].lower()
        k += 1
        if k==n:
            k=0
            upper = False
            if message[m].isupper():
                upper = True
            index = conso_list.index(temp)
            index += 1
            if index == len(conso_list):
                index = 0
            if upper:
                message[m] = conso_list[index].upper()
            else:
                message[m] = conso_list[index]
print("".join(message))
            
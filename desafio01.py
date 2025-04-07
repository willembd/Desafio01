h1 = int(input("Digite a hora: "))
m1 = int(input("Digite os minutos: "))
h2 = int(input("Digite a hora: "))
m2 = int(input("Digite os minutos: "))
somah = h1 + h2
somam = m1 + m2
if somah > 12 and somah < 24:
    somah -=12
else:
    if somah > 24:
        somah -=24
    if somah > 12:
        somah -=12
if somam > 59:
    somah +=1
    somam -=60
print(f"{somah} Horas e {somam} Minutos")
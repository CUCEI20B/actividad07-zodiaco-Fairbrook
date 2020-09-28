def getSigno(mes, dia):
    if(mes>12 or mes<1):
        raise Exception("Mes fuera del rango")
    if(dia>31 or dia<1):
        raise Exception("Dia fuera del rango")

    signos = ["aries", "tauro", "geminis", "cancer", "leo", "virgo",
              "libra", "escorpio", "sagitario", "capricornio", "acuario", "Piscis"]
    if(mes == 1):
        return signos[9 + dia//21]
    if(mes == 2):
        return signos[10 + dia//19]
    if(mes <= 5):
        return signos[mes-4 + dia//21]
    if(mes == 6):
        return signos[2 + dia//22]
    if(mes <= 11):
        return signos[mes-4 + dia//23]
    return signos[8 + dia//22]


dia = int(input())
mes = int(input())
print(getSigno(mes,dia))
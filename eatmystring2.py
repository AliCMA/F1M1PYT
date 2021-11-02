def functievandestring(s):   
    s = s[0:len(s)-1]
    if len(s) != 0:
        print(s)
        functievandestring(s)
    elif len(s) == 0:
        print('')
        return

zin = "Hallo ik ben een string en ik wordt opgegeten door een speciaal progamma!"
    
extratje = "Ik ben Ali Celiksu"
functievandestring(zin)
functievandestring(extratje)

print("Ik ben opgegeten :)")
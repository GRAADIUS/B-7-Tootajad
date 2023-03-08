from File import *
toolised=["Nadja", "Natalja", "Igor", "Mark", "Olga"]
sunniaasta=[1800, 2000, 1995, 5, 5]
toolised, sunniaasta=tootajad(toolised, sunniaasta)
while True:
    print(toolised)
    print(sunniaasta)
    menu=int(input("valik:\n1-pension\n2-keskmine tootajate aasta\n3-tipptoolised\n4-tootaja otsimine sunnikuupaeva jargi\n5-juhutooline\n"))
    if menu == 0:
        break                                                                               
    elif menu == 1:
        pen=pension(toolised, sunniaasta)
        print(pen)
    elif menu == 2:
        sred=avg(sunniaasta)
        print(sred)
    elif menu== 3:
        aeg=sort(toolised, sunniaasta)
        print(aeg)
    elif menu== 4:
        sss=nimi(toolised, sunniaasta)
        print(sss)
    elif menu== 5:
        t,s=random(toolised, sunniaasta)
        print(t,s)
from tkinter import *
import random
import time
import threading

mundo = Tk()
mundo.title("Mario Bros")
mundo.resizable (0,0)
mundo.geometry("800x600+0+0")

#Crear mundo

#Importar tuberías
canvas= Canvas(mundo,width=800,height=600, bg= "black")
Tub1 = PhotoImage (file="Tuberia derecha arriba.gif")
canvas.create_image (750,120,image= Tub1)
Tub2 = PhotoImage (file="Tuberia izquierda arriba.gif")
canvas.create_image (52,120,image= Tub2)
Tub3 = PhotoImage (file="Tuberia derecha abajo.gif")
canvas.create_image (770,550,image= Tub3)
Tub4 = PhotoImage (file="Tuberia izquierda abajo.gif")
canvas.create_image (36,550,image= Tub4)
lui01= PhotoImage (file="luigi.gif")

#POW & Powers up
pow1= PhotoImage(file="POW1.gif")
pow2=PhotoImage(file="POW2.gif")
pow3=PhotoImage(file="POW3.gif")
starR=PhotoImage(file="star1.gif")
vida=PhotoImage(file="1UP.gif")

#Vida Luigi
lhead=PhotoImage(file="LHEAD.gif")
poww= canvas.create_image(400,438,image=pow1)

#Vida Mario
mhead=PhotoImage(file="MHEAD.gif")

#Movimientos de Luigi
ld1= PhotoImage(file="LD1.gif")
ld2=PhotoImage(file="LD2.gif")
ld3=PhotoImage(file="LD3.gif")
ld4=PhotoImage(file="LD4.gif")
ljd=PhotoImage(file="LJUMPD.gif")
lji= PhotoImage(file="LJUMPI.gif")
li1=PhotoImage(file="LI1.gif")
li2= PhotoImage(file="LI2.gif")
li3= PhotoImage(file="LI3.gif")
li4=PhotoImage(file="lI4.gif")
ldie=PhotoImage(file="lDIE.gif")
ltdi= PhotoImage(file="LTURNDI.gif")
ltid= PhotoImage(file="LTURNID.gif")

#Movimientos de Mario
md1=PhotoImage(file="MD1.gif")
md2=PhotoImage(file="MD2.gif")
md3=PhotoImage(file="MD3.gif")
md4=PhotoImage(file="MD4.gif")
mjd=PhotoImage(file="MJUMPD.gif")
mji= PhotoImage(file="MJUMPI.gif")
mi1=PhotoImage(file="MI1.gif")
mi2= PhotoImage(file="MI2.gif")
mi3= PhotoImage(file="MI3.gif")
mi4=PhotoImage(file="MI4.gif")
mdie=PhotoImage(file="MDIE.gif")
mtdi= PhotoImage(file="MTURNDI.gif")
mtid= PhotoImage(file="MTURNID.gif")


#Enemigos
#Mosca
fly1=PhotoImage(file="FLY2.gif")
fly2= PhotoImage(file="FLY3.gif")
fly3= PhotoImage(file="FLY4.gif")
fly4=PhotoImage(file="FLY1.gif")

#Tortuga roja
trd1= PhotoImage(file="TRD1.gif")
trd2= PhotoImage(file="TRD2.gif")
tri1= PhotoImage(file="TRI1.gif")
tri2= PhotoImage(file="TRI2.gif")

#Tortuga Verde
tvd1= PhotoImage(file="TVD1.gif")
tvd2= PhotoImage(file="TVD2.gif")
tvi1= PhotoImage(file="TVI1.gif")
tvi2= PhotoImage(file="TVI2.gif")

#Slipice
fd2= PhotoImage(file="MBS.gif")
fi2=PhotoImage(file="FI2.gif")

def CuadradosDeLaPlataforma (x1,x2,x3,x4):
    """
    Procedimiento para crear los cuadrados de la platafoma del luigi
    """
    global canvas
    canvas.create_polygon(x1,605,x2,580,x3,580,x4,605,outline= "darkred", fill = "brown")

poscuadro=0
NumCuadrados = 1    
while (NumCuadrados <= 41):
    CuadradosDeLaPlataforma(0+poscuadro,0+poscuadro, 20+poscuadro, 20+poscuadro)
    poscuadro += 20
    NumCuadrados +=1

def CuadradosDelSegundoNivel (x1,x2,x3,x4):
    """
    Procedimineto para crear los cuadrados del segundo nivel
    """
    global canvas
    canvas.create_polygon (x1,460, x2,440, x3, 440, x4,460, outline="blue", fill= "cyan")

poscuadrado2 =0
NumCuadrados2 = 1
while (NumCuadrados2 <=14):
    CuadradosDelSegundoNivel (0+poscuadrado2,0+poscuadrado2, 20+poscuadrado2, 20+poscuadrado2)
    NumCuadrados2 +=1
    poscuadrado2 += 20

poscuadro2 = 0
NumCuadros2 = 1
while (NumCuadros2 <=14):
    CuadradosDelSegundoNivel (520+poscuadro2,520+poscuadro2, 540+poscuadro2, 540+poscuadro2)
    NumCuadros2 +=1
    poscuadro2 += 20

def CuadradosDelTercerNivel (x1,x2,x3,x4):
    """
    Procedimineto para crear los cuadrados del tercer nivel
    """
    global canvas
    canvas.create_polygon (x1,340, x2,320, x3, 320, x4,340, outline="blue", fill= "cyan")

poscuadrado3 =0
NumCuadrados3 = 1
while (NumCuadrados3 <=8):
    CuadradosDelTercerNivel (0+poscuadrado3,0+poscuadrado3, 20+poscuadrado3, 20+poscuadrado3)
    NumCuadrados3 +=1
    poscuadrado3 += 20

poscuadro3 = 0
NumCuadros3 = 1
while (NumCuadros3 <=8):
    CuadradosDelTercerNivel (640+poscuadro3,640+poscuadro3, 660+poscuadro3, 660+poscuadro3)
    NumCuadros3 +=1
    poscuadro3 += 20


def CuadradosDelTercerNivelMitad (x1,x2,x3,x4):
    """
    Procedimineto para crear los cuadrados del tercer nivel plataforma del centro
    """
    global canvas
    canvas.create_polygon (x1,320, x2,300, x3, 300, x4,320, outline="blue", fill= "cyan")

poscuadrado3m =0
NumCuadrados3m = 1
while (NumCuadrados3m <=14):
    CuadradosDelTercerNivelMitad (260+poscuadrado3m,260+poscuadrado3m, 280+poscuadrado3m, 280+poscuadrado3m)
    NumCuadrados3m +=1
    poscuadrado3m += 20

def CuadradosDelCuartoNivel (x1,x2,x3,x4):
    """
    Procedimineto para crear los cuadrados del cuartoNivel
    """
    global canvas
    canvas.create_polygon (x1,180, x2,160, x3, 160, x4,180, outline="blue", fill= "cyan")

poscuadrado4 =0
NumCuadrados4 = 1
while (NumCuadrados4 <=17):
    CuadradosDelCuartoNivel (0+poscuadrado4,0+poscuadrado4, 20+poscuadrado4, 20+poscuadrado4)
    NumCuadrados4 +=1
    poscuadrado4 += 20

poscuadro4 = 0
NumCuadros4 = 1
while (NumCuadros4 <=17):
    CuadradosDelCuartoNivel (460+poscuadro4,460+poscuadro4, 480+poscuadro4, 480+poscuadro4)
    NumCuadros4 +=1
    poscuadro4 += 20


hmax = False
Muert1=0
Muert2=0
Muert3=0
parc=False
parc1=False
parc2=False
presionado = [0,0,0,0]
powestado=True
puntajeLui=0
scoreL= canvas.create_text(120,20,fill="White",font=("Charlemagne Std",14),text=("Puntaje","Luigi:",puntajeLui))
player1= canvas.create_text(134,40,fill="White",font=("Charlemagne Std",14),text=("Jugador","1:"))

puntajeMar=0
player2= canvas.create_text(624,40,fill="White",font=("Charlemagne Std",14),text=("Jugador","2:"))
scoreM= canvas.create_text(620,20,fill="White",font=("Charlemagne Std",14),text=("Puntaje","Mario:",puntajeMar))
#Saltos del personaje

def saltar ():
    """
    Procedimiento para que luigi realice un salto
    """
    
    global hmax,parc,parc1,parc2,Muert1,Muert2,Muert3,canvas, mundo, luigi,posini,Ldie,posact,ShellcreeperTI,continuarV,SidestepperTI,muerto4RS,muerto4RS1
    global SlipiceTI,FigtherflyTI,continuarR,continuarF,muertoS,continuarS,SlipiceTI,continuarV1,continuarV2,muertoV1,muertoV2,ShellcreeperTD,ShellcreeperTD1
    global continuarR1,muertoR1,continuarR2,muertoR2,SidestepperTI1,SidestepperTD,continuarF1,muertoF1,figtherflyTD,continuarS1,muertoS1,SlipiceTD,poww,powestado,puntajeLui,scoreL
    posact=canvas.coords(luigi)
    if (Ldie==False and muertoV==False and canvas.coords(luigi)[1]-50 <= canvas.coords(ShellcreeperTI)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(ShellcreeperTI)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(ShellcreeperTI)[0]+40)): 
        continuarV= False
    elif (Ldie==False and muertoV1==False and canvas.coords(luigi)[1]-50 <= canvas.coords(ShellcreeperTD)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(ShellcreeperTD)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(ShellcreeperTD)[0]+40)):
        continuarV1= False
    elif (Ldie==False and muertoV2==False and canvas.coords(luigi)[1]-50 <= canvas.coords(ShellcreeperTD1)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(ShellcreeperTD1)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(ShellcreeperTD1)[0]+40)):
        continuarV2= False

    elif (Ldie==False and muertoR==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SidestepperTI)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SidestepperTI)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SidestepperTI)[0]+40)):
        parc=True
        if Muert1>=1:
            continuarR= False
    elif (Ldie==False and muertoR1==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SidestepperTD)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SidestepperTD)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SidestepperTD)[0]+40)):
        parc1=True
        if Muert2>=1:
            continuarR1= False
    elif (Ldie==False and muertoR2==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SidestepperTI1)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SidestepperTI1)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SidestepperTI1)[0]+40)):
        parc2=True
        if Muert3>=1:
            continuarR2= False
        
    elif (Ldie==False and muertoF==False and canvas.coords(luigi)[1]-50 <= canvas.coords(FigtherflyTI)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(FigtherflyTI)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(FigtherflyTI)[0]+40)):
        continuarF= False
    elif (Ldie==False and muertoF1==False and canvas.coords(luigi)[1]-50 <= canvas.coords(FigtherflyTD)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(FigtherflyTD)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(FigtherflyTD)[0]+40)):
        continuarF1= False
            
    elif (Ldie==False and muertoS==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SlipiceTI)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SlipiceTI)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SlipiceTI)[0]+40)):
        continuarS= False
        canvas.delete(SlipiceTI)
        SlipiceTI=canvas.create_polygon(0,0,0,0)
        puntajeLui+=500
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
        muertoS= True
        muerto4RS=True
    elif (Ldie==False and muertoS1==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SlipiceTD)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SlipiceTD)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SlipiceTD)[0]+40)):
        continuarS1= False
        canvas.delete(SlipiceTD)
        SlipiceTD=canvas.create_polygon(0,0,0,0)
        puntajeLui+=500
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
        muertoS1= True
        muerto4RS1=True


    if (Ldie==False and continuarV== True and muertoV==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTI)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarV1== True and muertoV1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarV2== True and muertoV2==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTD1)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTD1)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD1)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarR==True and muertoR==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTI)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarR1==True and muertoR1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTD)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTD)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarR2==True and muertoR2==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTI1)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTI1)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI1)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarF==True and muertoF==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(FigtherflyTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(FigtherflyTI)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTI)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarF1==True and muertoF1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(FigtherflyTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(FigtherflyTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTD)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarS==False and muertoS==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SlipiceTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SlipiceTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SlipiceTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SlipiceTI)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarS1==False and muertoS1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SlipiceTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SlipiceTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SlipiceTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SlipiceTD)[1]+15):
        Ldie=True
        muertelui()
    
    if (Ldie==False and posini[1]+30 ==580):

        if (posact[1]+30 > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,0,-10)
            if (posact[1]-30 == 460 and (posact[0]-18 <280 or posact[0]+18 >520)): ##salto limitado al encontrar segunda plataforma
                hmax= True
            elif (powestado==True and posact[1]-30==460 and (posact[0]-18>=canvas.coords(poww)[0]-48 and posact[0]+18<=canvas.coords(poww)[0]+48)):
                hmax=True
                POW()
            mundo.after(10,saltar)
        else:
            
            hmax= True
            if (posact [1]+30 < 580):            
                canvas.move(luigi,0,10)
                mundo.after(10,saltar)

    elif (Ldie==False and posini[1]+30 ==440): ##validamos que esta en la segunda plataforma

        if (posact[1]+30  > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,0,-10)
            if ((posact[1]-30 == 340 and (posact[0]-18 <160 or posact[0]+18 >640)) or (posact[1]-30 == 320 and (posact[0]-18 <540 and posact[0]+18 >260)) ): ##salto limitado al encontrar tercera plataforma
                hmax= True
            mundo.after(10,saltar)
        else:
            hmax= True
            if (posact [1]+30  < 440):            
                canvas.move(luigi,0,10)
                mundo.after(10,saltar)

    elif (Ldie==False and posini[1]+30 ==300): ##validamos que esta en la tercera plataforma central
        if (canvas.coords(luigi)[1]-50 <= canvas.coords(ShellcreeperTI)[1]+25 and (canvas.coords(luigi)[0]-20>= canvas.coords(ShellcreeperTI)[0]-30 and canvas.coords(luigi)[0]+20 <= canvas.coords(ShellcreeperTI)[0]+30)):
            canvas.move(ShellcreeperTI,0,0)
            continuar= False
            mundo.after(10,saltar)
        if (posact[1]+30 > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,0,-10)
            if (posact[1]-30 == 180 and (posact[0]-18 <340 or posact[0]+18 >460)): ##salto limitado al encontrar segunda plataforma
                hmax= True
            mundo.after(10,saltar)
        else:
            hmax= True
            if (posact [1]+30 < 300):            
                canvas.move(luigi,0,10)
                mundo.after(10,saltar)

    elif (Ldie==False and posini[1]+30 ==320): ##validamos que esta en la tercera plataforma laterales
        if (canvas.coords(luigi)[1]-50 <= canvas.coords(ShellcreeperTI)[1]+25 and (canvas.coords(luigi)[0]-20>= canvas.coords(ShellcreeperTI)[0]-30 and canvas.coords(luigi)[0]+20 <= canvas.coords(ShellcreeperTI)[0]+30)):
            canvas.move(ShellcreeperTI,0,0)
            continuar= False
            mundo.after(10,saltar)
            ShellcreeperD() 
        if (posact[1]+30  > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,0,-10)
            if (posact[1]-30 == 180 and (posact[0]-18 <340 or posact[0]+18 >460)): ##salto limitado al encontrar segunda plataforma
                hmax= True
            mundo.after(10,saltar)
        else:
            hmax= True
            if (posact [1]+30  < 320):            
                canvas.move(luigi,0,10)
                mundo.after(10,saltar)

    elif (Ldie==False and posini[1]+30 ==160): ##validamos que esta en la cuarta plataforma

        if (posact[1]+30  > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,0,-10)
            
            mundo.after(10,saltar)
        else:
            hmax= True
            if (posact [1]+30  < 160):            
                canvas.move(luigi,0,10)
                mundo.after(10,saltar)

def saltar2 ():
    """
    Procedimiento que realiza el salto en parabola a la derecha
    """
    global hmax,parc,parc1,parc2,Muert1,Muert2,Muert3, canvas, mundo,luigi,posini,posact,Ldie,ShellcreeperTI,continuarV,muerto4RS,muerto4RS1
    global SidestepperTI,SlipiceTI,FigtherflyTI,continuarR,continuarF,muertoS,continuarS,SlipiceTI,continuarV1,continuarV2,muertoV1,muertoV2,ShellcreeperTD,ShellcreeperTD1
    global continuarR1,muertoR1,continuarR2,muertoR2,SidestepperTI1,SidestepperTD,continuarF1,muertoF1,figtherflyTD,continuarS1,muertoS1,SlipiceTD,puntajeLui,scoreL
    
    posact=canvas.coords(luigi)
    if (Ldie==False and muertoV==False and canvas.coords(luigi)[1]-50 <= canvas.coords(ShellcreeperTI)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(ShellcreeperTI)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(ShellcreeperTI)[0]+40)): 
        continuarV= False
    elif (Ldie==False and muertoV1==False and canvas.coords(luigi)[1]-50 <= canvas.coords(ShellcreeperTD)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(ShellcreeperTD)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(ShellcreeperTD)[0]+40)):
        continuarV1= False
    elif (Ldie==False and muertoV2==False and canvas.coords(luigi)[1]-50 <= canvas.coords(ShellcreeperTD1)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(ShellcreeperTD1)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(ShellcreeperTD1)[0]+40)):
        continuarV2= False

    elif (Ldie==False and muertoR==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SidestepperTI)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SidestepperTI)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SidestepperTI)[0]+40)):
        parc=True
        if Muert1>=1:
            continuarR= False
    elif (Ldie==False and muertoR1==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SidestepperTD)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SidestepperTD)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SidestepperTD)[0]+40)):
        parc1=True
        if Muert2>=1:
            continuarR1= False
    elif (Ldie==False and muertoR2==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SidestepperTI1)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SidestepperTI1)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SidestepperTI1)[0]+40)):
        parc2=True
        if Muert3>=1:
            continuarR2= False
        
    elif (Ldie==False and muertoF==False and canvas.coords(luigi)[1]-50 <= canvas.coords(FigtherflyTI)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(FigtherflyTI)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(FigtherflyTI)[0]+40)):
        continuarF= False
    elif (Ldie==False and muertoF1==False and canvas.coords(luigi)[1]-50 <= canvas.coords(FigtherflyTD)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(FigtherflyTD)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(FigtherflyTD)[0]+40)):
        continuarF1= False
            
    elif (Ldie==False and muertoS==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SlipiceTI)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SlipiceTI)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SlipiceTI)[0]+40)):
        continuarS= False
        canvas.delete(SlipiceTI)
        SlipiceTI=canvas.create_polygon(0,0,0,0)
        puntajeLui+=500
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
        muertoS= True
        muerto4RS=True
    elif (Ldie==False and muertoS1==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SlipiceTD)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SlipiceTD)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SlipiceTD)[0]+40)):
        continuarS1= False
        canvas.delete(SlipiceTD)
        SlipiceTD=canvas.create_polygon(0,0,0,0)
        puntajeLui+=500
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
        muertoS1= True
        muerto4RS1=True

    if (Ldie==False and continuarV== True and muertoV==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTI)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarV1== True and muertoV1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarV2== True and muertoV2==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTD1)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTD1)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD1)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarR==True and muertoR==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTI)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarR1==True and muertoR1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTD)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTD)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarR2==True and muertoR2==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTI1)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTI1)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI1)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarF==True and muertoF==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(FigtherflyTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(FigtherflyTI)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTI)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarF1==True and muertoF1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(FigtherflyTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(FigtherflyTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTD)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarS==False and muertoS==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SlipiceTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SlipiceTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SlipiceTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SlipiceTI)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarS1==False and muertoS1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SlipiceTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SlipiceTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SlipiceTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SlipiceTD)[1]+15):
        Ldie=True
        muertelui()

    if (Ldie==False and posini[1]+30 ==580): ##validamos que esta en la primera plataforma

        if (posact[1]+30  > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,4,-10)
            mundo.after(10,saltar2)
            if (posact[1]-30== 460 and (posact[0]-18 <280 or posact[0]+18 >520)): ##salto limitado al encontrar segunda plataforma
                hmax= True
                mundo.after(10,saltar2)
        else:
            hmax= True
            if (posact [1]+30  < 580 and posact[0]+18 >520 and posact[1]+30 ==440):            
                canvas.move(luigi,0,0)
                return None
            elif(posact [1]+30 < 580 or (posact[0]+18 >=520 and posact[1]+30 ==440)):
                canvas.move(luigi,4,10)
                mundo.after(10,saltar2)

    elif (Ldie==False and posini[1]+30 >=440 and posini[1]+30 <580): ##validamos que esta en la segunda plataforma

        if (posact[1]+30 >= 440 and posact[1]+30 <580 and (posact[0]-18 >280 and posact[0]+18 <520)): ##validar espacio en blanco
            canvas.move(luigi,0,10)            
            mundo.after(10,saltar2)
            
            
        elif (posact[1]+30  > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,4,-10)
            mundo.after(10,saltar2)
            if ((posact[1]-30 == 340 and (posact[0]-18 <160 or posact[0]+18 >640)) or (posact[1]-30== 300 and (posact[0]-18 <540 and posact[0]+18>260 ))): ##salto limitado al encontrar tercera plataforma
                hmax= True
                mundo.after(10,saltar2)
    
        else:
            hmax= True
            if ((posact [1]+30 < 440 and posact[0]+18 >640 and posact[1]+30 ==320) or (posact [1]+30 < 440 and posact[0]+18 >260 and posact[0]-18 <540 and posact[1]+30 ==300)):            
                canvas.move(luigi,0,0)
                return None
            elif((posact [1]+30 < 440 or (posact[0]+18 >=640 and posact[1]+30 ==320))or (posact [1]+30 < 440 or (posact[0]+18>260 and posact[0]-18 <540 and posact[1]+30==300))):
                canvas.move(luigi,4,10)
                mundo.after(10,saltar2)

    elif (Ldie==False and posini[1]+30 ==300): ##validamos que esta en la tercera plataforma central
        if (posact[1]+30 >= 300 and posact[1]+30 <440 and (posact[0]-18 >540 and posact[0]+18 <640)): ##validar espacio en blanco a la derecha plataforma
            canvas.move(luigi,0,10)            
            mundo.after(10,saltar2)         
                

        elif (posact[1]+30 > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,4,-10)
            if (posact[1]-30 == 180 and (posact[0]-18 <340 or posact[0]+18 >460)): ##salto limitado al encontrar cuarta plataforma
                hmax= True
            mundo.after(10,saltar2)
        else:
            hmax= True
            if (posact [1]+30 == 300 and posact[0]+18 >640): ##validar si desciende a plataforma derecha        
                canvas.move(luigi,0,20)
                mundo.after(10,saltar2)
            elif(posact [1]+30 < 300 and posact[0]+20 >460 and posact[1]+30==160):
                canvas.move(luigi,0,0)
                return None
            elif(posact [1]+30 < 300 or (posact[0]+18 >=460 and posact[1]+30 ==160)):
                canvas.move(luigi,4,10)
                mundo.after(10,saltar2)

    elif (Ldie==False and posini[1]+30 ==320): ##validamos que esta en la tercera plataforma laterales

        if (posact[1]+30 >= 320 and posact[1]+30 <440 and (posact[0]-18 >160 and posact[0]+18 <260)): ##validar espacio en blanco a la derecha plataforma izquierda tercer nivel
            canvas.move(luigi,0,10)            
            mundo.after(10,saltar2)

        elif (posact[1]+30 > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,4,-10)
            if (posact[1]-30== 180 and (posact[0]-18 <340 or posact[0]+18 >460)): ##salto limitado al encontrar cuarta plataforma
                hmax= True
            mundo.after(10,saltar2)
        else:
            hmax= True
            if (posact [1]+30 < 320 and posact[0]+18 >260 and posact[0]-18 <540 and posact[1]+30 ==300): ##validar si asciende a siguiente plataforma           
                canvas.move(luigi,0,0)
                return None
            elif(posact [1]+30 < 320 or (posact[0]+18 >=260 and posact[0]-18 <540 and posact[1]+30 ==300)):
                canvas.move(luigi,4,10)
                mundo.after(10,saltar2)

    elif (Ldie==False and posini[1]+30 ==160): ##validamos que esta en la cuarta plataforma

        if (posact[1]+30 >= 160 and posact[1]+30 <300 and (posact[0]-18 >340 and posact[0]+18<460)): ##validar espacio en blanco a la derecha plataforma izquierda cuarto nivel
            canvas.move(luigi,0,10)            
            mundo.after(10,saltar2)

        elif (posact[1]+30 > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,4,-10)
            
            mundo.after(10,saltar2)
        else:
            hmax= True
            if (posact [1]+30 < 160):            
                canvas.move(luigi,4,10)
                mundo.after(10,saltar2)

def saltar3 ():
    """
    Procedimiento que realiza el salto en parabola a la izquierda
    """
    global hmax,parc,parc1,parc2,Muert1,Muert2,Muert3, canvas, mundo,luigi,posini,posact,Ldie,ShellcreeperTI,continuarV,muerto4RS,muerto4RS1
    global SidestepperTI,SlipiceTI,FigtherflyTI,continuarR,continuarF,muertoS,continuarS,SlipiceTI,continuarV1,continuarV2,muertoV1,muertoV2,ShellcreeperTD,ShellcreeperTD1,continuarR1
    global muertoR1,continuarR2,muertoR2,SidestepperTI1,SidestepperTD,continuarF1,muertoF1,figtherflyTD,continuarS1,muertoS1,SlipiceTD,puntajeLui,scoreL
    posact=canvas.coords(luigi)
    if (Ldie==False and muertoV==False and canvas.coords(luigi)[1]-50 <= canvas.coords(ShellcreeperTI)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(ShellcreeperTI)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(ShellcreeperTI)[0]+40)): 
        continuarV= False
    elif (Ldie==False and muertoV1==False and canvas.coords(luigi)[1]-50 <= canvas.coords(ShellcreeperTD)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(ShellcreeperTD)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(ShellcreeperTD)[0]+40)):
        continuarV1= False
    elif (Ldie==False and muertoV2==False and canvas.coords(luigi)[1]-50 <= canvas.coords(ShellcreeperTD1)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(ShellcreeperTD1)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(ShellcreeperTD1)[0]+40)):
        continuarV2= False

    elif (Ldie==False and muertoR==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SidestepperTI)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SidestepperTI)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SidestepperTI)[0]+40)):
        parc=True
        if Muert1>=1:
            continuarR= False
    elif (Ldie==False and muertoR1==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SidestepperTD)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SidestepperTD)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SidestepperTD)[0]+40)):
        parc1=True
        if Muert2>=1:
            continuarR1= False
    elif (Ldie==False and muertoR2==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SidestepperTI1)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SidestepperTI1)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SidestepperTI1)[0]+40)):
        parc2=True
        if Muert3>=1:
            continuarR2= False
        
    elif (Ldie==False and muertoF==False and canvas.coords(luigi)[1]-50 <= canvas.coords(FigtherflyTI)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(FigtherflyTI)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(FigtherflyTI)[0]+40)):
        continuarF= False
    elif (Ldie==False and muertoF1==False and canvas.coords(luigi)[1]-50 <= canvas.coords(FigtherflyTD)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(FigtherflyTD)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(FigtherflyTD)[0]+40)):
        continuarF1= False
            
    elif (Ldie==False and muertoS==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SlipiceTI)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SlipiceTI)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SlipiceTI)[0]+40)):
        continuarS= False
        canvas.delete(SlipiceTI)
        SlipiceTI=canvas.create_polygon(0,0,0,0)
        puntajeLui+=500
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
        muertoS= True
        muerto4RS=True
    elif (Ldie==False and muertoS1==False and canvas.coords(luigi)[1]-50 <= canvas.coords(SlipiceTD)[1]+25 and (canvas.coords(luigi)[0]-18>= canvas.coords(SlipiceTD)[0]-40 and canvas.coords(luigi)[0]+18 <= canvas.coords(SlipiceTD)[0]+40)):
        continuarS1= False
        canvas.delete(SlipiceTD)
        SlipiceTD=canvas.create_polygon(0,0,0,0)
        puntajeLui+=500
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
        muertoS1= True
        muerto4RS1=True

    if (Ldie==False and continuarV== True and muertoV==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTI)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarV1== True and muertoV1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarV2== True and muertoV2==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTD1)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTD1)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD1)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarR==True and muertoR==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTI)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarR1==True and muertoR1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTD)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTD)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarR2==True and muertoR2==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTI1)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTI1)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI1)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarF==True and muertoF==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(FigtherflyTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(FigtherflyTI)[0]+22))and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTI)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarF1==True and muertoF1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(FigtherflyTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(FigtherflyTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTD)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarS==False and muertoS==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SlipiceTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SlipiceTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SlipiceTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SlipiceTI)[1]+15):
        Ldie=True
        muertelui()
    elif (Ldie==False and continuarS1==False and muertoS1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SlipiceTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SlipiceTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SlipiceTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SlipiceTD)[1]+15):
        Ldie=True
        muertelui()
    
    if (Ldie==False and posini[1]+30==580): ##validamos que esta en la primera plataforma

        if (posact[1]+30 > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,-4,-10)
            if (posact[1]-30 == 460 and (posact[0]-18 <280 or posact[0]+18 >520)): ##salto limitado al encontrar segunda plataforma
                hmax= True
            mundo.after(10,saltar3)
        else:
            hmax= True
            if (posact [1]+30 < 580 and posact[0]-18 <280 and posact[1]+30 ==440):            
                canvas.move(luigi,0,0)
                return None
            elif(posact [1]+30 < 580 or (posact[0]-18 <=280 and posact[1]+30 ==440)):
                canvas.move(luigi,-4,10)
                mundo.after(10,saltar3)

    elif (Ldie==False and posini[1]+30 ==440): ##validamos que esta en la segunda plataforma

        if (posact[1]+30 >= 440 and posact[1]+30<580 and (posact[0]-18>280 and posact[0]+18<520)): ##validar espacio en blanco
            canvas.move(luigi,0,10)            
            mundo.after(10,saltar3)

        elif (posact[1]+30 > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,-4,-10)
            if ((posact[1]-30== 340 and (posact[0]-18<160 or posact[0]+18>640)) or (posact[1]-30 == 300 and (posact[0]-18 <540 and posact[0]+18>260 ))): ##salto limitado al encontrar tercera plataforma
                hmax= True
            mundo.after(10,saltar3)
        else:
            hmax= True
            if ((posact [1]+30 < 440 and posact[0]-18 <160 and posact[1]+30 ==320) or (posact [1]+30 < 440 and posact[0]+18 >260 and posact[0]-18<540 and posact[1]+30==300)):            
                canvas.move(luigi,0,0)
                return None
            elif((posact [1]+30 < 440 or (posact[0]-18<=160 and posact[1]+30==320))or (posact [1]+30 < 440 or (posact[0]+18 >260 and posact[0]-18 <540 and posact[1]+30==300))):
                canvas.move(luigi,-4,10)
                mundo.after(10,saltar3)

    elif (Ldie==False and posini[1]+30 ==300): ##validamos que esta en la tercera plataforma central

        if (posact[1]+30 >= 300 and posact[1]+30 <440 and (posact[0]-18>160 and posact[0]+18<260)): ##validar espacio en blanco a la izquierda plataforma
            canvas.move(luigi,0,10)            
            mundo.after(10,saltar3)     

        elif (posact[1]+30 > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,-4,-10)
            if (posact[1]-30 == 180 and (posact[0]-18<340 or posact[0]+18 >460)): ##salto limitado al encontrar cuarta plataforma
                hmax= True
            mundo.after(10,saltar3)
        else:
            hmax= True
            if (posact [1]+30 == 300 and posact[0]-18 <160): ##validar si desciende a plataforma izquierda        
                canvas.move(luigi,0,20)
                mundo.after(10,saltar3)
            elif (posact [1]+30 < 300 and posact[0]-18 <340 and posact[1]+30==160): ##validar si asciende a siguiente plataforma           
                canvas.move(luigi,0,0)
                return None
            elif(posact [1]+30 < 300 or (posact[0]-18<=340 and posact[1]+30==160)):
                canvas.move(luigi,-4,10)
                mundo.after(10,saltar3)

    elif (Ldie==False and posini[1]+30 ==320): ##validamos que esta en la tercera plataforma laterales

        if (posact[1]+30 >= 320 and posact[1]+30 <440 and (posact[0]-18>540 and posact[0]+18<640)): ##validar espacio en blanco a la izquierda plataforma derecha tercer nivel
            canvas.move(luigi,0,10)            
            mundo.after(10,saltar3)

        elif (posact[1]+30 > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,-4,-10)
            if (posact[1]-30 == 180 and (posact[0]-18 <340 or posact[0]+18 >460)): ##salto limitado al encontrar cuarta plataforma
                hmax= True
            mundo.after(10,saltar3)
        else:
            hmax= True
            if (posact [1]+30 < 320 and posact[0]-18 <540 and posact[1]+30 ==300): ##validar si asciende a siguiente plataforma           
                canvas.move(luigi,0,0)
                return None
            elif(posact [1]+30 < 320 or (posact[0]-18 <=540 and posact[1]+30==300)):
                canvas.move(luigi,-4,10)
                mundo.after(10,saltar3)

    elif (Ldie==False and posini[1]+30 ==160): ##validamos que esta en la cuarta plataforma

        if (posact[1]+30 >= 160 and posact[1]+30 <300 and (posact[0]-18 >340 and posact[0]+18 <460)): ##validar espacio en blanco a la izquierda plataforma derecha cuarto nivel
            canvas.move(luigi,0,10)            
            mundo.after(10,saltar3)

        elif (posact[1]+30 > ((posini[1]+30)-160) and hmax==False):##salto ascendente en extension completa 160
            canvas.move(luigi,-4,-10)
            mundo.after(10,saltar3)
        else:
            hmax= True
            if (posact [1]+30 < 160):            
                canvas.move(luigi,-4,10)
                mundo.after(10,saltar3)
            
img= False
muerto4RV=False
muerto4RV1=False
muerto4RV2=False
muerto4RR=False
muerto4RR1=False
muerto4RR2=False
muerto4RF=False
muerto4RF1=False
muerto4RS=False
muerto4RS1=False
def mover2 ():
        """
        Procedimiento que realiza el movimiento a la derecha
        """
        global canvas,puntajeLui, scoreL,Ayuda,st,LifesL,Vidaslui,starEstado,Pulsadastar,mundo,vid,vidaEstado,Pulsadavida,st,FigtherflyTI,FigtherflyTD,muertoF,muerto4RV,muerto4RV1,muerto4RV2,muerto4RR,muerto4RR1,muerto4RR2,muerto4RF,muerto4RF1,luigi, posini, img,posact,Ldie,ShellcreeperTI,continuarV,muertoV,muertoR,continuarR,SidestepperTI,muertoF,continuarF,FigtherflyTI,muertoS,continuarS,SlipiceTI,continuarV1,continuarV2,muertoV1,muertoV2,ShellcreeperTD,ShellcreeperTD1,continuarR1,muertoR1,continuarR2,muertoR2,SidestepperTI1,SidestepperTD,continuarF1,muertoF1,figtherflyTD,continuarS1,muertoS1,SlipiceTD
        posact=canvas.coords(luigi)

        if muerto4RV==True and muerto4RV1==True and muerto4RV2==True and muerto4RR==True and muerto4RR1==True and muerto4RR2==True and muerto4RF==True and muerto4RF1==True and muerto4RS==True and muerto4RS1==True:
            print ("HAS GANADO")
            mundo.destroy()
        elif (Ldie==False and vidaEstado==True and Pulsadavida==False and canvas.coords(luigi)[0]+16>=canvas.coords(vid)[0]-30 and canvas.coords(luigi)[0]-16<=canvas.coords(vid)[0]+30 and canvas.coords(luigi)[1]+30<= canvas.coords(vid)[1]+37 and canvas.coords(luigi)[1]+30 >= canvas.coords(vid)[1]+20):
            Pulsadavida=True
            canvas.delete(vid)
            Vidaslui+=1

            canvas.delete(LifesL)
            LifesL=canvas.create_text(54,60,fill="Lime Green",font=("Charlemagne Std",12),text=("X"+ str (Vidaslui)))   
            
        elif (Ldie==False and starEstado==True and Pulsadastar==False and canvas.coords(luigi)[0]+16>=canvas.coords(st)[0]-30 and canvas.coords(luigi)[0]-16<=canvas.coords(st)[0]+30 and canvas.coords(luigi)[1]+30<= canvas.coords(st)[1]+37 and canvas.coords(luigi)[1]+30 >= canvas.coords (st)[1]+20):
            Pulsadastar=True
            canvas.delete(st)
            Ayuda= True
        elif (Ldie==False and (continuarV== False or Ayuda==True) and muertoV==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(ShellcreeperTI)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(ShellcreeperTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTI)[1]+15):
            canvas.delete(ShellcreeperTI)
            ShellcreeperTI= canvas.create_polygon(0,0,0,0)
            muerto4RV=True
            puntajeLui+=100
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoV= True
        elif (Ldie==False and (continuarV1== False or Ayuda==True) and muertoV1==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(ShellcreeperTD)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(ShellcreeperTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD)[1]+15):
            canvas.delete(ShellcreeperTD)
            ShellcreeperTD= canvas.create_polygon(0,0,0,0)
            muerto4RV1=True
            puntajeLui+=100
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoV1= True
        elif (Ldie==False and (continuarV2== False or Ayuda==True) and muertoV2==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(ShellcreeperTD1)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(ShellcreeperTD1)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD1)[1]+15):
            canvas.delete(ShellcreeperTD1)
            ShellcreeperTD1= canvas.create_polygon(0,0,0,0)
            muerto4RV2=True
            puntajeLui+=100
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoV2= True
        elif (Ldie==False and (continuarR== False or Ayuda==True) and muertoR==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(SidestepperTI)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(SidestepperTI)[0]+22))  and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI)[1]+15):
            canvas.delete(SidestepperTI)
            SidestepperTI=canvas.create_polygon(0,0,0,0)
            muerto4RR=True
            puntajeLui+=200
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoR= True
        elif (Ldie==False and (continuarR1== False or Ayuda==True) and muertoR1==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(SidestepperTD)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(SidestepperTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTD)[1]+15):
            canvas.delete(SidestepperTD)
            SidestepperTD=canvas.create_polygon(0,0,0,0)
            muerto4RR1=True
            puntajeLui+=200
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoR1= True
        elif (Ldie==False and (continuarR2== False or Ayuda==True) and muertoR2==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(SidestepperTI1)[0]-22) and(canvas.coords(luigi)[0]-16 <= canvas.coords(SidestepperTI1)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI1)[1]+15 ):
            canvas.delete(SidestepperTI1)
            SidestepperTI1=canvas.create_polygon(0,0,0,0)
            muerto4RR2=True
            puntajeLui+=200
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoR2= True

        elif (Ldie==False and (continuarF== False or Ayuda==True) and muertoF==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(FigtherflyTI)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(FigtherflyTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTI)[1]+15):
            canvas.delete(FigtherflyTI)
            FigtherflyTI= canvas.create_polygon(0,0,0,0)
            muerto4RF=True
            puntajeLui+=400
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoF= True
        elif (Ldie==False and (continuarF1== False or Ayuda==True )and muertoF1==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(FigtherflyTD)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(FigtherflyTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTD)[1]+15):
            canvas.delete(FigtherflyTD)
            FigtherflyTD= canvas.create_polygon(0,0,0,0)
            muerto4RF1=True
            puntajeLui+=400
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoF1= True
        elif (puntajeLui>=1000):
            puntajeLui=0
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            Vidaslui+=1
            canvas.delete(LifesL)
            LifesL=canvas.create_text(54,60,fill="Lime Green",font=("Charlemagne Std",12),text=("X"+ str (Vidaslui)))

        elif (Ldie==False and (continuarV== True and  Ayuda==False) and muertoV==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTI)[1]+15):
            Ldie=True
            muertelui()
        elif (Ldie==False and (continuarV1== True and  Ayuda==False) and muertoV1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD)[1]+15):
            Ldie=True
            muertelui()
        elif (Ldie==False and (continuarV2== True and  Ayuda==False) and muertoV2==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTD1)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTD1)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD1)[1]+15):
            Ldie=True
            muertelui()

        elif (Ldie==False and (continuarR==True and  Ayuda==False) and muertoR==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI)[1]+15):
            Ldie=True
            muertelui()
        elif (Ldie==False and (continuarR1==True and  Ayuda==False) and muertoR1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTD)[1]+15):
            Ldie=True
            muertelui()
        elif (Ldie==False and (continuarR2==True and  Ayuda==False) and muertoR2==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTI1)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTI1)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI1)[1]+15):
            Ldie=True
            muertelui()
            
        elif (Ldie==False and (continuarF==True and  Ayuda==False) and muertoF==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(FigtherflyTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(FigtherflyTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTI)[1]+15):
            Ldie=True
            muertelui()
        elif (Ldie==False and (continuarF1==True and  Ayuda==False) and muertoF1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(FigtherflyTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(FigtherflyTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTD)[1]+15):
            Ldie=True
            muertelui()

        elif (Ldie==False and (continuarS== True and  Ayuda==False) and muertoS==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SlipiceTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SlipiceTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SlipiceTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SlipiceTI)[1]+15):
            Ldie=True
            muertelui()
        elif (Ldie==False and (continuarS1==False and  Ayuda==False) and muertoS1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SlipiceTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SlipiceTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SlipiceTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SlipiceTD)[1]+15):
            Ldie=True
            muertelui()   
        if (Ldie==False and posini[1]+30==580): ##validamos que esta en la primera plataforma
            if (posact[1]+30 ==580 and posact[0]+30>=800):
                canvas.delete(luigi)
                luigi= canvas.create_image(20,550,anchor="center",image=lui01)
            elif (img== False):
                canvas.delete(luigi)
                luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=ld3)
                canvas.move(luigi,5,0)
                img= True
            elif (img==True):
                canvas.delete(luigi)
                luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=ld4)
                img= False
                canvas.move(luigi,5,0)
                
        elif (Ldie==False and posini[1]+30>=440 and posini[1]+30 <580): ##validamos que esta en la segunda plataforma
            if (posact[1]+30 ==440 and posact[0]+18>=800):
                canvas.delete(luigi)
                luigi= canvas.create_image(30,410,anchor="center",image=lui01)
            elif (posact[1]+30>= 440 and posact[1]+30<580 and (posact[0]-18>280 and posact[0]+18<520)): ##validar espacio en blanco
                canvas.move(luigi,0,10)            
                mundo.after(10,mover2)
            else:
                if (img== False):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=ld3)
                    canvas.move(luigi,5,0)
                    img= True
                elif (img==True):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=ld4)
                    img= False
                    canvas.move(luigi,5,0)


        elif (Ldie==False and posini[1]+30 >=320 ): ##validamos que esta en la tercera plataforma laterales
            if (posact[1]+30 ==320 and posact[0]+18>=800):
                canvas.delete(luigi)
                luigi= canvas.create_image(30,290,anchor="center",image=lui01)
            elif (posact[1]+30 >= 320 and posact[1]+30 <440 and (posact[0]-18 >160 and posact[0]+18 <260)): ##validar espacio en blanco a la derecha plataforma izquierda tercer nivel
                canvas.move(luigi,0,10)            
                mundo.after(10,mover2)

            else:
                if (img== False):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=ld3)
                    canvas.move(luigi,5,0)
                    img= True
                elif (img==True):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=ld4)
                    img= False
                    canvas.move(luigi,5,0)
        elif (Ldie==False and posini[1]+30 >=300): ##validamos que esta en la tercera plataforma central

            if (posact[1]+30 >= 300 and posact[1]+30 <440 and (posact[0]-18 >540 and posact[0]+18 <640)): ##validar espacio en blanco a la derecha plataforma
                canvas.move(luigi,0,10)            
                mundo.after(10,mover2)       
            else:
                if (img== False):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=ld3)
                    canvas.move(luigi,5,0)
                    img= True
                elif (img==True):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=ld4)
                    img= False
                    canvas.move(luigi,5,0)

        elif (Ldie==False and posini[1]+30 >=160): ##validamos que esta en la cuarta plataforma
            if (posact[1]+30 ==160 and posact[0]+18>=800):
                canvas.delete(luigi)
                luigi= canvas.create_image(30,130,anchor="center",image=lui01)
            elif (posact[1]+30 >= 160 and posact[1]+30 <300 and (posact[0]-18 >340 and posact[0]+18 <460)): ##validar espacio en blanco a la derecha plataforma izquierda cuarto nivel
                canvas.move(luigi,0,10)            
                mundo.after(10,mover2)

            else:
                if (img== False):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=ld3)
                    canvas.move(luigi,5,0)
                    img= True
                elif (img==True):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=ld4)
                    img= False
                    canvas.move(luigi,5,0)

def mover3 ():
        """
        Procedimiento que realiza el movimiento a la izquierda
        """
        global canvas,puntajeLui,Ayuda,Vidaslui,scoreL,mundo,luigi,FigtherflyTI,muertoF,muerto4RV,muerto4RV1,muerto4RV2,muerto4RR,muerto4RR1,muerto4RR2,muerto4RF,muerto4RF1, posini,posact,img,ShellcreeperTI,muertoV,continuarRV,Ldie,muertoR,continuarR
        global SidestepperTI,continuarF,muertoF,FighterflyTI,muertoS,continuarS,SlipiceTI,continuarV1,continuarV2,muertoV1,muertoV2,ShellcreeperTD,ShellcreeperTD1,continuarR1,muertoR1,continuarR2,muertoR2,SidestepperTI1,SidestepperTD
        global LifesL,continuarF1,muertoF1,FigtherflyTD,continuarS1,muertoS1,SlipiceTD,muertoV1,continuarV1,pulsadaStar,starr,starEstado,Pulsadastar,Pulsadavida,vid,vidaEstado,st
        posact=canvas.coords(luigi)
        if muerto4RV==True and muerto4RV1==True and muerto4RV2==True and muerto4RR==True and muerto4RR1==True and muerto4RR2==True and muerto4RF==True and muerto4RF1==True and muerto4RS==True and muerto4RS1==True:
            print ("HAS GANADO")
            mundo.destroy()
        elif (Ldie==False and vidaEstado==True and Pulsadavida==False and canvas.coords(luigi)[0]+16>=canvas.coords(vid)[0]-30 and canvas.coords(luigi)[0]-16<=canvas.coords(vid)[0]+30 and canvas.coords(luigi)[1]+30<= canvas.coords(vid)[1]+37 and canvas.coords(luigi)[1]+30 >= canvas.coords(vid)[1]+20):
            Pulsadavida=True
            canvas.delete(vid)
            Vidaslui+=1
            canvas.delete(LifesL)
            LifesL=canvas.create_text(54,60,fill="Lime Green",font=("Charlemagne Std",12),text=("X"+ str (Vidaslui)))   

            
        elif (Ldie==False and Pulsadastar==False and starEstado==True and canvas.coords(luigi)[0]+16>=canvas.coords(st)[0]-30 and canvas.coords(luigi)[0]-16<=canvas.coords(st)[0]+30 and canvas.coords(luigi)[1]+30<= canvas.coords(st)[1]+37 and canvas.coords(luigi)[1]+30 >= canvas.coords (st)[1]+20):
            Pulsadastar=True
            canvas.delete(st)
            Ayuda= True
        elif (Ldie==False and (continuarV== False or Ayuda==True) and muertoV==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(ShellcreeperTI)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(ShellcreeperTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTI)[1]+15):
            canvas.delete(ShellcreeperTI)
            ShellcreeperTI= canvas.create_polygon(0,0,0,0)
            muerto4RV=True
            puntajeLui+=100
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoV= True
        elif (Ldie==False and (continuarV1== False or Ayuda==True) and muertoV1==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(ShellcreeperTD)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(ShellcreeperTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD)[1]+15):
            canvas.delete(ShellcreeperTD)
            ShellcreeperTD= canvas.create_polygon(0,0,0,0)
            muerto4RV1=True
            puntajeLui+=100
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoV1= True
        elif (Ldie==False and (continuarV2== False or Ayuda==True) and muertoV2==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(ShellcreeperTD1)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(ShellcreeperTD1)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD1)[1]+15):
            canvas.delete(ShellcreeperTD1)
            ShellcreeperTD1= canvas.create_polygon(0,0,0,0)
            muerto4RV2=True
            puntajeLui+=100
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoV2= True
        elif (Ldie==False and (continuarR== False or Ayuda==True) and muertoR==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(SidestepperTI)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(SidestepperTI)[0]+22))  and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI)[1]+15):
            canvas.delete(SidestepperTI)
            SidestepperTI=canvas.create_polygon(0,0,0,0)
            muerto4RR=True
            puntajeLui+=200
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoR= True
        elif (Ldie==False and (continuarR1== False or Ayuda==True) and muertoR1==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(SidestepperTD)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(SidestepperTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTD)[1]+15):
            canvas.delete(SidestepperTD)
            SidestepperTD=canvas.create_polygon(0,0,0,0)
            muerto4RR1=True
            puntajeLui+=200
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoR1= True
        elif (Ldie==False and (continuarR2== False or Ayuda==True) and muertoR2==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(SidestepperTI1)[0]-22) and(canvas.coords(luigi)[0]-16 <= canvas.coords(SidestepperTI1)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI1)[1]+15 ):
            canvas.delete(SidestepperTI1)
            SidestepperTI1=canvas.create_polygon(0,0,0,0)
            muerto4RR2=True
            puntajeLui+=200
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoR2= True

        elif (Ldie==False and (continuarF== False or Ayuda==True) and muertoF==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(FigtherflyTI)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(FigtherflyTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTI)[1]+15):
            canvas.delete(FigtherflyTI)
            FigtherflyTI= canvas.create_polygon(0,0,0,0)
            muerto4RF=True
            puntajeLui+=400
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoF= True
        elif (Ldie==False and (continuarF1== False or Ayuda==True )and muertoF1==False and ((canvas.coords(luigi)[0]+16 >= canvas.coords(FigtherflyTD)[0]-22) and (canvas.coords(luigi)[0]-16 <= canvas.coords(FigtherflyTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTD)[1]+15):
            canvas.delete(FigtherflyTD)
            FigtherflyTD= canvas.create_polygon(0,0,0,0)
            muerto4RF1=True
            puntajeLui+=400
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            muertoF1= True
        elif (puntajeLui>=1000):
            puntajeLui=0
            canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
            Vidaslui+=1
            canvas.delete(LifesL)
            LifesL=canvas.create_text(54,60,fill="Lime Green",font=("Charlemagne Std",12),text=("X"+ str (Vidaslui)))

        elif (Ldie==False and (continuarV== True and  Ayuda==False) and muertoV==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTI)[1]+15):
            Ldie=True
            muertelui()
        elif (Ldie==False and (continuarV1== True and  Ayuda==False) and muertoV1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD)[1]+15):
            Ldie=True
            muertelui()
        elif (Ldie==False and (continuarV2== True and  Ayuda==False) and muertoV2==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTD1)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTD1)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(ShellcreeperTD1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(ShellcreeperTD1)[1]+15):
            Ldie=True
            muertelui()

        elif (Ldie==False and (continuarR==True and  Ayuda==False) and muertoR==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI)[1]+15):
            Ldie=True
            muertelui()
        elif (Ldie==False and (continuarR1==True and  Ayuda==False) and muertoR1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTD)[1]+15):
            Ldie=True
            muertelui()
        elif (Ldie==False and (continuarR2==True and  Ayuda==False) and muertoR2==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTI1)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTI1)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SidestepperTI1)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SidestepperTI1)[1]+15):
            Ldie=True
            muertelui()
            
        elif (Ldie==False and (continuarF==True and  Ayuda==False) and muertoF==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(FigtherflyTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(FigtherflyTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTI)[1]+15):
            Ldie=True
            muertelui()
        elif (Ldie==False and (continuarF1==True and  Ayuda==False) and muertoF1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(FigtherflyTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(FigtherflyTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(FigtherflyTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(FigtherflyTD)[1]+15):
            Ldie=True
            muertelui()

        elif (Ldie==False and (continuarS== True and  Ayuda==False) and muertoS==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SlipiceTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SlipiceTI)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SlipiceTI)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SlipiceTI)[1]+15):
            Ldie=True
            muertelui()
        elif (Ldie==False and (continuarS1==False and  Ayuda==False) and muertoS1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SlipiceTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SlipiceTD)[0]+22)) and canvas.coords(luigi)[1]+30<=canvas.coords(SlipiceTD)[1]+20 and canvas.coords(luigi)[1]+30>=canvas.coords(SlipiceTD)[1]+15):
            Ldie=True
            muertelui()   

        if (Ldie==False and posini[1]+ 30 ==580): ##validamos que esta en la primera plataforma
            if (posact[1]+30==580 and posact[0]-20<=0):
                canvas.delete(luigi)
                luigi= canvas.create_image(770,550,anchor="center",image=li1)
            elif (img==False):
                canvas.delete(luigi)
                luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=li3)
                canvas.move(luigi,-5,0)
                img=True
            elif(img==True):
                canvas.delete(luigi)
                luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=li4)
                canvas.move(luigi,-5,0)
                img=False
            

        elif (Ldie==False and posini[1]+30>=440 and posini[1]+30<580): ##validamos que esta en la segunda plataforma
            if (posact[1]+30==440 and posact[0]-20<=0):
                canvas.delete(luigi)
                luigi= canvas.create_image(770,410,anchor="center",image=lui01)
            elif (posact[1]+30>= 440 and posact[1]+30<580 and (posact[0]-18>280 and posact[0]+18<520)): ##validar espacio en blanco
                canvas.move(luigi,0,10)            
                mundo.after(10,mover3)
            else:       
                if (img==False):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=li3)
                    canvas.move(luigi,-5,0)
                    img=True
                elif(img==True):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=li4)
                    canvas.move(luigi,-5,0)
                    img=False

        elif (Ldie==False and posini[1]+30>=320): ##validamos que esta en la tercera plataforma laterales
            if (posact[1]+30==320 and posact[0]-20<=0):
                canvas.delete(luigi)
                luigi= canvas.create_image(770,290,anchor="center",image=lui01)
            elif (posact[1]+30>= 320 and posact[1]+30<440 and (posact[0]-18 >540 and posact[0]+18<640)): ##validar espacio en blanco a la izquierda plataforma derecha tercer nivel
                canvas.move(luigi,0,10)            
                mundo.after(10,mover3)

            else:
                if (img==False):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=li3)
                    canvas.move(luigi,-5,0)
                    img=True
                elif(img==True):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=li4)
                    canvas.move(luigi,-5,0)
                    img=False
                
        elif (Ldie==False and posini[1]+30 >=300): ##validamos que esta en la tercera plataforma central 
            if (posact[1]+30>= 300 and posact[1]+30<440 and (posact[0]-18>160 and posact[0]+18<260)): ##validar espacio en blanco a la izquierda plataforma
                canvas.move(luigi,0,10)            
                mundo.after(10,mover3)       
            else:
                if (img==False):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=li3)
                    canvas.move(luigi,-5,0)
                    img=True
                elif(img==True):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=li4)
                    canvas.move(luigi,-5,0)
                    img=False

        elif (Ldie==False and posini[1]+30 >=160): ##validamos que esta en la cuarta plataforma
            if (posact[1]+30==160 and posact[0]-20<=0):
                canvas.delete(luigi)
                luigi= canvas.create_image(770,130,anchor="center",image=lui01)
            elif (posact[1] +30 >= 160 and posact[1]+30 <300 and (posact[0]-18 >340 and posact[0]+18 <460)): ##validar espacio en blanco a la izquierda plataforma derecha cuarto nivel
                canvas.move(luigi,0,10)            
                mundo.after(10,mover3)

            else:
                if (img==False):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=li3)
                    canvas.move(luigi,-5,0)
                    img=True
                elif(img==True):
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posact[0],posact[1],anchor="center",image=li4)
                    canvas.move(luigi,-5,0)
                    img=False

       
def pressed (event):
    """
    Procedimiento para que el usuario pueda oprimir más de una tecla a la vez
    direccionandola hacia un lado el salto.
    """
    global canvas, luigi, hmax, posact, posini,Ldie,menuu,LifesL,Vidaslui
    tecla = repr (event.char)
    posini=canvas.coords(luigi)
    if menuu==True:
        canvas.create_image (750,120,image= Tub1)
        canvas.create_image (52,120,image= Tub2)
        canvas.create_image (770,550,image= Tub3)
        canvas.create_image (36,550,image= Tub4)
        if (Ldie==False):
            if (tecla == "'w'"):
                presionado [0] = True
                if (presionado [2] == True):
                    hmax = False
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posini[0],posini[1],anchor="center",image=ljd)
                    saltar2()
                if (presionado [1]== True):
                    hmax= False
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posini[0],posini[1],anchor="center",image=lji)
                    saltar3()
                elif (presionado [1] == False and presionado [2]== False and Ldie==False):
                    hmax= False
                    canvas.delete(luigi)
                    luigi=canvas.create_image(posini[0],posini[1],anchor="center",image=ljd)
                    saltar()
                    
            elif (tecla == "'a'"):
                presionado [1] = True
                canvas.delete(luigi)
                luigi= canvas.create_image(posini[0],posini[1],anchor="center",image=li1)
                mover3()        
          
            elif (tecla == "'d'"):
                canvas.delete(luigi)
                luigi=canvas.create_image(posini[0],posini[1],anchor="center",image=ld1)
                presionado [2] = True
                mover2()

            elif (tecla=="'h'"):
                presionado[3]=True            
                muertelui()
                Vidaslui+=1
                canvas.delete(LifesL)
                LifesL=canvas.create_text(54,60,fill="Lime Green",font=("Charlemagne Std",12),text=("X"+ str (Vidaslui)))
            

def released(event):
    """
    Procedimiento para "liberar" las teclas, orpimiendolas una vez
    """
    global canvas, luigi, hmax,posact,Ldie,menuu
    tecla= repr (event.char)
    if menuu== True:
        canvas.create_image (750,120,image= Tub1)
        canvas.create_image (52,120,image= Tub2)
        canvas.create_image (770,550,image= Tub3)
        canvas.create_image (36,550,image= Tub4)
        if (Ldie==False):
            if (tecla == "'w'"):
                presionado [0]= False
                canvas.delete(luigi)
                luigi= canvas.create_image(posact[0],posact[1],anchor="center",image=li2)
            elif (tecla == "'a'"):
                presionado [1] = False
                canvas.delete(luigi)
                luigi= canvas.create_image(posact[0]-5,posact[1],anchor="center",image=li2)
            elif (tecla == "'d'"):        
                presionado [2] = False
                canvas.delete(luigi)
                luigi= canvas.create_image(posact[0]+5,posact[1],anchor="center",image=ld2)
            elif (tecla=="'h'"):
                presionado[3]=False

        
for char in ["w", "a","d","h"]:
    canvas.bind ("<KeyPress-%s>" % char, pressed)
    canvas.bind ("<KeyRelease-%s>" % char, released)
    canvas.focus_set ()
canvas.focus_set ()
canvas.pack()
mundo.resizable (0,0)

        

#Importarluigi
luigi= canvas.create_image(100,550,anchor="center", image=lui01)
coordsI= canvas.coords(luigi)

#Crear Enemigos parciales
ShellcreeperTI= canvas.create_polygon(0,0,0,0)
SidestepperTI=canvas.create_polygon(0,0,0,0)
FigtherflyTI= canvas.create_polygon(0,0,0,0)
SlipiceTI=canvas.create_polygon(0,0,0,0)
SidestepperTI1=canvas.create_polygon(0,0,0,0)
ShellcreeperTD= canvas.create_polygon(0,0,0,0)
SidestepperTD=canvas.create_polygon(0,0,0,0)
FigtherflyTD= canvas.create_polygon(0,0,0,0)
SlipiceTD=canvas.create_polygon(0,0,0,0)
ShellcreeperTD1= canvas.create_polygon(0,0,0,0)

#Estados de los enemigos
muertoV=True
muertoR= True
muertoF= True
muertoS= True
muertoV1=True
muertoV2=True
muertoR1=True
muertoR2=True
muertoF1=True
muertoS1=True
vel= 700

#Funciones que sirven para  llamar a los enemigos en el lado izquierdo de la pantalla
def LlamarShell():
    global ShellcreeperTI,muertoV
    canvas.create_image (750,120,image= Tub1)
    canvas.create_image (52,120,image= Tub2)
    canvas.create_image (770,550,image= Tub3)
    canvas.create_image (36,550,image= Tub4)
    canvas.delete(ShellcreeperTI)
    muertoV=False
    ShellcreeperTI= canvas.create_image(100+30,120+20,anchor="center",image=tvd1) #Creación del enemigo Shellcreeper si el numero es 0
    ShellcreeperD ()
def LlamarSides():
    global SidestepperTI,muertoR
    canvas.create_image (750,120,image= Tub1)
    canvas.create_image (52,120,image= Tub2)
    canvas.create_image (770,550,image= Tub3)
    canvas.create_image (36,550,image= Tub4)
    canvas.delete(SidestepperTI)
    muertoR= False
    SidestepperTI= canvas.create_image (100+30, 120+20, anchor="center", image=trd1) #Creación del enemigo Sidestepper si el numero es 1
    SidestepperD ()
def LlamarFigther():
    global FigtherflyTI,muertoF
    canvas.create_image (750,120,image= Tub1)
    canvas.create_image (52,120,image= Tub2)
    canvas.create_image (770,550,image= Tub3)
    canvas.create_image (36,550,image= Tub4)
    canvas.delete(FigtherflyTI)
    muertoF= False
    FigtherflyTI= canvas.create_image (100 + 30, 120+20, anchor="center",image=fly1) #Creación del enemigo Figtherfly si el numero es 2
    FigtherflyD ()
def LlamarSlipice():
    global SlipiceTI,muertoS
    canvas.create_image (750,120,image= Tub1)
    canvas.create_image (52,120,image= Tub2)
    canvas.create_image (770,550,image= Tub3)
    canvas.create_image (36,550,image= Tub4)
    canvas.delete(SlipiceTI)
    muertoS= False
    SlipiceTI = canvas.create_image (100 +30, 120+20, anchor="center", image=fd2) #Creación del enemigo Slipice si el numero es 3
    SlipiceD ()
def LlamarSides1():
    global SidestepperTI1,muertoR2
    canvas.delete(SidestepperTI1)
    canvas.create_image (750,120,image= Tub1)
    canvas.create_image (52,120,image= Tub2)
    canvas.create_image (770,550,image= Tub3)
    canvas.create_image (36,550,image= Tub4)
    muertoR2=False
    SidestepperTI1=canvas.create_image (100 +30, 120+20, anchor="center", image=trd1)
    SidestepperD1 ()

#Funciones que sirven para  llamar a los enemigos en el lado derecho de la pantalla

def LlamarShellD():
    global ShellcreeperTD,muertoV1
    canvas.create_image (750,120,image= Tub1)
    canvas.create_image (52,120,image= Tub2)
    canvas.create_image (770,550,image= Tub3)
    canvas.create_image (36,550,image= Tub4)
    canvas.delete(ShellcreeperTD)
    ShellcreeperTD= canvas.create_image(660+30,120+20,anchor="center",image=tvi1) #Creación del enemigo Shellcreeper
    muertoV1=False
    ShellcreeperI ()
def LlamarSidesD():
    global SidestepperTD,muertoR1
    canvas.create_image (750,120,image= Tub1)
    canvas.create_image (52,120,image= Tub2)
    canvas.create_image (770,550,image= Tub3)
    canvas.create_image (36,550,image= Tub4)
    canvas.delete(SidestepperTD)
    SidestepperTD= canvas.create_image (660+30, 120+20, anchor="center", image=tri1) #Creación del enemigo Sidestepper
    muertoR1=False
    SidestepperI ()
def LlamarFigtherD():
    global FigtherflyTD,muertoF1,vidaEstado,vid
    canvas.delete(FigtherflyTD)
    canvas.create_image (750,120,image= Tub1)
    canvas.create_image (52,120,image= Tub2)
    canvas.create_image (770,550,image= Tub3)
    canvas.create_image (36,550,image= Tub4)
    vid= canvas.create_image(120,284,anchor="center",image=vida)
    vidaEstado=True
    FigtherflyTD= canvas.create_image (660+30, 120+20, anchor="center",image=fly3) #Creación del enemigo Figtherfly
    muertoF1=False
    FigtherflyI ()
    canvas.after(500*20,vidaa)
def LlamarSlipiceD():
    global SlipiceTD,muertoS1
    canvas.create_image (750,120,image= Tub1)
    canvas.create_image (52,120,image= Tub2)
    canvas.create_image (770,550,image= Tub3)
    canvas.create_image (36,550,image= Tub4)
    canvas.delete(SlipiceTD)
    SlipiceTD = canvas.create_image (660+30, 120+20, anchor="center", image=fi2) #Creación del enemigo Slipice
    muertoS1=False
    SlipiceI ()
def LlamarShellD1():
    global ShellcreeperTD1,muertoV2,st,starEstado,starR,Ayuda
    st= canvas.create_image(650,284,anchor="center",image=starR)
    canvas.create_image (750,120,image= Tub1)
    canvas.create_image (52,120,image= Tub2)
    canvas.create_image (770,550,image= Tub3)
    canvas.create_image (36,550,image= Tub4)
    starEstado=True
    Ayuda=False
    canvas.delete(ShellcreeperTD1)
    ShellcreeperTD1=canvas.create_image(660+30, 120+20, anchor="center", image=tvi1) #Creación del segundo enemigo Shellcreeper
    muertoV2=False
    ShellcreeperI1 ()
    canvas.after(500*60,star)
vidaEstado=False 
continuarV= True
tortverde1= False
Ldie= False
def ShellcreeperD ():
    """
    Función que contiene los movimientos del enemigo Shellcreeper cuando sale por la tubería de la izquierda
    """
    global  ShellcreeperTI, puntajeLui,ScoreL,luigi,SidestepperTI, FighterflyTI, SlipiceTI,tortverde1,vel,continuarV,Ldie,Ayuda
    coordsShell = canvas.coords(ShellcreeperTI)
    if (Ldie==False and (continuarV== True and Ayuda==False) and muertoV==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTI)[0]+22)) and canvas.coords(luigi)[1]+30==canvas.coords(ShellcreeperTI)[1]+20):
        Ldie=True
        muertelui()
        mundo.after(vel,ShellcreeperD)
    if continuarV==False:
        mundo.after(900*7,MuerteEV)
              
    elif (coordsShell[0]-15 <= 330 and coordsShell [1] +20 == 160 and continuarV== True): #Se valida que el enemigo esté en la cuarta plataforma
        if (tortverde1==False):
            canvas.delete(ShellcreeperTI)
            ShellcreeperTI= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvd2)
            canvas.move(ShellcreeperTI,10,-0)
            tortverde1=True
            mundo.after(vel,ShellcreeperD)
        elif (tortverde1==True):
            canvas.delete(ShellcreeperTI)
            ShellcreeperTI= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvd1)
            canvas.move(ShellcreeperTI,10,0)
            tortverde1=False
            mundo.after(vel,ShellcreeperD)

    elif (coordsShell[0]-15 >310 and coordsShell[1]+15 < 295 ): #Se valida que cuando se llegue al limite de la cuarta plataforma el enemigo caiga hasta la tercera plataforma
        canvas.move(ShellcreeperTI,0,10)
        mundo.after(20,ShellcreeperD)

    elif (coordsShell [0]-15 <= 530 and coordsShell [1]+20==300 and continuarV== True): #Se valida que el enemigo esté en la tercera plataforma   
        if (tortverde1==False):
            canvas.delete(ShellcreeperTI)
            ShellcreeperTI= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvd2)
            canvas.move(ShellcreeperTI,10,-0)
            tortverde1=True
            mundo.after(vel,ShellcreeperD)
        elif (tortverde1==True):
            canvas.delete(ShellcreeperTI)
            ShellcreeperTI= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvd1)
            canvas.move(ShellcreeperTI,10,0)
            tortverde1=False
            mundo.after(vel,ShellcreeperD)

    elif (coordsShell [0]-15 > 520 and coordsShell [1]+15 <435 and continuarV== True): #Se valida que cuando se llegue al limite de la tercera plataforma el enemigo caiga hasta la segunda plataforma
        canvas.move(ShellcreeperTI,0,10)
        mundo.after(20,ShellcreeperD)

    elif (coordsShell [0]-15 >=535 and coordsShell[0] +15 < 800 and coordsShell [1]+20==440 and continuarV== True): #Se valida que el enemigo esté en la segunda plataforma del lado derecho
        if (tortverde1==False):
            canvas.delete(ShellcreeperTI)
            ShellcreeperTI= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvd2)
            canvas.move(ShellcreeperTI,10,-0)
            tortverde1=True
            mundo.after(vel,ShellcreeperD)
        elif (tortverde1==True):
            canvas.delete(ShellcreeperTI)
            ShellcreeperTI= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvd1)
            canvas.move(ShellcreeperTI,10,0)
            tortverde1=False
            mundo.after(vel,ShellcreeperD)

    elif (coordsShell[0] +15 >= 790 and coordsShell [1]+20==440 and continuarV== True): #Se valida que el enemigo esté en el borde de la segunda plataforma para aparecer al otro lado de la pantalla
        canvas.delete(ShellcreeperTI)
        ShellcreeperTI= canvas.create_image(15,420,anchor="center",image=tvd1)
        mundo.after(0,ShellcreeperD)

    elif (coordsShell [0]-15 < 270 and coordsShell [1]+20==440 and continuarV== True): #Se valida que el enemigo esté en la segunda plataforma del lazo izquierdo
        if (tortverde1==False):
            canvas.delete(ShellcreeperTI)
            ShellcreeperTI= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvd2)
            canvas.move(ShellcreeperTI,10,-0)
            tortverde1=True
            mundo.after(vel,ShellcreeperD)
        elif (tortverde1==True):
            canvas.delete(ShellcreeperTI)
            ShellcreeperTI= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvd1)
            canvas.move(ShellcreeperTI,10,0)
            tortverde1=False
            mundo.after(vel,ShellcreeperD)

    elif(coordsShell [0]-15 >260 and coordsShell [1]+15 <575 and continuarV== True): #Se valida que cuando se llegue al limite de la segunda plataforma el enemigo caiga hasta la primera plataforma
        canvas.move(ShellcreeperTI,0,10)
        mundo.after(20,ShellcreeperD)

    elif (coordsShell [0]+15 < 740 and coordsShell [1] + 20==580 and continuarV== True): #Se valida que el enemigo esté en la primera plataforma
        if (tortverde1==False):
            canvas.delete(ShellcreeperTI)
            ShellcreeperTI= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvd2)
            canvas.move(ShellcreeperTI,10,-0)
            tortverde1=True
            mundo.after(vel,ShellcreeperD)
        elif (tortverde1==True):
            canvas.delete(ShellcreeperTI)
            ShellcreeperTI= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvd1)
            canvas.move(ShellcreeperTI,10,0)
            tortverde1=False
            mundo.after(vel,ShellcreeperD)

    elif (coordsShell [0]+15 >=735 and coordsShell [1] + 20== 580 and continuarV== True): #Se valida que el enemigo esté en en el inicio de la tubería derecha de la pantalla para aparecer una vez más arriba al aldo izqueirdo de la pantalla
        canvas.delete(ShellcreeperTI)
        mundo.after(100)
        ShellcreeperTI= canvas.create_image(100+30,120+20,anchor="center",image=tvd1)
        puntajeLui-=100
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+str(puntajeLui)))
        mundo.after(100)
        mundo.after(100,ShellcreeperD)

tortverde=False
continuarV1=True
def ShellcreeperI ():
    """
    Función que contiene los movimientos del enemigo Shellcreeper cuando sale por la tuberia derecha
    """
    global  ShellcreeperTD, SidestepperTD, FighterflyTD, SlipiceTD,vel,tortverde,luigi,continuarV1,Ldie,puntajeLui,Ayuda
    coordsShell = canvas.coords(ShellcreeperTD)
    if (Ldie==False and (continuarV1== True and Ayuda==False) and muertoV1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTD)[0]+22)) and canvas.coords(luigi)[1]+30==canvas.coords(ShellcreeperTD)[1]+20):
        Ldie=True
        muertelui()
        mundo.after(vel,ShellcreeperD)

    if continuarV1==False:
        mundo.after(900*7,MuerteEV1)
    
    elif (coordsShell[0]-15 > 440 and coordsShell [1] +20== 160 and continuarV1== True): #Se valida que el enemigo esté en la cuarta plataforma
        if (tortverde==False):
            canvas.delete(ShellcreeperTD)
            ShellcreeperTD= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi2)
            canvas.move(ShellcreeperTD,-10,0)
            tortverde=True
            mundo.after(vel,ShellcreeperI)
        elif (tortverde==True):
            canvas.delete(ShellcreeperTD)
            ShellcreeperTD= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi1)
            canvas.move(ShellcreeperTD,-10,0)
            tortverde=False
            mundo.after(vel,ShellcreeperI)
        
    elif (coordsShell [0]-15 < 430 and coordsShell [1] + 15 <= 285 and continuarV1== True): #Se valida que cuando se llegue al limite de la cuarta plataforma el enemigo caiga hasta la tercera plataforma
        canvas.move(ShellcreeperTD,0,10)
        mundo.after(20,ShellcreeperI)

    elif (coordsShell[0]-15 >235 and coordsShell [1] +20== 300 and continuarV1== True): #Se valida que el enemigo esté en la tercera plataforma
        if (tortverde==False):
            canvas.delete(ShellcreeperTD)
            ShellcreeperTD= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi2)
            canvas.move(ShellcreeperTD,-10,0)
            tortverde=True
            mundo.after(vel,ShellcreeperI)
        elif (tortverde==True):
            canvas.delete(ShellcreeperTD)
            ShellcreeperTD= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi1)
            canvas.move(ShellcreeperTD,-10,0)
            tortverde=False
            mundo.after(vel,ShellcreeperI)

    elif (coordsShell [0]-15 < 240 and coordsShell [1] + 15 < 435 and continuarV1== True): #Se valida que cuando se llegue al limite de la tercera plataforma el enemigo caiga hasta la segunda plataforma
        canvas.move(ShellcreeperTD,0,10)
        mundo.after(20,ShellcreeperI)
        

    elif(coordsShell [0]+15 < 270 and coordsShell [0]-15 > 0 and coordsShell [1] + 20== 440 and continuarV1== True): #Se valida que el enemigo esté en la segunda plataforma del lado derecho
        if (tortverde==False):
            canvas.delete(ShellcreeperTD)
            ShellcreeperTD= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi2)
            canvas.move(ShellcreeperTD,-10,0)
            tortverde=True
            mundo.after(vel,ShellcreeperI)
        elif (tortverde==True):
            canvas.delete(ShellcreeperTD)
            ShellcreeperTD= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi1)
            canvas.move(ShellcreeperTD,-10,0)
            tortverde=False
            mundo.after(vel,ShellcreeperI)

    elif (coordsShell [0]-15 <= 20 and coordsShell [1] + 20== 440 and continuarV1== True): #Se valida que el enemigo esté en el borde de la segunda plataforma para aparecer al otro lado de la pantalla
        canvas.delete(ShellcreeperTD)
        ShellcreeperTD= canvas.create_image(790,420,anchor="center",image=tvi2)
        mundo.after(0,ShellcreeperI)

    elif (coordsShell [0]-15 > 500 and coordsShell [1]+20==440 and continuarV1== True): #Se valida que el enemigo esté en la segunda plataforma del lazo izquierdo
        if (tortverde==False):
            canvas.delete(ShellcreeperTD)
            ShellcreeperTD= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi2)
            canvas.move(ShellcreeperTD,-10,0)
            tortverde=True
            mundo.after(vel,ShellcreeperI)
        elif (tortverde==True):
            canvas.delete(ShellcreeperTD)
            ShellcreeperTD= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi1)
            canvas.move(ShellcreeperTD,-10,0)
            tortverde=False
            mundo.after(vel,ShellcreeperI)

    elif (coordsShell [0]-15 < 500 and coordsShell [1] + 15 < 575 and continuarV1== True): #Se valida que cuando se llegue al limite de la segunda plataforma el enemigo caiga hasta la primera plataforma
        canvas.move(ShellcreeperTD,0,10)
        mundo.after(20,ShellcreeperI)

    elif (coordsShell [0]-15 > 60 and coordsShell [1]+20==580 and continuarV1== True): #Se valida que el enemigo esté en la primera plataforma
        if (tortverde==False):
            canvas.delete(ShellcreeperTD)
            ShellcreeperTD= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi2)
            canvas.move(ShellcreeperTD,-10,0)
            tortverde=True
            mundo.after(vel,ShellcreeperI)
        elif (tortverde==True):
            canvas.delete(ShellcreeperTD)
            ShellcreeperTD= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi1)
            canvas.move(ShellcreeperTD,-10,0)
            tortverde=False
            mundo.after(vel,ShellcreeperI)
        
    elif (coordsShell [0]-15 <=60 and coordsShell [1] + 20== 580 and continuarV1== True): #Se valida que el enemigo esté en en el inicio de la tubería derecha de la pantalla para aparecer una vez más arriba al aldo izqueirdo de la pantalla
        canvas.delete(ShellcreeperTD)
        mundo.after(100)
        ShellcreeperTD= canvas.create_image(660+30,120+20,anchor="center",image=tvi1)
        puntajeLui-=100
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+str(puntajeLui)))
        mundo.after(100)
        mundo.after(100,ShellcreeperI)

tortverde2=False
continuarV2=True
def ShellcreeperI1 ():
    """
    Función que contiene los movimientos del enemigo Shellcreeper cuando sale por la tuberia derecha
    """
    global  ShellcreeperTD1, SidestepperTD, FighterflyTD, SlipiceTD,vel,tortverde2,continuarV2,Ldie,luigi,puntajeLui,Ayuda
    coordsShell = canvas.coords(ShellcreeperTD1)
    if continuarV2==False:
        mundo.after(900*7,MuerteEV2)

    if (Ldie==False and (continuarV2== True and Ayuda==False) and muertoV2==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(ShellcreeperTD1)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(ShellcreeperTD1)[0]+22)) and canvas.coords(luigi)[1]+30==canvas.coords(ShellcreeperTD1)[1]+20):
        Ldie=True
        muertelui()
        mundo.after(vel,ShellcreeperI1)

    elif (coordsShell[0]-15 > 440 and coordsShell [1] +20== 160 and continuarV2== True): #Se valida que el enemigo esté en la cuarta plataforma
        if (tortverde2==False):
            canvas.delete(ShellcreeperTD1)
            ShellcreeperTD1= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi2)
            canvas.move(ShellcreeperTD1,-10,0)
            tortverde2=True
            mundo.after(vel,ShellcreeperI1)
        elif (tortverde2==True):
            canvas.delete(ShellcreeperTD1)
            ShellcreeperTD1= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi1)
            canvas.move(ShellcreeperTD1,-10,0)
            tortverde2=False
            mundo.after(vel,ShellcreeperI1)
        
    elif (coordsShell [0]-15 < 430 and coordsShell [1] + 15 <= 285 and continuarV2== True): #Se valida que cuando se llegue al limite de la cuarta plataforma el enemigo caiga hasta la tercera plataforma
        canvas.move(ShellcreeperTD1,0,10)
        mundo.after(20,ShellcreeperI1)

    elif (coordsShell[0]-15 >235 and coordsShell [1] +20== 300 and continuarV2== True): #Se valida que el enemigo esté en la tercera plataforma
        if (tortverde2==False):
            canvas.delete(ShellcreeperTD1)
            ShellcreeperTD1= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi2)
            canvas.move(ShellcreeperTD1,-10,0)
            tortverde2=True
            mundo.after(vel,ShellcreeperI1)
        elif (tortverde2==True):
            canvas.delete(ShellcreeperTD1)
            ShellcreeperTD1= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi1)
            canvas.move(ShellcreeperTD1,-10,0)
            tortverde2=False
            mundo.after(vel,ShellcreeperI1)

    elif (coordsShell [0]-15 < 240 and coordsShell [1] + 15 < 435 and continuarV2== True): #Se valida que cuando se llegue al limite de la tercera plataforma el enemigo caiga hasta la segunda plataforma
        canvas.move(ShellcreeperTD1,0,10)
        mundo.after(20,ShellcreeperI1)
        

    elif(coordsShell [0]+15 < 270 and coordsShell [0]-15 > 0 and coordsShell [1] + 20== 440 and continuarV2== True): #Se valida que el enemigo esté en la segunda plataforma del lado derecho
        if (tortverde2==False):
            canvas.delete(ShellcreeperTD1)
            ShellcreeperTD1= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi2)
            canvas.move(ShellcreeperTD1,-10,0)
            tortverde2=True
            mundo.after(vel,ShellcreeperI1)
        elif (tortverde2==True):
            canvas.delete(ShellcreeperTD1)
            ShellcreeperTD1= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi1)
            canvas.move(ShellcreeperTD1,-10,0)
            tortverde2=False
            mundo.after(vel,ShellcreeperI1)

    elif (coordsShell [0]-15 <= 20 and coordsShell [1] + 20== 440 and continuarV2== True): #Se valida que el enemigo esté en el borde de la segunda plataforma para aparecer al otro lado de la pantalla
        canvas.delete(ShellcreeperTD1)
        ShellcreeperTD1= canvas.create_image(790,420,anchor="center",image=tvi2)
        mundo.after(0,ShellcreeperI1)

    elif (coordsShell [0]-15 > 500 and coordsShell [1]+20==440 and continuarV2== True): #Se valida que el enemigo esté en la segunda plataforma del lazo izquierdo
        if (tortverde2==False):
            canvas.delete(ShellcreeperTD1)
            ShellcreeperTD1= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi2)
            canvas.move(ShellcreeperTD1,-10,0)
            tortverde2=True
            mundo.after(vel,ShellcreeperI1)
        elif (tortverde2==True):
            canvas.delete(ShellcreeperTD1)
            ShellcreeperTD1= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi1)
            canvas.move(ShellcreeperTD1,-10,0)
            tortverde2=False
            mundo.after(vel,ShellcreeperI1)

    elif (coordsShell [0]-15 < 500 and coordsShell [1] + 15 < 575 and continuarV2== True): #Se valida que cuando se llegue al limite de la segunda plataforma el enemigo caiga hasta la primera plataforma
        canvas.move(ShellcreeperTD1,0,10)
        mundo.after(20,ShellcreeperI1)

    elif (coordsShell [0]-15 > 60 and coordsShell [1]+20==580 and continuarV2== True): #Se valida que el enemigo esté en la primera plataforma
        if (tortverde2==False):
            canvas.delete(ShellcreeperTD1)
            ShellcreeperTD1= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi2)
            canvas.move(ShellcreeperTD1,-10,0)
            tortverde2=True
            mundo.after(vel,ShellcreeperI1)
        elif (tortverde2==True):
            canvas.delete(ShellcreeperTD1)
            ShellcreeperTD1= canvas.create_image(coordsShell[0],coordsShell[1],anchor="center",image=tvi1)
            canvas.move(ShellcreeperTD1,-10,0)
            tortverde2=False
            mundo.after(vel,ShellcreeperI1)
        
    elif (coordsShell [0]-15 <=60 and coordsShell [1] + 20== 580 and continuarV2== True): #Se valida que el enemigo esté en en el inicio de la tubería derecha de la pantalla para aparecer una vez más arriba al aldo izqueirdo de la pantalla
        canvas.delete(ShellcreeperTD1)
        mundo.after(100)
        ShellcreeperTD1= canvas.create_image(660+30,120+20,anchor="center",image=tvi1)
        puntajeLui-=200
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+str(puntajeLui)))
        mundo.after(100)
        mundo.after(100,ShellcreeperI1)
tortroja= True
continuarR= True
def SidestepperD ():
    """
    Función que contiene los movimientos del enemigo Shidestepper cuando sale por la tubería de la izquierda
    """
    global  ShellcreeperTI, parc,Muert1,SidestepperTI, FigtherflyTI, SlipiceTI, vel,tortroja,continuarR,Ldie,puntajeLui,Ayuda
    coordsSides = canvas.coords(SidestepperTI)
    if parc==True:
        Muert1+=1
        parc=False
    if continuarR==False:
        mundo.after(900*7,MuerteER)
    if (Ldie==False and (continuarR== True and Ayuda==False) and muertoR==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTI)[0]+22)) and canvas.coords(luigi)[1]+30==canvas.coords(SidestepperTI)[1]+20):
        Ldie=True
        muertelui()
        mundo.after(vel,SidestepperD)

        
    elif (continuarR== True and coordsSides[0]-15 <= 330 and coordsSides [1] +20== 160): #Se valida que el enemigo esté en la cuarta plataforma
        if (tortroja==True):
            canvas.delete(SidestepperTI)
            SidestepperTI= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd2)
            canvas.move(SidestepperTI,10,-0)
            tortroja=False
            mundo.after(vel,SidestepperD)
        elif (tortroja==False):
            canvas.delete(SidestepperTI)
            SidestepperTI= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd1)
            canvas.move(SidestepperTI,10,0)
            tortroja=True
            mundo.after(vel,SidestepperD)
    

    elif (continuarR== True and coordsSides[0]-15 >310 and coordsSides[1]+20 < 300): #Se valida que cuando se llegue al limite de la cuarta plataforma el enemigo caiga hasta la tercera plataforma
        canvas.move(SidestepperTI,0,10)
        mundo.after(20,SidestepperD)

    elif (continuarR== True and coordsSides [0]-30 <= 510 and coordsSides [1]+20 ==300):  #Se valida que el enemigo esté en la tercera plataforma
        if (tortroja==True):
            canvas.delete(SidestepperTI)
            SidestepperTI= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd2)
            canvas.move(SidestepperTI,10,-0)
            tortroja=False
            mundo.after(vel,SidestepperD)
        elif (tortroja==False):
            canvas.delete(SidestepperTI)
            SidestepperTI= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd1)
            canvas.move(SidestepperTI,10,0)
            tortroja=True
            mundo.after(vel,SidestepperD)

    elif (continuarR== True and coordsSides [0]-30 > 510 and coordsSides [1]+20 <440): #Se valida que cuando se llegue al limite de la tercera plataforma el enemigo caiga hasta la segunda plataforma
        canvas.move(SidestepperTI,0,10)
        mundo.after(20,SidestepperD)

    elif (continuarR== True and coordsSides [0]-30 >=440 and coordsSides[0] -20 < 800 and coordsSides [1]+20 ==440): #Se valida que el enemigo esté en la segunda plataforma del lado derecho
        if (tortroja==True):
            canvas.delete(SidestepperTI)
            SidestepperTI= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd2)
            canvas.move(SidestepperTI,10,-0)
            tortroja=False
            mundo.after(vel,SidestepperD)
        elif (tortroja==False):
            canvas.delete(SidestepperTI)
            SidestepperTI= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd1)
            canvas.move(SidestepperTI,10,0)
            tortroja=True
            mundo.after(vel,SidestepperD)

    elif (continuarR== True and coordsSides[0] -20 >= 750 and coordsSides [1]+20==440): #Se valida que el enemigo esté en el borde de la segunda plataforma para aparecer al otro lado de la pantalla
        canvas.delete(SidestepperTI)
        SidestepperTI= canvas.create_image(0,420,anchor="center",image=trd2)
        mundo.after(0,SidestepperD)

    elif (continuarR== True and coordsSides [0]-30 <= 250 and coordsSides [1]+20==440):#Se valida que el enemigo esté en la segunda plataforma del lazo izquierdo
        if (tortroja==True):
            canvas.delete(SidestepperTI)
            SidestepperTI= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd2)
            canvas.move(SidestepperTI,10,-0)
            tortroja=False
            mundo.after(vel,SidestepperD)
        elif (tortroja==False):
            canvas.delete(SidestepperTI)
            SidestepperTI= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd1)
            canvas.move(SidestepperTI,10,0)
            tortroja=True
            mundo.after(vel,SidestepperD)

    elif(continuarR== True and coordsSides [0]-30 >250 and coordsSides [1]+20 <580): #Se valida que cuando se llegue al limite de la segunda plataforma el enemigo caiga hasta la primera plataforma
        canvas.move(SidestepperTI,0,10)
        mundo.after(20,SidestepperD)

    elif (continuarR== True and coordsSides [0]-20 < 710 and coordsSides [1] + 20 ==580): #Se valida que el enemigo esté en la primera plataforma
        if (tortroja==True):
            canvas.delete(SidestepperTI)
            SidestepperTI= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd2)
            canvas.move(SidestepperTI,10,-0)
            tortroja=False
            mundo.after(vel,SidestepperD)
        elif (tortroja==False):
            canvas.delete(SidestepperTI)
            SidestepperTI= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd1)
            canvas.move(SidestepperTI,10,0)
            tortroja=True
            mundo.after(vel,SidestepperD)



    elif (continuarR== True and coordsSides [0]-20 >=690 and coordsSides [1] +20 == 580): #Se valida que el enemigo esté en en el inicio de la tubería derecha de la pantalla para aparecer una vez más arriba al aldo izqueirdo de la pantalla
        canvas.delete(SidestepperTI) 
        mundo.after(100)
        SidestepperTI= canvas.create_image(100+30,120+20,anchor="center",image=trd1)
        puntajeLui-=200
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+str(puntajeLui)))
        mundo.after(100)
        mundo.after(100,SidestepperD)

tortroja1=False
continuarR2= True
def SidestepperD1 ():
    """
    Función que contiene los movimientos del enemigo Sidestepper cuando sale por la tubería de la izquierda
    """
    global  ShellcreeperTI, parc2,Muert3,SidestepperTI1, FigtherflyTI, SlipiceTI, vel,tortroja1,continuarR2,Ldie,muertoR2,luigi,puntajeLui,Ayuda   
    coordsSides = canvas.coords(SidestepperTI1)
    if parc2==True:
        Muert3+=1
        parc2=False
    if continuarR2==False:
        mundo.after(900*7,MuerteER2)
    if (Ldie==False and (continuarR2== True and Ayuda==False) and muertoR2==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTI1)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTI1)[0]+22)) and canvas.coords(luigi)[1]+30==canvas.coords(SidestepperTI1)[1]+20):
        Ldie=True
        muertelui()
        mundo.after(vel,SidestepperD1)
        
    elif (continuarR2== True and coordsSides[0]-15 <= 330 and coordsSides [1] +20== 160): #Se valida que el enemigo esté en la cuarta plataforma
        if (tortroja1==True):
            canvas.delete(SidestepperTI1)
            SidestepperTI1= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd2)
            canvas.move(SidestepperTI1,10,-0)
            tortroja1=False
            mundo.after(vel,SidestepperD1)
        elif (tortroja1==False):
            canvas.delete(SidestepperTI1)
            SidestepperTI1= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd1)
            canvas.move(SidestepperTI1,10,0)
            tortroja1=True
            mundo.after(vel,SidestepperD1)

    elif (continuarR2== True and coordsSides[0]-15 >310 and coordsSides[1]+20 < 300): #Se valida que cuando se llegue al limite de la cuarta plataforma el enemigo caiga hasta la tercera plataforma
        canvas.move(SidestepperTI1,0,10)
        canvas.after(20,SidestepperD1)

    elif (continuarR2== True and coordsSides [0]-30 <= 510 and coordsSides [1]+20 ==300):  #Se valida que el enemigo esté en la tercera plataforma

        if (tortroja1==True):
            canvas.delete(SidestepperTI1)
            SidestepperTI1= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd2)
            canvas.move(SidestepperTI1,10,-0)
            tortroja1=False
            mundo.after(vel,SidestepperD1)
        elif (tortroja1==False):
            canvas.delete(SidestepperTI1)
            SidestepperTI1= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd1)
            canvas.move(SidestepperTI1,10,0)
            tortroja1=True
            mundo.after(vel,SidestepperD1)

    elif (continuarR2== True and coordsSides [0]-30 > 510 and coordsSides [1]+20 <440): #Se valida que cuando se llegue al limite de la tercera plataforma el enemigo caiga hasta la segunda plataforma
        canvas.move(SidestepperTI1,0,10)
        mundo.after(20,SidestepperD1)

    elif (continuarR2== True and coordsSides [0]-30 >=440 and coordsSides[0] -20 < 800 and coordsSides [1]+20 ==440): #Se valida que el enemigo esté en la segunda plataforma del lado derecho
        if (tortroja1==True):
            canvas.delete(SidestepperTI1)
            SidestepperTI1= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd2)
            canvas.move(SidestepperTI1,10,-0)
            tortroja1=False
            mundo.after(vel,SidestepperD1)
        elif (tortroja1==False):
            canvas.delete(SidestepperTI1)
            SidestepperTI1= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd1)
            canvas.move(SidestepperTI1,10,0)
            tortroja1=True
            mundo.after(vel,SidestepperD1)

    elif (continuarR2== True and coordsSides[0] -20 >= 750 and coordsSides [1]+20==440): #Se valida que el enemigo esté en el borde de la segunda plataforma para aparecer al otro lado de la pantalla
        canvas.delete(SidestepperTI1)
        SidestepperTI1= canvas.create_image(0,420,anchor="center",image=trd2)
        mundo.after(0,SidestepperD1)

    elif (continuarR2== True and coordsSides [0]-30 <= 250 and coordsSides [1]+20==440):#Se valida que el enemigo esté en la segunda plataforma del lazo izquierdo
        if (tortroja1==True):
            canvas.delete(SidestepperTI1)
            SidestepperTI1= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd2)
            canvas.move(SidestepperTI1,10,-0)
            tortroja1=False
            mundo.after(vel,SidestepperD1)
        elif (tortroja1==False):
            canvas.delete(SidestepperTI1)
            SidestepperTI1= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd1)
            canvas.move(SidestepperTI1,10,0)
            tortroja1=True
            mundo.after(vel,SidestepperD1)

    elif(continuarR2== True and coordsSides [0]-30 >250 and coordsSides [1]+20 <580): #Se valida que cuando se llegue al limite de la segunda plataforma el enemigo caiga hasta la primera plataforma
        canvas.move(SidestepperTI1,0,10)
        mundo.after(20,SidestepperD1)

    elif (continuarR2== True and coordsSides [0]-20 < 710 and coordsSides [1] + 20 ==580): #Se valida que el enemigo esté en la primera plataforma
        if (tortroja1==True):
            canvas.delete(SidestepperTI1)
            SidestepperTI1= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd2)
            canvas.move(SidestepperTI1,10,-0)
            tortroja1=False
            mundo.after(vel,SidestepperD1)
        elif (tortroja1==False):
            canvas.delete(SidestepperTI1)
            SidestepperTI1= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=trd1)
            canvas.move(SidestepperTI1,10,0)
            tortroja1=True
            mundo.after(vel,SidestepperD1)

    elif (continuarR2== True and coordsSides [0]-20 >=690 and coordsSides [1] +20 == 580): #Se valida que el enemigo esté en en el inicio de la tubería derecha de la pantalla para aparecer una vez más arriba al aldo izqueirdo de la pantalla
        canvas.delete(SidestepperTI1) 
        mundo.after(100)
        SidestepperTI1= canvas.create_image(100+30,120+20,anchor="center",image=trd1)
        puntajeLui-=200
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+str(puntajeLui)))
        mundo.after(100)
        mundo.after(100,SidestepperD1)

tortroja2=False
continuarR1= True
def SidestepperI ():
    """
    Función que contiene los movimientos del enemigo Sidestepper cuando sale por la tuberia derecha
    """
    global  ShellcreeperTD, SidestepperTD, FighterflyTD, SlipiceTD,vel,tortroja2,continuarR1,Muert2,parc1,Ldie,puntajeLui,Ayuda
    coordsSides = canvas.coords(SidestepperTD)
    if parc1==True:
        Muert2+=1
        parc1=False
    if continuarR1==False:
        mundo.after(900*7,MuerteER1)
    elif (Ldie==False and (continuarR1== True and Ayuda==False) and muertoR1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SidestepperTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SidestepperTD)[0]+22)) and canvas.coords(luigi)[1]+30==canvas.coords(SidestepperTD)[1]+20):
        Ldie=True
        muertelui()
        mundo.after(vel,SidestepperI)

    elif (continuarR1==True and coordsSides[0]-30 >= 430 and coordsSides [1] +20 == 160): #Se valida que el enemigo esté en la cuarta plataforma
        if (tortroja2==True):
            canvas.delete(SidestepperTD)
            SidestepperTD= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=tri2)
            canvas.move(SidestepperTD,-10,-0)
            tortroja2=False
            mundo.after(vel,SidestepperI)
        elif (tortroja2==False):
            canvas.delete(SidestepperTD)
            SidestepperTD= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=tri1)
            canvas.move(SidestepperTD,-10,0)
            tortroja2=True
            mundo.after(vel,SidestepperI)
        
    elif (continuarR1==True and coordsSides [0]-30 < 430 and coordsSides [1] + 20 < 300): #Se valida que cuando se llegue al limite de la cuarta plataforma el enemigo caiga hasta la tercera plataforma
        canvas.move(SidestepperTD,0,10)
        mundo.after(20,SidestepperI)

    elif (continuarR1==True and coordsSides[0]-30 >= 230 and coordsSides [1] +20 == 300):  #Se valida que el enemigo esté en la tercera plataforma
        if (tortroja2==True):
            canvas.delete(SidestepperTD)
            SidestepperTD= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=tri2)
            canvas.move(SidestepperTD,-10,-0)
            tortroja2=False
            mundo.after(vel,SidestepperI)
        elif (tortroja2==False):
            canvas.delete(SidestepperTD)
            SidestepperTD= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=tri1)
            canvas.move(SidestepperTD,-10,0)
            tortroja2=True
            mundo.after(vel,SidestepperI)
            
    elif (continuarR1==True and coordsSides [0]-30 < 230 and coordsSides [1] + 30 < 440): #Se valida que cuando se llegue al limite de la tercera plataforma el enemigo caiga hasta la segunda plataforma
        canvas.move(SidestepperTD,0,10)
        mundo.after(20,SidestepperI)

    elif(continuarR1==True and coordsSides [0]-30 <= 225 and coordsSides [0]-30 >= -20 and coordsSides [1] + 20 == 440): #Se valida que el enemigo esté en la segunda plataforma del lado derecho
        if (tortroja2==True):
            canvas.delete(SidestepperTD)
            SidestepperTD= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=tri2)
            canvas.move(SidestepperTD,-10,-0)
            tortroja2=False
            mundo.after(vel,SidestepperI)
        elif (tortroja2==False):
            canvas.delete(SidestepperTD)
            SidestepperTD= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=tri1)
            canvas.move(SidestepperTD,-10,0)
            tortroja2=True
            mundo.after(vel,SidestepperI)

    elif (continuarR1==True and coordsSides [0]-30 < 20 and coordsSides [1] +20 == 440): #Se valida que el enemigo esté en el borde de la segunda plataforma para aparecer al otro lado de la pantalla
        canvas.delete(SidestepperTD)
        SidestepperTD= canvas.create_image(800,420,anchor="center",image=tri1)
        mundo.after(0,SidestepperI)

    elif (continuarR1==True and coordsSides [0]-30 >= 490 and coordsSides [1]+20==440): #Se valida que el enemigo esté en la segunda plataforma del lazo izquierdo
        if (tortroja2==True):
            canvas.delete(SidestepperTD)
            SidestepperTD= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=tri2)
            canvas.move(SidestepperTD,-10,-0)
            tortroja2=False
            mundo.after(vel,SidestepperI)
        elif (tortroja2==False):
            canvas.delete(SidestepperTD)
            SidestepperTD= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=tri1)
            canvas.move(SidestepperTD,-10,0)
            tortroja2=True
            mundo.after(vel,SidestepperI)

    elif (continuarR1==True and coordsSides [0]-30 < 490 and coordsSides [1] + 20 < 580): #Se valida que cuando se llegue al limite de la segunda plataforma el enemigo caiga hasta la primera plataforma
        canvas.move(SidestepperTD,0,10)
        mundo.after(20,SidestepperI)

    elif (continuarR1==True and coordsSides [0]-30 > 40 and coordsSides [1]+20==580): #Se valida que el enemigo esté en la primera plataforma
        if (tortroja2==True):
            canvas.delete(SidestepperTD)
            SidestepperTD= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=tri2)
            canvas.move(SidestepperTD,-10,-0)
            tortroja2=False
            mundo.after(vel,SidestepperI)
        elif (tortroja2==False):
            canvas.delete(SidestepperTD)
            SidestepperTD= canvas.create_image(coordsSides[0],coordsSides[1],anchor="center",image=tri1)
            canvas.move(SidestepperTD,-10,0)
            tortroja2=True
            mundo.after(vel,SidestepperI)
        
    elif (continuarR1==True and coordsSides [0]-30 ==40 and coordsSides [1] + 20 == 580): #Se valida que el enemigo esté en en el inicio de la tubería derecha de la pantalla para aparecer una vez más arriba al aldo izqueirdo de la pantalla
        canvas.delete(SidestepperTD)
        mundo.after(100)
        SidestepperTD= canvas.create_image(660+30,110+30,anchor="center",image=tri1)
        puntajeLui-=200
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+str(puntajeLui)))
        mundo.after(100)
        mundo.after(100,SidestepperI)

mosca=True
moscont=0
continuarF= True
def FigtherflyD ():
    """
    Función que contiene los movimientos del enemigo Figtherfly cuando sale por la tubería de la izquierda
    """
    global  ShellcreeperTI, SidestepperTI, FigtherflyTI, SlipiceTI,mosca,moscont,luigi,vel,continuarF,Ldie,muertoF,puntajeLui,Ayuda
    coordsFigther = canvas.coords(FigtherflyTI)
    if continuarF==False:
        mundo.after(900*7,MuerteEF)
    if (Ldie==False and (continuarF== True and Ayuda==False) and muertoF==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(FigtherflyTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(FigtherflyTI)[0]+22)) and canvas.coords(luigi)[1]+30==canvas.coords(FigtherflyTI)[1]+20):
        Ldie=True
        muertelui()
        mundo.after(vel,FigtherflyD)
    elif (continuarF==True and coordsFigther[0]-15 <= 310 and coordsFigther [1] +20<= 160): #Se valida que el enemigo esté en la cuarta plataforma
        if (mosca==True):
            canvas.delete(FigtherflyTI)
            FigtherflyTI= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly2)
            canvas.move(FigtherflyTI,10,-50)
            mosca=False
            mundo.after(vel+300,FigtherflyD)
        elif (mosca==False):
            canvas.delete(FigtherflyTI)
            FigtherflyTI= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly3)
            canvas.move(FigtherflyTI,10,50)
            mosca=True
            mundo.after(vel+300,FigtherflyD)
            
    elif (continuarF==True and coordsFigther[0]-15 >310 and coordsFigther[0]==350 and (coordsFigther[1]+20< 300 )): #Se valida que cuando se llegue al limite de la cuarta plataforma el enemigo caiga hasta la tercera plataforma
        canvas.move(FigtherflyTI,0,10)
        mundo.after(20,FigtherflyD)

    elif (continuarF==True and coordsFigther [0]-15 <= 530 and (coordsFigther [1]+15 <=300 )): #Se valida que el enemigo esté en la tercera plataforma
        if (mosca==True):
            canvas.delete(FigtherflyTI)
            FigtherflyTI= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly2)
            canvas.move(FigtherflyTI,10,-50)
            mosca=False
            mundo.after(vel+300,FigtherflyD)
        elif (mosca==False):
            canvas.delete(FigtherflyTI)
            FigtherflyTI= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly3)
            canvas.move(FigtherflyTI,10,50)
            mosca=True
            mundo.after(vel+300,FigtherflyD)      

    elif (continuarF==True and coordsFigther [0]-15 >= 530 and coordsFigther[0]==550 and coordsFigther [1]+20 <440): #Se valida que cuando se llegue al limite de la tercera plataforma el enemigo caiga hasta la segunda plataforma
        canvas.move(FigtherflyTI,0,10)
        mundo.after(20,FigtherflyD)

    elif (continuarF==True and coordsFigther [0]-15 >=440 and coordsFigther[0] -15 < 750 and (coordsFigther [1]+20 <=440 and coordsFigther[1]> 300)): #Se valida que el enemigo esté en la segunda plataforma del lado derecho
        if (mosca==True):
            canvas.delete(FigtherflyTI)
            FigtherflyTI= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly2)
            canvas.move(FigtherflyTI,10,-50)
            mosca=False
            mundo.after(vel+300,FigtherflyD)
        elif (mosca==False):
            canvas.delete(FigtherflyTI)
            FigtherflyTI= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly3)
            canvas.move(FigtherflyTI,10,50)
            mosca=True
            mundo.after(vel+300,FigtherflyD)

    elif (continuarF==True and coordsFigther[0] -20 >= 750 and (coordsFigther [1]+20 <=440 and coordsFigther[1]> 300)): #Se valida que el enemigo esté en el borde de la segunda plataforma para aparecer al otro lado de la pantalla
        canvas.delete(FigtherflyTI)
        FigtherflyTI= canvas.create_image(30,420,anchor="center",image=fly1)
        mundo.after(0,FigtherflyD)

    elif (continuarF==True and coordsFigther [0]-15 <= 270 and (coordsFigther [1]+20 <=440 and coordsFigther[1]> 300)): #Se valida que el enemigo esté en la segunda plataforma del lazo izquierdo
        if (moscont==0):
            mosca=True
            moscont+=1
            mundo.after(0,FigtherflyD)
        elif (mosca==True):
            canvas.delete(FigtherflyTI)
            FigtherflyTI= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly2)
            canvas.move(FigtherflyTI,10,-50)
            mosca=False
            mundo.after(vel+300,FigtherflyD)
        elif (mosca==False):
            canvas.delete(FigtherflyTI)
            FigtherflyTI= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly3)
            canvas.move(FigtherflyTI,10,50)
            mosca=True
            mundo.after(vel+300,FigtherflyD)

    elif(continuarF==True and coordsFigther [0]-15 >270 and coordsFigther[0]==290 and coordsFigther [1]+20 <580): #Se valida que cuando se llegue al limite de la segunda plataforma el enemigo caiga hasta la primera plataforma
        canvas.move(FigtherflyTI,0,10)
        mundo.after(20,FigtherflyD)

    elif (continuarF==True and coordsFigther [0]+15 < 720 and (coordsFigther [1]+20 <=580 and coordsFigther[1]> 440)): #Se valida que el enemigo esté en la primera plataforma
        if (mosca==True):
            canvas.delete(FigtherflyTI)
            FigtherflyTI= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly2)
            canvas.move(FigtherflyTI,10,-50)
            mosca=False
            mundo.after(vel+300,FigtherflyD)
        elif (mosca==False):
            canvas.delete(FigtherflyTI)
            FigtherflyTI= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly3)
            canvas.move(FigtherflyTI,10,50)
            mosca=True
            mundo.after(vel+300,FigtherflyD)

    elif (continuarF==True and coordsFigther [0]>=700 and coordsFigther [1] + 20 <= 580): #Se valida que el enemigo esté en en el inicio de la tubería derecha de la pantalla para aparecer una vez más arriba al aldo izqueirdo de la pantalla
        canvas.delete(FigtherflyTI)
        mundo.after(100)
        FigtherflyTI= canvas.create_image(100+30,120+20,anchor="center",image=fly1)
        puntajeLui-=400
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+str(puntajeLui)))
        mundo.after(100)
        mundo.after(100,FigtherflyD)

mosca1=True
continuarF1=True
def FigtherflyI ():
    """
    Función que contiene los movimientos del enemigo Figtherfly cuando sale por la tuberia derecha
    """
    global  ShellcreeperTD, SidestepperTD, FigtherflyTD, SlipiceTD,mosca1,moscont,fly3,luigi,posact,vel,continuarF1,muertoF1,Ldie,puntajeLui,Ayuda
    coordsFigther = canvas.coords(FigtherflyTD)
    if continuarF1==False:
        mundo.after(900*7,MuerteEF1)
    if (Ldie==False and (continuarF1== True and Ayuda==False)and muertoF1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(FigtherflyTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(FigtherflyTD)[0]+22)) and canvas.coords(luigi)[1]+30==canvas.coords(FigtherflyTD)[1]+20):
        Ldie=True
        muertelui()
        mundo.after(vel,FigtherflyI)
    elif (continuarF1==True and  coordsFigther[0]-15 > 440 and coordsFigther [1] +20 <= 160): #Se valida que el enemigo esté en la cuarta plataforma

        if (mosca1==True):
            canvas.delete(FigtherflyTD)
            FigtherflyTD= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly4)
            canvas.move(FigtherflyTD,-10,-50)
            mosca1=False
            mundo.after(vel+300,FigtherflyI)
        elif (mosca1==False):
            canvas.delete(FigtherflyTD)
            FigtherflyTD= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly1)
            canvas.move(FigtherflyTD,-10,50)
            mosca1=True
            mundo.after(vel+300,FigtherflyI)
        
    elif (continuarF1==True and  coordsFigther [0]-15 <= 460 and coordsFigther [1] + 20 < 300 and coordsFigther[0]==450): #Se valida que cuando se llegue al limite de la cuarta plataforma el enemigo caiga hasta la tercera plataforma
        canvas.move(FigtherflyTD,0,10)
        mundo.after(20,FigtherflyI)

    elif (continuarF1==True and  coordsFigther[0]-15 > 240 and coordsFigther [1] +20 <= 300 and coordsFigther[1] >180):  #Se valida que el enemigo esté en la tercera plataforma
        if (mosca1==True):
            canvas.delete(FigtherflyTD)
            FigtherflyTD= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly4)
            canvas.move(FigtherflyTD,-10,-50)
            mosca1=False
            mundo.after(vel+300,FigtherflyI)
        elif (mosca1==False):
            canvas.delete(FigtherflyTD)
            FigtherflyTD= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly1)
            canvas.move(FigtherflyTD,-10,50)
            mosca1=True
            mundo.after(vel+300,FigtherflyI)
            
    elif (continuarF1==True and  coordsFigther [0]-15 <= 240 and coordsFigther [1] + 20 < 440 and coordsFigther[0]==250): #Se valida que cuando se llegue al limite de la tercera plataforma el enemigo caiga hasta la segunda plataforma
        canvas.move(FigtherflyTD,0,10)
        mundo.after(20,FigtherflyI)

    elif(continuarF1==True and  coordsFigther [0]-15 <= 280 and coordsFigther [0]-20 >= 0 and coordsFigther [1] + 20 <= 440 and coordsFigther [1] + 20 > 320 ): #Se valida que el enemigo esté en la segunda plataforma del lado derecho
        if (mosca1==True):
            canvas.delete(FigtherflyTD)
            FigtherflyTD= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly4)
            canvas.move(FigtherflyTD,-10,-50)
            mosca1=False
            mundo.after(vel+300,FigtherflyI)
        elif (mosca1==False):
            canvas.delete(FigtherflyTD)
            FigtherflyTD= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly1)
            canvas.move(FigtherflyTD,-10,50)
            mosca1=True
            mundo.after(vel+300,FigtherflyI)

    elif (continuarF1==True and  coordsFigther [0]-15 < 20 and coordsFigther [1] + 20 == 440): #Se valida que el enemigo esté en el borde de la segunda plataforma para aparecer al otro lado de la pantalla
        canvas.delete(FigtherflyTD)
        FigtherflyTD= canvas.create_image(775,420,anchor="center",image=fly3)
        mundo.after(0,FigtherflyI)

    elif (continuarF1==True and  coordsFigther [0]-15 > 490 and coordsFigther [1]+20<=440 and coordsFigther [1] + 20 > 320): #Se valida que el enemigo esté en la segunda plataforma del lazo izquierdo
        if (moscont==0):
            mosca1=True
            moscont+=1
            mundo.after(0,FigtherflyI)
        elif (mosca1==True):
            canvas.delete(FigtherflyTD)
            FigtherflyTD= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly4)
            canvas.move(FigtherflyTD,-10,-50)
            mosca1=False
            mundo.after(vel+300,FigtherflyI)
        elif (mosca1==False):
            canvas.delete(FigtherflyTD)
            FigtherflyTD= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly1)
            canvas.move(FigtherflyTD,-10,50)
            mosca1=True
            mundo.after(vel+300,FigtherflyI)

    elif (continuarF1==True and  coordsFigther [0]-15 <= 490 and coordsFigther [1] + 20 < 580 and coordsFigther [0]-15 == 490): #Se valida que cuando se llegue al limite de la segunda plataforma el enemigo caiga hasta la primera plataforma
        canvas.move(FigtherflyTD,0,10)
        mosca1=True
        mundo.after(0,FigtherflyI)

    elif (continuarF1==True and  coordsFigther [0]-15 > 50 and coordsFigther [1]+20<=580 and coordsFigther [1]+20 >520): #Se valida que el enemigo esté en la primera plataforma
        if (mosca1==True):
            canvas.delete(FigtherflyTD)
            FigtherflyTD= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly4)
            canvas.move(FigtherflyTD,-10,-50)
            mosca1=False
            mundo.after(vel+300,FigtherflyI)
        elif (mosca1==False):
            canvas.delete(FigtherflyTD)
            FigtherflyTD= canvas.create_image(coordsFigther[0],coordsFigther[1],anchor="center",image=fly1)
            canvas.move(FigtherflyTD,-10,50)
            mosca1=True
            mundo.after(vel+300,FigtherflyI)
        
    elif (continuarF1==True and  coordsFigther [0]-15 <=50 and coordsFigther [1] + 20 == 580): #Se valida que el enemigo esté en en el inicio de la tubería derecha de la pantalla para aparecer una vez más arriba al aldo izqueirdo de la pantalla
        canvas.delete(FigtherflyTD)
        mundo.after(100)
        FigtherflyTD= canvas.create_image(660+30,120+20,anchor="center",image=fly3)
        puntajeLui-=400
        canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+str(puntajeLui)))
        mundo.after(100)
        mundo.after(100,FigtherflyI)


x=random.randint(0,2)
continuarS= True
def SlipiceD ():
    """
    Función que contiene los movimientos del enemigo Slipice cuando sale por la tubería de la izquierda
    """
    global  ShellcreeperTI, SidestepperTI, FigtherflyTI, SlipiceTI,vel,continuarS,muertoS,Ldie,luigi,x,plat1,plat2,puntajeLui,Ayuda,plat1,plat2,plat3

    coordsSlip = canvas.coords(SlipiceTI)
    if (x==0 and coordsSlip[1]+20==300 and continuarS==True and muertoS==False):
        canvas.after(500)
        canvas.create_rectangle(260,320,540,300,fill="blue")
        continuarS=False
        muertoS=True
        plat1=True
        canvas.after(500)
        platcong()
        canvas.delete(SlipiceTI)
        SlipiceTI=canvas.create_polygon(0,0,0,0)
        
    elif (x==1 and coordsSlip[1]+20==440 and coordsSlip[0]>520 and continuarS==True and muertoS==False):
        canvas.after(500)
        canvas.create_rectangle(520,460,800,440,fill="blue")
        continuarS=False
        muertoS=True
        plat2=True
        platcong()
        canvas.after(500)
        canvas.delete(SlipiceTI)
        SlipiceTI=canvas.create_polygon(0,0,0,0)
        
    elif (x==2 and coordsSlip[1]+20==440 and coordsSlip[0]<280 and continuarS==True and muertoS==False):
        continuarS=False
        muertoS=True
        canvas.after(500)
        plat3=True
        canvas.create_rectangle(0,460,280,440,fill="blue")
        canvas.after(500)
        platcong()
        canvas.delete(SlipiceTI)
        SlipiceTI=canvas.create_polygon(0,0,0,0)
      
    if (Ldie==False and continuarS== True and( muertoS==False and Ayuda==False) and ((canvas.coords(luigi)[0]+20>= canvas.coords(SlipiceTI)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SlipiceTI)[0]+22)) and canvas.coords(luigi)[1]+30==canvas.coords(SlipiceTI)[1]+20):
        Ldie=True
        muertelui()
        mundo.after(vel,SlipiceD)
    elif (continuarS==True and coordsSlip[0]-30 <= 310 and coordsSlip [1] +20 == 160): #Se valida que el enemigo esté en la cuarta plataforma
        canvas.move(SlipiceTI,5,0)
        mundo.after(vel,SlipiceD)

    elif (continuarS==True and coordsSlip[0]-30 >310 and coordsSlip[1]+20 < 300): #Se valida que cuando se llegue al limite de la cuarta plataforma el enemigo caiga hasta la tercera plataforma
        canvas.move(SlipiceTI,0,10)
        mundo.after(20,SlipiceD)

    elif (continuarS==True and coordsSlip [0]-30 <= 510 and coordsSlip [1]+20 ==300):  #Se valida que el enemigo esté en la tercera plataforma
        canvas.move(SlipiceTI,5,0)
        mundo.after(vel,SlipiceD)

    elif (continuarS==True and coordsSlip [0]-30 > 510 and coordsSlip [1]+20 <440): #Se valida que cuando se llegue al limite de la tercera plataforma el enemigo caiga hasta la segunda plataforma
        canvas.move(SlipiceTI,0,10)
        mundo.after(20,SlipiceD)

    elif (continuarS==True and coordsSlip [0]-30 >=440 and coordsSlip[0] -30 < 750 and coordsSlip [1]+20 ==440): #Se valida que el enemigo esté en la segunda plataforma del lado derecho
        canvas.move(SlipiceTI,5,0)
        mundo.after(vel,SlipiceD)

    elif (continuarS==True and coordsSlip[0] -30 >= 750 and coordsSlip [1]+20 ==440): #Se valida que el enemigo esté en el borde de la segunda plataforma para aparecer al otro lado de la pantalla
        canvas.delete(SlipiceTI)
        SlipiceTI= canvas.create_image(30,420,anchor="center",image=fd2)
        mundo.after(0,SlipiceD)

    elif (continuarS==True and coordsSlip [0]-30 <= 250 and coordsSlip [1]+20==440): #Se valida que el enemigo esté en la segunda plataforma del lazo izquierdo
        canvas.move(SlipiceTI,5,0)
        mundo.after(vel,SlipiceD)


y=random.randint(0,2)
continuarS1= True
plat1=False
plat2=False
plat3=False
def SlipiceI ():
    """
    Función que contiene los movimientos del enemigo Slipice cuando sale por la tuberia derecha
    """
    global  ShellcreeperTD, SidestepperTD, FighterflyTD, SlipiceTD,vel,continuarS1,y,muertoS1,Ldie,puntajeLui,Ayuda,plat1,plat2,plat3

    coordSlip = canvas.coords(SlipiceTD)
    if (y==0  and continuarS1==True and coordSlip[1]+20==300 and muertoS1==False):
        canvas.after(500)
        canvas.create_rectangle(260,320,540,300,fill="blue")
        continuarS1=False
        muertoS1=True
        plat1=True
        canvas.after(500)
        platcong()
        canvas.delete(SlipiceTD)
        SlipiceTD=canvas.create_polygon(0,0,0,0)
    elif (y==1 and continuarS1==True and coordSlip[1]+20==440 and coordSlip[0]>520 and muertoS1==False):
        canvas.after(500)
        canvas.create_rectangle(520,460,800,440,fill="blue")
        continuarS1=False
        muertoS1=True
        platcong()
        plat2=True
        canvas.after(500)
        canvas.delete(SlipiceTD)
        SlipiceTD=canvas.create_polygon(0,0,0,0)
    elif (y==2 and continuarS1==True and coordSlip[1]+20==440 and coordSlip[0]<280 and muertoS1==False):
        continuarS1=False
        muertoS1=True
        platcong()
        canvas.after(500)
        plat3=True
        canvas.create_rectangle(0,460,280,440,fill="blue")
        canvas.after(500)
        canvas.delete(SlipiceTD)
        SlipiceTD=canvas.create_polygon(0,0,0,0)

    if (Ldie==False and (continuarS1== True and Ayuda==False) and muertoS1==False and ((canvas.coords(luigi)[0]+20>= canvas.coords(SlipiceTD)[0]-22) and (canvas.coords(luigi)[0]-20 <= canvas.coords(SlipiceTD)[0]+22)) and canvas.coords(luigi)[1]+30==canvas.coords(SlipiceTD)[1]+20):
        Ldie=True
        muertelui()
        mundo.after(vel,SlipiceI)

    elif (continuarS1== True and coordSlip[0]-30 >= 430 and coordSlip [1] +20 == 160): #Se valida que el enemigo esté en la cuarta plataforma
        canvas.move(SlipiceTD,-5,0)
        mundo.after(vel,SlipiceI)
        
    elif (continuarS1== True and coordSlip[0]-30 < 430 and coordSlip [1] + 20 < 300): #Se valida que cuando se llegue al limite de la cuarta plataforma el enemigo caiga hasta la tercera plataforma
        canvas.move(SlipiceTD,0,10)
        mundo.after(20,SlipiceI)
 
    elif (continuarS1== True and coordSlip[0]-30 >= 230 and coordSlip [1] +20 == 300):  #Se valida que el enemigo esté en la tercera plataforma
        canvas.move(SlipiceTD,-5,0)
        mundo.after(vel,SlipiceI)

    elif (continuarS1== True and coordSlip [0]-30 < 230 and coordSlip [1] + 20 < 440): #Se valida que cuando se llegue al limite de la tercera plataforma el enemigo caiga hasta la segunda plataforma
        canvas.move(SlipiceTD,0,10)
        mundo.after(20,SlipiceI)

    elif(continuarS1== True and coordSlip  [0]-30 <= 225 and coordSlip  [0]-30 >= -20 and coordSlip  [1] + 20 == 440): #Se valida que el enemigo esté en la segunda plataforma del lado derecho
        canvas.move(SlipiceTD,-5,0)
        mundo.after(vel,SlipiceI)

    elif (continuarS1== True and coordSlip  [0]-30 < 20 and coordSlip  [1] + 20 == 440): #Se valida que el enemigo esté en el borde de la segunda plataforma para aparecer al otro lado de la pantalla
        canvas.delete(SlipiceTD)
        SlipiceTD= canvas.create_image(760,420,anchor="center",image=fi2)
        mundo.after(0,SlipiceI)

    elif (continuarS1== True and coordSlip  [0]-30 >= 490 and coordSlip  [1]+20==440): #Se valida que el enemigo esté en la segunda plataforma del lazo izquierdo
        canvas.move(SlipiceTD,-5,0)
        mundo.after(vel,SlipiceI)

def platcong():
    """
    Deslizamiento por la plataforma congelada
    """
    global plat1,plat2,plat3,luigi,Ldie
    if Ldie==False and (plat3==True or plat2==True or plat1==True):
        if canvas.coords(luigi)[0]+30<=280 and plat3==True and canvas.coords(luigi)[1]+30>=440 and canvas.coords(luigi)[1]+30<580:
            canvas.move(luigi,0.5,0)
        elif canvas.coords(luigi)[0]-30>=520 and plat2==True and canvas.coords(luigi)[1]+30>=440 and canvas.coords(luigi)[1]+30<580:
            canvas.move(luigi,0.5,0)
        elif canvas.coords(luigi)[0]+30<=540 and canvas.coords(luigi)[0]-30>=240 and plat1==True and canvas.coords(luigi)[1]+30>=300 and canvas.coords(luigi)[1]+30<460:
            canvas.move(luigi,0.5,0)
        canvas.after(100,platcong)
 
#Vidas iniciales de los jugadores
Vidaslui=3
lifeHL=canvas.create_image(30,60,image=lhead)
LifesL=canvas.create_text(54,60,fill="Lime Green",font=("Charlemagne Std",12),text=("X"+ str (Vidaslui)))

Vidasmar=3
lifeHM=canvas.create_image(520,60,image=mhead)
LifesM=canvas.create_text(544,60,fill="Red",font=("Charlemagne Std",12),text=("X"+ str(Vidasmar)))

Mar=60
#Función con la muerte de Luigi
def muertelui():
    global luigi,Ldie,Vidaslui,LifesL,Mar
    canvas.itemconfig(luigi,image=ldie)
    canvas.create_image (750,120,image= Tub1)
    canvas.create_image (52,120,image= Tub2)
    canvas.create_image (770,550,image= Tub3)
    canvas.create_image (36,550,image= Tub4)   
    if (canvas.coords(luigi)[1]+26 <620):
        canvas.move(luigi,0,20)
        mundo.after(10,muertelui)
    else:
        canvas.delete(luigi)
        luigi=canvas.create_image(coordsI[0],coordsI[1],anchor="center",image=lui01)
        Vidaslui= Vidaslui- 1
        Ldie=False
        canvas.delete(LifesL)
        LifesL=canvas.create_text(Mar,60,fill="Lime Green",font=("Charlemagne Std",12),text=("X"+ str (Vidaslui)))
        Mar= Mar+60
        if Vidaslui==0:
            Ldie=True
            canvas.delete(luigi)
            print("GAME OVER")
            mundo.destroy()

# Función que vuelve a llamar al enemigo respectivo si no se ha muerto y está paralizado
                                                                                          

def MuerteEV():
    global continuarV,muertoV,continuarR,muertoR,Muert1,continuarF,muertoF,continuarV1,continuarV2,muertoV1,muertoV2,Muert2,Muert3,continuarR1,continuarR2,muertoR1,muertoR2,muertoF1,continuarF1
    if (continuarV==False and muertoV==False):
        continuarV=True
        mundo.after(0,ShellcreeperD)
def MuerteER():
    global continuarR,muertoR,Muert1
    if (continuarR==False and muertoR==False):
        continuarR=True
        Muert1=0
        mundo.after(0,SidestepperD)
def MuerteEF():
    global continuarF,muertoF    
    if (continuarF==False and muertoF==False):
        continuarF=True
        mundo.after(0,FigtherflyD)
def MuerteEV1():
    global continuarV1,muertoV1
    if (continuarV1==False and muertoV1==False):
        continuarV1=True
        mundo.after(0,ShellcreeperI)
def MuerteEV2():
    global muertoV2,continuarV2
    if (continuarV2==False and muertoV2==False):
        continuarV2=True
        mundo.after(0,ShellcreeperI1)
def MuerteER1():
    global Muert2,continuarR1,muertoR1
    if (continuarR1==False and muertoR1==False):
        Muert2=0
        continuarR1=True
        mundo.after(0,SidestepperI)
def MuerteER2():

    global Muert3, continuarR2,muertoR2
    if (continuarR2==False and muertoR2==False):
        Muert3=0
        continuarR2=True
        mundo.after(0,SidestepperD1)
def MuerteEF1():
    global continuarF1,muertoF1
    if (continuarF1==False and muertoF1==False):
        continuarF1=True
        mundo.after(0,FigtherflyI)
contpow=3
def POW():
    """
    Función del POW
    """
    global continuarV,contpow,powestado,muertoV,muertoS, muertoS1,continuarR,muertoR,Muert1,continuarF,muertoF,continuarV1,continuarV2,muertoV1,muertoV2,Muert2,Muert3,continuarR1,continuarR2,muertoR1,muertoR2,muertoF1,continuarF1,continuarS,continuarS1
    if (powestado==True and contpow>0):
 
        continuarV=False
        mundo.after(0,ShellcreeperD)

        continuarR=False
        mundo.after(0,SidestepperD)

        continuarF=False
        mundo.after(0,FigtherflyD)

        continuarV1=False
        mundo.after(0,ShellcreeperI)

        continuarV2=False
        mundo.after(0,ShellcreeperI1)

        continuarR1=False
        mundo.after(0,SidestepperI)

        continuarR2=False
        mundo.after(0,SidestepperD1)

        continuarF1=False
        mundo.after(0,FigtherflyI)

    contpow= contpow-1
    if contpow==2:
        canvas.itemconfig(poww,image=pow2)
    elif contpow==1:
        canvas.itemconfig(poww,image=pow3)
    elif contpow==0:
        canvas.delete(poww)
        powestado=False

starEstado=False
Pulsadastar=False
Pulsadavida=False
Ayuda=False
def star():
    """
    Función del Power Up Estrella
    """
    global starEstado,Pulsadastar,st,Ayuda
    canvas.create_image (750,120,image= Tub1)
    canvas.create_image (52,120,image= Tub2)
    canvas.create_image (770,550,image= Tub3)
    canvas.create_image (36,550,image= Tub4)
    if starEstado== True and Pulsadastar==False:
        Ayuda=False
        starEstado=False
        canvas.delete(st)
    elif Pulsadastar==True and Ayuda==True:
        Ayuda= False
        Pulsadastar=False
        starEstado=False

def vidaa ():
    """
    Función del Power Up vida
    """
    global vidaEstado,Pulsadavida,vid
    canvas.create_image (750,120,image= Tub1)
    canvas.create_image (52,120,image= Tub2)
    canvas.create_image (770,550,image= Tub3)
    canvas.create_image (36,550,image= Tub4)
    if vidaEstado==True and Pulsadavida==False:
        canvas.delete(vid)
        vidaEstado=False
    else:
        return None 

def MandarAsalvar():
    """
    Función para mandar a salvar la partida, se llama sola cada cierto tiempo
    """
    SalvarPartida()
    canvas.after(100*100,MandarAsalvar)
    
def SalvarPartida():
    """
    Función para salvar la partida
    """
    global canvas,mundo,img,NomL,NomM,archv,puntajeLui,puntajeMar,Vidasmar,Vidaslui,LifesL,lifesM,player1,player2,luigi
    archv=open("Partida_MarioBros.txt","w")
    Nivel=str(vel)
    PosLX= str(canvas.coords(luigi)[0])
    PosLY=str(canvas.coords(luigi)[1])
    PointsL=str(puntajeLui)
    NombreL=str(NomL)
    NombreM=str(NomM)
    PointsM= str(puntajeMar)
    LifesL= str(Vidaslui)
    LifesM=str(Vidasmar)

    archv.write(Nivel +'\n')
    archv.write(PosLX +'\n')
    archv.write(PosLY +'\n')
    archv.write(PointsL +'\n')
    archv.write(NombreL +'\n')
    archv.write(NombreM +'\n')
    archv.write(PointsM +'\n')
    archv.write(LifesL +'\n')
    archv.write(LifesM +'\n')
    archv.close()
        
def CargarJuego ():
    """
    Función para cargar el juego
    """
    global nombreArchivo,fon1,opc,mv,tit,fon2,archv,vel,scoreL,scoreM,player1,player2,menuu
    global g,h,SidestepperTI,x,y,archv,puntajeLui,LifesL,LifesM,puntajeMar,Vidasmar,Vidaslui,LifesL,lifesM,player1,player2,luigi,mario,ShellcreeperTI,ShellcreeperTD,ShellcreeperTD1,SidestepperTI,SidestepperTI1,SidestepperTD,FigtherflyTI,FigtherflyTD,SpliceTD,SpliceTI
    global continuarV,Miau,Ldie,vel,luigi,SlipiceTI,SlipiceTD,muertoV,continuarR,muertoR,Muert1,continuarF,muertoF,continuarV1,continuarV2,muertoV1,muertoV2,Muert2,Muert3,continuarR1,continuarR2,muertoR1,muertoR2,muertoF1,continuarF1
    global muertoF,muerto4RV,muerto4RV1,ShellcreeperTI,muerto4RV2,muerto4RR,muerto4RR1,muerto4RR2,muerto4RF,muerto4RF1,muerto4RS,muerto4RS1

    nombreArchivo= "Partida_MarioBros"
    canvas.delete(fon1,opc,mv,tit,fon2)
    menuu=True
    archv=open("Partida_MarioBros.txt","r")

    vel=int(archv.readline())
    posSLX= archv.readline()
    posSLY= archv.readline()
    puntajeLui= int(archv.readline())
    NombreLui=archv.readline()
    NombreMar=archv.readline()
    puntajeMar=int(archv.readline())
    Vidaslui=int(archv.readline())
    Vidasmar=int(archv.readline())


    vel=vel
    canvas.delete(luigi)
    luigi=canvas.create_image(posSLX,posSLY,image=lui01)
    canvas.itemconfig(scoreL,text=("Puntaje Luigi:"+ str(puntajeLui)))
    canvas.delete(player1)
    player1= canvas.create_text(134,50,fill="White",font=("Charlemagne Std",14),text=("Jugador 1: "+str(NombreLui)))
    canvas.delete(player2)
    player2= canvas.create_text(624,50,fill="White",font=("Charlemagne Std",14),text=("Jugador 2: "+str(NombreMar)))

    canvas.itemconfig(scoreM,text=("Puntaje Mario:"+ str(puntajeMar)))
    canvas.delete(LifesL)
    LifesL= canvas.create_text(54,50,fill="Lime Green",font=("Charlemagne Std",12),text=("X"+ str (Vidaslui)))
    canvas.itemconfig(LifesM,text=("X"+ str(Vidasmar)))

    canvas.delete(ShellcreeperTI)
    ShellcreeperTI= canvas.create_polygon(0,0,0,0)
    mundo.after(500,LlamarShell)

    canvas.delete(ShellcreeperTD)
    ShellcreeperTD= canvas.create_polygon(0,0,0,0)
    mundo.after(500*20,LlamarShellD)

    canvas.delete(SidestepperTI)
    SidestepperTI=canvas.create_polygon(0,0,0,0)
    mundo.after(500*40,LlamarSides)

    canvas.delete(ShellcreeperTD1)
    ShellcreeperTD1= canvas.create_polygon(0,0,0,0)
    mundo.after(500*60,LlamarShellD1)

    canvas.delete(SidestepperTI1)
    SidestepperTI1=canvas.create_polygon(0,0,0,0)
    mundo.after(500*80,LlamarSides1)

    canvas.delete(FigtherflyTD)
    FigtherflyTD= canvas.create_polygon(0,0,0,0)
    mundo.after(500*100,LlamarFigtherD)

    canvas.delete(SlipiceTI)
    SlipiceTI=canvas.create_polygon(0,0,0,0)
    mundo.after(500*120,LlamarSlipice)

    canvas.delete(SidestepperTD)
    SidestepperTD=canvas.create_polygon(0,0,0,0)
    mundo.after(500*140,LlamarSidesD)

    canvas.delete(FigtherflyTI)
    FigtherflyTI= canvas.create_polygon(0,0,0,0)
    mundo.after(500*160,LlamarFigther)

    canvas.delete(SlipiceTD)
    SlipiceTD=canvas.create_polygon(0,0,0,0)
    mundo.after(500*180,LlamarSlipiceD)
    MandarAsalvar()

#Menú de opciones

Fondo1= PhotoImage(file="fondoM.gif")
fon1=canvas.create_image (402,301,image=Fondo1)
Fondo2= PhotoImage(file="fondoM.gif")
fon2=canvas.create_image(402,301,image=Fondo2)
Titulo=PhotoImage(file="Mb.gif")
tit=canvas.create_image(360,100,image=Titulo)
Opciones= PhotoImage(file="Options.gif")
opc=canvas.create_image(405,350,image=Opciones)
Selector= PhotoImage(file="Mariogif.gif")
mv= canvas.create_image(250,235,anchor="center",image=Selector)
Niveles= PhotoImage(file="Niveles.gif")
Segundoselector= PhotoImage(file="star.gif")
com=PhotoImage(file="pressc.gif")
instr1= PhotoImage(file="Instrucciones1.gif")
instr2= PhotoImage(file="Instrucciones2.gif")
instr3= PhotoImage(file="Instrucciones3.gif")

def upKey(event):
    """
    Función para mover los selectores del menú hacia arriba
    """
    global Seg,cni,menuu,mv,luigi
    if menuu==False:
        if Seg == False:
            cmv= canvas.coords(mv)
            if (cmv[1]>=275):
                canvas.move(mv,0,-65)
        elif Seg==True:
            coniv= canvas.coords(cni)
            if (coniv[1]>280):
                canvas.move(cni,0,-46)
def downKey(event):
    """
    Función para mover los selectores del menú hacia abajo
    """
    global Seg,cni,menuu,mv ,luigi
    if menuu==False:
        if Seg==False:
            cmv= canvas.coords(mv)
            if (cmv[1]<=340):
                canvas.move(mv,0,65)
        elif Seg==True:
            coniv= canvas.coords(cni)
            if (coniv[1]<450):
                canvas.move(cni,0,46)
Seg=False
menuu=False
Nm=False
lastone=False
continstruc=1
Instrucciones=False
NomM= ""
NomL=""
def teclac(event):
    """
    Función con las opciones 
    """
    global menuu,mv,lastone,instr,luigi,numpag,Seg,Nm,Instrucciones,opc,continstruc,h,g,Primernombre,contt,player1,player2,Segundonombre,nombreUsuario1,nombreUsuario2,ltemp,mtemp,Seg,cni,vel,niv,Nm,Enem,enemigo1,player1,player2,Jugador1,Jugador2
    global NomL,NomM
    cmv= canvas.coords(mv)
    tecla= repr(event.char)
    if tecla=="'c'" and menuu== False:
        if Nm==False and Seg==False and Instrucciones==False:
            if cmv[1]==365 and cmv[0]==250:
                canvas.delete(opc,mv)
                Instrucciones=True
                instr=canvas.create_image(400,390,image=instr1)

            elif (cmv[1]==235 and cmv[0]==250):
                canvas.after(500)
                canvas.delete(fon1,opc,mv)
                mundo.after(500)
                niv= canvas.create_image(400,400,anchor="center",image=Niveles)
                cni=canvas.create_image(325,280,anchor="center",image=Segundoselector)
                Seg= True
            elif (cmv[1]==300 and cmv[0]==250):
                CargarJuego()
        elif Instrucciones==True:
            if continstruc==1:
                numpag=canvas.create_text(780,550,text=(continstruc,"/3"),fill="red",font=("Charlemagne Std",14))
                continstruc+=1
            elif continstruc==2:
                canvas.itemconfig(instr,image=instr2)
                canvas.itemconfig(numpag,text=(continstruc,"/3"))                                       
                continstruc+=1
            elif continstruc==3:
                canvas.itemconfig(instr,image=instr3)
                canvas.itemconfig(numpag,text=(continstruc,"/3"))
                continstruc+=1
            elif continstruc==4:
                canvas.delete(instr,numpag)
                opc=canvas.create_image(405,350,image=Opciones)
                mv= canvas.create_image(250,235,anchor="center",image=Selector)
                Instrucciones=False
        elif Nm==False and (Seg==True or Instrucciones==False):
            coniv=canvas.coords(cni)
            if (coniv[0]==325 and coniv[1]==280):
                vel=400      
            elif coniv[0]==325 and coniv[1]==326:
                vel=200
            elif coniv[0]==325 and coniv[1]==372:
                vel=100
            elif coniv[0]==325 and coniv[1]==418:
                vel=90
            elif coniv[0]==325 and coniv[1]==464:
                vel=60
            canvas.delete(cni,niv)
            Nm=True
            if Nm==True and lastone==False and Instrucciones==False:
                nombreUsuario1= canvas.create_text(400,240,text="Primer jugador digite su nombre de usuario:",fill="white",font=("Charlemagne Std",10))
                Primernombre= Entry(mundo,bd=5)
                Primernombre.place(x=300,y=260)
                ltemp=canvas.create_image(350,320,image=ld1)
                nombreUsuario2=canvas.create_text(400,400,text="Segundo jugador digite su nombre de usuario:",fill="white",font=("Charlemagne Std",10))
                Segundonombre=Entry(mundo,bd=5)
                Segundonombre.place(x=300,y=420)
                mtemp=canvas.create_image(350,480,image=md1)
                contt=canvas.create_image(620,550,image=com)
        elif Nm==True and lastone==False and Instrucciones==False:
            g=Primernombre.get()
            NomL=g
            h=Segundonombre.get()
            NomM=h 
            canvas.itemconfig(player1,text=("Jugador 1: "+str(g)))
            canvas.itemconfig(player2,text=("Jugador 2: "+ str(h)))
            canvas.delete(ltemp,mtemp,fon2,tit,contt,nombreUsuario1,nombreUsuario2)
            Primernombre.destroy()
            Segundonombre.destroy()
            lastone=True
            menuu=True
            canvas.focus_set()
            mundo.after(500,LlamarShell)
            mundo.after(500*20,LlamarShellD)                 
            mundo.after(500*40,LlamarSides)
            mundo.after(500*60,LlamarShellD1)
            mundo.after(500*80,LlamarSides1)
            mundo.after(500*100,LlamarFigtherD)
            mundo.after(500*120,LlamarSlipice)
            mundo.after(500*140,LlamarSidesD)
            mundo.after(500*160,LlamarFigther)
            mundo.after(500*180,LlamarSlipiceD)
            MandarAsalvar()    


# Bind del menú de opciones
mundo.bind('<Up>',upKey)
mundo.bind('<Down>',downKey)
mundo.bind('<Key>',teclac)

#-------------------
mundo.mainloop()

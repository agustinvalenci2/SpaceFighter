import tkinter,math,random,winsound
from threading import Thread
T=False
wind = tkinter.Tk()
wind.config(bg="black")
menu = tkinter.Toplevel(bg="black",relief="flat")
(minivanvel,fightvel,h,m,X2,distancia,levelid,GAS,GAS2,m1,m2,vel,x) = ([0.25,0.5,1,2,3,18],[0.5,1,2,3,5,25],[],[],[],0,0,90000,90000,1,1,9,0)
Save = open("save.txt","r+")
class enemigos:
    def collisions(self, item1,item2,push):
        """
        funcion que detecta las collisiones
        """
        global GAS,GAS2
        h=40
        (xp,yp,xm,ym) =(Canvas.coords(item1)[0]-(h/2),Canvas.coords(item1)[1]-(h/2),Canvas.coords(item2)[0]-(h/2),Canvas.coords(item2)[1]-(h/2))
        a= (xp>=xm and xp<=xm+h and yp>=ym and yp<=ym+h or(xp+h>=xm and xp+h<=xm+h and yp>=ym and yp<=ym+h))
        b=(yp>=ym and yp<=ym+h and xp>xm and xp <xm+h or(yp+h>ym and yp+h <=ym+h and xp>=xm and xp<=xm) )
        c=(yp>=ym and yp<=ym+h and xp+h>xm and xp+h <xm+h or(yp+h>ym and yp+h <=ym+h and xp+h>=xm and xp+h<=xm+h) )
        if(a or b or c):
            if(item1 ==player) :
                if(item2 ==gasolina or item2 ==gasolina2):
                        GAS+=15000
                        if(item2==gasolina):
                            Canvas.move(gasolina,0,-900)
                        elif(item2==gasolina2):
                            Canvas.move(gasolina2,0,-900)
                elif(Canvas.coords(item1)[0]<225):
                    Canvas.move(item1,-push,0)
                    GAS-=4500
                else:
                    Canvas.move(item1,push,0)
                    GAS-=4500
                if(item2==gasolina):
                        Canvas.move(gasolina,0,-900)
                elif(item2==gasolina2):
                        Canvas.move(gasolina2,0,-900)
                elif(item2==misil1 or item2 ==misil2):
                    GAS=0
                
                    
          
            else:
                    if(Canvas.coords(item1)[0]<675):
                        Canvas.move(item1,-push,0)
                        GAS2-=1500
                    if(item2 ==gasolina12 or item2 ==gasolina22):
                        GAS2+=15000
                        if(item2==gasolina12):
                            Canvas.move(gasolina12,0,-900)
                        elif(item2==gasolina22):
                            Canvas.move(gasolina22,0,-900)
                    else:
                        Canvas.move(item1,push,0)
                        GAS2-=1500
                    if( item2==misil12 or item2 ==misil22):
                        GAS2=0
                    

    def minivan(self,item,v):
        """
        mueve la nave en linea recta sin nmunguncambio de direccion
        """
        Canvas.move(item,0,v)

    def fighter(self,item,item2,dx,dy):
        """
        mueve la nave persiguiendo al jugador
        """
        if(Canvas.coords(item2)[0]<Canvas.coords(item)[0]):
            Canvas.move(item,-dx,dy)
        elif(Canvas.coords(item2)[0]>Canvas.coords(item)[0]):
            Canvas.move(item,dx,dy)
        if(Canvas.coords(item2)[0]==Canvas.coords(item)[0]):
            Canvas.move(item,0,3*dy)
    def runner(self,item,v):
        """
        se mueve aleatroriamente
        """

        z = random.randint(-20,20)               
        Canvas.move(item,z,v)

    def cos(self,item,f,v):
        global x
        """
        va haciendo saltos de lado a lado
        """
        x+=.01
        Canvas.move(item,3*math.cos(x),3*math.sin(x))
        Canvas.move(item,0,v)
       
    def sin(self,item,f,v):
        """
        describe  curvas
        """
        y= math.sin(Canvas.coords(item)[1]*math.pi/f)*v*5
        Canvas.move(item,y,v)
    def limite_Y(self,item,limit):
        """
        esta funcion hace que todos las naves aparescan arriba de nuevo
        """
        w=random.randint(0,900)
        x=Canvas.coords(item)[0]
        if(Canvas.coords(item)[1]>=limit):
            Canvas.move(item,w-x,-limit)
    def limite_X(self,item,izq,der,G):
        """
        hace que las naves posean un limite y si el jugador la cruza perdera una cantidad considerable de energia
        """
        global GAS,GAS2
        if(Canvas.coords(item)[0]>=der):
            Canvas.move(item,-50,0)
            if(item==player):
                GAS//=2
            if(item==player2):
                 GAS2//=2
        if(Canvas.coords(item)[0]<=izq):
            Canvas.move(item,50,0)
            if(item==player):
                GAS//=2
            if(item==player2):
                 GAS2//=2
def reload():
    """
    funcion para cargar partida guardada 
    """
    global levelid,GAS,distancia,GAS2
    levelid=int(m[0])-1
    play_sound(levelid)
    GAS=int(m[1])
    distancia=int(m[2])
    GAS2= int(m[4])
    menu.wm_iconify()
    wind.wm_deiconify()
    Canvas.focus_set()
    label.pack(side = tkinter.RIGHT)
    Canvas.pack()
    main()
def boton(item,x,y):
        """
        funcion que habilita los botones
        """
        h=50
        if(CC.coords(item)[0]<x and CC.coords(item)[0]+h>x and CC.coords(item)[1]<y and CC.coords(item)[1]+h>y):
             return True
        else:
            return False
def nivel(Id):
       """
       funcion que carga el nivel
       """
       global levelid,m,T
       m=[]
       if(Id==5):
           for v in range(9):
               x=Save.readline()
               x.split()
               m.append(x)
               x.split("\n")
           reload()
       else:
           menu.iconify()
           wind.state('zoomed')
           levelid=Id
           play_sound(Id)
           Canvas.focus_set()
           label.pack(side = tkinter.RIGHT)
           Canvas.pack()
           T=True
           main()
def nivelselec(event):
    """
    funcion que detecta que nivel selecciono
    """
    global levelid
    menu.focus_set()
    botones =[boton1,boton2,boton3,boton4,boton5,boton6]
    for x in  range(6):
        if(boton(botones[x],event.x,event.y)):
                nivel(x)
def keyup(e):
  """
  funcion de tecla liberada
  """
  global h
  if(e.keycode in h):
    h.pop(h.index(e.keycode))
def keydown(e):
  """
  funcion tecla presionada
  """
  global h
  if( not e.keycode in h):
    h.append(e.keycode)
def key():
  """
  funcion que hace que la nave del jugador se mueva
  """
  global h,m1,m2
  if(65 in h and m1==1):
    Canvas.move(player,-5,0)
  if(74 in h and m2==1):
    Canvas.move(player2,-5,0)
  if(68 in h and m1==1):
    Canvas.move(player,5,0)
  if(76 in h and m2==1):
    Canvas.move(player2,5,0)
  if(83 in h or 75 in h):
        Save.seek(0)
        score= str(levelid+1)+" \n"+str(GAS)+" \n"+str(distancia)+" \n"+e.get()+" \n"+str(GAS2)+" \n"+f.get()
        Save.write(score)        
mons = enemigos()
Canvas = tkinter.Canvas(wind,height=900,width=900,bg="black")
Canvas.create_line(450,0,450,900,fill="white",dash=250)
Canvas.bind("<KeyPress>",keydown)
Canvas.bind("<KeyRelease>",keyup)
play = tkinter.PhotoImage(file="player.png")
enemigo1 = tkinter.PhotoImage(file="enemigo1.png")
enemigo2 = tkinter.PhotoImage(file="enemigo2.png")
enemigo3 = tkinter.PhotoImage(file="enemigo3.png")
enemigo4 = tkinter.PhotoImage(file="enemigo4.png")
enemigo5 = tkinter.PhotoImage(file="enemigo5.png")
enemigo6 = tkinter.PhotoImage(file="enemigo6.png")
space = tkinter.PhotoImage(file="space fighters.png")
fondo= tkinter.PhotoImage(file="fondo.png")
gas= tkinter.PhotoImage(file="gas.png")
BOOM = tkinter.PhotoImage(file="Bomb_Explosion.png")
for l in range(100):
    m=math.sin(l*math.pi/80)*100
    a=Canvas.create_oval(10+10*l,10+10*m,20+10*l,20+10*m,fill="white")
    X2.append(a)
gasolina=Canvas.create_image(150,-100,image=gas)
gasolina2=Canvas.create_image(150,-100,image=gas)
mini=Canvas.create_image(350,-150,image=enemigo1)
runner=Canvas.create_image(260,-150,image=enemigo2)
fight = Canvas.create_image(250,-150,image=enemigo3)
misil1 = Canvas.create_image(250,-1050,image=enemigo6)
misil2 = Canvas.create_image(250,-1050,image=enemigo6)
player = Canvas.create_image(150,650,image=play)
sini=Canvas.create_image(350,-150,image=enemigo4)
sini2=Canvas.create_image(250,-150,image=enemigo5)
gasolina12=Canvas.create_image(150+400,-100,image=gas)
gasolina22=Canvas.create_image(150+400,-100,image=gas)
mini2=Canvas.create_image(350+400,-150,image=enemigo1)
runner2=Canvas.create_image(260+400,-150,image=enemigo2)
fight2 = Canvas.create_image(250+400,-150,image=enemigo3)
misil12 = Canvas.create_image(250+400,-1050,image=enemigo6)
misil22 = Canvas.create_image(250+400,-1050,image=enemigo6)
player2 = Canvas.create_image(150+400,650,image=play)
sini12=Canvas.create_image(350,-150,image=enemigo4)
sini22=Canvas.create_image(250,-150,image=enemigo5)
e = tkinter.Entry(menu)
f = tkinter.Entry(menu)
wind.iconify()
lista =[mini,runner,sini,fight,sini2,misil1,misil2,gasolina,gasolina2]
lista2 =[mini2,runner2,sini12,fight2,sini22,misil12,misil22,gasolina12,gasolina22]
def limit(listid,li,b,c,pl):
    """
    esta funcion llama las collisions y los limites de los jugadores
    """
    global GAS,GAS2
    mons.limite_Y( li[listid],900)
    mons.limite_X(li[listid],b,c,GAS)
    if(pl==player):
        mons.collisions(pl,li[listid],35)
        mons.limite_X(li[listid],b,c,GAS)
    elif(pl==player2):
        mons.collisions(pl,li[listid],35)
        mons.limite_X(li[listid],b,c,GAS2)

def main():
    """
    funcion la cual llama a todas las demas y donde est a la recursion 
    """
    global GAS,distancia,levelid,Save,GAS2,m1,m2,X2,U,vel
    distancia+=10
    z = "level:  "+str(levelid+1)+"\n energy1: "+str(GAS)+"\n energy2:"+str(GAS2)+"\ndistance: "+str(distancia)+"\nplayer:\n "+e.get()+"\n"+f.get()+"\nSpace Fighters™\n"
    a.set(z)
    mons.runner( lista[1],minivanvel[levelid]*1.3)
    limit(1,lista,0,450,player)
    mons.sin( lista[2],100,minivanvel[levelid]*1.8)
    limit(2,lista,0,450,player)
    mons.fighter( lista[3],player,fightvel[levelid],minivanvel[levelid]*2.5)
    limit(3,lista,0,450,player)
    mons.cos( lista[4],60,minivanvel[levelid]*1.5)
    limit(4,lista,0,450,player)
    mons.runner( lista2[1],minivanvel[levelid]*1.3)
    limit(1,lista,0,450,player)
    mons.sin( lista[2],100,minivanvel[levelid]*1.8)
    limit(2,lista,0,450,player)
    mons.cos( lista[4],60,minivanvel[levelid])
    limit(4,lista,0,450,player)
    for contador in [0,5,6,7,8]:
        mons.minivan(lista[contador],minivanvel[levelid]*2)
        limit(contador,lista,0,450,player)
        mons.minivan(lista2[contador],minivanvel[levelid]*2)
        limit(contador,lista2,450,900,player2)
    mons.limite_X(player,0,400,GAS)
    mons.runner( lista[1],minivanvel[levelid]*1.3)
    limit(1,lista2,450,900,player2)
    mons.sin( lista2[2],100,minivanvel[levelid]*1.8)
    limit(2,lista2,450,900,player2)
    mons.fighter( lista2[3],player2,fightvel[levelid],minivanvel[levelid]*2.5)
    limit(3, lista2,450,900,player2)
    mons.cos( lista2[4],60,minivanvel[levelid])
    limit(4, lista2,450,900,player2)
    mons.limite_X(player2,450,900,GAS2)
    mons.runner( lista2[1],minivanvel[levelid]*1.3)
    limit(1,lista2,450,900,player2)
    mons.sin( lista2[2],100,minivanvel[levelid]*1.8)
    limit(2,lista2,450,900,player2)
    mons.cos( lista2[4],60,minivanvel[levelid])
    limit(4,lista2,450,900,player2)
    key()
    for b in range(100):
        Canvas.move(X2[b],0,10*minivanvel[levelid])
        mons.limite_Y(X2[b],900)
    if(distancia>30000 and levelid<=4):
        levelid+=1
        distancia=0
    if(levelid==5 and distancia>9000):
        if(Canvas.coords(player)[1]>-50):
            mons.minivan(player,-10)
            mons.minivan(player,-10)
        else:
           return 0
    if(m1==2):
            GAS=0
    if(m2==2):
            GAS2=0
    if(GAS<0 ):
        if(m1==1):
            Canvas.create_image(Canvas.coords(player)[0],Canvas.coords(player)[1],image=BOOM)
            m1=2
    else:
        GAS-=3
    if(GAS2<0 ):
        if(m2==1):
            Canvas.create_image(Canvas.coords(player2)[0],Canvas.coords(player2)[1],image=BOOM)
            m2=2
            GAS2=0
    else:
        GAS2-=3
    if(GAS<=0 and GAS2<=0):
        return 0
        Save.close()
    Canvas.after(5,main)
def sonido(lvl):
    global WW
    if(lvl==0):
         winsound.PlaySound("nvl1.wav",1)
    elif(lvl==1):
       winsound.PlaySound("nvl2.wav",1)
    elif(lvl==2):
       winsound.PlaySound("nvl3.wav",1)
    elif(lvl==3):
      winsound.PlaySound("nvl4.wav",1)
    elif(lvl==4):
        winsound.PlaySound("nvl5.wav",1)
def play_sound(lvl):
    pl = Thread(target=sonido,  args=[lvl])
    pl.start()
CC = tkinter.Canvas(menu,height=400,width=400,bg="black",relief="groove")
CC.bind("<Button-1>",nivelselec)
ff=CC.create_image(200,200,image=fondo)
boton1 =CC.create_rectangle(100,350,150,400,fill="white")
boton2 =CC.create_rectangle(160,350,210,400,fill="blue")
boton3 =CC.create_rectangle(220,350,270,400,fill="green")
boton4 =CC.create_rectangle(280,350,330,400,fill="purple")
boton5 =CC.create_rectangle(340,350,390,400,fill="red")
boton6 =CC.create_rectangle(40,350,90,400,fill="Pink")
anim= CC.create_image(300,300,image=enemigo3)
anima= CC.create_image(200,200,image=enemigo1)
animaa= CC.create_image(100,300,image=enemigo4)
def menu_anim():
    global vel,T
    if(T):
        return 0
    else:
        if(CC.coords(anima)[0]>300 or CC.coords(anima)[0]<40):
            vel*=-1
        CC.move(animaa,vel,vel)
        CC.move(anima,vel,0)
        CC.move(anim,vel,0)
        CC.after(10,menu_anim)
title=CC.create_image(150,150,image=space)
a = tkinter.StringVar()
label = tkinter.Label(wind,textvariable= a,font=("Times",12,"bold"),fg="white",bg="black")
e.pack()
f.pack()
menu_anim()
CC.pack()
wind.mainloop()


        


import tkinter
import random
import math

import time

level =[4000,3000,2000,1500,1000,150]
minus =[2,4,6,8,10,12]
choquelas =[100,200,300,400,500,2000]
push =[2,3,4,5,10,30]
levelid = 0
vel=[10,2]
GAS=200000
avance=0
Save = open("save.txt","r+")

 
  
  
def lose():
  global wind,GAS
  play = tkinter.PhotoImage(file="player.png")


  fondo = tkinter.PhotoImage(file="fondo1.png")
   
  enemigo1 = tkinter.PhotoImage(file="enemigo1.png")
  enemigo2 = tkinter.PhotoImage(file="enemigo2.png")
  enemigo3 = tkinter.PhotoImage(file="enemigo3.png")
  enemigo4 = tkinter.PhotoImage(file="enemigo4.png")
  enemigo5 = tkinter.PhotoImage(file="enemigo5.png")


  Canvas=tkinter.Canvas(wind,height=800,width=700)

  men = tkinter.Canvas(menu,height=400,width=400)
  fondoo = Canvas.create_image(400,350,image=fondo)
  gasolina=Canvas.create_rectangle(550,-100,500,-50,fill="white")
  gasolina2=Canvas.create_rectangle(150,-100,100,-50,fill="white")
  mini=Canvas.create_image(150,150,image=enemigo1)
  runner=Canvas.create_image(90,150,image=enemigo2)
  fight = Canvas.create_image(350,150,image=enemigo3)
  player = Canvas.create_image(450,650,image=play)
  sini=Canvas.create_image(150,650,image=enemigo4)
  sini2=Canvas.create_image(150,650,image=enemigo5)
  GAS=200000
  avance=0
  levelid=0
  menu.focus_set()
  wind.destroy()
  wind= tkinter.Tk()
  men.pack()
  menu.wm_state('normal')
def enemies():
 
  global GAS,levelid,avance,a
  a.set("nivel:  "+str(levelid+1)+"\t"+" gas: "+str(GAS)+"\t"+ " distancia: "+str(avance))
 
  collisions()
  j = random.randint(0,level[levelid])
  if(j in range(0,30)):
    summon()
    minivan()
  
  if(j in range(31,60)):
    run()
  if(j in range(61,90)):
    
    fighter()
  if(j in range(91,120)):
     sin()
  if(j in range(121,150)):
     sin2()
  if(j in range(0,15)):
      comb()
  if(j in range(16,30)):
      comb2()
  GAS-=minus[levelid]
  avance+=vel[0]
  
  if(GAS<=0):
    lose()
  elif(avance>=150000 and levelid<=5):
    levelid+=1
    avance=0
  elif(Canvas.coords(player)[0]<=0 or Canvas.coords(player)[0]>=610):
    GAS=0
  
  Canvas.after(1,enemies)
  
def collisions():
    i=push[levelid]
    h=90
    global GAS
   
    xp =Canvas.coords(player)[0]
    yp =Canvas.coords(player)[1]
    xm = Canvas.coords(mini)[0]
    ym = Canvas.coords(mini)[1]
    xr = Canvas.coords(runner)[0]
    yr = Canvas.coords(runner)[1]
    xf = Canvas.coords(fight)[0]
    yf = Canvas.coords(fight)[1]
    xs = Canvas.coords(sini)[0]
    ys = Canvas.coords(sini)[1]
    xz = Canvas.coords(sini2)[0]
    yz = Canvas.coords(sini2)[1]
    xg = Canvas.coords(gasolina)[0]
    yg = Canvas.coords(gasolina)[1]
    xg2 = Canvas.coords(gasolina2)[0]
    yg2 = Canvas.coords(gasolina2)[1]
    if(xp>=xg and xp<=xg+50 and yp>=yg and yp<=yg+50 or(xp+h>=xg and xp+h<=xg+50 and yp>=yg and yp<=yg+50)):
     
      
       GAS+=50000
       Canvas.move(gasolina,550,-800)
    if(xp>=xg2 and xp<=xg2+50 and yp>=yg2 and yp<=yg2+50 or(xp+h>=xg2 and xp+h<=xg2+50 and yp>=yg2 and yp<=yg2+50)):
     
      
       GAS+=50000
       Canvas.move(gasolina2,150,-800)
    if(Canvas.coords(player)[0]>350):
      
          
      if(xp>=xr and xp<=xr+90 and yp>=yr and yp<=yr+90 or(xp+h>=xr and xp+h<=xr+90 and yp>=yr and yp<=yr+90)):

        GAS-=choquelas[levelid]

        Canvas.move(player,1*i,0)
     

      if(xp>=xf and xp<=xf+90 and yp>=yf and yp<=yf+90 or(xp+h>=xf and xp+h<=xf+90 and yp>=yf and yp<=yf+90)):
 
        GAS-=choquelas[levelid]

        Canvas.move(player,1*i,0)


      if(xp>=xm and xp<=xm+90 and yp>=ym and yp<=ym+90 or(xp+h>=xm and xp+h<=xm+90 and yp>=ym and yp<=ym+90)):

        GAS-=choquelas[levelid]

        Canvas.move(player,1*i,0)

       
      if(xp>=xs and xp<=xs+90 and yp>=ys and yp<=ys+90 or(xp+h>=xs and xp+h<=xs+90 and yp>=ys and yp<=ys+90)):
          GAS-=choquelas[levelid] 
        
          Canvas.move(player,1*i,0)
           
      if(xp>=xz and xp<=xz+90 and yp>=yz and yp<=yz+90 or(xp+h>=xz and xp+h<=xz+90 and yp>=yz and yp<=yz+90)):

       GAS-=choquelas[levelid]

          
       Canvas.move(player,1*i,0)

    else:
    
        
       if(xp>=xr and xp<=xr+90 and yp>=yr and yp<=yr+90 or(xp+h>=xr and xp+h<=xr+90 and yp>=yr and yp<=yr+90)):

        GAS-=choquelas[levelid]

        Canvas.move(player,-1*i,0)


       if(xp>=xf and xp<=xf+90 and yp>=yf and yp<=yf+90 or(xp+h>=xf and xp+h<=xf+90 and yp>=yf and yp<=yf+90)):
    
          GAS-=choquelas[levelid]

          Canvas.move(player,-1*i,0)
     

       if(xp>=xm and xp<=xm+90 and yp>=ym and yp<=ym+90 or(xp+h>=xm and xp+h<=xm+90 and yp>=ym and yp<=ym+90)):

          GAS-=choquelas[levelid]
          
          Canvas.move(player,-1*i,0)
     
         
       if(xp>=xs and xp<=xs+90 and yp>=ys and yp<=ys+90 or(xp+h>=xs and xp+h<=xs+90 and yp>=ys and yp<=ys+90)):

          GAS-=choquelas[levelid]
  
          Canvas.move(player,-1*i,0)
  
       if(xp>=xz and xp<=xz+90 and yp>=yz and yp<=yz+90 or(xp+h>=xz and xp+h<=xz+90 and yp>=yz and yp<=yz+90)):

        GAS-=choquelas[levelid]

            
        Canvas.move(player,-1*i,0)

       

            
        Canvas.move(player,-1*i,0)

def main(event):
   global levelid
   men.focus_set()
   if(men.coords(boton1)[0]<event.x and men.coords(boton1)[0]+50>event.x):
     if(men.coords(boton1)[1]<event.y and men.coords(boton1)[1]+50>event.y):
       menu.wm_state('iconic')
       wind.wm_state('zoomed')
  
       Canvas.focus_set()
       levelid=0
       enemies()
       label.pack()
       Canvas.pack()
   elif(men.coords(boton2)[0]<event.x and men.coords(boton2)[0]+50>event.x):
     if(men.coords(boton2)[1]<event.y and men.coords(boton2)[1]+50>event.y):
       menu.wm_state('iconic')
       wind.wm_state('zoomed')
    
       Canvas.focus_set()
       levelid=1
       enemies()
       label.pack()
       Canvas.pack()
   elif(men.coords(boton3)[0]<event.x and men.coords(boton3)[0]+50>event.x):
     if(men.coords(boton3)[1]<event.y and men.coords(boton3)[1]+50>event.y):
       menu.wm_state('iconic')
       wind.wm_state('zoomed')
     
       Canvas.focus_set()
       levelid=2
       enemies()
       label.pack()
       Canvas.pack()
   elif(men.coords(boton4)[0]<event.x and men.coords(boton4)[0]+50>event.x):
     if(men.coords(boton4)[1]<event.y and men.coords(boton4)[1]+50>event.y):
       menu.wm_state('iconic')
       wind.wm_state('zoomed')
      
       Canvas.focus_set()
       levelid=3
       enemies()
       label.pack()
       Canvas.pack()
   elif(men.coords(boton5)[0]<event.x and men.coords(boton5)[0]+50>event.x):
     if(men.coords(boton5)[1]<event.y and men.coords(boton5)[1]+50>event.y):
       menu.wm_state('iconic')
       wind.wm_state('zoomed')
    
       Canvas.focus_set()
       levelid=4
       enemies()
       label.pack() 
       Canvas.pack()
     

def key(event):
    """
    """
    tecla = repr(event.char)

    if(tecla=="'d'" or tecla =="'D'"):
        Canvas.move(player,15,0)
    if(tecla=="'a'" or tecla =="'A'"):
        Canvas.move(player,-15,0)
        
wind =tkinter.Tk()
menu = tkinter.Tk()
def run():
    """
    """
    if(Canvas.coords(runner)[1]<800):
        
       z =random.randint(-100,100)
       y =random.randint(0,5000)
       if(Canvas.coords(runner)[0]>0 and Canvas.coords(runner)[0]<450):
           if(y<350):
               Canvas.move(runner,z,90)
              
           else:
               Canvas.move(runner,0,90)
         
       else:
            Canvas.move(runner,30,-Canvas.coords(runner)[1])
    else:
        Canvas.move(runner,0,-800)
def sin2():
  
      y = math.cos(Canvas.coords(sini2)[1]*math.pi*2/3)*40
      if(Canvas.coords(sini2)[1]<800):
        Canvas.move(sini2,y,90)
          
      else:
        Canvas.move(sini2,0,-800)
def sin():
      y = math.sin(Canvas.coords(sini)[1]*math.pi*2/3)*30
      if(Canvas.coords(sini)[1]<800):
        Canvas.move(sini,y,90)
          
      else:
        Canvas.move(sini,0,-800)
def comb():
    
    if(Canvas.coords(gasolina)[1]<800):
        Canvas.move(gasolina,0,80)
    else:
        Canvas.move(gasolina,0,-800)
def comb2():
    
    if(Canvas.coords(gasolina2)[1]<800):
        Canvas.move(gasolina2,0,80)
    else:
        Canvas.move(gasolina2,0,-800)
def minivan():
    if(Canvas.coords(mini)[1]<800):
        Canvas.move(mini,0,80)
    else:
        Canvas.move(mini,0,-800)
def summon():
  x=random.randint(0,40)
  if(Canvas.coords(mini)[0]<500):
    Canvas.move(mini,x,0)
  else:
      Canvas.move(mini,-2*x,0)
    

      
def fighter():
    if(Canvas.coords(fight)[1]<800):
         if(Canvas.coords(player)[0]<Canvas.coords(fight)[0]):
            Canvas.move(fight,-15,50)
            
         elif(Canvas.coords(player)[0]>Canvas.coords(fight)[0]):
            Canvas.move(fight,15,50)
            
         else:
            Canvas.move(fight,0,50)
          
    else:
         Canvas.move(fight,0,-800)
      


play = tkinter.PhotoImage(file="player.png")


fondo = tkinter.PhotoImage(file="fondo1.png")
 
enemigo1 = tkinter.PhotoImage(file="enemigo1.png")
enemigo2 = tkinter.PhotoImage(file="enemigo2.png")
enemigo3 = tkinter.PhotoImage(file="enemigo3.png")
enemigo4 = tkinter.PhotoImage(file="enemigo4.png")
enemigo5 = tkinter.PhotoImage(file="enemigo5.png")


Canvas=tkinter.Canvas(wind,height=1000,width=700)

men = tkinter.Canvas(menu,height=400,width=400)

gasolina=Canvas.create_rectangle(550,-100,500,-50,fill="white")
gasolina2=Canvas.create_rectangle(150,-100,100,-50,fill="white")
mini=Canvas.create_image(150,150,image=enemigo1)
runner=Canvas.create_image(90,150,image=enemigo2)
fight = Canvas.create_image(350,150,image=enemigo3)
player = Canvas.create_image(450,650,image=play)
sini=Canvas.create_image(150,650,image=enemigo4)
sini2=Canvas.create_image(150,650,image=enemigo5)

men.bind("<Button-1>",main)
Canvas.bind("<Key>", key)
boton1 =men.create_rectangle(100,150,150,200)
boton2 =men.create_rectangle(160,150,210,200)
boton3 =men.create_rectangle(220,150,270,200)
boton4 =men.create_rectangle(280,150,330,200)
boton5 =men.create_rectangle(340,150,390,200)
a = tkinter.StringVar()
label = tkinter.Label(wind,textvariable= a,font=("",16,"bold"))
wind.wm_state('iconic')
men.pack()
wind.mainloop()


    




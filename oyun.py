import turtle
import random
 
 
sayi = 0
genişlik = 600
yükseklık = 600
gecikme = 100
zehir = turtle.Turtle()
zehir.shape("square")
zehir.color("purple")
yem = 12
renkler = ["red", "blue", "yellow","orange","green", "pink","brown","gray"]
yilan = [(0, 0), (-10, 0), (-20, 0)]
sekileme = turtle.Screen()
sekileme.setup(width=genişlik, height=yükseklık)
sekileme.bgcolor("black")
sekileme.title("Yılan Oyunu")
sekileme.tracer(0)
 
yonler = {
    'yukarı': (0, 20),
    'asağı': (0, -20),
    'sağ': (20, 0),
    'sol': (-20, 0)
}
 
mevcut_yon = "sağ"
 
 
def yilan_oluştur():
    sekileme.onkey(lambda: yöndeğiştir('yukarı'), 'Up')
    sekileme.onkey(lambda: yöndeğiştir('asağı'), 'Down')
    sekileme.onkey(lambda: yöndeğiştir('sağ'), 'Right')
    sekileme.onkey(lambda: yöndeğiştir('sol'), 'Left')
 
def yöndeğiştir(yon):
    global mevcut_yon
    if yon == 'yukarı' and mevcut_yon != 'asağı':
        mevcut_yon = 'yukarı'
    elif yon == 'asağı' and mevcut_yon != 'yukarı':
        mevcut_yon = 'asağı'
    elif yon == 'sağ' and mevcut_yon != 'sol':
        mevcut_yon = 'sağ'
    elif yon == 'sol' and mevcut_yon != 'sağ':
        mevcut_yon = 'sol'
 
 
def hareket_yilan():
    global yilan, mevcut_yon
    bas.clearstamps()
 
    
    yeni_kafa = yilan[0].copy()
    yeni_kafa[0] += yonler[mevcut_yon][0]
    yeni_kafa[1] += yonler[mevcut_yon][1]
 
    if yeni_kafa in yilan or yeni_kafa[0] < -genişlik/2 or yeni_kafa[0] > genişlik/2 or yeni_kafa[1] < -yükseklık/2 or yeni_kafa[1] > yükseklık/2:
        sekileme.title(f"Oyun bitti! Skor: {len(yilan)-3}")
        return
    else:
        yilan.insert(0, yeni_kafa)
 
        if not yem_etkilesım():
            yilan.pop()
 
        for segment in yilan:
            bas.goto(segment[0], segment[1])
            bas.stamp()
 
    sekileme.title(f"skor: {len(yilan)-3}")
    sekileme.update()
 
    sekileme.ontimer(hareket_yilan, gecikme)
 
def yem_etkilesım():
     global  yem_pozisyonu,yilan,skor
 
     if abs(yilan[0][0] - yem_pozisyonu[0]) < 15 and abs(yilan[0][1] - yem_pozisyonu[1]) < 15:
         skor += 1
         yem_x = random.randint(-yükseklık//2 + 10, yükseklık//2 - 10)
         yem_y = random.randint(-yükseklık//2 + 10, yükseklık//2 - 10)
         yem_pozisyonu = (yem_x, yem_y)
         yem.goto(*yem_pozisyonu)
         return True
 
     elif uzaklık_hsapla(yilan[0], yem_pozisyonu) < 20:
         skor += 1
         yem_pozisyonu = rastgele_yem()
         yem.goto(*yem_pozisyonu)
         return True
     return False
 
def rastgele_yem():
    y = random.randint(-yükseklık//2 + 10,yükseklık//2-10)
    x = random.randint(-genişlik//2 + 10, genişlik//2-10)
    yem.color(random.choice(renkler))
    return (x, y)
 
def uzaklık_hsapla(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    uzaklık = ((x2 -x1) ** 2 + (y2 -y1) ** 2) ** 0.5
    return uzaklık
 
 
def reset_oyun():
    global skor,yilan,yilan_yon,yem_pozisyonu,zehir_pozisyonu
    skor = 0 
    yilan = [[0,0],[-20,0],[-40,0],[-60,0]]
    yilan_yon = 'sağ'
 
    yem_pozisyonu = rastgele_yem()
    yem.goto(*yem_pozisyonu)
 
    zehir_pozisyonu = rastgele_yem()
    zehir.goto(*zehir_pozisyonu)
 
    hareket_yilan()
 
bas = turtle.Turtle()
bas.shape("square")
bas.color("pink")
bas.penup()
bas.hideturtle()
bas.goto(0,0)
 
yem = turtle.Turtle()
yem.shape("circle")
yem.shapesize(0.5, 0.5)
yem.penup()
 
zehir = turtle.Turtle()
zehir.shape("circle")
zehir.color("red")
zehir.shapesize(0.5,0.5)
zehir.penup()
 
sekileme.listen()
yilan_oluştur()
 
reset_oyun()
sekileme.mainloop()
 
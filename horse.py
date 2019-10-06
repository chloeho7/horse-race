# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:42:38 2019

@author: 0715334
"""
###setuptheworld
coins = 500
import random
import turtle as t
#image = "blue.png"
horse1p = "horse1.gif"
horse2p ="horse2.gif"
horse3p = "horse3.gif"
horse4p = "horse4.gif"
horse5p ="horse5.gif"
coinpic = "coinf1.gif"
t.setup(960,640)
world = t.Screen()
world.bgcolor("lightgreen")
world.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))
#world.bgpic(image)
world.register_shape(horse1p)
world.addshape(horse1p)
world.register_shape(horse2p)
world.addshape(horse2p)
world.register_shape(horse3p)
world.addshape(horse3p)
world.register_shape(horse4p)
world.addshape(horse4p)
world.register_shape(horse5p)
world.addshape(horse5p)
world.register_shape(coinpic)
world.addshape(coinpic)
    ###makehorses
h1 = t.Turtle()
h1.up()
#h1.setpos(-300,100)
h1.color("blue")
h1.pensize(3)
h1.speed(10)
h1.shape(horse1p)

h2 = t.Turtle()
h2.up()
#h2.setpos(-300,50)
h2.color("red")
h2.pensize(3)
h2.speed(10)
h2.shape(horse2p)

h3 = t.Turtle()
h3.up()
#h3.setpos(-300,0)
h3.color("orange")
h3.pensize(3)
h3.speed(10)
h3.shape(horse3p)

h4 = t.Turtle()
h4.up()
#h4.setpos(-300,-50)
h4.color("yellow")
h4.pensize(3)
h4.speed(10)
h4.shape(horse4p)

h5 = t.Turtle()
h5.up()
#h5.setpos(-300,-100)
h5.color("green")
h5.pensize(3)
h5.speed(10)
h5.shape(horse5p)

boss = t.Turtle()
boss.hideturtle
boss.up()
boss.setpos(0,200)
boss.color("black")
boss.speed(0)

coinp = t.Turtle()
coinp.hideturtle
coinp.up()
coinp.setpos(-400,250)
coinp.color("yellow")
coinp.speed(0)
coinp.shape(coinpic)

##ACTUALGAME
def game():
    global coins
    coinp.clear()
    coinp.write(str(coins) + " coins" , font = ('Fixedsys' , 22, 'bold'))
    global h1
    global h2
    global h3
    global h4
    global h5
    #move them
    h1.setpos(-300,200)
    h2.setpos(-300,100)
    h3.setpos(-300,0)
    h4.setpos(-300,-100)
    h5.setpos(-300,-200)

    h1.clear()
    h2.clear()
    h3.clear()
    h4.clear()
    h5.clear()

    boss.clear()
    boss.write('click a horse to bet on it', font = ('Fixedsys' , 20, 'bold'))
    main()


    def main():
        t.onscreenclick(getPos)
        t.mainloop()

    def decide():
        global boss
        global coins
        #create speed and horselist
        horselist = []
        horse1 = random.randint(0,10)
        horselist.append(horse1)
        horse2 = random.randint(0,10)
        horselist.append(horse2)
        horse3 = random.randint(0,10)
        horselist.append(horse3)
        horse4 = random.randint(0,10)
        horselist.append(horse4)
        horse5 = random.randint(0,10)
        horselist.append(horse5)
        #find winner
        i=0
        winner = 0
        while i <= 4:
            if horselist[i] > winner:
                winner = horselist[i]
                i += 1
            else:
                i += 1
        if winner == horselist[0]:
            h1.speed(10)
            winninghorse = 0
        elif winner == horselist[1]:
            h2.speed(10)
            winninghorse = 1
        elif winner == horselist[2]:
            h3.speed(10)
            winninghorse = 2
        elif winner == horselist[3]:
            h4.speed(10)
            winninghorse = 3
        elif winner == horselist[4]:
            h5.speed(10)
            winninghorse = 4
            #horses move

        ##set speeds
        h1.speed(horse1)
        h2.speed(horse2)
        h3.speed(horse3)
        h4.speed(horse4)
        h5.speed(horse5)
        ##move all at the same time 

        boss.hideturtle()
        def moveall():
            h1.forward(horse1*5)
            h2.forward(horse2*5)
            h3.forward(horse3*5)
            h4.forward(horse4*5)
            h5.forward(horse5*5)
        m = 0
        while m <= 11:
            moveall()
            m = m + 1


        #state winner
        if winner == horselist[0]:
            saywin = 1
            winninghorse = 0
        elif winner == horselist[1]:
            saywin = 2
            winninghorse = 1
        elif winner == horselist[2]:
            saywin = 3
            winninghorse = 2
        elif winner == horselist[3]:
            saywin = 4
            winninghorse = 3
        elif winner == horselist[4]:
            saywin = 5
            winninghorse = 4
        if choice == winninghorse:
            coins += bet
            coinp.clear()
            coinp.write(str(coins) + " coins" , font = ('Fixedsys' , 22, 'bold'))
            boss.write("horse " +str(saywin)+ " wins! \nyou win \nyou have "+str(coins)+" coins left", font = ('Fixedsys' , 20, 'bold'))
            replay = world.textinput("play again?", "enter y for to play again \n enter n to quit")
            y = "y"
            while replay == y:
                game()
        else:
            coins -= bet
            coinp.clear()
            coinp.write(str(coins) + " coins" , font = ('Fixedsys' , 22, 'bold'))
            boss.write("horse "+str(saywin)+" wins! \nyou lose \nyou have "+str(coins)+" coins left", font = ('Fixedsys' , 20, 'bold'))
            if coins == 0:
                coinp.clear()
                coinp.write(str(coins) + " coins" , font = ('Fixedsys' , 22, 'bold'))
                boss.clear()
                boss.write("horse "+str(saywin)+" wins! \nyou lose \nyou have "+str(coins)+" coins left\ngame over", font = ('Fixedsys' , 20, 'bold'))
                pass
            else:
                replay = world.textinput("play again?", "enter y for to play again \nenter n to quit")
                print(replay)
                y = "y"
                while replay == y:
                    game()
                t.bye()


    def mbet():
        boss.clear()
        global bet
        bet = world.numinput("Place a bet", "You have "+ str(coins) + " coins \nEnter how many coins you want to bet:", default=None, minval=(round(coins/6)), maxval= coins)
        decide()

    def getPos(x, y): 
        global clickpos
        global choice
        choice = 7
        clickpos = x,y
        clickX = clickpos[0]
        clickY = clickpos[1] 
        while choice == 7:
            if clickX <= (-280) and clickX >= (-330):
                if clickY <= (220) and clickY >= (180):
                    h1.write ('My Choice', font = ('Fixedsys', 10, 'bold'))
                    choice = 0
                    print(choice)
                if clickY <= (120) and clickY >= (80):
                    h2.write ('My Choice', font = ('Fixedsys' , 10, 'bold'))
                    choice = 1
                    print(choice)
                if clickY <= (20) and clickY >= (-20):
                    h3.write ('My Choice', font = ('Fixedsys' , 10, 'bold'))
                    choice = 2
                    print(choice)
                if clickY <= (-80) and clickY >= (-120):
                    h4.write('My Choice', font = ('Fixedsys' , 10, 'bold'))
                    choice = 3
                    print(choice)
                if clickY <= (-180) and clickY >= (-220):
                    h5.write('My Choice', font = ('Fixedsys' , 10, 'bold'))
                    choice = 4
                    print(choice)
                while choice in [0, 1, 2, 3, 4]:
                    mbet()
                    break

game()
t.exitonclick()
t.bye()



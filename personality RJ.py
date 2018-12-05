import time as t
import webbrowser as wb
import pyautogui as pg
points = 0

show = pg.prompt ("What is your favorite show? " )

if show == "parks and rec":
    pg.alert("That is a really good show!")
    points += 2
    wb.open("https://www.youtube.com/watch?v=Tch4v0L0GHA")
elif show ==  "The Office":
    pg.alert ("Ilove Dwight!")
    points +=  5
elif show == "Game of Thrones":
    pg.alert("its very long")
    points -= 1
elif show == "The Walking Dead":
    pg.alert("The best show ever")
    points += 100
    wb.open("https://www.youtube.com/watch?v=q9FpeqNxX40")
elif show == "Breaking Bad":
    pg.alert("Best drama series ever")
elif show == "Bojack Horseman":
    pg.alert ("Best Netfix show")
else:
    pg.alert("Your favorite is " + show)
t.sleep(4)
food = pg.prompt("What is your favorite food? ")

if food =="pizza":
    pg.alert("I love pizza!!")
    points+= 4
    wb.open("https://img.grouponcdn.com/bynder/27xDMxLW88kb9imeJUfv14xV929J/27-2048x1229/v1/c700x420.jpg")
elif food == "ice cream":
    pg.alert("I hate getting a brain freeze")
elif food == "Tacos":
    pg.alert("I love tacos")
elif food == "Pasta":
    pg.alert("An easy food to have")
elif food == "Burgers":
    pg.alert("Love it when I am hungry")
elif food == "Gelato":
    pg.alert("It is very refreshing")
else:
    pg.alert("Your favorite food is" +  food)

name = pg.prompt ("What is your name")
if name == "Rhys":
    pg.alert("Hello Rhys")
    points += 25
elif name == "Dad":
    pg.alert("Hello Dad")
    points -= 20
elif name == "Gigi":
    pg.alert ("Hello Gigi")
elif name == "Barbara":
    pg.alert("Hello Barbara")
elif name == "Nero":
    pg.alert ("Hello Nero")
elif name == "Cookie":
    pg.alert ("Hello Cookie")
elif name == "Mom":
    pg.alert ("Hello Mom")
else:
    pg.alert ("You're name is" + name)
pg.alert(points)

movies = pg.prompt ("What is your favorite movies? " )

if movies == "Mulan":
    pg.alert("That is a really good movies!")
    points += 2
    wb.open("https://www.youtube.com/watch?v=ZSS5dEeMX64")
elif movies ==  "Deadpool":
    pg.alert ("Great Marvel film")
    points +=  5
elif movies == "Anchorman 2":
    pg.alert("funniest movie ever")
    points -= 1
elif movies == "Halloween":
    pg.alert("best scary movie")
    points += 100
    wb.open("https://www.youtube.com/watch?v=LvOu7iRUFY4")
elif movies == "Moana":
    pg.alert("Great sing along")
elif movies == "Blades of glory":
    pg.alert ("Very funny")
else:
    pg.alert("Your favorite is " + movies)

videogames = pg.prot ("What is your favorite video game? " )

if videogames == "Overwatch":
    pg.alert("That is a fun game")
    points += 2
    wb.open("https://www.youtube.com/watch?v=dushZybUYnM")
elif videogames ==  "Rainbow Six Siege":
    pg.alert ("Great tactical game")
    points +=  5
elif videogames == "Battlefield 4":
    pg.alert("best multiplayer gameplay")
    points -= 1
elif videogames == "Black ops 4":
    pg.alert("Fun game to grind at")
    points += 100
    wb.open("https://www.youtube.com/watch?v=6kqe2ICmTxc")
elif videogames == "GTA V":
    pg.alert("Cool free roam game")
elif videogames == "Halo":
    pg.alert ("classic game to play")
else:
    pg.alert("Your favorite is " + videogames)

pg.alert("Your score is: " + str(points))


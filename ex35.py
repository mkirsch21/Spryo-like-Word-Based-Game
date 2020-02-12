from sys import exit

print("""OH NOO!! Lyro, the evil witch has stole our eggs and is sitting atop Mount Dragon.
Please help save our kingdom, in order to do so you must collect all the eggs and face the witch at the top of the mountain.
Here are the instructions for the game, in every scenario there are four options, choose carefully as you only get 3 lives.
You can 'flame', 'charge', 'roll' or do nothing. Choose wisely based on your opponent.""")

spyroLives = 3

def lifeLost(why, spyroLives):
    print(why, "You lost a life.")

    if spyroLives > 0:
        print(f"You have {spyroLives} lives left, choose carefully.")
    else:
        print("You have no lives left. GAME OVER.")
        exit(0)

def grabEgg():
    print("An egg appeared! Grab it!")
    while True:
        choice = input("> ").lower()

        if choice == "grab":
            print("Good job!")
            return
        else:
            print("Grab it!")

def witchLifeLost(witch_lives):
    if witch_lives > 0:
        print(f"The witch has {witch_lives} lives left, keep going!")
    else:
        print("The witch has no lives left!")
        grabEgg()
        print("Congratulations!!! You have completed your quest for the eggs and defeated the evil witch!")
        exit(0)

def bossRealm(spyroLives):
    print("""You have made it to the Witch's Layer.
The witch is charging up an attack on you, what do you do?""")
    flame_defense = True
    charge_defense = True
    witch_lives = 3
    while witch_lives > 0:
        choice = input("> ").lower()
        
        if choice == "roll" and flame_defense == True:
            flame_defense = False
            print("You dodged her first attack, now what?")
        elif choice == "roll" and flame_defense == False and charge_defense == True:
            charge_defense = False
            print("You dodged her second attack, now what?")
        elif choice == "roll" and flame_defense == False and charge_defense == False:
            flame_defense = True
            charge_defense = True
            print("You can't roll forever...")
        elif choice == "flame" and flame_defense == True:
            spyroLives = spyroLives - 1
            lifeLost("The witch was unaffected by the flame and struck you with a lightning bolt.",spyroLives)
        elif choice == "flame" and witch_lives == 2:
            flame_defense = True
            charge_defense = True
            print("The witch saw your flame attack coming and dodged it!")
        elif choice == "flame" and flame_defense == False and witch_lives != 2:
            flame_defense = True
            charge_defense = True
            witch_lives = witch_lives - 1
            witchLifeLost(witch_lives)
        elif choice == "charge" and charge_defense == True:
            flame_defense = True
            charge_defense = True
            spyroLives = spyroLives - 1
            lifeLost("The witch dodged your charge and struck you with a lightning bolt.",spyroLives)
        elif choice == "charge" and charge_defense == False:
            flame_defense = True
            charge_defense = True
            witch_lives = witch_lives - 1
            witchLifeLost(witch_lives)
        else:
            flame_defense = True
            charge_defense = True
            spyroLives = spyroLives - 1
            lifeLost("The witch struck you with a lightning bolt.",spyroLives)
          
def ironRealm(spyroLives):
    print("""You have entered the Iron Realm,
all of the sudden, a monkey wearing iron armor is running at you!""")
    print("What do you do?")
    while True:
        choice = input("> ").lower()

        if choice == "charge":
            print("You cracked the monkey's armor with your horns! You defeated him!")
            grabEgg()
            #next realm
            print("A door with the witch's face appears...Continue? yes or no?")
            while True:
                choice = input("> ").lower()

                if choice == "yes":
                    bossRealm(spyroLives)
                elif choice == "no":
                    exit(0)
                else:
                    print("I do not understand? yes or no?")

        elif choice == "flame":
            spyroLives = spyroLives - 1
            lifeLost("The monkey is wearing armor your flames are ineffective, the monkey clubs you to death!", spyroLives)
        elif choice == "roll":
            print("You dodged the attack, the monkey is squaring up to charge you again. What do you do next?")
        else:
            spyroLives = spyroLives - 1
            lifeLost("The monkey charged at you and you stood there doing nothing.", spyroLives)

def lavaRealm(spyroLives):
    print("""You appear in a circle area surronded by lava. 
A large rhino is awaiting you when you enter the realm.""")
    print("What do you do?")
    while True:
        choice = input("> ").lower()

        if choice == "flame":
            print("The rhino turns black and falls over sideways. You defeated him!")
            grabEgg()
            #next realm
            print("Another door appears behind the rhino's crisp corpse. Continue? yes or no?")
            while True:
                choice = input("> ").lower()

                if choice == "yes":
                    ironRealm(spyroLives)
                elif choice == "no":
                    exit(0)
                else:
                    print("I do not understand? yes or no?")

        elif choice == "charge":
            spyroLives = spyroLives - 1
            lifeLost("The rhino is too big to charge, he spears you with his horn!", spyroLives)
        elif choice == "roll":
            spyroLives = spyroLives - 1
            lifeLost("You rolled into the molten lava.", spyroLives)
        else:
            spyroLives = spyroLives - 1
            lifeLost("The rhino charged at you and you stood there doing nothing.", spyroLives)

def salamanderRealm(spyroLives):
    print("A poison-tongued salamander is awaiting you when you enter the realm.")
    print("What do you do?")
    while True:
        choice = input("> ").lower()

        if choice == "flame" or choice == "charge":
            print("The salamander was defeated!")
            grabEgg()
            #go to next realm
            print("A door reveals itself behind the defeated salamander. Continue? yes or no?")
            while True:
                choice = input("> ").lower()

                if choice == "yes":
                    lavaRealm(spyroLives)
                elif choice == "no":
                    exit(0)
                else:
                    print("I do not understand? yes or no?")

        elif choice == "roll":
            print("You dodge the attack! What do you want to do next?")
        else:
            spyroLives = spyroLives - 1
            lifeLost("The salamander tongue punched your throatbox!",spyroLives)

def beginGame(spyroLives):
    print("Are you ready for your quest?")
    
    while True:
        choice = input("> ").lower()

        if choice == "yes":
            salamanderRealm(spyroLives)
        elif choice == "no":
            exit(0)
        else:
            print("I do not understand? yes or no?")

beginGame(spyroLives)


class ANSI():
	def background(code):
		return "\33[{code}m".format(code=45)

	def style_text(code):
		return "\33[{    if name!="":
        print ("\nThankyou for playing again, {}!".format(name))
    else:
        stop=True
        while stop:
            if name=="":
                name=input("What is your name? \n>>>   ").capitalize()
                if name !="":
                    print("Welcome, {}.".format(name))
                    print("\nIn this game you will be greeted by several different \npeople.You can choose to be nice or mean.\n At the end your fate will be decided by your actions!")
                    stop=False


    return name}m".format(code=5)

	def color_text(code):
		return "\33[{code}m".format(code=91)


example_ansi = ANSI.background(
	97) + ANSI.color_text(35) + ANSI.style_text(4)

def start(nice=0,mean=0,name=""):
    # get user's name
    name=describe_game(name)
    nice,mean,name,=nice_mean(nice,mean,name)
    


def describe_game(name):
    """
        Check it this is a new game or not.
        If its is new,get the user's name.
        If its not a new game, thank the player for
        playing again and continue with the game.
    """
    # meaning , if we do not already have this user's name,
    # then they are a new player and we need to get their name.
    if name!="":
        print ("\nThankyou for playing again, {}!".format(name))
    else:
        stop=True
        while stop:
            if name=="":
                name=input("What is your name? \n>>>   ").capitalize()
                if name !="":
                    print("Welcome, {}.".format(name))
                    print("\nIn this game you will be greeted by several different \npeople.You can choose to be nice or mean.\n At the end your fate will be decided by your actions!")
                    stop=False


    return name
    
        
    
    
def nice_mean(nice,mean,name):
    stop=True
    while stop:
        show_score(nice,mean,name)
        pick=input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean?  (N/M) \n>>>:   ").lower()
        if pick=="n":
            print("\nThe stranger walks away smiling...")
            nice=(nice + 1)
            stop=False
        if pick=="m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean=(mean + 1)
            stop=False
    score(nice,mean,name) # pass the 3 variables to the score()





def show_score(nice,mean,name):
    print("\n{}, your current total: \n{}, Nice) and ({}, Mean)".format(name,nice,mean))
    

def score(nice,mean,name):
    if nice>2:
        win(nice,mean,name)
    if mean>2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice job {},you win! \nEveryone loves you and you've \nmade lots of friends along the way".format(name))
    again(nice,mean,name)


def lose(nice,mean,name):
      print("Ahh too bad you lost game over you got beaten {}".format(name))
      again(nice,mean,name)


def again(nice,mean,name):
    stop=True
    while stop:
        choice=input("Do you want to play again? (y/n);\n>>> ").lower()
        if choice=='y':
            stop= False
            reset(nice,mean,name)
        if choice=="n":
            print("Sorry to see you go")
            stop=False
            quit()
        else:
            print("Enter Y for Yes, N for No:\n>>> ")

def reset(nice,mean,name):
    nice=0
    mean=0
    start(nice,mean,name)
  











if __name__ == "__main__":
    start()

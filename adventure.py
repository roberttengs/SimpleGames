#kommentar

def diamond_room():
    print("\nDu er i et rum fyldt med diamanter!")
    print("Men der er også en dør!")
    print("Hvad gør du? (1 eller 2)")
    print("1). Tager nogle diamanter og går igennem døren.")
    print("2). Går bare igennem døren.")


    answer = input("> ")

    if answer == "1":
        game_over("Der er en forbandelse over diamanterne, når du rører dem vælter bygningen sammen og du dør!")
    elif answer == "2":
        print("\nDet var godt at du var en ærlig mand, tillykke ! Du vandt spillet !")
        play_again()
    else:
        game_over("Ved du ikke hvordan man bruger tastaturet ?")


def bear_room():
    print("\nDer er en bjørn her.")
    print("Bag ved bjørnen er der en anden dør.")
    print("Bjørnen spiser noget lækkert honning!")
    print("Hvad vil du gøre? (1 eller 2)")
    print("1). Ta bjørnens honning.")
    print("2). Driller bjørnen.")

    answer = input("> ")

    if answer == "1":
        game_over("Bjørnen dræber dig!")
    elif answer == "2":
        print("\n Du er heldig og bjørnen flytter sig væk fra døren og du kan gå videre igennem døren nu!")
        diamond_room()
    else:
        game_over("Ved du ikke hvordan man bruger tastaturet ?")


def monster_room():
    print("\nDu er nu ankommet til et rum med et monster!")
    print("Monsteret sover.\nBagved monsteret er der en ny dør. Hvad gør du (1 eller 2)")
    print("1). Lister igennem rummet til den næste dør.")
    print("2). Du er modig og dræber monsteret!")

    answer = input("> ")

    if answer == "1":
        diamond_room()
    elif answer == "2":
        game_over("Monsteret var sulten, han spiste dig.")
    else:
        game_over("Ved du ikke hvordan man bruger tastaturet ?")


def play_again():
    print("\nVil du spille igen ? (j or n)")

    answer = input("> ").lower()

    if "j" in answer:
        start()
    else:
        exit()


def game_over(reason):
    print("\n" + reason)
    print("GAME OVER!")
    play_again()


def start():
    print("\nDu står i et mørk rum.")
    print("Der er en dør til venstre og en dør til højre, hvilken vælger du (v eller h)")
    answer = input("> ").lower()

    if "v" in answer:
        bear_room()
    elif "h" in answer:
        monster_room()
    else:
        game_over("Ved du ikke hvordan man bruger tastaturet ?")


start()




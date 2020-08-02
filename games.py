import time, random

def cvirus(): # The Discovery of the most sophisticated virus on the planet.
    print('You found this amazing program that is so said to be "The Best AntiVirus in the WORLD!!!!" ')
    time.sleep(3)
    print('You went to the website which was really convincing.')
    choice = input('Do you download it?\n1) Of course!\n2) I\'ll put it on a VM.\n')
    if choice == "1":
        print('You unwittingly downloaded one of the most sophisticated viruses on the planet. For the 3 days it works as an actual antivirus.\nThen it becomes a virus.')
        time.sleep(4)
        print('None of your other antiviruses work against it. It encrypts the entire drive. It then starts to delete everything on it. And finally. It deletes the contents of the BIOS chip.')
    elif choice == "2":
        print('You made the smart choice. The "antivirus" encrypts the drive, deletes the drive, and then deletes the BIOS of the VM.')
        time.sleep(3)
        choice = input('You think about telling someone. Do you?\n1) They should learn not to trust adverts the hard way.\n2) I\'ll just tell my friends and family.\n3) Make a post on all your social medias saying "DO NOT DOWNLOAD THIS!!!!" with a link to the virus.')
        if choice == 1: print('Your family and closest friends download the virus and have everything wiped.')
        elif choice == 2: print('Your family and friends didn\'t get it but everyone who follows you on twitter and facebook and youtube lose there valuable data.')
        elif choice == 3: print('You saved 34 million peoples data by posting it on social media. Some people though thought you didn\'t know what you were talking about and downloaded it anyway. I mean. Your only one of the smartest programming enthusiasts in the northern hemisphere.')
    else: print('Invalid option.')
    time.sleep(2)

def scp(id):
    if id == 33033:
        print('Your daughter found a turtle in your pond. She brings it to you and asks \'Why does this turtle have a button on it\'s back?\' Thankfully you have watched enough ASDFmovie to know that isn\'t a regular turtle. You say \'PUT THAT TH-- THTH-- THING BACK!\' Your daughter asks you why.')
        choice = input('1)You tell her the truth about mine turtles\n2)You say it\'s a government spy turtle.\n')
        if choice == 1: print('You have not only you and your daughter from death, but the entire human population. Whoever gets exploded by a mine turtle (scp-33033) turns into a mine turtle.')
        elif choice == 2: print('Your daughter plays with it behind your back and eventually presses the button. Exploding you and your daughter. Your now both mine turtles which infiltrate other houses.')


def games():
    game = int(input('1)The C Virus\n2)SCP 33033\n'))
    if game == 1: cvirus()
    elif game == 2: scp(33033)

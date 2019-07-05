##Defining player stats
atk = 100
modatk = atk
defense = 100
moddefense = defense
health = 100
modhealth = health
HP = 100
mana = 100
gold = 100
bombs = 0
runs = 5
## Tracking player items
sacredshrooms = 0
beggerhelped = 0
mystshrooms = 0
tornrags = 0
shittysword = 0
livingsword = 0
moonblade = 0
parmor = 'none'
pweapon = 'shittysword'
def damagedenemy():
    global matk
    global moddefense
    global mhp
    global HP
    global mdef
    damage = matk / 8 - moddefense / 16
    HP = HP - damage
    mdamage = modatk / 4 - mdef / 16
    mhp = mhp - mdamage
    print("[You've landed the hit!]")
    print("[You've damaged the monster for ",mdamage,"!")
    print("[They now have ",mhp," HP!")
def yesnoprompt():
    choice = input("Type [Yes] or [No] to continue: ")
    return choice
print('Wake up! Come on already!')
##Player decision on waking up
print("[Will you wake up?]")
choice = yesnoprompt()
if choice == 'yes':
    print("Thank god you're awake!")
    print("I thought I'd lost you for a second there")
else:
    print("ZzzZzzZzz")
    print("Come on! You can't sleep all day!")
    print("...")
    wakestatus2 = input("Type [Sleep] or [Wake] to continue: ")
    if wakestatus2.lower() == 'sleep':
        print("ZzzZzzZzz")
        print("Surely the hero can't be so lazy? I'm asking one last time...")
        print("WAKE THE HELL UP!")
        wakestatus3 = input("Shall you continue to [Sleep] or [Wake] up and rise to the challenge?!: ")
        if wakestatus3.lower() == 'wake':
            print("It's about time!")
        if wakestatus3.lower() == 'sleep':
            print("You're really going back to sleep?")
            print("I guess you're not the hero we thought you were...")
            print("Click OK to end your suffering.")
            exit()
print("I have three potions. One for attack, one for defence, and one for health")
print("You may take one of them.")
potionchoice = input("Type [ATK] or [DEF] or [HEALTH] to continue: ")
if potionchoice.lower() == 'atk':
    atk = 105
    modatk = atk
    print("[Your Attack is now",atk,"!]")
if potionchoice.lower() == 'def':
    defense = 105
    print("[Your Defense is now",defense,"!]")
if potionchoice.lower() == 'health':
    health = 105
    print("[Your Health is now",health,"!]")
## Player receives the Torn Rags
print("You can't stay here long. Take this.")
print("[Received 'Torn Rags!' They smell pretty funky though...]")
tornrags = 1
print("Would you like to equip this item now?")
equipprompt1 = yesnoprompt()
if equipprompt1.lower() == 'yes':
    parmor = 'tornrags'
    if parmor == 'tornrags':
        moddefense = defense + 10
        modhealth = health + 10
        print("You've equipped the [Torn Rags!]")
        print("[Your health is now",modhealth,"!]")
        print("[Your defense is now",moddefense,"!]")
if equipprompt1.lower() == 'no':
    parmor == 'none'
    print("[You put the item in your bag!]")
    tornrags = 1
if parmor == 'none':
    health = 100
    defense = 100
print("You should take this potion as well!")
## Player receives HP Potion
potions = 1
print("[You received one 'HP POTION!' Use it wisely]")
print("Now go! Head to Moonwell's Keep just north of here. You'll meet with the grand magician Trippy Hippy for further instructions!")
print('In a frantic hurry you crawl out of the cave into the blinding sunlight')
print("You find yourself amongst the brush of a thick forest. The moon reflects off the gunked up piles of mud last night's rain left. As you continue forward, you stumble upon a gnome struggling to carry a large mushroom.")
print("'Please help me sir' he cries out to you")
print("Do you stop to help?")
## Player choice to help the gnome 
encounter1 = yesnoprompt()
if encounter1.lower() == 'yes':
    print('As you bend over to help him, he pulls out a knife! This little homie aint playing around!')
    print("'Give me all your money, you little limp dicked chicken fucker!'")
    print("Do you give him the money? You only have 100 gold to your name")
    robbery = yesnoprompt()
    if robbery.lower() == 'yes':
        gold = 0
        print("He took all your money! But your health is more important, right?")
    else:
        if defense < 105:
            print("He tries to stab you! But you're able to dodge it!")
            print("Your superior defense has paid off!")
            print("Do you want to try your luck and attack him?")
            encounter3 = yesnoprompt()
            HP = HP - 50
            print("You kept your gold, but the gnome stabbed you for 50 HP")
            print("Do you want to try your luck and attack him?")
            encounter3 = yesnoprompt()
        else:
            print("He tries to stab you! But you're able to dodge it!")
            print("Your superior defense has paid off!")
            print("Do you want to try your luck and attack him?")
            encounter3 = yesnoprompt()
        if encounter3.lower() == 'yes':
            if modatk < 105:
                HP = 0
                print("Your attack isn't high enough!")
                print("Your attack misses, and he stabs you again. You've learned a valuable lesson about fucking around with gnomes today")
            else:
                print("Your superior strength has paid off!")
                print("You overpower him and smash his smug gnome face in!")
                print("You raid his pockets and find [50 Gold!]")
                gold = gold + 50
        else:
            print("You run away with all your might! You might look like a huge pussy, but at least you're safe, right?")
else:
    print ("You shoot the gnome a look of bored apathy. You feel for his struggle, but not enough to do anything about it")
if HP == 0:
    print("You're not too good at this are you?")
    print("Click OK to end your suffering.")
    exit()
print("You continue on your travels, your spirit unbroken")
print("Rain begins to drizzle, as the drowning sound of crickets surrounds you. You come upon a sign, covered with a thick layer of moss. You can faintly make out 'Moonlights Keep' beneath it.")
print("The sillouhette of high sprawling castles and crystal blue windows grow closer. A cold wind hits as you ascend the crumbling stone stairs leading into town.")
print("'AH! I have been waiting for your arrival' In front of you stands a raggedy, travelled looking man dressed head to toe in torn sapphire colored robes. His wizard's hat gave off a strange pearlescent glow that illuminated the dark flush of night.")
print("What is your name young adventurer?")
name = input("Type your [Name] to continue: ")
print("It's a pleasure to meet with you,",name,"!")
print("As I'm sure you've already gathered, I am the grand magician Trippy Hippy. You may think you were just in the wrong place at the wrong time when that earthquake struck. I assure you my child you were destined to end up here.")
print("I'm sure my appearance must have thrown you off, yes?")
encounter2 = yesnoprompt()
if encounter2.lower() == 'yes':
    print("That is to be expected. I was not always like this, you see.")
else:
        print("Oh, you're just being modest!")
print("I'm sure by now you've heard of the recent... changes in our beloved King Casper. Word has gotten around that he is posessed by a demon or perhaps bewitched. This is partially true, but my dear",name,", the truth is much more terrible.")
print("He has made a deal with a very dark and evil individual. It's been said that a mysterious trader made his way into town, going only by the ominous name of 'The Drifter'")
print("The mysterious man was clad head to toe in a spiraling black and white patterned suit, and a large striped hat.")
print("The strange man set up shop right at the base of the king's castle. The guard's would kick him out only to find as soon as they'd turned their backs, he'd set up shop again")
print("Eventually the guards grew tired of this routine, and reasoned that trying to get him to leave was more trouble than it was worth.")
print("Late into the evening one day, the man approached one of the guards. He insisted that he must speak with the king right away.")
print("The guard scoffed at his request. What exactly happened here is unclear, but nearby guards reported witnessing the man pull something out of the pocket of his tattered striped pants for just a second. The guard simply nodded and began leading him inside.")
print("In the weeks following, a dark aura seemed to follow the King. Rumours began to spread that he had been cursed by that mysterious salesman...")
print("This recent chaos is his doing! I've discovered a very rare and fascinating species of fungi, my dear,",name,". These mushrooms grew in the cave underneath the Tree of Healing. The sacred tree's medical properties were infused into these mushrooms.")
print("You must deliver this sacrement to the king! It's the only way we can rid of him of this curse! But I warn you, it will not be an easy task...")
print("Do you understand what I've told you ",name,"?")
##    Confirm the player understood Trippy Hippie
trippyencounter = yesnoprompt()
##   If they did understand
if trippyencounter.lower() == 'yes':
    print("[Received [Sacred Mushrooms]! They don't look so special...]")
    sacredshrooms = 1
    print("Excellent! Now I'm going to...")
    print("OH NO! Behind you, my boy!")
##  if they didn't understand
if trippyencounter.lower() == 'no':
    print("These mushrooms must be delivered to the king!")
    print("[Received [Sacred Mushrooms]! They don't look so special...]")
    sacredshrooms = 1
    print("They've been infused with the magical energy of the Tree of Healing.")
    print("It's the only way we can rid the king of the drifter's evil curse!")
    print("Now go quickly before...")
    print("OH NO! Behind you, my boy!")
print("[An ANGRY GHOST appears!]")
print("It seems there's no time left! Quick, take this sword! We must defeat this ghost!")
##   Player receives the SHitty Sword
print("[Received [Shitty Sword!] This thing's seen better days]")
print("[You equip it immediately!]")
print("[The ANGRY GHOST approaches]")
## Stats for ANGRY GHOST
def ANGRYGHOST():
    matk = 105
    mdef = 100
    mhp = 90
    return(matk,mdef,mhp)
matk, mdef, mhp = ANGRYGHOST()
## Stats for FRIED ALIEN
def FRIEDALIEN():
    matk = 110
    mdef = 105
    mhp = 85
    return(matk,mdef,mhp)
## Stats for Misty Demon
def MISTYDEMON():
    matk = 150
    mdef = 110
    mhp = 150
    return(matk,mdef,mhp)
## Stats for Rasta Mushroom
def RASTAMUSHROOM():
    matk = 160

    mhp = 160
    return(matk,mdef,mhp)
##  Battle function
def battle():
    global mhp
    global HP
    global modatk
    global bombs
    global potions
##  Initiate battle
    while mhp > 0:
        global battlechoice
##      Get players battle choice
        battlechoice = input("Type [Attack] [Defend] [Item] or [Run] to continue: ")
##      Player [Attacks]
        if battlechoice.lower() == 'attack':
##          When player's attack is lower than monster's defense
            if mdef >= modatk:
                if mhp > 0:
                    print("[This monster's defense is too high!]")
                    print("[Your attacks will be less effective]")
                    damage = matk / 8 - moddefense / 16
                    HP = HP - damage
                    print ("[The monster attacks for",damage,"damage!]")
                    print ("[Your HP is ",HP,"/",modhealth,"!]")
                    damagedenemy()
                if mhp < 0:
                    print("[You've successfully defeated the monster!]")
                    if HP < 0:
                        print("You're not too good at this are you?")
                        print("Click Okay to end your suffering.")
                        exit()
            else:
                damagedenemy()
                if mhp > 0:
                    damage = matk / 8 - moddefense / 16
                    print("[The monster attacks for",damage,"damage!]")
                    print("[Your HP is ",HP,"/",modhealth,"!]")
                    if HP <= 0:
                                print("You're not too good at this are you?")
                                print("Click OK to end your suffering.")
                                exit()
                else:
                    print("[You've successfully defeated the monster!]")
                    if battlechoice.lower() == 'defend':
                        if moddefense>= matk:
                         print("[You've successfully defended yourself!]")
                        else:
                            print("[It's no use! Your defense is too low!]")
                            damage = matk / 8 - mdef / 16
                            HP = HP - damage
                            print ("[The monster attacks for",damage,"damage!]")
                            print ("[Your HP is ",HP,"/",modhealth,"!]")
                            if HP <= 0:
                                print("You're not too good at this are you?")
                                print("Click OK to end your suffering.")
                                exit()
##            If player uses [Item]
        if battlechoice.lower() == 'item':
                itemchoice = input("Type [Potion] or [Bomb] to continue")
                if itemchoice.lower() == 'potion':
                    if potions >= 1:
                        HP = modhealth
                        potions = potions - 1
                        print("[You've healed your HP fully!]")
                        print("[Your HP is now ",modhealth,"!]")
                    if potions == 0:
                        print("You don't have any more potions to use!")
                if itemchoice.lower() == 'bomb':
                    if bombs > 0:
                        bombs = bombs - 1
                        mhp = mhp / 4
                        print("[You took 75% of the monster's health!]")
                        print("[The enemy now has",mhp,"health!")
                    if bombs == 0:
                        print("You don't have any bombs to use!")
        if battlechoice.lower() == 'run':
                if runs >= 1:
                    print("[Are you sure you want to do this? You can only run from your problems so many times...]")
                    runchoice = input("Type [Run] or [Cancel] to continue: ")
                    if runchoice.lower() == 'run':
                        runs - 1
                        mhp = 0
                        print("[You've successfully run from the monster!]")
                        print("That was close!")
                if runs == 0:
                    print("You've done this too many times!")
## Set monster stats to ANGRY GHOST and run battle function
ANGRYGHOST()
battle()
print("You've got to get out of here,",name,", before it's too late. I suggest stopping by the trading post just north of town for supplies.")
print("[You've obtained Sacred Mushrooms! Far out, man!]")
## Give player sacred mushrooms
sacredmushrooms = 1
print("You run with all your might, heading for the hills to the north.")
print("You see the trading post to the right, and off to the left an Angry Ghost. There could be treasure though...")
## Player chooses to go to the trading post or fight the ANGRY GHOST
directionin = input("Type [Right] to go the trading post, or [Left] to fight the ANGRY GHOST: ")
lefttaken = 0
if directionin.lower() == 'left':
    leftencounter = 'yes'
else:
    leftencounter = 'no'
if leftencounter == 'yes':
    lefttaken = 1
    ANGRYGHOST()
    matk, mdef, mhp = ANGRYGHOST()
    print("[You've encountered an Angry Ghost!]")
    battle()
    potions = potions + 3
    print("You've gained three potions! Sometimes its the greatest risks that have the best rewards.")
def dreamscene():
          print("'You there!' a voice calls out to you")
          print("You find yourself in a grim cavern, dimly lit by a candle")
          print("'Surely you remember me",name,"'")
          recognize = yesnoprompt()
          if recognize.lower() == 'yes':
              print("'Very good my boy!'")
          else:
              print("'Surely you have not forgotten me...'")
          print("You begin to recognize his voice.")
          print("It's Trippy Hippie!")
          print("'I have put a great amount of faith in you '")
          print("'You would never betray me, right my boy?'")
          chosen = 0
          while chosen == 0:
              dreamchoice = input("Type [Never] or [Distrust] to continue: ")
              if dreamchoice.lower() == 'never':
                  print("'Of course my boy... I just had to be sure.'")
                  chosen = 1
              if dreamchoice.lower() == 'distrust':
                  print("'You need to do what I have asked of you.'")
                  print("'It is the only way the prohecy will be fufilled...'")
                  chosen = 1
              else:
                    print("What was that?")
          print("'I hope you trust me as much as I have trusted you...")
          print("He stands above a rickety market stall")
          print("He's wearing the same clothes the Drifter wore!")
          print("As your eyes adjust the light, you're able to make out their face.")    
def shopfunc():
    global gold
    global potions
    global bombs
    global shopchoice
    if shopchoice.lower() == 'shop':
        print("He has health potions that cost 30 gold, and bombs that cost 50 gold")
        print("Would you like to purchase something?")
        shopchoice = 'loop'
        while shopchoice == 'loop':
            print("You have",gold,"gold.")
            shopchoice = input("Type [Potion] or [Bomb] or [Leave] to continue: ")
            while shopchoice.lower() == 'potion':
                if gold < 30:
                    print("You haven't got enough gold!")
                    print("'Come back when you get some money!'")
                    shopchoice = 'loop'
                if gold >=30:
                    gold = gold - 30
                    potions = potions + 1
                    print("[You've received a [Potion!]")
                    potionchoice2 = input("Would you like to purchase another one?")
                    if potionchoice2.lower() == 'no':
                        print ("Very well then!")
                        shopchoice = 'loop'
                    while potionchoice2.lower() == 'yes':
                        if gold >=30:
                            gold = gold - 30
                            potions = potions + 1
                            print("[You've received a [Potion!]")
                            potionchoice2 = input("Would you like to purchase another one?")
                        else:
                            print("You haven't got enough gold!")
                            print("'Come back when you get some money!'")
                            potionchoice2 = 'done'
                            shopchoice = 'loop'
            while shopchoice.lower() == 'bomb':
                if gold >=50:
                    gold = gold - 50
                    bombs = bombs + 1
                    print("[You've received a [Bomb!]")
                    bombchoice2 = input("Would you like to purchase another one?")
                    if bombchoice2.lower() == 'no':
                        print ("Very well then!")
                        shopchoice = 'loop'
                    while bombchoice2.lower() == 'yes':
                            if gold >=50:
                                gold = gold - 50
                                bombs = bombs + 1
                                print("[You've received a [Potion!]")
                                bombchoice2 = input("Would you like to purchase another one?")
                else:
                    print("You haven't got enough gold!")
                    print("'Come back when you get some money!'")
                    shopchoice = 'loop'
                    bombchoice2 = 'done'
        if shopchoice.lower() == 'leave':
            print("Very well! I hope the darkness fares well for you my friend.")
            shopchoice = 'done'
def rightencounter():
    print("A rickety merchant stall stands in front of you, tended by a man with a blank, expressionless mask. The two black dots that served as eyes had a hauntingly empty glare to them.")
    print("'Welcome to my shop! Hahaha! Welcome welcome welcome!'")
    print("Despite your best judgement, you approach the man closer.")
    print("'Come on, buy something! Whatever your heart desires is for sale right here at this stall.'")
    shopfunc()
if directionin.lower() == 'right':
    shopchoice = input("Type [Shop] or [Leave] to continue: ")
    rightencounter()
if lefttaken == 0:
    print("Would you like to go fight that Angry Ghost you saw earlier?: ")
    alternate2 = input("Type [Yes]  or [No] to continue: ")
    if alternate2.lower() == 'yes':
        lefttaken = 1
        ANGRYGHOST()
        matk, mdef, mhp = ANGRYGHOST()
        print("[You've encountered an Angry Ghost!]")
        battle()
        potions = potions + 3
        print("You've gained three potions! Sometimes its the greatest risks that have the best rewards.")
if lefttaken == 1:
    print("Would you like to go visit that trading post now?")
    alternate1 = yesnoprompt()
    if alternate1.lower() == 'yes':
        shopchoice = input("Type [Shop] or [Leave] to continue: ")
        rightencounter()
    else:
        print("Very well then!")
print("As you continue on your journey to the king, you can not help but shake the feeling that you are being watched.")
print("The sound of crunching leaves behind you seems to grow closer")
print("'Wait!' a voice cries off in the distance 'Please stop for just a second I need to talk to you")
shadystranger = 'talk'
def shadystranger():
    global modatk
    global shadystranger
    global mystshrooms
##  If player chooses to ignore the stranger
    while shadystranger == 'talk':
        if shadystranger != 'ignore':
            shadystranger = input("Type [Talk] or [Ignore] to continue: ")
            if shadystranger == 'ignore':
                print("You're distrustful of strangers, and decide to keep pushing.")
                print("Hopefully that was the right choice.")
                shadystranger = 'ignore'
##  If player chooses to talk to the stranger
    if shadystranger == 'talk':
        print("'You are on your way to see the king, right?' The shady stranger is dressed in a dapper purple suit, and his eyes were barely visible between his wide brimmed hat and flowing scarf.")
        print("I know what you're going to do. You're Trippy Hippie's newest pawn.")
        print("The same evil that has possessed our king has taken over the grand magician himself!")
        print("He's trying to set you up. The mushrooms he gave you will not heal the king at all... they'll kill him!")
        print("The Tree of Healing's power waned off many years ago. The truth is the Drifter's dark energy has taken over the caves beaneath it as well.")
        print("I have with me a mushroom that a very strong and powerful alchemist synthesized for me. He believes these mushrooms have the ability to ward of all evil.")
        print("If you care about the fate of your kingdom, you'll bring these to the king!")
        print("There's no way he'll trust you. You must tell him they're the same mushrooms Trippy Hippie gave you.")
        print("[Do you take the mushrooms from the stranger?]")
        getgooms = yesnoprompt()
        if getgooms.lower() == yes:
            print("'Splendid!'")
            print("You've received the [Mysterious Mushrooms.] Are these the real deal?")
            print("'Take this as well! There are many dark forces out there, and you are not strong enough to face them alone.")
            print("You've received [Living Sword!] Did it just wink at me?")
            print("Would you like to equip this item now?")
            livingsword = 1
            lvswordequip = input("Type [Equip] or [Skip] to continue: ")
            if lvswordequip.lower() == 'equip':
                print("You've equipped the [Living Sword!]")
                pweapon = 'living sword'
                if pweapon == 'living sword':
                    modatk = atk + 15
                    print("[Your attack is now",modatk ,"!]")
                    livingsword = 1
            mystshrooms = 1
        if getgooms.lower() == 'no':
            print("You're making a terrible mistake I assure you...")
            print("You really should take these. The fate of our kingdom depends on it.")
            persuasion = input("Type [Take] or [Deny] to continue: ")
            if persuasion.lower() == 'take':
                mystshrooms = 1
                livingsword = 1
                print("You've received the [Mysterious Mushrooms.] Are these the real deal?")
                print("'Now be sure these get to the king' the stranger sternly reminds you.")
                print("'Take this as well! There are many dark forces out there, and you are not strong enough to face them alone.")
                print("You've received [Living Sword!] Did it just wink at me?")
                print("Would you like to equip this item now?")
                lvswordequip = input("Type [Equip] or [Skip] to continue: ")
                if lvswordequip.lower() == 'equip':
                    print("You've equipped the [Living Sword!]")
                    pweapon = 'living sword'
                    if pweapon == 'living sword':
                        modatk = atk + 15
                        print("[Your attack is now",modatk ,"!]")
                        livingsword = 1
            if persuasion.lower() == 'deny':
                print("I guess some things can't be helped...")
                print("You'll regret this though.")
            else:
                print("Please type [Take] or [Deny] to continue: ")
    else:
        shadystranger = input("Type [Talk] or [Ignore] to continue: ")
    if shadystranger.lower() == 'ignore':
        print("You're distrustful of strangers, and decide to keep pushing.")
        print("Hopefully that was the right choice.")
##  If player chooses to talk to the stranger
    if shadystranger.lower() == 'talk':
        print("'You are on your way to see the king, right?' The shady stranger is dressed in a dapper purple suit, and his eyes were barely visible between his wide brimmed hat and flowing scarf.")
        print("I know what you're going to do. You're Trippy Hippie's newest pawn.")
        print("The same evil that has possessed our king has taken over the grand magician himself!")
        print("He's trying to set you up. The mushrooms he gave you will not heal the king at all... they'll kill him!")
        print("The Tree of Healing's power waned off many years ago. The truth is the Drifter's dark energy has taken over the caves beaneath it as well.")
        print("I have with me a mushroom that a very strong and powerful alchemist synthesized for me. He believes these mushrooms have the ability to ward of all evil.")
        print("If you care about the fate of your kingdom, you'll bring these to the king!")
        print("There's no way he'll trust you. You must tell him they're the same mushrooms Trippy Hippie gave you.")
        getgooms = input("[Do you take the mushrooms from the stranger?]")
        if getgooms.lower() == 'yes':
            print("You've received the [Mysterious Mushrooms.] Are these the real deal?")
            print("'It is very dangerous out there! Take this as well!")
            print("You've received [Living Sword!] Did it just wink at me?")
            print("Would you like to equip this item now?")
            lvswordequip = input("Type [Equip] or [Skip] to continue: ")
            if lvswordequip.lower() == 'equip':
                print("You've equipped the [Living Sword!]")
                pweapon = 'living sword'
                if pweapon == 'living sword':
                    modatk = atk + 15
                    print("[Your attack is now",modatk ,"!]")
                    livingsword = 1
##        Give player the Mysterious Mushrooms
                mystshrooms = 1
        if getgooms.lower() == 'no':
            print("You're making a terrible mistake I assure you...")
            print("You really should take these. The fate of our kingdom depends on it.")
            persuasion = input("Type [Take] or [Deny] to continue")
            if persuasion.lower() == 'take':
                mystshrooms=1
                print("You've received the [Mysterious Mushrooms.] Are these the real deal?")
                print("'Now be sure these get to the king' the stranger sternly reminds you.")
                print("'It is very dangerous out there! Take this as well!")
                ## Player receives the Living Sword
                print("You've received [Living Sword!] Did it just wink at me?")
                livingsword = 1
                print("Would you like to equip this item now?")
                lvswordequip = input("Type [Equip] or [Skip] to continue: ")
                if lvswordequip.lower() == 'equip':
                    print("You've equipped the [Living Sword!]")
                    pweapon = 'living sword'
                    if pweapon == 'living sword':
                        modatk = atk + 15
                        print("[Your attack is now",modatk ,"!]")
            if persuasion.lower() == 'deny':
                print("'I guess some things can't be helped...'")
                print("'You will regret this though.'")
shadystranger()
print("You return to the trail and get back to your travels. Things seem futile as an overwhelming melancholy aura pervades")
print("You come upon an Inn. You can stop to heal, but it will cost 10 gold.")
innchoice = input("Type [Inn] or [Pass] to continue: ")
if innchoice.lower() == 'inn':
    print("Welcome to our inn! We're the best inn around, because it's the only one!")
    if gold >=10:
        gold = gold - 10
        HP = health
        print("You settle in for the night.")
        print("You and your HP wake up feeling refreshed.")
    else:
        print ("This isn't a free loader's longue, you dirty dope head!")
        print ("Get out of here before I call the guards!")
if innchoice.lower() == 'pass':
    print("You decide the Inn wasn't worth your time. You're too good for that rundown crab shack")
print("You come upon a treasure chest. Maybe you should open it?")
trchoice = input("Type [Open] or [Ignore] to continue: ")
if trchoice.lower() == 'open':
    print("You reach to open the treasure chest")
    print("[A Fried Alien appears! This guy looks stoned off his ass...]")
    matk, mdef, mhp = FRIEDALIEN()
    battle()
    gold = gold + 50
    print("[You open the treasure chest!]")
    print("[You've received [50 gold!] Don't spend it all in one place]")
print("Would you like to stop and use a potion?")
potionuse = input("Type [Potion] or [Skip] to continue: ")
if potionuse.lower() == 'potion':
    HP = health
    print("You're healed your HP fully!")
    print("Your health is now ",health,"!")
if potionuse.lower() == 'skip':
    print("You're willing to risk your health for the sake of conservation")
print("The sun begins to dawn as you pass a small riverbed. A group of travellers are gathered by a fire next to it.")
print("They're all humming an enchanting tune. Broken pieces of wood tied to together to form strange ornaments are scattered next to them.")
print("Would you like to stop and talk to them?")
## Get player choice to approach the group on the beach
travencounter = input("Type [Talk] or [Skip] to continue: ")
if travencounter.lower() == 'talk':
    print("You nervously approach the group, as their humming grows higher pitch.")
    print("'You came at just the right time!' one yells out to you")
    print("We've gathered here to summon a very powerful demon.")
    print("We believe this demon has the power to overturn the darkness and restore our kingdom.")
    print("It's like fighting fire with fire.")
    print("Would you like to join us?")
    demonenc = input("Type [Join] or [Leave] to continue: ")
    if demonenc.lower() == 'join':
        print("Very well! Come join in our circle. We believe the demon is nearly here.")
        print("[You sit amongst their congregation]")
        print("You feel compelled to join in their humming as the tone grows higher and higher.")
        print("[The fire goes out!]")
        print("[From it's ashes rise a shadowy mist that forms a humanoid figure!]")
        print("[His red eyes glow from beneath the mist]")
        print("A [Misty Demon] appears! You're in too deep now...]")
        print("'You fools!' he laughs maniacally. 'The same energy that corrupts this land posseses me now!'")
        print("'I would never help you! Now give your energy to me!'")
        matk, mdef, mhp = MISTYDEMON()
        battle()
        ##player receives the Mist Armor
        print("You've received 50 gold! Don't spend it all in one place")
        gold = gold + 50
        print("You've received the [Mist Armor!] Pretty convenient it fits, huh?")
        mistarmor = 1
        print("Would you like to equip this item now?")
        mistequip = yesnoprompt()
        if mistequip.lower() == 'yes':
            print("You've equipped the [Mist Armor!]")
            parmor = 'mist armor'
            if parmor == 'mist armor':
                moddefense = defense + 15
                modhealth = health + 15
                print("[Your defense is now",moddefense,"!]")
    if demonenc.lower() == 'leave':
        print("You decide not to dabble with the dark arts and take off running.")
print("And just like that you're back on the trail again!")
print("You come upon a beggar, who looks sickly and grey. He weakly reaches his hand out to you")
print("'Please sir if you could spare a few gold!'")
print("He looks hungry... would you like to give him 5 gold?")
beggerprompt = input("Type [Give] or [Ignore] to continue: ")
if beggerprompt.lower() == 'give':
    gold = gold - 5
    beggerhelped = 1
    print("'Thank you so much, kind sir! I will reward your good faith one day!")
if beggerprompt.lower() == 'ignore':
    print("'Okay sir I understand... times are tough for us all'")
    print("You are truly a cold hearted meiser.")
print("You feel you must be getting close to the king by now.")
print("With each step, the weight on your shoulders feels increasingly heavy")
print("You continue down a spiraling path leading through the woods.")
print("You hear crows cawing in the distance")
print("You stumble upon a travelling merchant wearing knight's armor. How bizzare...")
print("'You there!' he calls out 'No customers have come out here for many moons'")
print("'I have many items for sale!'")
shopchoice = input("Type [Shop] or [Leave] to continue: ")
if shopchoice.lower() == 'shop':
    shopfunc()
if shopchoice.lower() == 'leave':
    print("'Very well then...'")
print("'Those mushrooms in your pocket... I will buy them for a great price.")
print("He points to the Sacred Mushrooms.")
print("'I will buy them for 300 gold and my whole stock of potions.")
print("'Won't you make a deal with me?'")
def sacredshroomsale():
    global gold
    global potions
    global sacredshrooms
    progress = 0
    while progress == 0:
        choice = yesnoprompt()
        if choice.lower() == 'yes':
            print("'You are very wise to make this choice!'")
            print("'I'll be taking those now.")
            print("[You hand over the [Sacred Mushrooms!]")
            sacredshrooms = 0
            gold = gold + 300
            potions = potions + 3
            print("[You received [300 Gold] and [3 Potions!]")
            progress = 1
        if choice.lower() == 'no':
            print("'Very well then... But you would be wise to reconsider'")
            print("'I guess it's your loss'")
            progress = 1
sacredshroomsale()
print("'Before you go, I have one more  item for sale...'")
print("It's an incredibly rare sword called the Moon Blade.")
print("'For just 100 gold, this incredible weapon can be yours!'")
print("'So how about it?'")
moonbladechoice = input("Type [Buy] or [Leave] to continue: ")
if moonbladechoice.lower() == 'buy':
    if gold >= 100:
        gold = gold - 100
        moonblade = 1
        print("You've received the [Moon Blade!] That glow is mesmerizing.")
        print("Would you like to equip this item now?")
        moonequip = input("Type [Equip] or [Skip] to continue: ")
        if moonequip.lower() == 'equip':
            print("You've equipped the [Moon Blade!]")
            pweapon = 'moonblade'
            if pweapon =='moonblade':
                modatk = atk + 20
                print("Your attack is now",modatk,"!")
        if moonequip.lower() == 'skip':
            print("You've put the item in your bag!")
    else:
        print("You can't afford this sword!")
print("'Be safe on your travels!'")
print("You see a Rasta Mushroom holding a conspicious sack of gold coins")
print("Would you like to fight him and take his gold?")
rastafight = input("Type [Fight] or [Skip] to continue: ")
if rastafight.lower() == 'fight':
    print("A [Rasta Mushroom] appears!")
    matk, mdef, mhp = RASTAMUSHROOM()
    battle()
    print("You've gained [75 gold]")
    gold = gold + 75
if rastafight.lower() == 'skip':
    print("You decide to shy away from confrontation. Money isn't everything.")
print("You grow increasingly weary")
print("You can't continue on much longer")
print("You see a nearby inn. It will cost 25 gold to stay, but you'll be safe for the night")
print("Otherwise, you can brave it in the nearby woods for the night.")
dreamcount = 0
while dreamcount == 0:
    wearychoice = input("Type [Inn] or [Woods] to continue: ")
    if wearychoice.lower() == 'inn':
        if gold >= 25:
            print("You enter the inn looking downtrotten.")
            print("As your legs feel like they'll give out, you collapse into bed.")
            print("ZzzZzzZzz")
            print("ZzzZzzZzzZzz")
            dreamscene()
            HP = health
            print("You wake up! It was just a dream!")
            print("You feel well rested.")
            print("Your HP is now full!")
            dreamcount = 1
        if gold < 25:
            print("You can't afford this inn")
            print("You need at least 25 gold!")
    if wearychoice.lower() == 'woods':
              print("You decide to set up camp and sleep under the stars for the night")
              print("Your whole body aches with exhausion as you finally lay down to rest.")
              print("ZzzZzzZzz")
              print("ZzzZzzZzzZzz")
              dreamscene()
              HP = health - health / 4
              print("You wake up! It was just a dream!")
              print("You don't feel well rested.")
              print("Your HP is now 75% full!")
              dreamcount = 1
def dreamscene():
    global sacredshrooms
    print("Your vision is blurry, and the night sky blankets you in darkness")
    print("A voice cuts through the shadows.")
    print("'My dear boy!' You recognize the old wizard's crackling voice.")
    print("'You remember me, right my boy?'")
    choice = yesnoprompt()
    if choice.lower() == 'yes':
        print("'I knew you wouldn't forget!'")
        print("The voice sounds familiar. It's Trippy Hippie.")
        print("'You still have the sacrametal mushrooms, correct?'")
    else:
        print("'Surely you haven't forgotten so soon...'")
        print("'It's me, Trippy Hippie!'")
        print("'You've held on to the mushrooms I gave you, right my boy?")
        if sacredshrooms == 0:
            print("'You sold them? Now the prophecy will never be fufilled...'")
            print("'I should have known better than to trust you.'")
            print("Your eyes begin to adjust. You notice he is standing in front of the very same market stall the drifter used!")
        if sacredshrooms == 1:
            print("'Very good. It is of the utmost importance you get those to the king.")
            print("'I was right to trust you... It will all be as it should now'")
            print("Your eyes begin to adjust. You notice he is standing in front of the very same market stall the drifter used!")


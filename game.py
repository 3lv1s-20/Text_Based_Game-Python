#=========================================================================
#This is "Certified Lover Boy"
#PROGRAM AUTHOR: Elvis Budrevicius
#=========================================================================

#game and title screen imports

import time #Imports a module to add a pause
import sys #Imports a module to access system specific parameters and functions
import keyboard #Imports keyboard module...may not work on machines without keyboard module installed...?
import colorama #imports package to make colored text
from colorama import Fore, Back, Style 
colorama.init()

#title screen imports

import cmd
import textwrap
import os
import random
    
#Figuring out how users could give their answers
answer_one = ["1", "one"]
answer_two = ["2", "two"]
answer_three = ["3", "three"]
answer_four = ["4", "four"]

required_four = ("\nUse only 1, 2, 3 or 4\n") #If the user types in an unavailable option one of these texts will pop up depending on the amount of options available
required_three = ("\nUse only 1, 2 or 3\n")
required_two = ("\nUse only 1 or 2\n")
required_one = ("\nUse only 1\n")
required_menu = ("\nUse obly Play, Help or Quit\n")

#make text appear letter by letter and give the option to use space to speed up the rate at which the letters show up + set color

#print for text
def print_ci(s): 
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)

#print for text art

#Default
def print_Ta(s): 
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.001)

#Blue             
def print_ci_TaBlue(s, color=''): 
    print(Fore.BLUE) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.001)
    print('\033[A\033[39m') # reset the terminal color

#Red
def print_ci_TaRed(s, color=''): 
    print(Fore.RED) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.001)
    print('\033[A\033[39m') # reset the terminal color

#Yellow
def print_ci_TaYellow(s, color=''): 
    print(Fore.YELLOW) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.001)
    print('\033[A\033[39m') # reset the terminal color

#Green
def print_ci_TaGreen(s, color=''): 
    print(Fore.GREEN) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.001)
    print('\033[A\033[39m') # reset the terminal color

#Cyan
def print_ci_TaCyan(s, color=''): 
    print(Fore.CYAN) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.001)
    print('\033[A\033[39m') # reset the terminal color

#Magenta
def print_ci_TaMagenta(s, color=''): 
    print(Fore.MAGENTA) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.001)
    print('\033[A\033[39m') # reset the terminal color

    

#text art slow

    
#Default
def print_TaS(s): 
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)

#Blue             
def print_ci_TaSBlue(s, color=''): 
    print(Fore.BLUE) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)
    print('\033[A\033[39m') # reset the terminal color

#Red
def print_ci_TaSRed(s, color=''): 
    print(Fore.RED) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)
    print('\033[A\033[39m') # reset the terminal color

#Yellow
def print_ci_TaSYellow(s, color=''): 
    print(Fore.YELLOW) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)
    print('\033[A\033[39m') # reset the terminal color

#Green
def print_ci_TaSGreen(s, color=''): 
    print(Fore.GREEN) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)
    print('\033[A\033[39m') # reset the terminal color

#Cyan
def print_ci_TaSCyan(s, color=''): 
    print(Fore.CYAN) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)
    print('\033[A\033[39m') # reset the terminal color

#Magenta
def print_ci_TaSMagenta(s, color=''): 
    print(Fore.MAGENTA) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)
    print('\033[A\033[39m') # reset the terminal color




#makes text appear color by color, will use a different color for every character's speech

#Kaser's color (blue)
def print_ci_K(s, color=''):    
    print(Fore.BLUE) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)
    print('\033[A\033[39m') # reset the terminal color

#Rosorus's color (red)
def print_ci_Ro(s, color=''):    
    print(Fore.RED) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)
    print('\033[A\033[39m') # reset the terminal color

#Rebekah's color (magenta)
def print_ci_R(s, color=''):    
    print(Fore.MAGENTA) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)
    print('\033[A\033[39m') # reset the terminal color

#Xavier's color (green)
def print_ci_X(s, color=''):    
    print(Fore.GREEN) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)
    print('\033[A\033[39m') # reset the terminal color

#Xavier slow
def print_ci_Xs(s, color=''):    
    print(Fore.GREEN) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.055)
    print('\033[A\033[39m') # reset the terminal color

#Zane's color (Cyan)
def print_ci_Z(s, color=''):    
    print(Fore.CYAN) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)
    print('\033[A\033[39m') # reset the terminal color

#principal's color (Yellow)
def print_ci_P(s, color=''):    
    print(Fore.YELLOW) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)
    print('\033[A\033[39m') # reset the terminal color


#other colors

#red slow
def print_ci_red_slow(s, color=''):    
    print(Fore.RED) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.035)
    print('\033[A\033[39m') # reset the terminal color

#red fast
def print_ci_red_fast(s, color=''):    
    print(Fore.RED) #set text color
    for c in s:        
         print(c, end='', flush=True)
         if not keyboard.is_pressed("ctrl"):
             time.sleep(0.002)
    print('\033[A\033[39m') # reset the terminal color

#title screen

def title_screen_selections():
    option = input("\nYour choice: ")
    if option.lower().strip() == ("play"):
	    notes()
    elif option.lower().strip() == ("quit"):
	    sys.exit()
    elif option.lower().strip() == ("help"):
	    help_menu()		
    else:
      print_ci (required_menu)
      title_screen_selections()

def title_screen():
    print(Fore.RED + "#######################################")
    print("        # Certified Lover Boy #        ")
    print("#######################################")
    print('\033[39m')
    print("\033[A                - Play-                ") 
    print("                - Help-                ")
    print("                - Quit-                ")
    print(Fore.RED + "#######################################")
    print('\033[A\033[39m')
    title_screen_selections()

#hep menu in title screen
def help_menu():
    print(Fore.GREEN + "\n#####################################################################################################")
    print("                                          # The help menu #                                          ")
    print("#####################################################################################################")
    print("When 'Your choice:' line apperas type a number from the options given above.\n" 
          "The options will always be numbered from one to four.\n"
          "You can type your choice either in numbers(1,2,3,4) or in letters(one,two,three,four)\n"
          "\nAnytime while the text is appearing you can hold 'Ctrl' on your keyboard to greatly increase\n"
          "the speed at which text is showig up.\n"
          "This will usually lead to the rest of the text showing up instantly, it's recommended to only use\n"
          "this feature if you have already completed the game once and want to get to the next choice faster\n"
          "\nAt certain parts of the game text art shows up, you'll be able to tell as words won't be\n"
          "printing themselves anymore but just a mix of symbols and punctuation marks. It is a viable\n"
          "option to use the 'Ctrl' feature at this stages, even on your first playthrough, as the text\n"
          "art takes some time to print it self out. If you choose to do so no text will show up unless\n"
          "'Ctrl' is held down for too long after the text art has finihsed printing it self out.\n"
          "\nDuring the game anytime you're at the 'Your choice:' screen you can type 'help' instead of any of\n"
          "the available options and this screen will pop up if you need it.\n")
    print ('\033[A\033[39m')
    print ("Good luck and have fun!")
    print(Fore.GREEN + "#####################################################################################################")
    print('\033[A\033[39m')
    title_screen_selections()

#help menu in game
def help_menuInGame():
    print(Fore.GREEN + "\n#####################################################################################################")
    print("                                          # The help menu #                                          ")
    print("#####################################################################################################")
    print("When 'Your choice:' line apperas type a number from the options given above.\n" 
          "The options will always be numbered from one to four.\n"
          "You can type your choice either in numbers(1,2,3,4) or in letters(one,two,three,four)\n"
          "\nAnytime while the text is appearing you can hold 'Ctrl' on your keyboard to greatly increase\n"
          "the speed at which text is showig up.\n"
          "This will usually lead to the rest of the text showing up instantly, it's recommended to only use\n"
          "this feature if you have already completed the game once and want to get to the next choice faster\n"
          "\nAt certain parts of the game text art shows up, you'll be able to tell as words won't be\n"
          "printing themselves anymore but just a mix of symbols and punctuation marks. It is a viable\n"
          "option to use the 'Ctrl' feature at this stages, even on your first playthrough, as the text\n"
          "art takes some time to print it self out. If you choose to do so no text will show up unless\n"
          "'Ctrl' is held down for too long after the text art has finihsed printing it self out.\n"
          "\nDuring the game anytime you're at the 'Your choice:' screen you can type 'help' instead of any of\n"
          "the available options and this screen will pop up if you need it.\n")
    print ('\033[A\033[39m')
    print ("Good luck and have fun!")
    print(Fore.GREEN + "#####################################################################################################")
    print('\033[A\033[39m')
    
#Gmae over screen for when user dies
def gameOverScreen():
    time.sleep(1)
    print (Fore.RED + "\nGAME-OVER")
    print ('\033[A\033[39m')
    print (Fore.RED + """\n1. Replay from last death
  \n2. Start over completely
  \n3. Quit the game\n""")
    print ('\033[A\033[39m')

#Game over screen after credits

def gameOverScreenEnd():
    time.sleep(1)
    print (Fore.GREEN + "\nGAME COMPLETED!")
    print ('\033[A\033[39m')
    print (Fore.GREEN + """\n1. Go to main menu
  \n2. Start over completely
  \n3. Quit the game\n""")
    print ('\033[A\033[39m')
    gameOverScreenEndControls()

def gameOverScreenEndControls():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      title_screen()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       gameOverScreenEnd()
    else:
      print_ci (required_three)
      gameOverScreenEnd()

def notes():
    print_ci_red_fast ('####################################################################################################')
    print_ci_red_fast ('####################################################################################################')
    print_ci_red_fast ('############################################################           ##########################')
    print_ci_red_fast ('################################################################  - - - - ,   ######################')
    print_ci_red_fast ('#############################################################     \""""""",    #####################')
    print_ci_red_fast ('##############################################################     \"""""",    #####################')
    print_ci_red_fast ('##############################################################      /""""",    #####################')
    print_ci_red_fast ('    ####################################    _____   #####   _____  ///\""",    #######################')
    print_ci_red_fast ('  ####################################  ,ad8PPPP88b, ### ,d88PPPP///,  \"",    #######################')
    print_ci_red_fast ('    #################################  d8P"      "Y8b, ,d8P"      "Y8b  \",    ##########################')
    print_ci_red_fast ("####################################  dP'           '8a8'           `Yd    #########################")
    print_ci_red_fast ('    ###############################   8(              "              )8   ###########################')
    print_ci_red_fast ('       ############################   I8       \                     8I   #############################')
    print_ci_red_fast ('       ############################   8b,    Cer\ified Lover Boy   ,dP   ###############################')
    print_ci_red_fast ('#####################################   "8a,     \               ,a8"   ##########################')
    print_ci_red_fast ('     #################################   "8a,   //\           ,a8"   ###############################')
    print_ci_red_fast ('     ###################################   "Y //   |        adP"   ##################################')
    print_ci_red_fast ("     #####################################   //Y8a  '      a8P'   #################################")
    print_ci_red_fast ("   ####################################,   //   `88,t    ,88'   ################################")
    print_ci_red_fast ('  ########################### ######### \//       "8b   d8"   ###################################')
    print_ci_red_fast (' ####################################  /\          "8b d8"   #####################################')
    print_ci_red_fast ("#################################### //   '         `888'   ########################################")
    print_ci_red_fast ('####################################################  "   ########################################')
    print_ci_red_fast (' ###################################################################################################')
    print_ci ("\n\nNotes, please read before playing\n")
    print (Fore.GREEN + "\nAnytime while the text is appearing you can hold 'Ctrl' on your keyboard to greatly increase\n"
          "the speed at which text is showig up.\n"
          "This will usually lead to the rest of the text showing up instantly, it's recommended to only use\n"
          "this feature if you have already completed the game once and want to get to the next choice faster\n"
          "\nAt certain parts of the game text art shows up, you'll be able to tell as words won't be\n"
          "printing themselves anymore but just a mix of symbols and punctuation marks. It is a viable\n"
          "option to use the 'Ctrl' feature at this stages, even on your first playthrough, as the text\n"
          "art takes some time to print it self out. If you choose to do so no text will show up unless\n"
          "'Ctrl' is held down for too long after the text art has finihsed printing it self out.\n"
          "\nDuring the game anytime you're at the 'Your choice:' screen you can type 'help' instead of any of\n"
          "the available options and this screen will pop up if you need it.\n")
    print ('\033[A\033[39m')
    print ("Good luck and have fun!\n")
    input ("[Press enter to continue]\n")
    sceneOne()
    
#The story is split into scenes starting from scene one
def sceneOne():
 
  print_ci ("You’re Kaser, one of the youngest yet the most respected, brave and skilled knight in Orys, \n"
  "riding on top of the most prestigious dragon in the kingdom, with teeth as sharp as the \n" 
  "rarest rocks you can find, fire as hot as the magma within the roughest mountains, faster \n"
  "than any other dragon desirable by a man.\n")

  time.sleep(1.5)
            
  print_ci ("\nThe majestic White Agate.\n")

  print_ci_TaBlue (r"""

     /'                                                         
     ||
     ||      ** *
     ||      __X_
     ||     ( ___\
     ||     |:  \\
    ><><  ___)..:/_#__,
    (X|) (|+(____)+\ _)
     o|_\/>> + + + << \
       |:\/|+ + + +| \_\<
       \./  XXXXXX.  (o_)_
           /+ + + |   \:|
          /+ +/+ +|  -/->>>----.
         /+ +|+ /XX /   _--,  _ \
        \+ + + /  |X   (,\- \/_ ,
        /\+ + /\  |X \    /,//_/
       +_+_+_( )o_)X  \  (( ///
        (_o(  /__/ X   \  \\//
         \_|  |_/  X    \ ///
         \_| >(_/        \,/
    ,////__o\ /__////,    V                  



 """)

  print_ci_TaBlue(r"""
                                                 __----~~~~~~~~~~~------___
                                      .  .   ~~//====......          __--~ ~~
                      -.            \_|//     |||\\  ~~~~~~::::... /~
                   ___-==_       _-~o~  \/    |||  \\            _/~~-
           __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
       _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
     .~       .~       |   \\ -_    /  /-   /   ||      \   /
    /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
    |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\
             '         ~-|      /|    |-~\~~       __--~~
                         |-~~-_/ |    |   ~\_   _-~            /\
                              /  \     \__   \/~                \__
                          _--~ _/ | .-~~____--~-/                  ~~==.
                         ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                    -_     ~\      ~~---l__i__i__i--~~_/
                                    _-~-__   ~)  \--______________--~~
                                  //.-~~~-~_--~- |-------~~~~~~~~
                                         //.-~~~--\


""")
  
  input("\n[Press enter to continue]")

  print_ci ("\nIn front of you, Rosorus, son of the king of Orys, who’s souring through the air  \n"
  "on top of the vicious Black Agate. Rosorus is going to the gates of Hellheim.  \n" 
  "A prohibited place that’s only accessible by sacrificing the king’s most prised possession.\n")

  print_ci_TaRed(r"""

                                   _
                            ==(W{==========-      /===-
                              ||  (.--.)         /===-_---~~~~~~~~~------____
                              | \_,|**|,__      |===-~___                _,-'
                 -==\\        `\ ' `--'   ),    `//~\\   ~~~~`---.___.-~~
             ______-==|        /`\_. .__/\ \    | |  \\           _-~`
       __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\        ,'
    _-~       /'    |  \\     )__/==0==-\<>/   / /      \      /
  .'        /       |   \\      /~\___/~~\/  /' /        \   /'
 /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                  \_|      /        _) | ;  ),   __--~~
                    '~~--_/      _-~/- |/ \   '-~ \
                   {\__--_/}    / \\_>-|)<__\      \
                   /'   (_/  _-~  | |__>--<__|      |
                  |   _/) )-~     | |__>--<__|      |
                  / /~ ,_/       / /__>---<__/      |
                 o-o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~
                ,/|           /__>--<__/     _-~
             ,//('(          |__>--<__|     /                  .----_
            ( ( '))          |__>--<__|    |                 /' _---_~\
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\
        ,/,'//( (             \__>--<__\    \            /'  //        ||
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
   ;'( ')/ ,)(                              ~~~~~~~~~~
  ' ') '( (/
    '   '  `  



 """)

  input("\n[Press enter to continue]\n")

  print_ci ("He’s getting away with the king’s daughter,Rebekah, and you need to catch him \n"
         "before he gets to the gates of Hellhaim. \n")
  sceneOneOptions()

#First set of choices in the game, everything correct
    
def sceneOneOptions(): 
  print_ci ("\nWhat are you going to do?\n"
  """  \n1. Use the dragon’s power to get a boost and speed up to jump onto the Black Agate
  \n2. Use your grappling hook to slow down Rosorus’s dragon and jump onto him
  \n3. You get a boost of your dragon’s head and jump on top of Rosorus’s dragon\n""")
  choice = input("\nYour choice: ")
  if choice.lower().strip() in answer_one:
    option_power()
  elif choice.lower().strip() in answer_two:
    option_hook()
  elif choice.lower().strip() in answer_three:
    option_boost()
  elif choice.lower().strip() == ("help"):
	    help_menuInGame()
	    sceneOneOptions()
  else:
    print_ci (required_three)
    sceneOneOptions()

def option_power(): 
  print_ci ("\nYour dragon generates power through his tail and gets a speed boost that \n"
         "allows you to jump onto the Black Agate")
  sceneOnePartTwo()

def option_hook():
  print_ci ("\nYou successfully connected the hook to the wing of the dragon, slowed \n"
         "him down and jumped onto the Black Agate")
  sceneOnePartTwo()
  
def option_boost():
  print_ci ("\nYou successfully managed to jump on top of the Black Agate. \n")
  sceneOnePartTwo()


def sceneOnePartTwo():

  print_ci ("\nUnfortunately you were already really close to the gate and Rosorus manages to stop the \n"
  "dragon and lands it on the patio in front of the gate of Hellehim \n"
  "he gets off of it as quickly as he can while holding the unconscious princess over his left shoulder. \n" )
  time.sleep(1)
  print_ci_K ("\nKaser: Stop, I won't let you! \n",)
  time.sleep(0.5)
  print_ci_Ro ("\nRosorus: You're so stupid, just say out of this, she doesn't like you anyways. \n")
  sceneOneOptionsTwo()

#Second batch of options for scene one, everything correct

def sceneOneOptionsTwo():
    print_ci ("\nWhat do you do?\n"
    """  \n1. Take out your sword and challenge Rosorus
  \n2. Use your grappling hook to attack Rosorus\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_challenge()
    elif choice.lower().strip() in answer_two:
      option_hookAttack()
    elif choice.lower().strip() == ("help"):
      help_menuInGame()
      sceneOneOptionsTwo()
    else:
      print_ci (required_two)
      sceneOneOptions()

def option_hookAttack():
    print_ci ("\nYou take out your grappling hook and shoot it straight into Rosorus’s chest who just grabs it \n"
           "out of the air and pulls it towards himself. You lose the grip and Rosorus has the grappling hook. \n")
    time.sleep(2)
    print_ci ("\nHe throws it away \n")
    time.sleep(1)
    print_ci_Ro ("\nRosorus: Silly of you to think that that would work today. \n")
    time.sleep(1)
    print_ci ("\nWhat do you do?\n"
    """ \n1. Take out your sword and challenge Rosorus\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_challenge()
    elif choice.lower().strip() == ("help"):
	    help_menuInGame()
	    option_hookAttack()  
    else:
      print_ci (required_one)
      option_hookAttack()

def option_challenge():
    print_ci ("\nAs you pull out your sword out of your scabbard, Rosorus teleports himself in front of you and \n"
           "quickly extends his arm out where a sword with a black handle and a pommel in the shape of a skull \n"
           "appears. The blade itself wasn’t rigid, it looked like a black flame but it was atrociously hard \n"
           "to stare at it as anytime you did you could feel yourself getting dizzy and losing strength on your \n"
           "legs and arms. You could also hear sounds of people fainting in absolute pain and agony coming from \n"
           "the blade, where these all the poor people killed by that sword?  Rosorus quickly swung his blade \n"
           "diagonally from the top but you blocked it with yours. As soon as the two swords touched the ground \n"
           "trembled, the ocean around the patio started moving, multiple fish, dolphins and other animals \n"
           "jumped out of the water, hundreds if not thousands of birds could be heard flying out of their tress \n"
           "and then no other sound but both of you breathing. You and Rosorus were staring at each other with\n"
           "absolute disgust and anger wishing the worse for each other while applying as much pressure as you could\n"
           "with your blade on the other’s until Rosorus noticed a white dragon engraving on the handle of your sword.\n")

    print_Ta(r"""

                            ,--.                       ,--.
                          _',|| )                     ( \\ |
            ,.,,.,-----""' "--v-.___                   `_\\.'--,..__
            |,"---.--''/       /,.__"")`-:|._________-"'     (--..__'/--.
                      /     ,."'    ""-'-"|'  _.,-"_.'-"\     \     ` '""
                   _ )____---------------(|--"_|--'      '__   \_
                _,' |  .''''""---.        '""'       ,---'''.   /".
            _,-'  ." \/,,..---/_ /                   | -|.._____|  \_
          ,-\,.'''            \ (                    |"")       "-,  \
      _ .".--"                ( :                    | (           '. "\_
    ,- ,."                    ; !                    ; |             \,_ `.
___(_(."                      L_">        _________.-/_J                '\_')


 """)

    input ("\n[Press enter to continue]")
    print_ci_Ro ("\nRosorus: Is that my dad’s sword? \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Yes \n\n")
    time.sleep(1)
    print_ci ("\nRosorus was getting visibly worried. His confident smirk quickly turned into a face full of terror. \n"
         "The voices from his blade were getting quieter, his legs started to shake, then his body, arms shoulders.")
    time.sleep(1)
    print_ci ("\nYou squeezed your blade’s handle as hard as you could and pushed against Rosorus’s sword as hard as you \n"
         "could. You gave it all you had and your blade lit up in a whitely angelic colour and his sword flew away \n"
         "in the ocean that was around the patio. The shockwave made Rosorus fly and hit his back violently against \n"
         "the pillar that was holding the gates to Hellheim.")
    print_ci_TaRed(r"""

           
|| |_| |_| |_| |------------------------------------|_| |_| |_| |_||
|______________|[=][=][=][=][=][=][=][=][=][=][=][=]|______________|
|--------------|____________________________________|--------------|
|   _______    |------------------------------------|    _______   |
|  |   _   |   |     |           .-.           /    |   |   _   |  |
|  |.'* *'.|   |     \     _..--('[|)-..__     |    |   |.'* *'.|  |
|  |'. * .'|   |      |_.-'   .-'/'\'-.   '-._/     |   |'. * .'|  |
|  '. )_( .'   |      /   _.-' .'   '. '-._   \     |   '. )_( .'  |
|    '._.'     |     /_.-' _.-'       '-._ '-._\    |     '._.'    |
|______________|     |_.--'               '--._|    |______________|
|-.   .--.   .-|    /'                         '\ ' |-.   .--.   .-|
|  \ /    \ /  |  | |                          .' | |  \ /    \ /  |
| * v *  * v * | || '.                         | || | * v *  * v * |
|   *      *   | || ||                         | || |   *      *   |
|              ||   ||                         | || |              |
|              ||  | |                         || | |              |
[=][=][==][=][=]'. ' |                        | ' `.[=  =][= ]]  [=]
|              | | | |                        | |  ||              |
|              | | | |                        | |  ||       |  #   |
|              ||  \  \                      /  /  ||(     /       |
|              |'.   '/                      \'    `| \  # #  #    |
[=][=][==][=][=] '    \                      /    / |  #(.--.) #   |   
|              |                                    | \_,|**|,__   |   
|              |                            #       `\ ' `--'   ),    #
|              |                         \_          /`\_. .__/\ \        #
|              |                           \_ #     (   | .  |~~~~|  #   #
|              |                             \_     )__/==0==-\<>         #                     
`--...____...--'                     _____#_______  `--..        --'   ________     
                              


 """)

    time.sleep(2)
    
    print_ci ("\nThe impact left him unconsious.\n")

    input("\n[Press enter to continue]")
    
    print_ci ("\nYou go up to the princess, Rebekah, pick her up and take her to the dragon, you gently put her on the \n"
          "front seat as she slowly starts waking up and you stop. And start staring at her, at how her hair fell \n"
          "perfectly without her even trying, at how all of her facial details beautifully complimented each other. \n"
          "And just at how absolutely stunning she really was. You could feel your heart pounding as hard as the first \n"
          "time you had seen her if not harder.\n")
    time.sleep(3)
    print_ci ("\nRebekah looks around.\n")
    time.sleep(2)
    print_ci_R ("\nRebekah: You saved me. \n")
    print_ci_K ("\nKaser: mmm, ye, maybe, I don’t know, mmm. I mean I wouldn’t say- \n\n")
    print_ci ("\nShe grabs your hand as you slowly sit behind her. She turns around and you’re facing face to face with \n"
          "your knees and hands touching.\n")
    time.sleep(2)
    print_ci_R ("\nRebekah: Thank you \n")
    time.sleep(2)
    print_ci_R ("\nRebekah: Let’s get high tonight \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Woah, chill you know I don’t do that \n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: Just make an exception for today. It’ll be worth it… \n")
    time.sleep(2)
    print_ci_R ("\nRebekah: …I promise \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Ok, but only because it’s you. \n")
    time.sleep(2)
    print_ci_R ("\nRebekah pulls you by your jacket, she leans in closer and closer until your noses are touching. \n"
          "You put your hands behind her head and…\n")

    input("\n[Press enter to continue]")

    print ("\n*KNOCK*")
    print ("\n*KNOCK*")

    time.sleep(1)

    input("\n[Press enter to continue]")

    print ("\n*KNOCK*")
    print ("\n*KNOCK*")

    time.sleep(1)

    input("\n[Press enter to continue]")

    print ("\nMum enters room")

    time.sleep(3)

    print_ci ("\nMum: Wake up or you’re gonna be late to lesson again for the third morning in a row.\n"
              "I really don’t wanna get another letter home from the school. \n")
    
    time.sleep(0.5)
    
    print_ci_K ("\nKaser: Ok ok I’m going, just chill \n\n")
    
    time.sleep(0.5)

    print ("\nMum leaves the room")

    time.sleep(2)

    print_ci_K ("\nKaser: She so fine, daaamn. Can’t even get her in my dreams…urgh…\n")
    sceneTwo()

#Scene two starts here
    
def sceneTwo():
    print ("\nYou get out of bed")
    sceneTwoOptions()

def sceneTwoOptions():    
    print_ci ("\nPick an option:\n"
    """  \n1. Check backpack\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_backpackTwo()
    elif choice.lower().strip() == ("help"):
	    help_menuInGame()
	    sceneTwoOptions()  
    else:
     print_ci (required_one)
     sceneTwoOptions()

def option_backpackTwo():
    print ("\nIron Sword - [empty] - [empty] - [empty]")

    time.sleep(2)
    
    sceneTwoOptionsTwo()

def sceneTwoOptionsTwo():
    print_ci ("\nPick an option:\n"
    """  \n1. Go to school\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneThree()
    elif choice.lower().strip() == ("help"):
	    help_menuInGame()
	    sceneTwoOptionsTwo()  
    else:
     print_ci (required_one)
     sceneTwoOptionsTwo()

def sceneThree():
    time.sleep(1)

    print_ci_TaGreen(r'''

           
                                 ____                                         
                              .-     `-.      ,                               
                            .'          '.   /j\                              
                           /              \,/:/#\                /\           
                          ;              ,//' '/#\              //#\          
                          |             /' :   '/#\            /  /#\         
                          :         ,  /' /'    '/#\__..--""""/    /#\__      
                           \       /'\'-._:__    '/#\        ;      /#, """---
                            `-.   / ;#\']" ; """--./#J       ':____...!       
                               `-/   /#\  J  [;[;[;Y]         |      ;        
""""""---....             __.--"/    '/#\ ;   " "  |     !    |   #! |        
             ""--.. _.--""     /      ,/#\'-..____.;_,   |    |   '  |        
                   "-.        :_....___,/#} "####" | '_.-",   | #['  |        
                      '-._      |[;[;[;[;|         |.;'  /;\  |      |        
                      ,   `-.   |        :     _   .;'    /;\ |   #" |        
                      !      `._:      _  ;   ##' .;'      /;\|  _,  |        
                     .#\"""---..._    ';, |      .;{___     /;\  ]#' |__....--
          .--.      ;'/#\         \    ]! |       "| , """--./_J    /         
         /  '%;    /  '/#\         \   !' :        |!# #! #! #|    :`.__      
        i__..'%] _:_   ;##J         \      :"#...._!   '  "  "|__  |    `--.._
         | .--""" !|""""  |"""----...J     | '##"" `-._       |  """---.._    
     ____: |      #|      |         #|     |          "]      ;   ___...-"T,  
    /   :  :      !|      |   _______!_    |           |__..--;"""     ,;MM;  
   :____| :    .-.#|      |  /\      /#\   |          /'               ''MM;  
    |""": |   /   \|   .----+  ;      /#\  :___..--"";                  ,'MM; 
   _Y--:  |  ;     ;.-'      ;  \______/#: /         ;                  ''MM; 
  /    |  | ;_______;     ____!  |"##"""MM!         ;                    ,'MM;
 !_____|  |  |"#"#"|____.'""##"  |       :         ;                     ''MM  
  | """"--!._|     |##""         !       !         :____.....-------"""""" |'
  |          :     |______                        ___!_ "#""#""#"""#"""#"""|  
__|          ;     |MM"MM"""""---..._______...--""MM"MM]                   |   
  "\-.      :      |#                                  :                   |  
    /#'.    |      /##,                                !                   |  
   .',/'\   |       #:#,                                ;       .==.       |  
  /"\'#"\',.|       ##;#,                               !     ,'||||',     |  
        /;/`:       ######,          ____             _ :     M||||||M     |  
       ###          /;"\.__"-._   """                   |===..M!!!!!!M_____|  
                           `--..`--.._____             _!_                    
                                          `--...____,="_.'`-.____            
                            

 ''')

    time.sleep(2.5)
    
    print_ci ("\nAs you reach the school and get to the corridor where your classroom is you see your friend Xavier waiting outside\n")
    time.sleep(1)
    print_ci_X ("\nXavier: Been waiting ages for you \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: What do you mean? Just go in \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Nah, we going down to the basement \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: What? No, we can’t do that. Just go lesson \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: It’s about Rosorus. \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Bro, we not even allowed down there. \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Ye I know but this is important. Trust me and we can only go now. I’m not sure we’re getting another chance \n")
    sceneThreeOptions()

def sceneThreeOptions():
    print_ci ("\nWhat do you do?\n"
    """  \n1. I really don’t wanna miss another sword fighting lesson, sorry maybe next time
  \n2. *gasps* ok let’s go…\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneFour()
    elif choice.lower().strip() in answer_two:
      sceneFive()
    elif choice.lower().strip() == ("help"):
	    help_menuInGame()
	    sceneThreeOptions()  
    else:
      print_ci (required_two)
      sceneThreeOptions()

def sceneFour():
    print_ci ("\nMiss Greys: You boys kind of late, but its ok don’t worry about it. Just pair up and do the drill on the board. \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Thank God miss Greys is chill \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Ye... \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Is everything good? \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Ye… \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: You had another one of those dreams? \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Ye, this shit was crazy. \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Why you smiling like that? Damn…It was definitely with her haha… \n")
    time.sleep(0.5)
    print_ci ("\nMiss Greys: come on boys, focus please. \n")
    print_ci ("\n*You pick up wooden equipment and get in your stance to practice against Xavier* \n")
    print_ci ("\nYou look at the board \n")
    print ("\nHeavy Sword swing: Heavy and slow hit that works very well to break parts of demons \n"
           "or brake human’s armours and weapons if these are weak enough. Also works well to finish \n"
           "off an enemy.")
    print_ci ("\nYou get in your fighting stance and face Xavier who does the same \n")
    sceneFourOptions()
    
def sceneFourOptions():
    print_ci ("\nWhat do you do?\n"
    """  \n1. Heavy sword swing\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneFourPartTwo()
    elif choice.lower().strip() == ("help"):
	    help_menuInGame()
	    sceneFourOptions()  
    else:
      print_ci (required_one)
      sceneFourOptions()

def sceneFourPartTwo():

    print_ci ("\nYou take a step back and start charging towards Xavier as he moves his sword up and closer to his body to \n"
              "get ready to absorb the hit. You jump and swing sideways towards his sword. The impact causes his sword to \n"
              "break in half as he falls while dropping what was left of the wood.\n")
    
    input("\n[Press enter to continue]")
    
    print_ci ("\nThe whole class looks towards you in awe\n"
              "Miss Greys: Yes Kaser, that’s exactly how that move is meant to be executed. Well Done.\n")
    print ("\n*Bell Rings*\n")
    print_ci ("Miss Greys: Oh well, I guess you're all off\n")

    input("\n[Press enter to continue]\n")
    sceneSix()


def sceneFive():
    print_ci_K ("\nKaser: Ok so…why exactly are we here?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Well…I told you it’s about Rosorus. He did something he shouldn’t have.\n"
                "And I wanna show you. Also, it’s just fun here.\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: I mean ye I guess. Finally we get to fight some demons. It’s been ages \n"
                "since I’ve seen any of them.\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Nah I’m going to use my dad’s old card it should still work. In theory…\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: You finally got it! What took you so long to tell me damn\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: I’m not even sure it’s going to work. I just snatched it from my mum’s room while she was sleeping.\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Ok here’s the gate. Let’s try swiping the card.\n\n")
    time.sleep(1.5)
    print ("\n*Xavier swiped the card on the scanner*")
    time.sleep(0.5)
    print_ci ("\nThe screen turns red and a reoccurring beep noise starts playing\n")
    time.sleep(1)
    print_ci_K ("\nKaser: I don’t think that’s what should have happened.\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: They disabled the card. Get ready…\n\n")
    time.sleep(0.5)
    print_ci ("\n2 demons come out from the walls. One from the left and one from the right\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Ok you get the Gollex and I get the Lexin\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: It’s always me getting the biggest demons\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: ehm…Duh “Student of the month”\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Shut up bruh\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Remember destroy one of his arms first and then attack his core.\n\n")
    time.sleep(1)
    print ("\nYou unlocked heavy sword swing")
    print_ci ("\nSword swing: Heavy and slow hit that works very well to break parts of demons or brake human’s armours and \n"
              "weapons if these are weak enough. Also works well to finish off an enemy.\n")
    
    print_ci_TaRed(r"""

                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
                  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"

 """)
    
    input("\n[Press enter to continue]")
    
    sceneFiveOptions()

def sceneFiveOptions():
    print_ci ("\nWhat move are you going to do?\n"
  """  \n1. Light sword swing (simple light attack)
  \n2. Sword frisbee throw (You throw your sword towards the enemy and it comes back to you)
  \n3. Heavy sword swing\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_deathOneSceneFive()
    elif choice.lower().strip() in answer_two:
      option_deathTwoSceneFive()
    elif choice.lower().strip() in answer_three:
      option_correctOneSceneFive()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       sceneOneOptions()
    else:
      print_ci (required_three)
      sceneFiveOptions()

def option_deathOneSceneFive():
    print_ci ("\nYou sprint towards the Gollex and get your sword out of your scabbard. As you get within reach of the Gollex \n"
              "you swing the sword towards it's leg.\n")
    time.sleep(1)
    print_ci ("\nIt does not bother him at all and he picks you up and tears you apart in two pieces as Xavier screams for \n"
              "help at the top of his lungs. He then gets torn apart and both of your bodies slowly start turning into demons.\n")
    gameOverScreen()
    gameOverSceneFiveDeathOne()

def gameOverSceneFiveDeathOne():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneFiveOptions()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathOneSceneFive()
    else:
      print_ci (required_three)
      option_deathOneSceneFive()

def option_deathTwoSceneFive():
    print_ci ("\nYou get your sword out of your scabbard. Cock it back and throw it as hard as you can towards the Gollex.\n"
              "You aim for his chest but he uses his arm to parry the sword which goes back towards your direction\n")
    time.sleep(1)
    print_ci ("\nThe Gollex charges at you. Grabs you before you can react to anything and your own sword penetrates \n"
              "through your head as Xavier screams for help at the top of his lungs. He then gets torn apart and both \n"
              "of your bodies slowly start turning into demons.\n")
    gameOverScreen()
    gameOverSceneFiveDeathTwo()
    
def gameOverSceneFiveDeathTwo():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneFiveOptions()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathTwoSceneFive()
    else:
      print_ci (required_three)
      option_deathTwoSceneFive()

def option_correctOneSceneFive():
    print_ci ("\nYou take a step back and sprint towards the Gollex as fast as you can. When you get close enough you jump \n"
              "on his shoulder. Jump again and while in the air you take out your sword out of your scabbard and horizontally \n"
              "penetrate through the Gollex’s shoulder which causes his arm to fall off and you land right next to his foot.\n")
    time.sleep(1)
    print_ci ("\nThe Gollex screams in Agony and falls on his back.\n")
    sceneFiveOptionsTwo()

def sceneFiveOptionsTwo():
    print_ci ("\nWhat do you do?\n"
    """  \n1. Destroy the Gollex's core\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneFivePartTwo()
    elif choice.lower().strip() == ("help"):
	    help_menuInGame()
	    sceneTwoOptionsTwo()  
    else:
     print_ci (required_one)
     sceneFiveOptionsTwo()

def sceneFivePartTwo():
    print_ci ("\nYou sprint and jump on top of the Gollex’s belly and penetrate through his chest and break the purplish \n"
              "sphere that was orbiting between the rocks that made up his crusty body. All the rocks fall apart on the ground. \n"
              "Some of them break in half. Others in multiple pieces.\n")

    input ("\n[Press enter to continue]")

    print_ci ("\nXavier got rid of the Lexin and he is now walking towards you\n")
    time.sleep(1)
    print_ci_X ("\nXavier: Ok good job. Let’s get in. \n")
    time.sleep(0.5)
    print_ci ("\nXavier extends his arms towards the gate and moves his right foot slightly behind him as if he was \n"
              "pushing something extremely heavy. He starts shaking and his veins pop out more. A cold breeze can be felt\n"
              "pass through the corridor where the remaining’s of the Demons were resting. Xavier’s face gets redder and \n"
              "redder as he starts to clench his jaw, hold his breath, his eyebrows get lower and closer together, \n"
              "his lips start pointing downwards and then he seems to relax for a split second until a blast of dark and \n"
              "purplish light comes out of his hand and flies towards the gate. The beeping stopped and the gate began to open. \n")
    time.sleep(1)
    print_ci_K ("\nKaser: Was that Dark magic?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Ye...\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: That shit looks so fucking cool\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: You wish you could do that\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: bruh shut up, won’t you get in trouble like last time though?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: No, When I said I had been waiting for ages, I mean ages. I came as early as I could to avoid as \n"
                "many teachers and students as possible. I managed to sneak into the department of dark magic and use my \n"
                "dad’s card to give my self-permission to use dark magic anywhere in the school without alerting the government. \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Something is genuinely wrong with you. You could have gotten in so much trouble I don’t even want to imagine. \n"
                "Whatever\n")
    time.sleep(1)
    print_ci_K ("\nKaser: Did you...\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser:...Give permission to anyone else by any chance?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: You?\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: What no. I don’t know the first thing about this. I was thinking about you know….\n")
    time.sleep(1)
    print_ci_X ("\nXavier: Rebekah?\n")
    print_ci_K ("\nKaser: Ye\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Bro we’re not even friends with her. Plus… you know she’s for the streets. Like come on now. Do better. \n")
    print_ci_K ("\nKaser: No she’s not. Stop saying that. Rosorus said she a virgin and how she never had a boyfriend She cool. \n")
    print_ci_X ("\nXavier: Ye definitely bro. Just look at her. There is virtually no way that girl hasn’t done it but whatever you say simp\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Whatever bro…Let’s just go in\n")
    time.sleep(0.5)
    print_ci ("\nYou and Xavier make your way through the old rusty gate. You close the gate behind you and follow him to the dark and\n"
              "mysterious basement.\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: 'Litmus'\n\n")
    print_ci ("\nA small white ball of light appears in the air in front of Xavier. It shined hard enough to illuminate everything around you.\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Where we going?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Just wait we’re almost there\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: So, you said this is about Rosorus. What exactly about him and why couldn’t you just tell me?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Well…he kind of messed up…I mean it depends how you look at it. It’s just funny. I cannot wait to see your reaction.\n"
                "Anyways here we are\n")
    time.sleep(0.5)
    print_ci ("\nXavier turns on one of the computers on the table. He sits down on the chair and pulls out a CD from one of the inside \n"
              "pockets of his jacket. You sit on the chair next to his.\n")

    print_ci_TaGreen(r'''

           
  /                /|
              /                / |
             /________________/ /|
          ###|      ____      |//|
         #   |     /   /|     |/.|
        #  __|___ /   /.|     |  |_______________
       #  /      /   //||     |  /              /|                  ___
      #  /      /___// ||     | /              / |                 / \ \
      # /______/!   || ||_____|/              /  |                /   \ \
      #| . . .  !   || ||                    /  _________________/     \ \
      #|  . .   !   || //      ________     /  /\________________  {   /  }
      /|   .    !   ||//~~~~~~/   0000/    /  / / ______________  {   /  /
     / |        !   |'/      /9  0000/    /  / / /             / {   /  /
    / #\________!___|/      /9  0000/    /  / / /_____________/___  /  /
   / #     /_____\/        /9  0000/    /  / / /_  /\_____________\/  /
  / #                      ``^^^^^^    /   \ \ . ./ / ____________   /
 +=#==================================/     \ \ ./ / /.  .  .  \ /  /
 |#                                   |      \ \/ / /___________/  /
 #                                    |_______\__/________________/
 |                                    |               |  |  / /       
 |                                    |               |  | / /       
 |                                    |       ________|  |/ /________       
 |                                    |      /_______/    \_________/\       
 |                                    |     /        /  /           \ )       
 |                                    |    /OO^^^^^^/  / /^^^^^^^^^OO\)       
 |                                    |            /  / /        
 |                                    |           /  / /
 |                                    |          /___\/
 |                                    |           oo
 |____________________________________|


 ''')

    input("\n[Press enter to continue]")
    
    time.sleep(0.5)
    print_ci_X ("\nXavier: Here we go…\n\n")
    time.sleep(0.5)
    print_ci ("\nYou both begin watching\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: What is this place?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: I don’t know exactly but you see that guy next to Rosorus. That’s one of his friends. Apparently his rich and \n"
                "he’s gonna pay for an escort for Rosorus…\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: ehm?? What?? Yooo this dude is wilding.\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Ye the funniest part is that the friend is 16…\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Nah bro they tripping. Is this even legal?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: I don’t know but it really does not matter. Ok now watch cause holy is this funny\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Is she going to put the condom on for him?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: With her mouth hahaha\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: what the fu-…ok…\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: look at his thing he can’t even get it up hahah\n\n")
    time.sleep(0.5)
    print_ci ("\nXavier: *keeps laughing louder and louder*\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Bro what is this. This man trash bruh\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: You don’t got much room to talk…\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: I promise on everything whenever I do it…It will be better than whatever this is…\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Xavier: You’d choke worse with the one you want\n")
    print_ci_K ("\nKaser: bro shut up\n")
    time.sleep(1)
    print_ci_K ("\nKaser:How long is this crap bruh?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Too long to watch the whole thing let’s skim through it.\n")
    print_ci ("\nXavier skips through the video\n")
    time.sleep(1.5)
    print_ci_K ("\nKaser: Ok they changed positions and…bruh this man really had to get his small weiner sucked off with a condom on…ergh…not gonna \n"
                "lie I’m kinda jealous\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: You wanna loose your virginity to a prostitute?\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: What? no, just the-\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Anyways that's it\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: This man didn’t even bust…\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: No hahaha\n\n")
    time.sleep(0.5)
    print_ci ("\nBoth start laughing\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Nah This dude is not gonna catch a break from me. I’m about to make fun of him for the rest of the year.\n\n")
    time.sleep(0.5)
    print_ci ("\nBoth you and Xavier start leaving the basement\n")
    print_ci_K ("\nKaser: This is the part where I tell Rebekah and she gets jealous cause her ugly ass brother lost his Virginity\n"
                "before her and then she wants to do it with me…\n")
    print_ci_X ("\nXavier: That’s assuming she hasn’t already lost it and done it 100nds of times with hella different guys.\n")
    print_ci_K ("\nKaser: Stop with this slut shaming shit. You think her brother wouldn’t know she lost it.\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Yes…he kept telling me and Zane to not tell his sister. He also said to not tell his other friends\n"
                "cause they might tell her and he just kept saying to not tell he, so if he’s hiding it from her, I’m sure\n"
                "she’d be hiding it from him too.\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Guess I’m not telling her anymore…\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Not like you would have anyways, you’re too scared to even look at her.\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: daaaamn…Imagine if she seduced me cause she knows Rosorus is hiding a secret from her and she knows I’d\n"
                "tell her…aww please God let that happen\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: You’d tell her as soons as she'd ask you\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Hell nah, I'd make her wanna seduce me\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: You’d actually tell her if she seduced you?\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Hell ye, how do you expect me to control myself. Like come on now.\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Mans gonna break Bro code over some slutty girl.\n")
    print_ci_K ("\nKaser: OH MY-\n")
    print_ci_X ("\nXavier: Shhh!\n")
    print_ci ("\nXavier grabs you around your neck, puts his hand over your mouth and pulls you behind a Gondola (a standing\n"
              "fixture commonly used in supermarkets to place products).\n")
    print_ci_X ("\nXavier: *quietly* 'Litmus'\n")
    time.sleep(0.5)
    print_ci ("\nThe little ball of lights disappears and you’re in complete darkness\n")
    time.sleep(0.5)
    print_ci_Ro ("\n?:Where did the scream come from?\n")
    time.sleep(0.5)
    print_ci_Ro ("\nMultiple people: Don't *Unintelligible* No idea *Unintelligible*\n")
    time.sleep(0.5)
    print_ci_Ro ("\n?: SHOW YOURSELVES INTRUDERS!\n")
    time.sleep(2)
    print_ci ("\n...\n")
    time.sleep(1)
    print_ci_Ro ("\n?:SPREAD OUT, FIND THEM AND BRING THEM ALIVE THEY MIGHT BE STUDENTS.\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: *quietly* There’s a fucking army out there.\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: *quietly* 7 people, we can’t take them.\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: *quietly* Especially when they would recognise us.\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: *quietly* Ye, let’s split up so they don’t find me when you get caught\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: *quietly* Urgh\n")
    time.sleep(0.5)
    print_ci ("\nYou’re behind the Gondola facing away from the exit which is about 20 metres behind you to the left.\n"
              "The guards are all behind you covering the exit and moving quickly around the basement to find you and Xavier.\n"
              "Hurry up before one of you is found.\n")

    input("\n[Press enter to continue]")

    sceneFiveOptionsThree()

def sceneFiveOptionsThree():
    print_Ta(r"""

                 ----------------------------------------------
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |
                 ----------------------------------------------
 LEFT                                                            RIGHT  

           LIGHT      X   <----YOU
          \     /----------------------------------------------
           \   / |                                            |
            \ /  |                                            |
             o   |                                            |
                 |                                            |(2)
                 |                                            |
                 ----------------------------------------------



                 ----------------------------------------------
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |
                 ----------------------------------------------
...

EXIT(1)
...              ----------------------------------------------
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |
                 ----------------------------------------------



 """)

    time.sleep(1)
    print_ci ("\nYou can see a light getting closer and closer to you\n"
    "\nWhere do you want to go?\n"
  """  \n1. Move to the left to turn to the exit
  \n2. Move to the right along the Gondola to hide behind the short side
  \n3. Wait\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_deathThreeSceneFive()
    elif choice.lower().strip() in answer_two:
      option_correctTwoSceneFive()
    elif choice.lower().strip() in answer_three:
      option_deathFourSceneFive()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       sceneFiveOptionsThree()
    else:
      print_ci (required_three)
      sceneFiveOptionsThree()

def option_deathThreeSceneFive():
    print_ci_Ro ("\n?: Ugh?\n")
    print_ci_Ro ("?: I FOUND ONE OF THEM QUICK RUSH HIM HERE! HERE!\n")
    time.sleep(0.5)
    print_ci ("\nYou get over run by the guards. Xavier rushes to help you and you try to fight them off but you\n"
              "both end up getting knocked out and taken to the principal’s office.\n")
    gameOverScreen()
    gameOverSceneFiveDeathThree()
    
def gameOverSceneFiveDeathThree():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneFiveOptionsThree()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathThreeSceneFive()
    else:
      print_ci (required_three)
      option_deathThreeSceneFive()

def option_deathFourSceneFive():
    print_ci ("\nThe light gets closer and closer to you.\n")
    time.sleep(2)
    print_ci_Ro ("\n?: I FOUND ONE OF THEM QUICK RUSH HIM HERE! HERE!\n")
    time.sleep(0.5)
    print_ci ("\nYou get over run by the guards. Xavier rushes to help you and you try to fight them off but you both\n"
              "end up getting knocked out and taken to the principal’s office.\n")
    gameOverScreen()
    gameOverSceneFiveDeathFour()

def gameOverSceneFiveDeathFour():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneFiveOptionsThree()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathFourSceneFive()
    else:
      print_ci (required_three)
      option_deathFourSceneFive()

def option_correctTwoSceneFive():
    print_Ta(r"""

                 ----------------------------------------------
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |(1)
                 ----------------------------------------------
                                                               
                                                                  RIGHT
                 
                 ----------------------------------------------
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |X <----YOU
                 |                                            |
                 ----------------------------------------------
                                            (2)          .../'''  
                                                       o<        LIGHT    
                                                         '''\...
                 ----------------------------------------------
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |    LEFT
                 |                                            |
                 ----------------------------------------------
...

EXIT
...              ----------------------------------------------
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |
                 ----------------------------------------------




 """)

    time.sleep(1)
    print_ci ("\nThere is darkness on your right and light on your left that’s getting closer to you\n"
    "\nWhere do you want to go?\n"
  """  \n1. Move to the next Gondola to the right
  \n2. Move to the left along the Gondola
  \n3. Wait\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_deathFiveSceneFive()
    elif choice.lower().strip() in answer_two:
      option_deathSixSceneFive()
    elif choice.lower().strip() in answer_three:
      option_correctThreeSceneFive()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_correctTwoSceneFive()
    else:
      print_ci (required_three)
      option_correctTwoSceneFive()

def option_deathFiveSceneFive():
    print_ci ("\nAs you move to the right a guard walks by where you previously were hiding and spots you.\n")
    time.sleep(0.5)
    print_ci_Ro ("\n?: Ugh?\n")
    print_ci_Ro ("\n?: I FOUND ONE OF THEM QUICK RUSH HIM HERE! HERE!\n")
    time.sleep(0.5)
    print_ci ("\nYou get over run by the guards. Xavier rushes to help you and you try to fight them off but\n"
              "you both end up getting knocked out and taken to the principal’s office.\n")
    gameOverScreen()
    gameOverSceneFiveDeathFive()

def gameOverSceneFiveDeathFive():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_correctTwoSceneFive()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathFiveSceneFive()
    else:
      print_ci (required_three)
      option_deathFiveSceneFive()

def option_deathSixSceneFive():
    print_ci_Ro ("\n?: I FOUND ONE OF THEM QUICK RUSH HIM HERE! HERE!\n")
    time.sleep(0.5)
    print_ci ("\nYou get over run by the guards. Xavier rushes to help you and you try to fight them off but you both\n"
              "end up getting knocked out and taken to the principal’s office.\n")
    gameOverScreen()
    gameOverSceneFiveDeathSix()

def gameOverSceneFiveDeathSix():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_correctTwoSceneFive()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathSixSceneFive()
    else:
      print_ci (required_three)
      option_deathSixSceneFive()

def option_correctThreeSceneFive():
    print_ci ("\nAs you wait the light gets closer and closer to you but never turns the corner and you don’t get seen.\n"
              "The light is now moving away from you.\n")
    time.sleep(1)
    sceneFiveOptionsFive()

def sceneFiveOptionsFive():
    print_Ta(r"""

                 ----------------------------------------------
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |
                 ----------------------------------------------
                                                               
                                                                  RIGHT
                 
                 ----------------------------------------------
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |X <----YOU
                 |                                            |
                 ----------------------------------------------
                                             '''\...      2  
                                                    >o            
                                             .../'''      
                 ----------------------------------------------
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |    LEFT
                 |                                            |
                 ----------------------------------------------
...

EXIT
...              ----------------------------------------------
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |
                 |                                            |
                 ----------------------------------------------





 """)

    time.sleep(1)
    print_ci ("\nWhat do you do?\n"
  """  \n1. Wait
  \n2. Move to the left along the Gondola\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_deathSevenSceneFive()
    elif choice.lower().strip() in answer_two:
      option_correctFourSceneFive()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       sceneFiveOptionsFive()
    else:
      print_ci (required_two)
      sceneFiveOptionsFive()

def option_deathSevenSceneFive():
    print_ci ("\nAs you wait a guard from the right turns the corner of the Gondola and spots you\n")
    time.sleep(0.5)
    print_ci_Ro ("\n?: Ugh?\n")
    print_ci_Ro ("\n?: I FOUND ONE OF THEM QUICK RUSH HIM HERE! HERE!\n")
    time.sleep(0.5)
    print_ci ("\nYou get over run by the guards. Xavier rushes to help you and you try to fight them off but\n"
              "you both end up getting knocked out and taken to the principal’s office.\n")
    gameOverScreen()
    gameOverSceneFiveDeathSeven()

def gameOverSceneFiveDeathSeven():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneFiveOptionsFive()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathSevenSceneFive()
    else:
      print_ci (required_three)
      option_deathSevenSceneFive()

def option_correctFourSceneFive():
    print_ci ("\nYou slowly move to the left, get around the Gondola and the guard is a few metres in front of you.\n"
              "On one of the shelfs you see something shiny that looks like a switchblade.\n")
    time.sleep(0.5)
    sceneFiveOptionsSix()

def sceneFiveOptionsSix():
    print_ci ("\nWhat do you do?\n"
  """  \n1. Pick up the switchblade and stealth kill the guard
  \n2. Wait\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_correctFiveSceneFive()
    elif choice.lower().strip() in answer_two:
      option_deathEightSceneFive()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       sceneFiveOptionsSix()
    else:
      print_ci (required_two)
      sceneFiveOptionsSix()

def option_deathEightSceneFive():
    print_ci ("\nAs you wait the guard decides to turn around to check his surroundings and spots you.\n")
    time.sleep(0.5)
    print_ci_Ro ("\n?: Ugh? \n")
    print_ci_Ro ("\n?: I FOUND ONE OF THEM QUICK RUSH HIM HERE! HERE!\n")
    time.sleep(0.5)
    print_ci ("\nYou get over run by the guards. Xavier rushes to help you and you try to fight them off but\n"
              "you both end up getting knocked out and taken to the principal’s office.\n")
    gameOverScreen()
    gameOverSceneFiveDeathEight()

def gameOverSceneFiveDeathEight():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneFiveOptionsSix()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathEightSceneFive()
    else:
      print_ci (required_three)
      option_deathEightSceneFive()

def option_correctFiveSceneFive():
    print_ci ("\nYou slowly pick up the switchblade. You move towards the guard as quietly as possible. As you get\n"
              "within arm’s reach you put the guard in a headlock and cover their mouth before they’re able to react.\n"
              "As you do that you press the button on your switchblade to get the blade out and stab the guard in \n"
              "their neck, once the handle touches the neck you pull it out and quickly stab them in the side of \n"
              "their head about 3 inches above their ear. You gently put the guard on the floor. You use the sleeves \n"
              "of your tunica to dry the blood on your face and hands.\n")  

    input("\n[Press enter to continue]")
    sceneFiveOptionsSeven()
    
def sceneFiveOptionsSeven():
    print_ci ("\nWhat do you do?\n"
  """  \n1. Hide the guard’s body in between the shelfs next to you.\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneFiveEnding()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       sceneFiveOptionsSeven()
    else:
      print_ci (required_one)
      sceneFiveOptionsSeven()

def sceneFiveEnding():
    print_ci ("\nYou drag the dead body of the guard by their arms and get them on the shelfs.\n")
    time.sleep(1)
    print_ci_Ro ("\nAHHHHHH!\n\n")
    print_ci ("\nYou quickly get on top of the dead body in between the shelfs to hide.\n")
    print_ci_Ro ("\n?: WHAT’S GOING ON?\n")
    print_ci_Ro ("\n?: WHERE ARE YOU?\n")
    print_ci_Ro ("\n?: OMG WHAT IS THAT\n")
    print_ci_Ro ("\n?: JUST LEAVE IT MUST’VE EATEN THE INTRUDRES\n")
    time.sleep(1)
    print_ci ("\nThe guards rush for the exit \n")
    print_ci ("\nThrough the gaps of the shelfs you can see the shadow of a big monstrous creature moving towards\n"
              "where the exit is. It’s making sounds similar to the ones that came from Rosorus’s sword in the dream.\n"
              "The shadow is slowly getting smaller and smaller and resembling a normal human being as the fainting\n"
              "noises also get quieter and quieter.\n")
    time.sleep(2)
    print_ci_X ("\nXavier: KASER!\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: IT'S SAFE TO LEAVE NOW\n")
    time.sleep(0.5)
    sceneFiveLastChoice()

def sceneFiveLastChoice():
    print_ci ("\nWhat do you do?\n"
  """  \n1. Get out of your hiding spot\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneFiveEndingTwo()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       sceneFiveLastChoice()
    else:
      print_ci (required_one)
      sceneFiveLastChoice()

def sceneFiveEndingTwo():
    print_ci_K ("\nKaser: YE I'M HERE\n")
    time.sleep(0.5)
    print_ci ("\nYou run towards the exit and see Xavier sitting on the floor against the wall,\n"
              "crunched over and breathing heavily\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: You good?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Ye\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier One of those guys saw me and I panicked and turned into that thing again\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: It’s ok, don’t worry\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: No, It’s not. They’ll tell the principal and he’ll know it was me.\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: We’ll get away with it\n")
    time.sleep(0.5)
    print_ci ("\nYou help Xavier get up\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Like we always do\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Ye, let's get out\n\n")
    time.sleep(0.5)
    print_ci ("\nAs You and Xavier get out of the basement you’re greeted by Zane, your other friend\n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: Yo. You saw it?\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Ye\n\n")
    time.sleep(0.5)
    print_ci ("\nYou all start laughing\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: ok well I’m gonna go home over lunch but I’ll see you next lesson\n")

    print_ci_TaGreen(r'''

                                    /)
                                   //
                 __*_             //
              /-(____)           //
             ////- -|\          //
          ,____o% -,_          //
         /  \\   |||  ;       //
        /____\....::./\      //
       _/__/#\_ _,,_/--\    //
       /___/######## \/""-(\</
      _/__/ '#######  ""^(/</
    __/ /   ,)))=:=(,    //.
   |,--\   /Q...... /.  (/
   /       .Q....../..\
          /.Q ..../...\
         /......./.....\
         /...../  \.....\
         /_.._./   \..._\
          (` )      (` )
          | /        \ |
          '(          )'
         /+|          |+\
         |,/          \,/  

 ''')

    print_ci_TaCyan(r'''

              . ,
            <( .)>
             //'
            //                |||
         __//_   _,,,,,    \_///|
        /___\\  (.  __\_   \_,_/
       / Q--\'  |_o \:::)  / |
      /.(|_______)\___/___/-.|
      |  / /' \ _  ~ \_  /  /
      .---/__  """\_/""_/--'
            /\......./
           (_/_ _,,_/
            ;;;;[X];__
           /# . ._) . )-----.
          /. . . .\. /   , __>
          | . . . .\|__-( __/
           \ . . . .\   |__/
            ) .--., )  >Xxx
            //  _>)/    / X\
           (/  __/     O  X\
            / __/       \ X\
            |__/         `._\  ))
            Xxx<
            / X\
           O  X\
            \ X\
           ,,`._\,,,,, ,,

  

 ''')


    

    input("\n[Press enter to continue]")
    sceneSeven()
    
def sceneSix():
    print_ci ("\nMiss Greys: Wait, Kaser I have something for you.\n")
    time.sleep(0.5)
    print_ci ("\nMiss Grey hands you a switchblade.\n")
    time.sleep(0.5)
    print_ci ("\nMiss Grey: You know your way around weapons and fighting and you’ve been an\n"
              "excellent student the past few months so I think you should have a little gift. \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Wow thanks\n\n")
    time.sleep(0.5)
    print_ci ("\nMiss Greys: Just remember. Don’t use this weapon outside of real fights.\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Yes miss.\n\n")
    time.sleep(0.5)
    print_ci ("\nYou and Xavier make your way out of the class.\n")
    time.sleep(0.5)
    print_ci ("\nYou close the door and make your way towards the exit of the corridor until\n")

    input("\n[Press enter to continue]")

    print_ci_K ("\nKaser: Ahh!\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Ahh!\n\n")
    time.sleep(0.5)
    print_ci ("\nYou and Xavier both get grabbed by two students that were standing against the wall\n")
    time.sleep(0.5)
    print_ci_Ro ("\nHajam: Give me what miss greys gave you\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Are you joking? What sense does-\n\n")
    time.sleep(0.5)
    print_ci ("\nYou get pulled harder by the throat.\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Aahh!\n\n"
                "\nKaser: Chill!\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: You two know miss gre-\n\n")
    print_ci ("\nXavier gets hit across the back of his head.\n")
    time.sleep(0.5)
    print_ci_Ro ("\nGregory: Shut up you\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Ok I’ll give it to you just le-\n\n")
    print_ci ("\nThe guy holding Xavier gets hit across the head. Xavier gets out of the headlock and pushes Gregory.\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Zane! Let’s go. Great timing\n\n")
    time.sleep(0.5)
    print_ci ("\nYou feel Hajam releasing some pressure from you as he watches the scene play out.\n")
    sceneSixOptions()

def sceneSixOptions():
    print_ci ("\nWhat do you do?\n"
  """  \n1. Free yourself out of the headlock
  \n2. Do nothing\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_correctOneSceneSix()
    elif choice.lower().strip() in answer_two:
      option_correctTwoSceneSix()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       sceneSixOptions()
    else:
      print_ci (required_two)
      sceneSixOptions()

def option_correctOneSceneSix():
    print_ci ("\nYou grab Hajam’s forearm with both of your hands. Pull down and spin to face him. As you do that you\n"
              "twist his arm behind his back. Kick the back of his knee and make him fall while letting go of his arm\n")
    time.sleep(1.5)
    print_ci ("\nHajam and Gregory look at each other\n")

    input("\n[Press enter to continue]")
    sceneSixPartTwo()

def option_correctTwoSceneSix():
    print_ci ("\nZane grabs Gregory as Xavier rushes towards you and punches Hajam in the face. Hajam falls on his\n"
              "back as he lets go of you.\n")
    time.sleep(1.5)
    print_ci ("\nHajam and Gregory look at each other.\n")

    input("\n[Press enter to continue]")
    sceneSixPartTwo()

def sceneSixPartTwo():
    print_ci ("\nGregory attacks Zane\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Me and Zane handle the big guy you get Haram\n\n")
    
    input("\n[Press enter to continue]")
    sceneSixOptionsTwo()

def sceneSixOptionsTwo():
    print_ci ("\nWhat are you going to do?\n"
  """  \n1. light punch
  \n2. Heavy punch
  \n3. Throw switchblade at Haram's neck\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_correctThreeSceneSix()
    elif choice.lower().strip() in answer_two:
      option_correctFourSceneSix()
    elif choice.lower().strip() in answer_three:
      option_deathOneSceneSix()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       sceneSixOptionsTwo()
    else:
      print_ci (required_three)
      sceneSixOptionsTwo()

def option_deathOneSceneSix():
    print_ci ("\nYou pull out your switchblade out of your back pocket. Press the button to get the blade out and swing \n"
              "it behind your head to get momentum, you then throw it towards Haram who’s unable to dodge it as it goes \n"
              "right into his neck.\n")
    time.sleep(0.5)
    print_ci ("\nHaram bends over and starts choking and spitting blood. He gets on his knees, puts his hands on the \n"
              "switchblade and takes it out. Blood starts pouring from his neck until he eventually dies.\n")
    time.sleep(0.5)
    print_ci ("\nYou’re later caught by the school stuff and taken to the principal’s office whom gives you a life \n"
              "sentence in prison.\n")
    gameOverScreen()
    gameOverSceneSixDeathOne()

def gameOverSceneSixDeathOne():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneSixOptionsTwo()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathOneSceneSix()
    else:
      print_ci (required_three)
      option_deathOneSceneSix()

def option_correctThreeSceneSix():
    print_ci ("\nYou rush Haram and throw a quick jab at his chest. He’s unable to react and stumbles backwards\n")
    time.sleep(0.5)
    print_ci ("\nHe quickly gains control back, pulls out his sword and starts charging at you\n")
    sceneSixOptionsThree()

def sceneSixOptionsThree():
    print_ci ("\nWhat do you do?\n"
  """  \n1. Dodge his attack
  \n2. Throw your switchblade at him\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_correctFiveSceneSix()
    elif choice.lower().strip() in answer_two:
      option_deathTwoSceneSix()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       sceneSixOptionsThree()
    else:
      print_ci (required_two)
      sceneSixOptionsThree()

def option_deathTwoSceneSix():
    print_ci ("\nYou pull out your switchblade out of your back pocket. Press the button to get the blade out and swing \n"
              "it behind your head to get momentum, you then throw it towards Haram who’s unable to dodge it as it goes \n"
              "right into his neck.\n")
    time.sleep(0.5)
    print_ci ("\nHaram bends over and starts choking and spitting blood. He gets on his knees, puts his hands on the \n"
              "switchblade and takes it out. Blood starts pouring from his neck until he eventually dies.\n")
    time.sleep(0.5)
    print_ci ("\nYou’re later caught by the school stuff and taken to the principal’s office whom gives you a life \n"
              "sentence in prison.\n")
    gameOverScreen()
    gameOverSceneSixDeathTwo()

def gameOverSceneSixDeathTwo():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneSixOptionsThree()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathTwoSceneSix()
    else:
      print_ci (required_three)
      option_deathTwoSceneSix()

def option_correctFiveSceneSix():
    print_ci ("\nYou rush Haram and throw a quick jab at his chest. He’s unable to react and stumbles backwards\n")
    time.sleep(0.5)
    print_ci ("\nHe quickly gains control back, pulls out his sword and starts charging at you\n")

    input("\n[Press enter to continue]")
    sceneSixLastOptionsTwo()

def sceneSixLastOptionsTwo():
    print_ci ("\nWhat do you do?\n"
  """  \n1. Heavy punch
  \n2. Throw your switchblade at him\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_correctFourSceneSix()
    elif choice.lower().strip() in answer_two:
      option_deathLastTwoSceneSix()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       sceneSixLastOptionsTwo()
    else:
      print_ci (required_two)
      sceneSixLastOptionsTwo()

def option_deathLastTwoSceneSix():
    print_ci ("\nYou pull out your switchblade out of your back pocket. Press the button to get the blade out and swing \n"
              "it behind your head to get momentum, you then throw it towards Haram who’s unable to dodge it as it goes \n"
              "right into his neck.\n")
    time.sleep(0.5)
    print_ci ("\nHaram bends over and starts choking and spitting blood. He gets on his knees, puts his hands on the \n"
              "switchblade and takes it out. Blood starts pouring from his neck until he eventually dies.\n")
    time.sleep(0.5)
    print_ci ("\nYou’re later caught by the school stuff and taken to the principal’s office whom gives you a life \n"
              "sentence in prison.\n")
    gameOverScreen()
    gameOverSceneSixDeathLastTwo()

def gameOverSceneSixDeathLastTwo():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneSixLastOptionsTwo()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathLastTwoSceneSix()
    else:
      print_ci (required_three)
      option_deathLastTwoSceneSix()

def option_correctFourSceneSix():
    print_ci ("\nYou rush towards Haram and as you get closer, you cock your arm back.  With a mighty power, you let\n"
              "it go, and it arced forward, headed right to Haram's smug face. Your fist landed with a thud on his \n"
              "left cheek, sending ripples of fat cascading down to his ears, then back forward. He looked like a\n"
              "spitting seal.\n")
    time.sleep(0.5)
    print_ci ("\nHaram stumbled backwards till he hit the brick wall, teetering on one foot until his hulking mass \n"
              "crashed on the floor below\n")
    time.sleep(0.5)
    print_ci ("\nGregory lets go of Zane’s neck as Xavier gets off of his back. He goes pick Zane up and they both leave\n")

    input("\n[Press enter to continue]")

    print_ci_Z ("\nZane: God, I hate those guys\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Ye, we all do\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: They really thought they could take down the 'student of the month'\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Someone is jealous\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Anyways, we have a free period let’s go for lunch\n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: Did you show Kaser the…you know…\n\n")
    time.sleep(0.5)
    print_ci ("\nXavier and Zane both start laughing hysterically\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: On what type of fun did I decide to miss out?\n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: Let’s just tell him then\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Ye I guess, watching it would have been so much more fun though \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: I need to go home for lunch though\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: ok bro it’s not that long \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Aight, I’m listening\n")

    print_ci_TaGreen(r'''

                                    /)
                                   //
                 __*_             //
              /-(____)           //
             ////- -|\          //
          ,____o% -,_          //
         /  \\   |||  ;       //
        /____\....::./\      //
       _/__/#\_ _,,_/--\    //
       /___/######## \/""-(\</
      _/__/ '#######  ""^(/</
    __/ /   ,)))=:=(,    //.
   |,--\   /Q...... /.  (/
   /       .Q....../..\
          /.Q ..../...\
         /......./.....\
         /...../  \.....\
         /_.._./   \..._\
          (` )      (` )
          | /        \ |
          '(          )'
         /+|          |+\
         |,/          \,/  

 ''')

    print_ci_TaCyan(r'''

              . ,
            <( .)>
             //'
            //                |||
         __//_   _,,,,,    \_///|
        /___\\  (.  __\_   \_,_/
       / Q--\'  |_o \:::)  / |
      /.(|_______)\___/___/-.|
      |  / /' \ _  ~ \_  /  /
      .---/__  """\_/""_/--'
            /\......./
           (_/_ _,,_/
            ;;;;[X];__
           /# . ._) . )-----.
          /. . . .\. /   , __>
          | . . . .\|__-( __/
           \ . . . .\   |__/
            ) .--., )  >Xxx
            //  _>)/    / X\
           (/  __/     O  X\
            / __/       \ X\
            |__/         `._\  ))
            Xxx<
            / X\
           O  X\
            \ X\
           ,,`._\,,,,, ,,

  

 ''')

    input("\n[Press enter to continue]")
    sceneSeven()

def sceneSeven():
    print_ci ("\nYou're home\n")
    sceneSevenOptions()

def sceneSevenOptions():    
    print_ci ("\nPick an option:\n"
    """  \n1. Check backpack
    \n2. Continue\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_backpackSeven()
    elif choice.lower().strip() in answer_two:
        sceneSevenPartTwo()
    elif choice.lower().strip() == ("help"):
	    help_menuInGame()
	    sceneSevenOptions()  
    else:
     print_ci (required_two)
     sceneSevenOptions()

def option_backpackSeven():
    print ("\nIron Sword - Switchblade - [empty] - [empty]")

    time.sleep(2)
    
    sceneSevenOptionsTwo()

def sceneSevenOptionsTwo():
    print_ci ("\nPick an option:\n"
    """  \n1. Continue\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneSevenPartTwo()
    elif choice.lower().strip() == ("help"):
	    help_menuInGame()
	    sceneSevenOptionsTwo()  
    else:
     print_ci (required_one)
     sceneSevenOptionsTwo()
    
def sceneSevenPartTwo():
    print ("\n*knock*\n")
    time.sleep(0.2)
    print ("\n*knock*\n")
    time.sleep(0.5)
    print_ci ("\nMum: Go open the door, I think It’s for you\n")
    time.sleep(0.5)
    print_ci ("\nYou open the door\n"
              "\nIt's Zane and Xavier\n")
    print_ci_Z ("\nZane: Yoo, we need go school there is a meeting\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: *whispering* It’s about Rosorus\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: I'm going school mum!\n\n")
    time.sleep(0.5)
    print_ci ("\nMum: Ok go darling. Just be safe!\n")
    time.sleep(0.5)
    print_ci ("\nYou take your things and leave with Xavier and Zane\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Ok so basically there is no meeting but the king, principal or whatever you wanna call him wants to see you\n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: He said Rosorus is going to...some place and you need to get there before him\n\n")
    time.sleep(0.5)
    print_ci ("\nYou start running\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Let’s hurry then, damn\n")

    print_ci_TaYellow(r'''

              _,._      
  .||,       /_ _\\     
 \.`',/      |'L'| |    
 = ,. =      | -,| L    
 / || \    ,-'\"/,'`.   
   ||     ,'   `,,. `.  
   ,|____,' , ,;' \| |  
  (3|\    _/|/'   _| |  
   ||/,-''  | >-'' _,\\ 
   ||'      ==\ ,-'  ,' 
   ||       |  V \ ,|   
   ||       |    |` |   
   ||       |    |   \  
   ||       |    \    \ 
   ||       |     |    \
   ||       |      \_,-'
   ||       |___,,--")_\
   ||         |_|   ccc/
   ||        ccc/       
   ||                  

 ''')

    input("\n[Press enter to continue]")
    sceneSevenPartThree()

def sceneSevenPartThree():
    print_ci ("\nYou knock on the principal’s office door and wait\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: I know what you’re hoping for\n\n")
    time.sleep(0.5)
    print_ci ("\nXavier and Zane start giggling\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Stop\n\n")
    time.sleep(0.5)
    print_ci ("\nYou smile\n")
    time.sleep(0.5)
    print_ci ("\nThe principal opens the door and you see him in his fitted black suit that cleanly outlined how his arms\n"
              "and shoulders are. His face was red with veins coming out of his temples. He was in clear stress.\n")
    time.sleep(0.5)
    print_ci_P ("\nThe principal: Come in\n\n")
    time.sleep(0.5)
    print_ci ("\nYou go in first and there is one chair in front of what looked like the principal’s main desk with\n"
              "one big golden chair behind it.\n")
    time.sleep(0.5)
    print_ci_P ("\nThe principal: Don’t sit down it will be quick.\n"
                "\nThe principal: Rosorus took the Black Agate from the pit and he’s going to the caves of Jihij.\n"
                "I’ve hidden all my biggest treasures there including my sword and you can only find them if you’re part \n"
                "of our bloodline. My daughter, Rebekah, knows where that is. She’ll take you there with the white Agate.\n"
                "You should get there before him.\n\n")
    time.sleep(0.5)
    print_ci ("\nXavier and Zane look to the side as they put their hands over their mouths and can be heard giggling in \n"
              "the background. You start blushing and feeling your heart beating as your face grows hot.\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: O-Ok\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: I’ll do it\n")
    time.sleep(0.5)
    print_ci_P ("\nThe principal: I trust you. Don’t disappoint.\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: I won’t I promise\n\n")
    time.sleep(0.5)
    print_ci ("\nSuddenly the whole room starts shaking, an empty cup falls on the floor. The shelfs on the walls start to\n"
              "tremble as a roar can be heard coming from outside. Everyone is looking at the only window in the room except\n"
              "you, who’s still facing the principal as you get hotter and feel more and more sweat running down your body and face.\n")

    input("\n[Press enter to continue]")

    print_ci ("\nThe rather distinct sound of a dragon’s wings soaring through the air can be felt getting closer and closer until\n"
              "a big roar right behind you abruptly opens the window everyone was facing.\n")
    
    input("\n[Press enter to continue]")

    print_ci_P ("\nThe principal: That’s her, you better get going\n\n")
    time.sleep(0.5)
    print_ci ("\nYou turn around and there was the white agate in all of its absolutely stunning beauty and rough elegance. Her body \n"
              "was covered in white shiny scales that twisted with her body and made a soft metallic sound as they touched each other.\n"
              "Her wings were in a shape similar to a bat’s. With the ears and face features resembling those of an axolotl. On top of\n"
              "her, someone just as if not more beautiful and stunning to you, the king’s daughter, Rebekah. As you take a step forward,\n"
              "she flicks her hair and stares right into what felt like your soul. The whole world seemed to have gone quiet until Xavier\n"
              "gives you a push on your lower back and says come on.\n")
    
    time.sleep(0.5)

    print_ci_TaMagenta(r'''
                    ____                       
                 .-"    `.--.                  
              .-"            \                 
          _.-"                \                
        .'                     ;               
       /    .-" .'          \  :               
      :   .'   /             ;  ;              
      :  /    :     /      : :  ;              
       \:     ;    :       ; ;  :              
        ;     :    ;      /.'   :   ;          
        :      \   ;    .'";\    ; /;          
       .'"+._.-J`-.:   /_  : `.__;'/           
      /   : : /dB   \ :db\ ;`j.__.'            
     :     \ ; TP    `;TP : /    :             
     ;     /":"""  +   """;T      ;            
     ;    :   `.  '--'  .' :      ;            
     :    ;  :  "+.__.+";   ;     :            
      \   :  :   :    ; :   :     :            
       \   \  \ .;    :  \   \     \           
        `.__J.-"       "-.J.  `.  `-^._        
       .' /::_           :;""--.L.     "-.     
     _:_.'/:: ""--.  .---:;"     \`.      `.   
  .-" " -'--,            :;       ; \       \  
 /      .-"\:            ;:       :  ;       ; 
:   _.+"   ;;            ;:       :  :       : 
:   ; :   `;;            ;: :     ;  ;       ;


 ''')
    print_ci_TaMagenta(r"""
                                                    .%,
                                                   X:-x\',
                                                  X:/%;::\:X
                                                 X:l%  ; :'\:X
                                                X:l%   :  : '\:X
                                                X:l%   :   :  '\:X
                             b,      b,        X:/l%   :    :   \:X
                            JPQ,    JPQ,       X:l%    :     :   '\:X
                          .dP'd|._,=dPQq\     X:l%'    :      :    '\:X
                         xdP  #P"'_    _,:   .X:l%     :       :    '\:X
                      .d/"p   '  'O \  'O:;  X:l%'     :       :      \:X
                    ,pP' q.          \:  `#  X:ld       :       :      ':X
                  ,d"   ,pq  .,-qx_,  "\  `Q:  l%       :       :       k:X
                ./'     Jp       .      `  ` 3  %       :        ;      k:X
               dP       p            p    `  `q         :        :      k:X
              d/       ; J,/";xpx"\: '*q    ` `\,       :         :     l:X.
             dP      ;'    dP      "\:_,`.q. /d b\      :         :      k:X
           .d'      ;    dP            .\_j '- u-'      :         :      k:X
X         ./'     ;'    /"            .'                :         ;      k:X
\X       .d'     ;    ,"             :      X:l%        :        :       k:X
:\X      d'     ;   ./'             :       X:/%        :        ;       k:X
::lX    JP     ;    J              :      .X:/ %        :       :        k;X
k:lX    #'    :    j'             :    .X:/ %           :       :       d:lX
k:lX   |P    ;     |             :  .X:/ %              :       ;       k;lX
k:lX   ||    ;    |'            : X:/ %                 ;       :      d:;X'
k:lX   d|   ;     :l           :X:/ %'                 :        :      k:lX
k:iX   #|   ;     ||          X:/ %                    ;        ;      k:lX
 k:\X  ||  ;       ||       X:/ %                     :        :       k:lX
  k:\pQJb  ;        \N.PQ XX/ %                      ;         ;       k:lX
   kJP.Ql\;          XQ. J Q J                      :         ;        k:lX
   6Q : Q%           \Q  Q   J              ;''''':.:;''::.  :         k:lX
  6QQ  : Ql           lQ'   J              ;        ;     ': :;''':.   k::X.
 6QQQ )  Ql           i6    Q             ;                 .;     ':.  k:\X
  6QQ   J l           \  6  Q            ;                            ':.k:X
 9QQ   J  i            l 6   6          ;                                 k;

 """)

    input("\n[Press enter to continue]")

    print_ci_Z ("\nZane: Ugh, I hate these things.\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Yeah, well you don’t have another choice other than getting on.\n\n")
    time.sleep(0.5)
    print_ci ("\nZane looks at Rebekah\n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: Anyways, what are you doing here?\n\n")
    time.sleep(0.5)
    print_ci ("\nRebekah ignores him and doesn't even look at him\n")
    time.sleep(0.5)
    print_ci ("\nYou and Xavier start laughing\n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: She really just aired me yikes\n\n")
    time.sleep(0.5)
    print_ci ("\nXavier gets on the creature first, then he helps Zane get on it. As they look for where to sit, they look at you as\n"
              "you’re getting on the dragon. Xavier’s eyes and body language were clearly inviting you to move forward so you could \n"
              "sit behind Rebekah as the back of the creature was wide enough to sit comfortably and stably but not enough to sit next\n"
              "to somebody else.\n")
    time.sleep(0.5)
    sceneSevenOptionsLast()

def sceneSevenOptionsLast():
    print_ci ("\nWhat do you do?\n"
    """  \n1. Sit behind her
    \n2. Sit behind Xavier and Zane\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_extra()
    elif choice.lower().strip() in answer_two:
        sceneSevenEnding()
    elif choice.lower().strip() == ("help"):
	    help_menuInGame()
	    sceneSevenOptionsLast()  
    else:
     print_ci (required_two)
     sceneSevenOptionsLast()

def option_extra():
    print_ci ("\nAs you sit down the white Agate quickly takes altitude and starts flying east.\n")
    time.sleep(1)
    print_ci ("\n*Awkward silence*\n")
    time.sleep(1)
    print_ci ("\nYou can hear Xavier do a face palm and while laughing say:\n")
    print_ci_X ("\nXavier: Man, I’m dead\n\n")
    time.sleep(0.5)
    print_ci ("\nYou feel pretty uncomfortable and awkward until Rebekah turns around\n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: Hi, what’s your name\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: I'm Kaser\n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: I’m Rebekah, are you British British?\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: nah, I’m Lithuanian\n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: We should get a portrait painted together one day\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: A portrait?\n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: Ye, so you can look at my beautiful face every night before falling asleep\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: haha ye, let’s just make sure we get a good artist so the painting isn’t blurry\n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: Ye, so definitely not my brother\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: He paints?\n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: Kind of…mmm anyways…\n\n")
    time.sleep(0.5)
    print_ci ("\nRebekah looks at Zane\n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: You look so innocent\n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: what\n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: The way you dress and sit, I don't know...It's just bad\n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: bruh what?\n")
    sceneEight()

def sceneSevenEnding():
    print_ci ("\nAs you sit down the white Agate quickly takes altitude and starts flying east.\n")
    time.sleep(1)
    sceneEight()

def sceneEight():
    print_ci ("\nThe dragon started to gain more and more speed after it was eventually going so fast that you couldn't talk or her anyone.\n"
              "You couldn't distinguish anything you was flying by. It was all just a mess of unrecognisable colours and sounds. After 2 minutes like\n"
              "this you start to slow down and everything is back to normal.\n"
              "\nYou are now above an ocean and can see an island in front of you with a bunch of tall mountains\n")
    print_ci_TaRed(r'''


   .......::::::::::::)..           .......................(::::::........
      .:::::;;;;;;;;):::::::.... .           .......:::::::::::::<......
          <  >>>                   ,.
  .::..  ;   I;L\  /L\.  ..::..   /iL.           |         ..::::::::::::..
        ;    II;L\/LLLL;         / I;L\    \     |     / /\_   
             II;..LLLLLL\    _._/ I;:.L\     \   |   / _/J; \    
      :     IIIIi;..LLLLL\__/   IIII:..L\____  \###/  /JJI:  \
    ,;     ILIi;;;:...:LLL;\      IIIII;.LLLLL\#####/JJ II;   \
   ;     I LLii;;;.:.. :LLL;\     III;;;::LLLLL\###/JJ IIII;   \_.
  :     IIILiii;;::.... :LLL;|      ;;I;;::.:LLLLLL:;IJ IIIII;:   \__.

           IIIII IIii;;::;..;\          ;;:::...LLLL;IJIII;;    :::   \
:    ;    IIIIIIIIIii;;::.;..      _==|      ;..  :;IJIII;:::    ::    \
    ;    ::::::::::::;;::..;  _==|   )__)  |                            \
 "  ""  "  """"""""  """"  ""    )_)  )___) ))  """""   """"  """ """"""  """"
        """   ""^^       ^~   )___) )____))_)   ~~         ""^^^""  "  "  "~"
" ^^            ^        _    )____)_____))__)\      ~^~~^           ^^"
     "^^          ^~      \---__|____/|___|___-\\--        "~"~         "~"
   ""    "^          ~"~   \   oo oo oo oo     /      ~"      "~       ""~"
        ____   ^^^"~   ~~^^^^^^^^^^^^^^^^^^^^^^    ^~^            ^~^^^
      /  o   \     """"  __          __ """""     "   ""~     ~""~"`    """"
    < ____     \"""    /    \   "" /    \       _          _    "~    _
          |     |     |  __  |    |  __  |    /   \      /   \       / |
    """   |_____|  "  |__||__| "" |__||__| " |_____| "" |_____| ""  /_/
         """     ~^^^^      """"^^"""""^        """""""""        """""^^""
   ""          "^^           ~^^~          ~^ "      ~~      "  ^   ^^^^^^^^


 ''')
    input("\n[Press enter to continue]")
    
    print_ci_R ("\nWe're here\n")
    time.sleep(0.5)
    print_ci ("\nYou all get off the dragon and Rebekah leads the way to the entrance.\n")
    time.sleep(0.5)
    print_ci ("\nThe whole island was made out of rock. There wasn’t any other colour but black with some purplish cracks in certain places.\n"
              "The entrance to the cave was about as big as a plane and was in a slight decline that got progressively steeper.\n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: 'Litmus'\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: 'Litmus'\n\n")
    time.sleep(0.5)
    print_ci ("\nAfter a few minutes of walking you go through a decently sized passage in the wall that leads you to an open circled area\n"
              "with rocks of all sizes in what seemed like random patterns and a bunch of small lakes in random places. The wall were as \n"
              "uneven as they could be with bumps of all sizes and length coming out of every spot.\n")
    print_ci_R ("\nRebekah: Make yourselves comfortable while I find the way to my father’s possessions.\n\n")
    time.sleep(0.5)
    print_ci ("\nYou, Xavier and Zane go sit on some rocks far enough from Rebekah so she can’t hear you\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: ok, so…you need to do something to mmm…impress her?\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: What?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Bro. Like flirt I don’t know\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: No, like now?? We’re trying to save the world and you’re talking about how I need to pull her\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Bro stop stressing. Look how relaxed she is. She won’t mind\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Wasn’t she a hoe though?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: You still like her though. Come on bro let’s do something\n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: how about you get her a drink?\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: And where am I gonna pull that from, We’re in some dead cave in the middle of no where\n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: that vending machine right there\n\n")
    time.sleep(0.5)
    print_ci ("\nZane, who was sitting on the left side, points across to the right\n")
    time.sleep(0.5)
    print_ci ("\nYou turn around to look\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: what? Ok that doesn’t make any sense wh-\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: bro shut up. Let’s go\n\n")
    time.sleep(0.5)
    print_ci ("\nYou all walk towards the vending machine\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: ok so C9 is Coca Cola.\n\n")
    time.sleep(0.5)
    print_ci ("\nYou type in C9 in the vending machine\n")
    time.sleep(0.5)
    print_ci ("\nA Coca-Cola bottle comes out and you pick it up\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: When you give it to her be like “Where’s my hug”\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Unless she hugs me first haha\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: *slowly* ye…\n")
    time.sleep(0.5)
    print_ci_Z ("\nLet me get something\n\n")
    time.sleep(0.5)
    print_ci ("\nZane starts giggling\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: What’s funny?\n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: Don't worry\n\n")
    time.sleep(0.5)
    print_ci ("\nZane types in a code\n")
    time.sleep(0.5)
    print_ci ("\nThe machine gets stuck\n")
    time.sleep(0.5)
    print_ci ("\nA thunder is heard through the cave\n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: *shouting* Are you guys ok?\n\n")
    time.sleep(0.5)
    print_ci ("\nAll three at the same time: *shouting* Yeah\n")
    time.sleep(0.5)
    print_ci ("\nA wall near by breaks and three Gollexs come out along with what looked like 2 flying Lexins\n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: Really?\n\n")
    time.sleep(0.5)
    print_ci ("\nHe quickly shakes the machine and you see a red bull come out as he picks it up.\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Since when can they fly?\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: No idea. You get the flying fucks and we deal with the Gollexs\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Gosh…ok\n")
    print_ci_TaRed(r'''


             \                  /
    _________))                ((__________
   /.-------./\\    \    /    //\.--------.\
  //#######//##\\   ))  ((   //##\\########\\
 //#######//###((  ((    ))  ))###\\########\\
((#######((#####\\  \\  //  //#####))########))
 \##' `###\######\\  \)(/  //######/####' `##/
  )'    ``#)'  `##\`->oo<-'/##'  `(#''     `(
          (       ``\`..'/''       )
                     \""(
                      `- )
                      / /
                     ( /\
                     /\| \
                    (  \
                        )
                       /
                      (
                      `    

 ''')
    input("\n[Press enter to continue]")
    sceneEightOptions()

def sceneEightOptions():
    print_ci ("\nOne of the flying Lexins opens their mouth and a sharp purple blade in the shape of a cone comes out\n"
              "as the creature charges at you full speed\n"
              "\nWhat do you do?\n"
  """  \n1. Dodge
  \n2. Light sword swing
  \n3. Heavy sword swing
  \n4. Throw switchblade\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      pathOne()
    elif choice.lower().strip() in answer_two:
      option_deathOneSceneEight()
    elif choice.lower().strip() in answer_three:
      option_deathOneSceneEight()
    elif choice.lower().strip() in answer_four:
      pathTwo()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       sceneEightOptions()
    else:
      print_ci (required_four)
      sceneEightOptions()

def option_deathOneSceneEight():
    print_ci ("\nYou’re too slow to take your sword out and the Lexin’s sharp tongue goes right through the middle \n"
              "of your chest as you slowly lose air and blood and die.\n")
    time.sleep(0.5)
    print_ci ("\nYour friends are not able to take out the demons themselves and they die too.\n")
    gameOverScreen()
    gameOverSceneEightDeathOne()

def gameOverSceneEightDeathOne():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneEightOptions()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathOneSceneEight()
    else:
      print_ci (required_three)
      option_deathOneSceneEight()

def pathOne():
    print_ci ("\nAs the Lexin gets closer to you, you’re able to dodge his sharp tongue last second and\n"
              "you’re now facing his back.\n")
    sceneEightOptionsTwo()

def sceneEightOptionsTwo():
    print_ci ("\nThe other flying Lexin is now charging at you full speed from the other side\n"
              "\nWhat do you do?\n"
    """  \n1. Attack Lexin charging at you
    \n2. Attack other Lexin\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_Lexin()
    elif choice.lower().strip() in answer_two:
        option_otherLexin()
    elif choice.lower().strip() == ("help"):
	    help_menuInGame()
	    sceneEightOptionsTwo()  
    else:
     print_ci (required_two)
     sceneEightOptionsTwo()

def option_Lexin():
    print_ci ("\nWhat do you do?\n"
  """  \n1. Dodge
  \n2. Light sword swing
  \n3. Heavy sword swing
  \n4. Throw switchblade\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_deathTwoSceneEight()
    elif choice.lower().strip() in answer_two:
      option_deathThreeSceneEight()
    elif choice.lower().strip() in answer_three:
      option_deathThreeSceneEight()
    elif choice.lower().strip() in answer_four:
      option_correctOneSceneEight()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_Lexin()
    else:
      print_ci (required_four)
      option_Lexin()

def option_deathTwoSceneEight():
    print_ci ("\nYou manage to dodge the attack of the Lexin charging at you full speed but now the\n"
              "other Lexin is back on you and you’re unable to handle them both at the same time as\n"
              "you get overpowered and die.\n")
    time.sleep(0.5)
    print_ci ("\nYour friends are not able to take out the demons themselves and they die too.\n")
    gameOverScreen()
    gameOverSceneEightDeathTwo()

def gameOverSceneEightDeathTwo():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_Lexin()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathTwoSceneEight()
    else:
      print_ci (required_three)
      option_deathTwoSceneEight()

def option_deathThreeSceneEight():
    print_ci ("\nYou’re too slow to take your sword out and the Lexin’s sharp tongue goes right through the middle \n"
              "of your chest as you slowly lose air and blood and die.\n")
    time.sleep(0.5)
    print_ci ("\nYour friends are not able to take out the demons themselves and they die too.\n")
    gameOverScreen()
    gameOverSceneEightDeathThree()
    
def gameOverSceneEightDeathThree():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_Lexin()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathTwoSceneEight()
    else:
      print_ci (required_three)
      option_deathTwoSceneEight()

def option_correctOneSceneEight():
    print_ci ("\nAs the Lexin is rushing you at full speed you whip out your switchblade, cock it back as you \n"
              "press the button to push the blade out and throw it towards the Lexin.\n")
    time.sleep(0.5)
    print_ci ("\nThe switchblade goes straight in between the Lexin’s eyes as he quickly loses altitude until \n"
              "he violently hits the floor and keeps sliding towards you up to your feet as the purplish cracks \n"
              "on his body were slowly losing light as if the creature’s battery was running out.\n")
    time.sleep(0.5)
    print_ci ("\nThe other Lexin is about to attack you from behind before he gets crushed by the remaining’s of\n"
              "one of the Gollex’s Zane and Xavier were fighting\n")
    time.sleep(0.5)

    input("\n[Press enter to continue]")
    sceneEightTwo()

def option_otherLexin():
    print_ci ("\nWhat do you do?\n"
  """  \n1. Light sword swing and dodge Lexin charging at you
  \n2. Heavy sword swing and dodge Lexin charging at you
  \n3. Throw switchblade and dodge Lexin charging at you\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_deathFourSceneEight()
    elif choice.lower().strip() in answer_two:
      option_deathFiveSceneEight()
    elif choice.lower().strip() in answer_three:
      option_correctTwoSceneEight()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_otherLexin()
    else:
      print_ci (required_three)
      option_otherLexin()

def option_deathFourSceneEight():
    print_ci ("\nYou whip out your sword, rush at the Lexin with his back facing you and cut right through him as\n"
              "your sword comes out of his chest on the other side.\n")
    time.sleep(0.5)
    print_ci ("\nYou try to take your sword out but it’s stuck. You try again but you’re too slow to take your sword\n"
              "out and the other Lexin’s sharp tongue goes right through the middle of your chest as you slowly lose\n"
              "air and blood and die.\n"
              "\nYour friends are not able to take out the demons themselves and they die too.\n")
    gameOverScreen()
    gameOverSceneEightDeathFour()

def gameOverSceneEightDeathFour():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_otherLexin()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathFourSceneEight()
    else:
      print_ci (required_three)
      option_deathFourSceneEight()

def option_deathFiveSceneEight():
    print_ci ("\nYou whip out your sword, rush at the Lexin with his back facing you and jump as high as you can to\n"
              "be above it. You point your sword downwards and penetrate through the top of the Lexin’s skull. The sword\n"
              "keeps going deeper until the handle is touching the demon’s head and you land with your feet on the back\n"
              "of the, now dead, enemy.\n")
    time.sleep(0.5)
    print_ci ("\nYou try to take your sword out but it’s stuck. You try again but you’re too slow to take your sword\n"
              "out and the other Lexin’s sharp tongue goes right through the middle of your chest as you slowly lose\n"
              "air and blood and die.\n"
              "\nYour friends are not able to take out the demons themselves and they die too.\n")
    gameOverScreen()
    gameOverSceneEightDeathFive()

def gameOverSceneEightDeathFive():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_otherLexin()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathFiveSceneEight()
    else:
      print_ci (required_three)
      option_deathFiveSceneEight()

def option_correctTwoSceneEight():
    print_ci ("\nYou whip out your switchblade. As you press the button to get the blade out you cock it back and throw it\n"
              "at the back of the Lexin’s head. He falls on the ground clearly dead. You quickly turn around and see the\n"
              "other Lexin charging full speed at you. You’re able to dodge it’s attack last second.\n")
    time.sleep(0.5)
    print_ci ("\nYou’re now facing the back of the Lexin\n")
    time.sleep(0.5)
    sceneEightOptionsThree()

def sceneEightOptionsThree():
    print_ci ("\nWhat do you do?\n"
    """  \n1. Light sword swing
    \n2. Heavy sword swing\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_light()
    elif choice.lower().strip() in answer_two:
        option_heavy()
    elif choice.lower().strip() == ("help"):
	    help_menuInGame()
	    sceneEightOptionsThree()  
    else:
     print_ci (required_two)
     sceneEightOptionsThree()

def option_light():
    print_ci ("\nYou whip out your sword, rush at the Lexin with his back facing you and cut right through him as your sword\n"
              "comes out of his chest on the other side.\n")
    time.sleep(0.5)
    print_ci ("\nWith some struggle you manage to get your sword out of the Lexin’s dead body\n")
    time.sleep(0.5)

    input("\n[Press enter to continue]")
    sceneEightTwo()

def option_heavy():
    print_ci ("\nYou whip out your sword, rush at the Lexin with his back facing you and jump as high as you can to be above it.\n"
              "You point your sword downwards and penetrate through the top of the Lexin’s skull. The sword keeps going deeper\n"
              "until the handle is touching the demon’s head and you land with your feet on the back of the, now dead, enemy.\n")
    time.sleep(0.5)
    print_ci ("\nWith some struggle you manage to get your sword out of the Lexin’s dead body\n")
    time.sleep(0.5)

    input("\n[Press enter to continue]")
    sceneEightTwo()
              
def pathTwo():
    print_ci ("\nAs the Lexin is rushing you at full speed you whip out your switchblade, cock it back as you press the button\n"
              "to push the blade out and throw it towards the Lexin.\n")
    time.sleep(0.5)
    print_ci ("\nThe switchblade goes straight in between the Lexin’s eyes as he quickly loses altitude until he violently hits the\n"
              "floor and keeps sliding towards you up to your feet as the purplish cracks on his body were slowly losing light as if\n"
              "the creature’s battery was running out.\n")
    time.sleep(0.5)
    sceneEightOptionsFour()

def sceneEightOptionsFour():
    print_ci ("\nThe other Lexin is now charging at you\n"
              "\nWhat do you do?\n"
  """  \n1. Dodge
  \n2. Light sword swing
  \n3. Heavy sword swing\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_correctLastSceneEight()
    elif choice.lower().strip() in answer_two:
      option_deathLastSceneEight()
    elif choice.lower().strip() in answer_three:
      option_deathLastSceneEight()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_otherLexin()
    else:
      print_ci (required_three)
      option_otherLexin()

def option_deathLastSceneEight():
    print_ci ("\nYou’re too slow to take your sword out and the Lexin’s sharp tongue goes right through the middle \n"
              "of your chest as you slowly lose air and blood and die.\n")
    time.sleep(0.5)
    print_ci ("\nYour friends are not able to take out the demons themselves and they die too.\n")
    gameOverScreen()
    gameOverSceneEightDeathLast()
    
def gameOverSceneEightDeathLast():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneEightOptionsFour()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathLastSceneEight()
    else:
      print_ci (required_three)
      option_deathLastSceneEight()

def option_correctLastSceneEight():
    print_ci ("\nAs the Lexin gets closer to you, you’re able to dodge his sharp tongue last second and you’re now facing his back.\n")
    time.sleep(0.5)
    sceneEightOptionsFive()

def sceneEightOptionsFive():
    print_ci ("\nWhat do you do?\n"
    """  \n1. Light sword swing
    \n2. Heavy sword swing\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_correctLastTwoSceneEight()
    elif choice.lower().strip() in answer_two:
        option_correctLastThreeSceneEight()
    elif choice.lower().strip() == ("help"):
	    help_menuInGame()
	    sceneEightOptionsFive()  
    else:
     print_ci (required_two)
     sceneEightOptionsFive()

def option_correctLastTwoSceneEight():
    print_ci ("\nYou whip out your sword, rush at the Lexin with his back facing you and cut right through him as your sword comes\n"
              "out of his chest on the other side.\n")
    time.sleep(0.5)
    print_ci ("\nWith some struggle you manage to get your sword out of the Lexin’s dead body\n")

    input("\n[Press enter to continue]")
    sceneEightTwo()

def option_correctLastThreeSceneEight():
    print_ci ("\nYou whip out your sword, rush at the Lexin with his back facing you and jump as high as you can to be above it.\n"
              "You point your sword downwards and penetrate through the top of the Lexin’s skull. The sword keeps going deeper until\n"
              "the handle is touching the demon’s head and you land with your feet on the back of the, now dead, enemy.\n")
    time.sleep(0.5)
    print_ci ("\nWith some struggle you manage to get your sword out of the Lexin’s dead body\n")

    input("\n[Press enter to continue]")
    sceneEightTwo()

def sceneEightTwo():
    print_ci_Z ("\nZane: Help us, we only got 2 left!\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: AHHHH!\n\n")
    time.sleep(0.5)
    print_ci ("\nOne of the Gollex’s grabs Xavier by the neck with his right hand and starts choking him.\n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: Save Xav, I’ll get the other Gollex!\n")
    time.sleep(0.5)
    sceneEightTwoOptions()

def sceneEightTwoOptions():
    print_ci ("\nWhat do you do?\n"
  """  \n1. Light sword swing
  \n2. Heavy sword swing
  \n3. Sword frisbee throw\n""")
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      option_deathSceneEightTwo()
    elif choice.lower().strip() in answer_two:
      option_correctOneSceneEightTwo()
    elif choice.lower().strip() in answer_three:
      option_correctTwoSceneEightTwo()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       sceneEightTwoOptions()
    else:
      print_ci (required_three)
      sceneEightTwoOptions()

def option_deathSceneEightTwo():
    print_ci ("\nYou rush towards the Gollex. As you get within reach you swing your sword and hit his leg.\n")
    time.sleep(0.5)
    print_ci ("\nThe hit does not bother the Gollex at all. He grabs you with his other hand and strangles both\n"
              "of you and Xavier to death.\n"
              "\nZane is not able to take out the remaining demons by himself and he dies too.\n")
    gameOverScreen()
    gameOverSceneEightTwoDeath()
    
def gameOverSceneEightTwoDeath():
    choice = input("\nYour choice: ")
    if choice.lower().strip() in answer_one:
      sceneEightTwoOptions()
    elif choice.lower().strip() in answer_two:
      sceneOne()
    elif choice.lower().strip() in answer_three:
      sys.exit()
    elif choice.lower().strip() == ("help"):
       help_menuInGame()
       option_deathSceneEightTwo()
    else:
      print_ci (required_three)
      option_deathSceneEightTwo()

def option_correctOneSceneEightTwo():
    print_ci ("\nYou take a step back and sprint towards the Gollex as fast as you can. When you get close enough you jump on his\n"
              "left shoulder. Jump again and while in the air you point your sword downwards and horizontally penetrate through\n"
              "the Gollex’s shoulder which causes his arm to fall off and you land right next to his foot.\n")
    time.sleep(0.5)
    print_ci ("\nThe Gollex screams in Agony and lets Xavier go while falling on his back.\n")
    time.sleep(0.5)
    print_ci ("\nXavier lands and immediately jumps on the Gollex’s stomach and opens his core. He puts his hands inside it and \n"
              "starts absorbing the energy from the Gollex as the creature shakes as if it was having a seizure. The purplish cracks\n"
              "on the demon’s skin are getting darker and darker until they were pitch black and the Gollex stopped shaking.\n")
    time.sleep(0.5)
    print_ci ("\nParts of the Gollex Zane was fighting come flying in your direction as you see him land from a jump after what seemed\n"
              "like destroying the demon’s core.\n")

    input("\n[Press enter to continue]")
    sceneEightThree()

def option_correctTwoSceneEightTwo():
    print_ci ("\nYou cock your sword back and throw it as hard as you can towards the Gollex. You hit his elbow without making much\n"
              "damage but he loosens the grip over Xavier’s neck, whom manages to take advantage by getting himself out of the choke.\n")
    time.sleep(0.5)
    print_ci ("\nAs he’s landing on the ground, he extends his arms out towards the demon and purple and dark coloured light beams come\n"
              "out of each one of his arms.\n")
    time.sleep(0.5)
    print_ci ("\nThe beams hit the middle of the Gollex’s chest and before you’re able to realise what happened the creature explodes in\n"
              "thousands of pieces.\n")
    time.sleep(0.5)
    print_ci ("\nParts of the Gollex Zane was fighting come flying in your direction as you see him land from a jump after what seemed\n"
              "like destroying the demon’s core.\n")

    input("\n[Press enter to continue]")
    sceneEightThree()

def sceneEightThree():
    print_ci_Z ("\nZane: And that’s the last one\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: ye…Kaser your sword is broken\n"
                "\nXavier: in half\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: ye…\n\n")
    time.sleep(0.5)
    print_ci ("\nRebekah starts walking towards you and your friends\n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: You guys are good at this\n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Did you just watch all of that and decided not to help us?\n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: I was ehm…protecting this stuff, anyways…Kaser…\n")
    time.sleep(0.5)
    print_ci ("\nShe puts the chest down, opens it and gets an absolutely prestigious looking sword in a white and gold scabbard.\n"
              "very similiar to the one in your dream\n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: This is for you\n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Thank you\n")
    time.sleep(0.5)
    print_ci ("\nAs you grab the handle you can feel the absolutely high-quality material the sword was made of.\n"
              "It was surprisingly lighter than your older sword.\n")
    time.sleep(0.5)
    print_ci ("\nYou detach your old scabbard and put the new one on. \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: I got something for you \n")
    time.sleep(0.5)
    print_ci ("\nYou pull out the Coca-Cola bottle out of your pocket and extend your arm in front of her. \n")
    time.sleep(0.5)
    print_ci ("\nShe gets happy and takes it and as you’re about to say something she extends her arms around you and hugs you\n"
              "around your neck. You do the same thing; you hug her around her neck… \n")
    time.sleep(0.5)
    print_ci ("\nYou get excited and for some reasons a quiet “thank you” comes out of your mouth. You really hope that no one\n"
              "heard that, especially Rebekah. \n")
    time.sleep(0.5)
    print_ci ("\nAs you let go of each other Zane gets closer to her and pulls out his Red-Bull \n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: I got you a better drink \n")
    time.sleep(0.5)
    print_ci ("\nEveryone laughs and giggles a little except you… \n")
    time.sleep(0.5)
    print_ci ("\nRebekah clearly gets happy and excited as she sees the drink. \n")
    time.sleep(0.5)
    print_ci ("\nShe takes it \n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: I guess I have to hug you as well now \n")
    time.sleep(0.5)
    print_ci ("\nShe hugs Zane \n")
    time.sleep(0.5)
    print_ci ("\nYou watch, quite confused on what just happened but too happy about the hug to process anything as you fell your\n"
              "heart pound violently against your chest.  \n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: Ok well, we can go now…. \n")
    time.sleep(0.5)
    print_ci ("\nRebekah goes in front and you three stay far back enough from her to be able to talk without her hearing you. \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Sooo, how do you feel? \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Bro, it’s just a hug. How much of a virgin do you think I am? \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Stop with the cap, let me feel your heart \n")
    time.sleep(0.5)
    print_ci ("\nXavier puts his hand on your chest \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: brooo, there’s a whole party going on in there. Man never got a hug from a girl hahah \n")
    time.sleep(0.5)
    print_ci ("\nZane feels your chest too and starts laughing \n")
    time.sleep(0.5)
    print_ci ("\nXavier: Bro you get no girls either hahah. That’s probably like your first time ever haha. Virginity duo out here \n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: Chill, damn. It’s not that deep. \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Ok now. Zane what the fuck was that? \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Ye. Exactly what was that red bull shit uh? \n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: just a prank chill damn \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: That was meant to be Kaser’s moment like why would you do that? \n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: Cause it would have been funny \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Can’t lie it was but like…You literally cockblocked him \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Oh my god now it sounds 1000 times worse \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: imagine getting cockblocked by Zane hahaha \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Also, why did you have to slide that better drink bulshit in there. It’s all subjective \n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: That’s her favourite drink \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: And how do you know? \n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: Rosorus told me \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: What? No\n")
    time.sleep(0.5)
    print_ci_K ("Kaser: I’m out here getting set up to fail bruh \n")
    time.sleep(0.5)
    print_ci ("\nAs you start to see light at the end of the cave. From behind you, you hear a dragon’s growl so evil and disturbing\n"
              "that you all cover your ears and duck \n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: What was that? \n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: That’s Rosorus… \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Was that the Bl- \n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: Please not another one of those flying wankers \n")
    time.sleep(0.5)
    print_ci ("\nThe sound of a pair of wings violently thrusting through the air gets everyone’s attention. It’s quickly getting closer\n"
              "and closer and before you know it a dragon with the devilish looks is coming at you from behind. His skin was covered in \n"
              "the toughest black scales you had ever seen with a purplish light glowing in between every scale. Before you’re able to\n"
              "pick out any other detail he flies above you and a black smoke is released from its skin. \n")

    print_ci_TaRed(r"""


                                              ,....,.
                                          ..''   .'
                                       .''       |
                                    .''          \
                                 .''              \.
                               .'                  .'.,
                             ,:'             ..,'''   '...,..::/''.....
                           /''          .,'''  .,',:,''''         .,''
                         ,'.'      .,''' ..,''' ''         .'   .''
                       ,'  \, ..,''  .,''. ..,'''        ./   .'
                     .'     .,'  .,''.,''./           ..''   /
                    ,'    .'  ./'.,''  .'  ''     .' '.     /
                  .'   ./' ./'.'\,..,''     '' ../,     ,  |
                 ,   ./' .'./'|/     ............        ',|
                /   /' ,'.'.,'''\..... ''''''''''  .::/'.., |
               /  .' ,' ':\ '''  |  ,      ''          '''   \
              /  /'.''. |:::::::''' ,' ' ''. '.,.,  ''''    .''
             | .' /.,':. ''..,   '\'..''..  ;''  '\.''''  .'
             | \.:\.    '''./\ \  | ' '' .,''.           /
             / \'   ''..     ', \  \,',     ''..  .,     '
            /.'',''..,  '\,   '\ '. '\'.,     , ''. ''.,|
           .,'        ''. ',    \ '.'.. ''../'      '' __\
           '             \,',    \  '.'\..,  ',''  .''
                         |  |    '| ,\'''\/.  |  .'
            .'          .|  .    / / ./'. '.'.' /'
            /'        ..|':'''\././  /   '  '/\.'
           //  ./  .''    /' ./'.' .'  | ..,  ':|
         ./:  ,/   |',   ' .''  :  '   |    .../:,
        .'.'.\/   /.'           ''  .,   ..\'
      .,\.\'.'   /'    ,'' \...,      '\.\| ',
     /    ./'''''   ..:    ',|  ''.,     '\  ',
  .,' ''   \|     ''.''.    '/  .| '\.     ', '\
 /          \.    ../,   './ '\ |'  \/'' ''.'\  \
/   '\\:.   \,'\::'  ./'''    ./|  .'     .''/| '|
' ,'\:'/'''  /'  .'\'  .., |:| .| |'    .'' .\|  ',
|/  / /'    .'| /  |. \,    /''/. |  |:\..,' .||  \
'' /.'      //\|'  '\/\:.   :,/''::.  ,   ..::'|  |
            ||'/,    '\\/'\ '/|    '\ ''::::'| || .
            || \\       ''.   ...,  '.  \\...| |' |
            ||  '\,         .'.\, '. ', | \  '||  |
             '              |\|'|\/.''\ | |\  ||  |
                            ||\/'/| '\, ., / / /  ,
                             ' \  '   ''  / / .' /
                                '      .''.' .' /
                                  ..'''..' .' .'
                              .,'':.'''..'' .'
                         .,:'''''  .''  ..''
                       .' .''..'''...,''
                    ..' '    , '''
                   /  . :/''
                 .'  :/'
                /  /'
               / .'
              / '
             /.'
             '


 """)

    input("\n[Press enter to continue]")
    
    print_ci ("\nEverything is pitch black, you start coughing and you hear your friends cough too. Your legs start to tremble and the feeling \n"
              "moves up to your head until all of your body is shaking and you fall down on your side. \n")
    time.sleep(1)
    print_ci ("\nYou’re slowly closing your eyes until you hear a scream come from the exit of the cave. It was Rebekah. You feel a sharp pain \n"
              "go through your heart as you get goosebumps all through your body. Your blood boils as hard as it ever has. You try to get up \n"
              "but you just can’t. \n")
    time.sleep(2)
    print_ci ("\nYou feel someone put their hands on your shoulder. It felt like Xavier, he turns you on your back and puts both of his hands on\n"
              "your chest. You feel an incredible amount of power and energy flow through every single particle of your body as you quickly get \n"
              "more and more energy. You open your eyes and have full vision. You see Xavier with his hands on your chest before he falls down \n"
              "on his hip. A few meters away Zane was laying down, unconscious. \n")
    time.sleep(1)
    print_ci ("\nXavier starts speaking in a quiet, rough and slow tone as if he had just gotten 50 years older. \n")
    time.sleep(0.5)
    print_ci_Xs ("\nXavier: Go, save her, we’ll be fine. \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: I’m not leaving you. \n")
    time.sleep(0.5)
    print_ci ("\nYou try to pick Xavier up but he starts moving away from you and trying to stop you from helping him up. \n")
    time.sleep(0.5)
    print_ci_Xs ("\nXavier: Just go, you don’t have time, I think he’s going to the gates of Hellheim. \n")
    time.sleep(0.5)
    print_ci ("\nGoosebumps go through your body once again, you let Xavier go and sprint towards the exit. \n")
    time.sleep(1.5)
    print_ci ("\nThe white Agate was still there but its neck was wrapped with a purple braided chain connected to what seemed like nothing \n"
              "in the middle of the air. \n")
    time.sleep(0.5)
    print_ci ("\nYou take out your new sword out of your scabbard and cut the chain. \n")
    time.sleep(0.5)
    print_ci ("\nYou get on the dragon who quickly takes off and starts flying and gaining speed.  \n")
    time.sleep(0.5)
    print_ci ("\nYou’re going faster and faster until you literally can’t distinguish anything around you \n")
    sceneNine()

def sceneNine():
    time.sleep(0.5)
    print_ci ("\nAfter about 15 seconds at this supersonic speed, you start feeling slightly dizzy but instantly remember what’s at stake.\n"
              "You shake your head as you try to get back to a normal state. Thankfully the dragon starts slowing down and you see the\n"
              "Black Agate with Rosorus on top \n")
    time.sleep(1.5)
    print_ci ("\nEverything plays out just like in the dream.  \n")
    time.sleep(1.5)
    print_ci ("\nYou get on top of his dragon. \n")
    time.sleep(1.5)
    print_ci ("\nYou land on the patio with the gates of Hellheim. \n")
    time.sleep(1.5)
    print_ci ("\nYou challenge Rosorus to a sword fight. \n")
    time.sleep(1.5)
    print_ci ("\nYou leave him unconscious. \n")
    time.sleep(1.5)
    print_ci ("\nYou carry Rebekah back on the White Agate. \n")
    time.sleep(1.5)
    print_ci_TaRed(r"""

                          (,);    /\                        
                         ((  ^_   ||            ...         
                          ' /  \  ||           (()))        
                            L {=) ||           {' ())       
                             ) -  ||            )_ (()      
                           (_   \====       @  (   (_)      
                           | (___/{ }        \7 \ _) |      
                            \____\/)          {)=== / \     
                            |    |             \ |     )    
                            |_/\_|               |    /    
                             |  |                |    |    
                              ) )\               |    |     
                            _/| |/               |    |     
                           ( ,\ |_               '~~~~'     
                            \_(___)               _/Y


 """)
    time.sleep(1.5)
    print_ci ("\nRebekah pulls you by your jacket, she leans in closer and closer until your noses are touching. You put your hands behind her\n"
              "head and you see the Golden Quitch, the King’s dragon. You quickly pull back and push her away. \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Your dad is coming \n")
    time.sleep(0.5)
    print_ci ("\nShe looks behind her and watches him land. Zane and Xavier were with him too. \n")
    time.sleep(0.5)
    print_ci ("\nA bunch of other dragon’s come on the patio to take Rosorus and to check on you and Rebekah \n")
    time.sleep(0.5)
    print_ci ("\nRebekah goes to her dad while Xavier and Zane go to you. \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Yall could have came about 2 minutes later. \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: Ye…sorry. Anyways….mm… \n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: You saved her \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: You know, I did my thing a little bit. \n")
    time.sleep(0.5)
    print_ci_R ("\nRebekah: So we have to go back. Do you guys want to go with us or… \n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: We’ll go with you \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: What? No, leave them together \n")
    time.sleep(0.5)
    print_ci_X ("\nXavier: You’re doing it again? \n")
    time.sleep(0.5)
    print_ci_Z ("\nZane: doing what? \n")
    time.sleep(0.5)
    print_ci_K ("\nKaser: Oh it’s fine, just come. \n")
    time.sleep(0.5)
    print_ci ("\nYou all get on the dragon with you sitting behind Rebekah and Xavier and Zane behind you. \n")
    time.sleep(2.5)
    print_ci ("\nYou fly North, towards the town with the sunset at your back and all the other dragons following you. \n")
    time.sleep(2.5)
    print_ci ("\nAfter a fun journey full of jokes you made it back to the town.  \n")
    time.sleep(2.5)
    print_ci ("\nRosorus was locked up. After eventually getting his powers taken away from him, he became a full-time construction worker at the town. \n")
    time.sleep(2.5)
    print_ci ("\nYou, Rebekah, Zane and Xavier stayed friends and eventually made peace with Rosorus and got him back in the friend group and lived happily ever after…\n")

    input("\n[Press enter to continue]")
    creditsOne()

def creditsOne():
    print_ci ("\nCongrats!!!\n")
    time.sleep(1)
    print_ci ("\nYou have completed the game!\n")
    time.sleep(1)
    print_ci_red_slow ('####################################################################################################')
    print_ci_red_slow ('####################################################################################################')
    print_ci_red_slow ('############################################################           ##########################')
    print_ci_red_slow ('################################################################  - - - - ,   ######################')
    print_ci_red_slow ('#############################################################     \""""""",    #####################')
    print_ci_red_slow ('##############################################################     \"""""",    #####################')
    print_ci_red_slow ('##############################################################      /""""",    #####################')
    print_ci_red_slow ('    ####################################    _____   #####   _____  ///\""",    #######################')
    print_ci_red_slow ('  ####################################  ,ad8PPPP88b, ### ,d88PPPP///,  \"",    #######################')
    print_ci_red_slow ('    #################################  d8P"      "Y8b, ,d8P"      "Y8b  \",    ##########################')
    print_ci_red_slow ("####################################  dP'           '8a8'           `Yd    #########################")
    print_ci_red_slow ('    ###############################   8(              "              )8   ###########################')
    print_ci_red_slow ('       ############################   I8       \                     8I   #############################')
    print_ci_red_slow ('       ############################   8b,    Cer\ified Lover Boy   ,dP   ###############################')
    print_ci_red_slow ('#####################################   "8a,     \               ,a8"   ##########################')
    print_ci_red_slow ('     #################################   "8a,   //\           ,a8"   ###############################')
    print_ci_red_slow ('     ###################################   "Y //   |        adP"   ##################################')
    print_ci_red_slow ("     #####################################   //Y8a  '      a8P'   #################################")
    print_ci_red_slow ("   ####################################,   //   `88,t    ,88'   ################################")
    print_ci_red_slow ('  ########################### ######### \//       "8b   d8"   ###################################')
    print_ci_red_slow (' ####################################  /\          "8b d8"   #####################################')
    print_ci_red_slow ("#################################### //   '         `888'   ########################################")
    print_ci_red_slow ('####################################################  "   ########################################')
    print_ci_red_slow (' ###################################################################################################')
    
    print_ci_TaSBlue (r"""

  Kaser

     /'                                                         
     ||
     ||      ** *
     ||      __X_
     ||     ( ___\
     ||     |:  \\
    ><><  ___)..:/_#__,
    (X|) (|+(____)+\ _)
     o|_\/>> + + + << \
       |:\/|+ + + +| \_\<
       \./  XXXXXX.  (o_)_
           /+ + + |   \:|
          /+ +/+ +|  -/->>>----.
         /+ +|+ /XX /   _--,  _ \
        \+ + + /  |X   (,\- \/_ ,
        /\+ + /\  |X \    /,//_/
       +_+_+_( )o_)X  \  (( ///
        (_o(  /__/ X   \  \\//
         \_|  |_/  X    \ ///
         \_| >(_/        \,/
    ,////__o\ /__////,    V                  



 """)
    print_ci_TaSMagenta(r'''

  Rebekah
                    ____                       
                 .-"    `.--.                  
              .-"            \                 
          _.-"                \                
        .'                     ;               
       /    .-" .'          \  :               
      :   .'   /             ;  ;              
      :  /    :     /      : :  ;              
       \:     ;    :       ; ;  :              
        ;     :    ;      /.'   :   ;          
        :      \   ;    .'";\    ; /;          
       .'"+._.-J`-.:   /_  : `.__;'/           
      /   : : /dB   \ :db\ ;`j.__.'            
     :     \ ; TP    `;TP : /    :             
     ;     /":"""  +   """;T      ;            
     ;    :   `.  '--'  .' :      ;            
     :    ;  :  "+.__.+";   ;     :            
      \   :  :   :    ; :   :     :            
       \   \  \ .;    :  \   \     \           
        `.__J.-"       "-.J.  `.  `-^._        
       .' /::_           :;""--.L.     "-.     
     _:_.'/:: ""--.  .---:;"     \`.      `.   
  .-" " -'--,            :;       ; \       \  
 /      .-"\:            ;:       :  ;       ; 
:   _.+"   ;;            ;:       :  :       : 
:   ; :   `;;            ;: :     ;  ;       ;


 ''')

    print_ci_TaSRed(r"""

  Kaser and Rebekah 

                          (,);    /\                        
                         ((  ^_   ||            ...         
                          ' /  \  ||           (()))        
                            L {=) ||           {' ())       
                             ) -  ||            )_ (()      
                           (_   \====       @  (   (_)      
                           | (___/{ }        \7 \ _) |      
                            \____\/)          {)=== / \     
                            |    |             \ |     )    
                            |_/\_|               |    /    
                             |  |                |    |    
                              ) )\               |    |     
                            _/| |/               |    |     
                           ( ,\ |_               '~~~~'     
                            \_(___)               _/Y

                                        (,);
                                       ((  ^_.  ...
                                        ' / /_\(()))
                                          L( '}{' ())
                                          ) (   )_ (()
                                        (_   \ (   (_)
                                        | (__'__\_)  |
                                         \___|_(}==/  \
                                         |    |  |     )
                                         |_/\_|  |    /
                                          |  |   |    |
                                           ) )\  |    |
                                         _/| |/  |    \
                                        ( ,\ |_  '~~~~/7
                                         \_(___)  _/Y


 """)
    print_ci_TaSGreen(r'''

  Xavier

                                    /)
                                   //
                 __*_             //
              /-(____)           //
             ////- -|\          //
          ,____o% -,_          //
         /  \\   |||  ;       //
        /____\....::./\      //
       _/__/#\_ _,,_/--\    //
       /___/######## \/""-(\</
      _/__/ '#######  ""^(/</
    __/ /   ,)))=:=(,    //.
   |,--\   /Q...... /.  (/
   /       .Q....../..\
          /.Q ..../...\
         /......./.....\
         /...../  \.....\
         /_.._./   \..._\
          (` )      (` )
          | /        \ |
          '(          )'
         /+|          |+\
         |,/          \,/  

 ''')
    print_ci_TaSCyan(r'''

  Zayn

              . ,
            <( .)>
             //'
            //                |||
         __//_   _,,,,,    \_///|
        /___\\  (.  __\_   \_,_/
       / Q--\'  |_o \:::)  / |
      /.(|_______)\___/___/-.|
      |  / /' \ _  ~ \_  /  /
      .---/__  """\_/""_/--'
            /\......./
           (_/_ _,,_/
            ;;;;[X];__
           /# . ._) . )-----.
          /. . . .\. /   , __>
          | . . . .\|__-( __/
           \ . . . .\   |__/
            ) .--., )  >Xxx
            //  _>)/    / X\
           (/  __/     O  X\
            / __/       \ X\
            |__/         `._\  ))
            Xxx<
            / X\
           O  X\
            \ X\
           ,,`._\,,,,, ,,

  

 ''')
    print_ci_TaSYellow(r'''

  The principal

              _,._      
  .||,       /_ _\\     
 \.`',/      |'L'| |    
 = ,. =      | -,| L    
 / || \    ,-'\"/,'`.   
   ||     ,'   `,,. `.  
   ,|____,' , ,;' \| |  
  (3|\    _/|/'   _| |  
   ||/,-''  | >-'' _,\\ 
   ||'      ==\ ,-'  ,' 
   ||       |  V \ ,|   
   ||       |    |` |   
   ||       |    |   \  
   ||       |    \    \ 
   ||       |     |    \
   ||       |      \_,-'
   ||       |___,,--")_\
   ||         |_|   ccc/
   ||        ccc/       
   ||                  

 ''')

    print_ci_TaSMagenta(r"""

  White Agate
                                                    .%,
                                                   X:-x\',
                                                  X:/%;::\:X
                                                 X:l%  ; :'\:X
                                                X:l%   :  : '\:X
                                                X:l%   :   :  '\:X
                             b,      b,        X:/l%   :    :   \:X
                            JPQ,    JPQ,       X:l%    :     :   '\:X
                          .dP'd|._,=dPQq\     X:l%'    :      :    '\:X
                         xdP  #P"'_    _,:   .X:l%     :       :    '\:X
                      .d/"p   '  'O \  'O:;  X:l%'     :       :      \:X
                    ,pP' q.          \:  `#  X:ld       :       :      ':X
                  ,d"   ,pq  .,-qx_,  "\  `Q:  l%       :       :       k:X
                ./'     Jp       .      `  ` 3  %       :        ;      k:X
               dP       p            p    `  `q         :        :      k:X
              d/       ; J,/";xpx"\: '*q    ` `\,       :         :     l:X.
             dP      ;'    dP      "\:_,`.q. /d b\      :         :      k:X
           .d'      ;    dP            .\_j '- u-'      :         :      k:X
X         ./'     ;'    /"            .'                :         ;      k:X
\X       .d'     ;    ,"             :      X:l%        :        :       k:X
:\X      d'     ;   ./'             :       X:/%        :        ;       k:X
::lX    JP     ;    J              :      .X:/ %        :       :        k;X
k:lX    #'    :    j'             :    .X:/ %           :       :       d:lX
k:lX   |P    ;     |             :  .X:/ %              :       ;       k;lX
k:lX   ||    ;    |'            : X:/ %                 ;       :      d:;X'
k:lX   d|   ;     :l           :X:/ %'                 :        :      k:lX
k:iX   #|   ;     ||          X:/ %                    ;        ;      k:lX
 k:\X  ||  ;       ||       X:/ %                     :        :       k:lX
  k:\pQJb  ;        \N.PQ XX/ %                      ;         ;       k:lX
   kJP.Ql\;          XQ. J Q J                      :         ;        k:lX
   6Q : Q%           \Q  Q   J              ;''''':.:;''::.  :         k:lX
  6QQ  : Ql           lQ'   J              ;        ;     ': :;''':.   k::X.
 6QQQ )  Ql           i6    Q             ;                 .;     ':.  k:\X
  6QQ   J l           \  6  Q            ;                            ':.k:X
 9QQ   J  i            l 6   6          ;                                 k;

 """)


    print_ci_TaSBlue(r"""
                                                 __----~~~~~~~~~~~------___
                                      .  .   ~~//====......          __--~ ~~
                      -.            \_|//     |||\\  ~~~~~~::::... /~
                   ___-==_       _-~o~  \/    |||  \\            _/~~-
           __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
       _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
     .~       .~       |   \\ -_    /  /-   /   ||      \   /
    /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
    |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\
             '         ~-|      /|    |-~\~~       __--~~
                         |-~~-_/ |    |   ~\_   _-~            /\
                              /  \     \__   \/~                \__
                          _--~ _/ | .-~~____--~-/                  ~~==.
                         ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                    -_     ~\      ~~---l__i__i__i--~~_/
                                    _-~-__   ~)  \--______________--~~
                                  //.-~~~-~_--~- |-------~~~~~~~~
                                         //.-~~~--\


""")
    print_ci_TaSRed(r"""

  Rosorus and the Black Agate

                                   _
                            ==(W{==========-      /===-
                              ||  (.--.)         /===-_---~~~~~~~~~------____
                              | \_,|**|,__      |===-~___                _,-'
                 -==\\        `\ ' `--'   ),    `//~\\   ~~~~`---.___.-~~
             ______-==|        /`\_. .__/\ \    | |  \\           _-~`
       __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\        ,'
    _-~       /'    |  \\     )__/==0==-\<>/   / /      \      /
  .'        /       |   \\      /~\___/~~\/  /' /        \   /'
 /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                  \_|      /        _) | ;  ),   __--~~
                    '~~--_/      _-~/- |/ \   '-~ \
                   {\__--_/}    / \\_>-|)<__\      \
                   /'   (_/  _-~  | |__>--<__|      |
                  |   _/) )-~     | |__>--<__|      |
                  / /~ ,_/       / /__>---<__/      |
                 o-o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~
                ,/|           /__>--<__/     _-~
             ,//('(          |__>--<__|     /                  .----_
            ( ( '))          |__>--<__|    |                 /' _---_~\
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\
        ,/,'//( (             \__>--<__\    \            /'  //        ||
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
   ;'( ')/ ,)(                              ~~~~~~~~~~
  ' ') '( (/
    '   '  `  



 """)
    print_ci_TaSRed(r"""

  Black Agate


                                              ,....,.
                                          ..''   .'
                                       .''       |
                                    .''          \
                                 .''              \.
                               .'                  .'.,
                             ,:'             ..,'''   '...,..::/''.....
                           /''          .,'''  .,',:,''''         .,''
                         ,'.'      .,''' ..,''' ''         .'   .''
                       ,'  \, ..,''  .,''. ..,'''        ./   .'
                     .'     .,'  .,''.,''./           ..''   /
                    ,'    .'  ./'.,''  .'  ''     .' '.     /
                  .'   ./' ./'.'\,..,''     '' ../,     ,  |
                 ,   ./' .'./'|/     ............        ',|
                /   /' ,'.'.,'''\..... ''''''''''  .::/'.., |
               /  .' ,' ':\ '''  |  ,      ''          '''   \
              /  /'.''. |:::::::''' ,' ' ''. '.,.,  ''''    .''
             | .' /.,':. ''..,   '\'..''..  ;''  '\.''''  .'
             | \.:\.    '''./\ \  | ' '' .,''.           /
             / \'   ''..     ', \  \,',     ''..  .,     '
            /.'',''..,  '\,   '\ '. '\'.,     , ''. ''.,|
           .,'        ''. ',    \ '.'.. ''../'      '' __\
           '             \,',    \  '.'\..,  ',''  .''
                         |  |    '| ,\'''\/.  |  .'
            .'          .|  .    / / ./'. '.'.' /'
            /'        ..|':'''\././  /   '  '/\.'
           //  ./  .''    /' ./'.' .'  | ..,  ':|
         ./:  ,/   |',   ' .''  :  '   |    .../:,
        .'.'.\/   /.'           ''  .,   ..\'
      .,\.\'.'   /'    ,'' \...,      '\.\| ',
     /    ./'''''   ..:    ',|  ''.,     '\  ',
  .,' ''   \|     ''.''.    '/  .| '\.     ', '\
 /          \.    ../,   './ '\ |'  \/'' ''.'\  \
/   '\\:.   \,'\::'  ./'''    ./|  .'     .''/| '|
' ,'\:'/'''  /'  .'\'  .., |:| .| |'    .'' .\|  ',
|/  / /'    .'| /  |. \,    /''/. |  |:\..,' .||  \
'' /.'      //\|'  '\/\:.   :,/''::.  ,   ..::'|  |
            ||'/,    '\\/'\ '/|    '\ ''::::'| || .
            || \\       ''.   ...,  '.  \\...| |' |
            ||  '\,         .'.\, '. ', | \  '||  |
             '              |\|'|\/.''\ | |\  ||  |
                            ||\/'/| '\, ., / / /  ,
                             ' \  '   ''  / / .' /
                                '      .''.' .' /
                                  ..'''..' .' .'
                              .,'':.'''..'' .'
                         .,:'''''  .''  ..''
                       .' .''..'''...,''
                    ..' '    , '''
                   /  . :/''
                 .'  :/'
                /  /'
               / .'
              / '
             /.'
             '


 """)

    print_ci_TaSRed(r"""

  Lexin

  

          ,----.__                         |
                                ,'        `.                       |
                            _  /            :                      ,-.
                           |.`:              :                    /  -
            ,'''''-._      | )               :                 _.'  --
           /         '.  _.`.   (88o    _    |_           _.-''      -
           |           `/    |   '''   9@8o  / )-..__._.-'      ,/'`-/
           ]     \    ,:     `.         ''  :_/              ,-'  |
            :     \-_/        `. `a,    ,   :              ,'    /
             `.    Y'       ,_  \ '7888'  ,'   _.--''''---')     |
               \ .'      _/'  `._\      ,'---.<...        /     |
               .'      ,' '-.._   ':._,::...,'   /'     ,'      /
              /'     ,/        '`''''           /     ,'       /
             ,'    /  :                        /    ,'       ,-''''._
             |    ()   :                      |    |      .-'        '
             `.   :     ) __............____ .'    |_ .--'
              `.   `.  ,'                   `/       `'-.__
      _,....--'>    : /                     |   __...-._   `\
   ,-'       .' |   `.                      '--'        ` ._/'--._
 ,'        /'    |   `.                                           'akn
/         (.,   /|     :                                            \.
             `'' :     :\
                 )     :.:
                 : ; . ; '
                 '_: . '
                   '_:
 """)
    print_ci_TaSRed(r"""

  Gollex
  

                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
                  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"

 """)
    print_ci_TaSRed(r'''

  Flying Lexin


             \                  /
    _________))                ((__________
   /.-------./\\    \    /    //\.--------.\
  //#######//##\\   ))  ((   //##\\########\\
 //#######//###((  ((    ))  ))###\\########\\
((#######((#####\\  \\  //  //#####))########))
 \##' `###\######\\  \)(/  //######/####' `##/
  )'    ``#)'  `##\`->oo<-'/##'  `(#''     `(
          (       ``\`..'/''       )
                     \""(
                      `- )
                      / /
                     ( /\
                     /\| \
                    (  \
                        )
                       /
                      (
                      `    

 ''')

    print_TaS(r"""

                            ,--.                       ,--.
                          _',|| )                     ( \\ |
            ,.,,.,-----""' "--v-.___                   `_\\.'--,..__
            |,"---.--''/       /,.__"")`-:|._________-"'     (--..__'/--.
                      /     ,."'    ""-'-"|'  _.,-"_.'-"\     \     ` '""
                   _ )____---------------(|--"_|--'      '__   \_
                _,' |  .''''""---.        '""'       ,---'''.   /".
            _,-'  ." \/,,..---/_ /                   | -|.._____|  \_
          ,-\,.'''            \ (                    |"")       "-,  \
      _ .".--"                ( :                    | (           '. "\_
    ,- ,."                    ; !                    ; |             \,_ `.
___(_(."                      L_">        _________.-/_J                '\_')


 """)
    print_ci_TaSRed(r"""

  Gates oh Hellheim with unconscious Rosorus

           
|| |_| |_| |_| |------------------------------------|_| |_| |_| |_||
|______________|[=][=][=][=][=][=][=][=][=][=][=][=]|______________|
|--------------|____________________________________|--------------|
|   _______    |------------------------------------|    _______   |
|  |   _   |   |     |           .-.           /    |   |   _   |  |
|  |.'* *'.|   |     \     _..--('[|)-..__     |    |   |.'* *'.|  |
|  |'. * .'|   |      |_.-'   .-'/'\'-.   '-._/     |   |'. * .'|  |
|  '. )_( .'   |      /   _.-' .'   '. '-._   \     |   '. )_( .'  |
|    '._.'     |     /_.-' _.-'       '-._ '-._\    |     '._.'    |
|______________|     |_.--'               '--._|    |______________|
|-.   .--.   .-|    /'                         '\ ' |-.   .--.   .-|
|  \ /    \ /  |  | |                          .' | |  \ /    \ /  |
| * v *  * v * | || '.                         | || | * v *  * v * |
|   *      *   | || ||                         | || |   *      *   |
|              ||   ||                         | || |              |
|              ||  | |                         || | |              |
[=][=][==][=][=]'. ' |                        | ' `.[=  =][= ]]  [=]
|              | | | |                        | |  ||              |
|              | | | |                        | |  ||       |  #   |
|              ||  \  \                      /  /  ||(     /       |
|              |'.   '/                      \'    `| \  # #  #    |
[=][=][==][=][=] '    \                      /    / |  #(.--.) #   |   
|              |                                    | \_,|**|,__   |   
|              |                            #       `\ ' `--'   ),    #
|              |                         \_          /`\_. .__/\ \        #
|              |                           \_ #     (   | .  |~~~~|  #   #
|              |                             \_     )__/==0==-\<>         #                     
`--...____...--'                     _____#_______  `--..        --'   ________     
                              


 """)
    print_ci_TaSGreen(r'''

  The school

           
                                 ____                                         
                              .-     `-.      ,                               
                            .'          '.   /j\                              
                           /              \,/:/#\                /\           
                          ;              ,//' '/#\              //#\          
                          |             /' :   '/#\            /  /#\         
                          :         ,  /' /'    '/#\__..--""""/    /#\__      
                           \       /'\'-._:__    '/#\        ;      /#, """---
                            `-.   / ;#\']" ; """--./#J       ':____...!       
                               `-/   /#\  J  [;[;[;Y]         |      ;        
""""""---....             __.--"/    '/#\ ;   " "  |     !    |   #! |        
             ""--.. _.--""     /      ,/#\'-..____.;_,   |    |   '  |        
                   "-.        :_....___,/#} "####" | '_.-",   | #['  |        
                      '-._      |[;[;[;[;|         |.;'  /;\  |      |        
                      ,   `-.   |        :     _   .;'    /;\ |   #" |        
                      !      `._:      _  ;   ##' .;'      /;\|  _,  |        
                     .#\"""---..._    ';, |      .;{___     /;\  ]#' |__....--
          .--.      ;'/#\         \    ]! |       "| , """--./_J    /         
         /  '%;    /  '/#\         \   !' :        |!# #! #! #|    :`.__      
        i__..'%] _:_   ;##J         \      :"#...._!   '  "  "|__  |    `--.._
         | .--""" !|""""  |"""----...J     | '##"" `-._       |  """---.._    
     ____: |      #|      |         #|     |          "]      ;   ___...-"T,  
    /   :  :      !|      |   _______!_    |           |__..--;"""     ,;MM;  
   :____| :    .-.#|      |  /\      /#\   |          /'               ''MM;  
    |""": |   /   \|   .----+  ;      /#\  :___..--"";                  ,'MM; 
   _Y--:  |  ;     ;.-'      ;  \______/#: /         ;                  ''MM; 
  /    |  | ;_______;     ____!  |"##"""MM!         ;                    ,'MM;
 !_____|  |  |"#"#"|____.'""##"  |       :         ;                     ''MM  
  | """"--!._|     |##""         !       !         :____.....-------"""""" |'
  |          :     |______                        ___!_ "#""#""#"""#"""#"""|  
__|          ;     |MM"MM"""""---..._______...--""MM"MM]                   |   
  "\-.      :      |#                                  :                   |  
    /#'.    |      /##,                                !                   |  
   .',/'\   |       #:#,                                ;       .==.       |  
  /"\'#"\',.|       ##;#,                               !     ,'||||',     |  
        /;/`:       ######,          ____             _ :     M||||||M     |  
       ###          /;"\.__"-._   """                   |===..M!!!!!!M_____|  
                           `--..`--.._____             _!_                    
                                          `--...____,="_.'`-.____            
                            

 ''')



    print_ci_TaSGreen(r'''

  Basement PC ( ͡°͜ʖ͡°)

           
  /                /|
              /                / |
             /________________/ /|
          ###|      ____      |//|
         #   |     /   /|     |/.|
        #  __|___ /   /.|     |  |_______________
       #  /      /   //||     |  /              /|                  ___
      #  /      /___// ||     | /              / |                 / \ \
      # /______/!   || ||_____|/              /  |                /   \ \
      #| . . .  !   || ||                    /  _________________/     \ \
      #|  . .   !   || //      ________     /  /\________________  {   /  }
      /|   .    !   ||//~~~~~~/   0000/    /  / / ______________  {   /  /
     / |        !   |'/      /9  0000/    /  / / /             / {   /  /
    / #\________!___|/      /9  0000/    /  / / /_____________/___  /  /
   / #     /_____\/        /9  0000/    /  / / /_  /\_____________\/  /
  / #                      ``^^^^^^    /   \ \ . ./ / ____________   /
 +=#==================================/     \ \ ./ / /.  .  .  \ /  /
 |#                                   |      \ \/ / /___________/  /
 #                                    |_______\__/________________/
 |                                    |               |  |  / /       
 |                                    |               |  | / /       
 |                                    |       ________|  |/ /________       
 |                                    |      /_______/    \_________/\       
 |                                    |     /        /  /           \ )       
 |                                    |    /OO^^^^^^/  / /^^^^^^^^^OO\)       
 |                                    |            /  / /        
 |                                    |           /  / /
 |                                    |          /___\/
 |                                    |           oo
 |____________________________________|


 ''')
    print_ci_TaSRed(r'''

   Caves of Jihij


   .......::::::::::::)..           .......................(::::::........
      .:::::;;;;;;;;):::::::.... .           .......:::::::::::::<......
          <  >>>                   ,.
  .::..  ;   I;L\  /L\.  ..::..   /iL.           |         ..::::::::::::..
        ;    II;L\/LLLL;         / I;L\    \     |     / /\_   
             II;..LLLLLL\    _._/ I;:.L\     \   |   / _/J; \    
      :     IIIIi;..LLLLL\__/   IIII:..L\____  \###/  /JJI:  \
    ,;     ILIi;;;:...:LLL;\      IIIII;.LLLLL\#####/JJ II;   \
   ;     I LLii;;;.:.. :LLL;\     III;;;::LLLLL\###/JJ IIII;   \_.
  :     IIILiii;;::.... :LLL;|      ;;I;;::.:LLLLLL:;IJ IIIII;:   \__.

           IIIII IIii;;::;..;\          ;;:::...LLLL;IJIII;;    :::   \
:    ;    IIIIIIIIIii;;::.;..      _==|      ;..  :;IJIII;:::    ::    \
    ;    ::::::::::::;;::..;  _==|   )__)  |                            \
 "  ""  "  """"""""  """"  ""    )_)  )___) ))  """""   """"  """ """"""  """"
        """   ""^^       ^~   )___) )____))_)   ~~         ""^^^""  "  "  "~"
" ^^            ^        _    )____)_____))__)\      ~^~~^           ^^"
     "^^          ^~      \---__|____/|___|___-\\--        "~"~         "~"
   ""    "^          ~"~   \   oo oo oo oo     /      ~"      "~       ""~"
        ____   ^^^"~   ~~^^^^^^^^^^^^^^^^^^^^^^    ^~^            ^~^^^
      /  o   \     """"  __          __ """""     "   ""~     ~""~"`    """"
    < ____     \"""    /    \   "" /    \       _          _    "~    _
          |     |     |  __  |    |  __  |    /   \      /   \       / |
    """   |_____|  "  |__||__| "" |__||__| " |_____| "" |_____| ""  /_/
         """     ~^^^^      """"^^"""""^        """""""""        """""^^""
   ""          "^^           ~^^~          ~^ "      ~~      "  ^   ^^^^^^^^


 ''')

    gameOverScreenEnd()
    
title_screen()


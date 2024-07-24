import time as t
import pyfiglet
import random
import os
import hashlib

#global variables
aye_no = ["aye", "no"]
stored_hash = "cfeec4e68965f7c633cdf9846e10f656dbb12a2a2663fef33c12018f80127eb0"
choice =["you", "mission"]


# function for clear the screen
def clear_screen():
    # check of OS 
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Unix-based Systems (Linux, macOS)
        os.system('clear')

# chars in slowMo
def slowChars(text, color_code='0'):
    # ANSI Escape-Sequence for color start and end
    color_start = f"\033[{color_code}m"
    color_end = "\033[0m"
    for char in text:
        # the break between the chars
        t.sleep(random.uniform(0.06, 0.09))
        print(f"{color_start}{char}{color_end}", end='', flush=True)

# wrapper instead of print()
def slowPrint(text, color='reset'):
    color_codes = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
        'greeny': '1;32',
        'reset': '0'
    }
    
    slowChars(text + "\n", color_codes.get(color,'0'))




# start screen, welcome text, enter name
def start_screen():
    ascii_art = pyfiglet.figlet_format("Psychosiz", font="crawford")
    print(ascii_art)
    global name # here name is defined as a global variable
    slowPrint("\nWelcome to the resistance...")
    name = (input("Choose a Name> "))

    slowPrint(f'''\nConstructor: Welcome {name}, you playin' this game on your own risk. 
You've been warned!''','cyan')
    slowPrint("Let the trip begin...",'cyan')

start_screen()
t.sleep(4)
clear_screen()

# the story intro
slowPrint(f"""Unknown: Greetings "Mr." {name}. You don't know me ...but I know you. 
Unknown: I was in this IRC chat from yesterday too. You shouldn't click random links dude. 
Unknown: But it's seems you are curious. In this case, that is exceptionally good.
Unknown: I've read that you are not bad with computers and are very interested in cryptography. 
Unknown: I'm writing you, because there are strange things happening and I need some help from a guy I can trust to discover a huge secret.  
Unknown: Be warned, it could gone really dangerous and disturbing.""")
while True:
    answer = input("Unknown: Are you interested in? ")
    if answer == "aye":
        slowPrint(f'''Unknown: Sounds good {name}. Let's meet up in an private IRC.
Unknown: Here is the password for the chat: cfeec4e68965f7c633cdf9846e10f656dbb12a2a2663fef33c12018f80127eb0 
Unknown: Of course you have to de-hash it. What did you think?''')
        input("Constructor: Continue with Enter if you got the hash")
        break
    elif answer == "no":
        slowPrint("Unknown: I knew you don't have what it takes. Watch ya!",'red') 
        quit()
    else: slowPrint("Constructor: You have to type aye or no",'cyan')

clear_screen()
t.sleep(2)
act_zero_art = pyfiglet.figlet_format ('''Act zero: Unknown to well known''',font="crawford") 
print(act_zero_art)
t.sleep(1)
slowPrint(f'''Constructor: You are alone in your Apartment. It's pitch black except the light of your screen. 
You feelin' weird about what happened\n''','cyan')
t.sleep(2)
slowPrint(f"{name}: Fuck! Who was this guy and how could he enter my messenger?")
slowPrint(f"{name}: Why he'd chose me? Shit, I have to join this stupid chat or I'm goin paranoid about this Questions.\n")
t.sleep(3)

def check_password(password):
    # calculate the hash value of the plain text entered
        input_hash = hashlib.sha256(password.encode()).hexdigest()

    # compare the calculated hash value with the saved hash value
        if input_hash == stored_hash:
            return True
        else:
            return False

while True:
    
        player_input = input("Enter the password for the Chat: ")

        if check_password(player_input):
            slowPrint("Password correct! You now have access to the chat.",'greeny')
            break
        else:
            slowPrint("Password incorrect. Access denied. Try again.",'red')


slowPrint(f"Unknown: Well, welcome to the room {name}.",'greeny')
slowPrint("Unknown: What do you wanna know? Is it something about me or nail into the coffin and dive into the Mission?",'greeny')
while True:
    choice = input("Unknown: For Infos about me, type 'you'. For the Mission, type 'mission'. ").lower()
    
    if choice == "you":
        slowPrint(f"{name}: About You. I need some answers. Who are you?",'greeny')
        slowPrint(f"Unknown: Call me Resident {name}",'greeny')
        slowPrint('''Resident: I was a security employee in the IT department of a large tech company. 
When I found out what they were doing, I could no longer reconcile it with myself and my moral values. 
Now I'm sort of... a kind of freelancer ;) .''','greeny')
        
    
    if choice == "mission":
            slowPrint(f'''First {name}, you have to understand that this is no joke! I know you feel like in a game but this is serious.
I was working for a well known, big company, 1 year ago. 
As I found out they use the data to manipulate you - not in the way we know already.
No, they now use AI to create personal profiles. 
They are starting to store each person individually in a storage system. It's a kind of object orientation. 
It starts with continent, country and goes on to your house and your habits. Quantum computing already exists. 
For a while now and it's used... misused exactly for this. 
But it's only available to the military and specialized companies. Everything has already been corrupted. 
People think they are revealing something or bringing a truth to light, 
but even conspiracies and the theories are a part of the agenda. 
Youpoop, Goggle, TikTik... they all wanted and unwanted parts of a web, that is hard to see through. 
They're laughing their heads off because we're driving each other crazy and nobody knows what's true and what's false or fiction anymore.''','greeny')
    
            
    elif choice == "you":
        choice2 = input("Resident: For the Mission, type 'mission'. ").lower()       

        if choice2 == "mission":
                slowPrint(f'''First {name}, you have to understand that this is no joke! I know you feel like in a game but this is serious.
I was working for a well known, big company, 1 year ago. 
As I found out they use the data to manipulate you - not in the way we know already.
No, they now use AI to create personal profiles. 
They are starting to store each person individually in a storage system. It's a kind of object orientation. 
It starts with continent, country and goes on to your house and your habits. Quantum computing already exists. 
For a while now and it's used... misused exactly for this. 
But it's only available to the military and specialized companies. Everything has already been corrupted. 
People think they are revealing something or bringing a truth to light, 
but even conspiracies and the theories are a part of the agenda. 
Youpoop, Goggle, TikTik... they all wanted and unwanted parts of a web, that is hard to see through. 
They're laughing their heads off because we're driving each other crazy and nobody knows what's true and what's false or fiction anymore.''','greeny')

        break

    if choice == "mission":
        choice2 = input("Unknown: For the unecessary Infos about me, type 'you'. ").lower()       

        if choice2 == "you":
             slowPrint(f"{name}: About You. I need some answers. Who are you?")
        slowPrint(f"Unknown: Call me Resident {name}")
        slowPrint('''Resident: I was a security employee in the IT department of a large tech company. 
When I found out what they were doing, I could no longer reconcile it with myself and my moral values. 
Now I'm sort of... a kind of freelancer ;) .''')
        
        break

    else:
        print("Please type 'you' or 'mission'.")
    
        

slowPrint("\nTo be continued...",'yellow')

t.sleep(2)     
beta_art = pyfiglet.figlet_format ("Thank you! from Psychosiz",font='crawford')
print(beta_art)
slowPrint("\n...for playin' the Beta-Demo. Stay tuned for updates and stay safe.",'yellow')
    



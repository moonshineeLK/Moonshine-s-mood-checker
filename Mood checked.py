name = input(f"Care to tell me your name, darling?:  ")
identity = input("\nhow do you identify? (girl/boy/other):  ").lower()
hobby = input("\nwhat is your hobby?: ").lower()

if identity == "girl":
     title = "my girl"
elif identity == "boy":
     title = "my boy"
else:
     title = "my love"
     
count = (0)

greetings = {
             "Morning": f"\nmorning, {name}, slept well?", 
              "Afternoon": f"\nWhy don't you take a nap, {title}?",
              "Evening": f"\nGood evening, {title}, getting cozy?",
              "Night": f"\nC'mon, sleep now, sweetdreams, don't let bed bugs bite or they'll fall in love with your taste😉"
}

while True:  
    count += 1
    
    print(f"\nConversation count: {count}")
    
    time = input(f"\nis it morning, afternoon, evening or night?:  ").capitalize()

    print(f"\nHello, {name}")
    print(f"\nhow's my baby feeling?:")
    print("Happy")
    print("Sad")    
    print("Tired")
    print("Peaceful")
    
    mood = input("\nhow's my baby feeling? happy/sad/tired/peaceful?: ").capitalize()
    
    if mood == "Happy":
       print(f"\nSo glad {title} is happy, i bet the reason is probably {hobby}")
        
    elif mood == "Sad":
         print(f"\nWho made {title} sad? how about you focus on yourself to feel better?")
         
    elif mood == "Tired":
        print(f"\nAww tired of being so cool? no worries, rest, baby")
        
    elif mood == "Peaceful":
         print(f"\nmy peace is getting peace finally")
             
    else:
         print(f"\nconfuse with feelings? {title} still deserves a hug")
         
    choice = input("\nType 'exit' to stop or enter to continue: ")
    if choice == "exit":
         break
         
                  
print(f"\nyou yapped {count} times today, such a yapper")

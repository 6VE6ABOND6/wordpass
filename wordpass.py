import regex
import engine_tr as e_tr
import datetime as T
import art
import sys
todayYear=int(T.date.today().year)
user = {}
WHITE = "\033[97m"


 
def askinfoBasic():   
 def regexTest(data):
     if not regex.match(r"^\p{L}+$",data)or len(data) > 32:
      print(WHITE+f"Whats that? {data}")
      return False
     else:
      return True
      
 while True:
  name=str(input(WHITE+"Name:")).strip()
  if not name:
   break  
  if regexTest(name) is True:
   user["name"]=name
   break
 while True:
  scndname=str(input(WHITE+"SecondName:")).strip()
  if not scndname:
   break  
  if regexTest(scndname) is True:
   user["scndname"]=scndname
   break  
  
 while True:
  surname=str(input(WHITE+"Surname:")).strip()
  if not surname:
   break  
  if regexTest(surname) is True:
   user["surname"]=surname
   break
  
  
 while True:
  partner=str(input(WHITE+"Partner Name:")).strip()
  if not partner:
   break  
  if regexTest(partner) is True:
   user["partner"]=partner
   break

  
 while True:
  child=str(input(WHITE+"Child Name:")).strip()
  if not child:
   break  
  if regexTest(child) is True:
   user["child"]=child
   break
  
  
 while True:
  pet=str(input(WHITE+"Pet Name:")).strip()
  if not pet:
   break  
  if regexTest(pet) is True:
   user["pet"]=pet
   break   
  
 while True:      
   username=input(WHITE+"Username:").strip()
   if not username:
    break  
   if len(username)>32:
       print(WHITE+"Probably less than 32 xd :")
       continue
   elif not regex.match(r"^[\p{L}\p{M}\p{Nd}._-]+$", username):
       print(WHITE+"What we are hacking? ")
       continue

   else:
       user["username"]=username
       break       
 while True:
    birth=input(WHITE+"Birthday(DD/MM/YYYY):").strip()
    if not birth:
     break
    try:
     birthDay=int(birth[0:2])
     birthMonth=int(birth[2:4])
     birthYear=int(birth[4:])
    except Exception as e:
     print(WHITE+"Enter like this (Example-->|01012001|) ")
     continue
    if len(birth)<8 or len(birth)>8 or birthDay<0 or birthDay>31 or birthMonth<0 or birthMonth>12  or birthYear<1600 or birthYear>2200 :
        print(WHITE+"smtng get wrong :/")
    else:
     user["birthDay"]=str(birthDay)
     user["birthMonth"]=str(birthMonth)
     user["birthYear"]=str(birthYear)
     break
 


def trDef():
    
    user.clear() 
    
    askinfoBasic()
    
    name = user.get("name", "")
    scndname = user.get("scndname", "")
    birthYear = user.get("birthYear", "")
    partner = user.get("partner", "")
    child = user.get("child", "")
    pet = user.get("pet", "")
    username = user.get("username", "")
    
    print(WHITE + "\n[+] Generating wordlist... Please wait.")
    
    count = 0
    with open("letstry.txt", "w", encoding="utf-8") as file:
        for password in e_tr.engineHearth(name, scndname, birthYear, partner, child, pet, username):
            file.write(password + "\n")
            count += 1
            
  
    print(art.GREEN + f"[OK] Process completed! {count} passwords saved to 'letstry.txt'" + art.RESET)
    
    
    while True:
        yesorn = input(WHITE + "\nDo you want to create another wordlist? (y/n): ").strip().lower()
        
        if yesorn in ["y", "yes", "evet"]:
            print(art.CYAN + "\nRestarting..." + art.RESET)
            user.clear() 
            askRegion() 
            break
            
        elif yesorn in ["n", "no", "hayır"]:
            print(WHITE + "See you later! 👋")
            sys.exit()
            
        else:
            print(art.RED + "Please type 'y' or 'n'" + art.RESET)
 
     
     
 
def usDef():
 pass  
def ruDef():    
 pass       
def brDef():     
 pass
def inDef():    
 pass
def askRegion():
  
 while True:
   
    country=input(WHITE+"Region..:Turkiye(tr),United States(us),Russia(ru),Brazil(br),India(in)..:")
    if country not in ["tr", "us", "ru", "br", "in"]:
     continue
    else:  
     match country:
         case "tr":
             trDef()
         case "us":
             usDef()    
         case "ru":
             ruDef()
         case "br":
             brDef()
         case "in":
             inDef()         
if __name__ == "__main__":
    try:
        art.show()  
        askRegion()
    except KeyboardInterrupt:
        print("\n\n 👋")
  



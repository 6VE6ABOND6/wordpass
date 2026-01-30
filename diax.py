import regex
import engine_tr as e_tr
user = {}
 


 
def askinfoBasic():   
 def regexTest(data):
     if not regex.match(r"^\p{L}+$",data)or len(data) > 32:
      print(f"Whats that? {data}")
      return False
     else:
      return True
      
 while True:
  name=str(input("Name:")).strip()
  if not name:
   break  
  if regexTest(name) is True:
   user["name"]=name
   break
 while True:
  scndname=str(input("SecondName:")).strip()
  if not scndname:
   break  
  if regexTest(scndname) is True:
   user["scndname"]=scndname
   break  
  
 while True:
  surname=str(input("Surname:")).strip()
  if not surname:
   break  
  if regexTest(surname) is True:
   user["surname"]=surname
   break
  
  
 while True:
  partner=str(input("Partner Name:")).strip()
  if not partner:
   break  
  if regexTest(partner) is True:
   user["partner"]=partner
   break
  
 while True:
  child=str(input("Child Name:")).strip()
  if not child:
   break  
  if regexTest(child) is True:
   user["child"]=child
   break
  
  
 while True:
  pet=str(input("Pet Name:")).strip()
  if not pet:
   break  
  if regexTest(pet) is True:
   user["pet"]=pet
   break   
  
 while True:      
   username=input("Username:").strip()
   if not username:
    break  
   if len(username)>32:
       print("Probably less than 32 xd :")
       continue
   elif not regex.match(r"^[\p{L}\p{M}\p{Nd}._-]+$", username):
       print("What we are hacking? ")
       continue

   else:
       user["username"]=username
       break       
 while True:
    birth=input("Birthday(DD/MM/YYYY):").strip()
    if not birth:
     break
    try:
     birthDay=int(birth[0:2])
     birthMonth=int(birth[2:4])
     birthYear=int(birth[4:])
    except Exception as e:
     print("Enter like this (Example-->|01012001|) ")
     continue
    if len(birth)<8 or len(birth)>8 or birthDay<0 or birthDay>31 or birthMonth<0 or birthMonth>12  or birthYear<1600 or birthYear>2200 :
        print("smtng get wrong :/")
    else:
     user["birthDay"]=str(birthDay)
     user["birthMonth"]=str(birthMonth)
     user["birthYear"]=str(birthYear)
     break
 
def trDef():
 askinfoBasic()
 with open("test.txt","w",encoding="utf-8") as file:
  for password in e_tr.engineHearth(user["name"],user["scndname"],user["birthYear"]):
    file.write(password+"\n")
       
 
 
 
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
    country=input("Region..:Turkiye(tr),United States(us),Russia(ru),Brazil(br),India(in)..:")
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
    askRegion()
  

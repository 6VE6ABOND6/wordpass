import itertools
import datetime as T
import regex

todayYear=int(T.date.today().year)

def engineHearth(name, secondName, yearBirth, partner, child, pet,username):
    
    partner = str(partner) if partner else ""
    name = str(name) if name else ""
    username = str(username) if username else ""
    secondName = str(secondName) if secondName else ""
    yearBirth = str(yearBirth) if yearBirth else ""
    child = str(child) if child else ""
    pet = str(pet) if pet else ""

   
    if name:
        yield from nameGen(name, secondName, yearBirth)
        yield from teamGen(name)
        yield from plateGen(name)
    
    if partner:
        yield from partnerGen(name, partner)
    
    if child:
        yield from childGen(child)
    
    if pet:
        yield from petGen(name, pet)
    if username:
        yield from usernameGen(username)
 
    
def iterTool(req1):

    for lenght in range(2,4):
     if len(req1) < lenght:
      continue
     for shootIt in itertools.permutations(req1,lenght):
        if shootIt[0].lower() == shootIt[1].lower():
         continue
        yield from symbolGen("".join(shootIt))
def symbolGen(word):
    
    symbols=["_",".","-","!"]
    for sembol in symbols:   
     if word[-4:].isdigit():
       yield word[:-4] + sembol + word[-4:] 
        
        
     elif word[:4].isdigit():
      yield word[:4] + sembol + word[4:]

       
     elif word[-2:].isdigit():
        yield word[:-2] + sembol + word[-2:] 
             
       
     yield word + sembol      
     yield sembol + word 
     
def nameGen(name,secondName,yearBirth):
 
 for i in range(2000,todayYear+1): #Name + 2002 + !
     f=f"{i}"
     
     yield from symbolGen(name+f)
     yield from symbolGen(name.capitalize()+f)
     
    
     
 pool={
     name,
     name.upper(),
     name[::-1],
     name.capitalize(),
     name.capitalize()+str(yearBirth),
     name+str(yearBirth),
     name+str(yearBirth[2:]),
     (name+secondName).capitalize(),
     (name+secondName).capitalize()+str(yearBirth), 
 }
 
 yield from pool
 yield from symbolGen((name+secondName).capitalize()+yearBirth)
 yield from symbolGen(name.capitalize()+"123")
 yield from symbolGen(name.capitalize()+"12345")
 
def teamGen(name):
     teamNames=["gs","bjk","fb","ts","bsk","ksk","goz","samsun","ads","eses","bursa","cimbom","aslan","ultraslan","kanarya","sari","lacivert",
                "kartal","kara","bordomavi","firtina","sarikirmizi","sari_lacivert","siyahbeyaz",
     ]
     teamYears=["1905","1907","1903","1967","1963","1954","1965","1925","1912","1453","1881","1938"]
     
     for t, y in itertools.product(teamNames, teamYears):
        peaces = [name, t, y,name.capitalize()]  
        yield from iterTool(peaces)
          

     
def plateGen(name):
        for i in range(1,82): #plate
         y=f"{i:02}"
        
        yield from symbolGen(y+name)
        yield from symbolGen(name+y)
        if i>9:
         yield from symbolGen(name+y+y)
        
        
def partnerGen(name,partner):
    extraLoveWords={"askim","birtanem","hayatim","canim","bebegim","kuzum","balim","prensesim","yavrum"}
    partnerPool={
        partner+"1234",
        partner.capitalize()+"12345",
    } 
    yield from partnerPool     
    
    yield from plateGen(partner)
    yield from plateGen(partner.capitalize())    
      
    for i in extraLoveWords:
      yield i+"123"
      yield i.capitalize()+"1234"
 
      for a in range(5):
       yield from symbolGen(i+str(a))
      
    years = [str(y) for y in range(2000, todayYear + 1)] 
    for year in years:
        peaces=[name,partner,year] 
        yield from iterTool(peaces)
          
        
def childGen(child):
     for year in range(2000,todayYear+1):
      yield child.capitalize()+str(year)
      yield from symbolGen(child.capitalize()+str(year))
    
def petGen(petName,name):
    
   for year in range(2000,todayYear+1):
    yield from symbolGen(petName+str(year))
    yield from symbolGen(petName.capitalize()+str(year))
    peaces=[name,petName,name.capitalize(),petName.capitalize()]
    yield from iterTool(peaces)
    
   for combo in itertools.permutations(peaces, 2):
        base_word = "".join(combo)
        if combo[0].lower() == combo[1].lower(): 
         continue
        for year in range(2000, todayYear + 1):
            yield from symbolGen(base_word + str(year))
         
         
def usernameGen(username):
    
    
    yield username
    yield username.capitalize()
    withRegex = regex.sub(r"[^\p{L}\p{Nd} ]+", "", username)

    yield from symbolGen(username)
    yield from symbolGen(username.capitalize())
    yield from symbolGen(withRegex.capitalize())
    
    
    for i in range(2000, todayYear + 1):
        yield from symbolGen(username + str(i))
        yield from symbolGen(username.capitalize() + str(i))
        yield from symbolGen(withRegex + str(i))
        yield from symbolGen(withRegex.capitalize() + str(i))    

    platforms = [
        "insta", "ig", "x", "fb", "tt", "mail", "gmail", 
        "123mail", "lol", "valo", "cs", "pubg", "fps", 
        username, 
        username.capitalize(),
        withRegex, 
        withRegex.capitalize()
        
    ]
    
   
    yield from iterTool(platforms)
    



    


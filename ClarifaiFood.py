from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import sys

#Function will analyze ouput and return list of all the ingredient
def RetrieveTags(ResultOfClarifai):
    ListTag = []
    WeInterested = 0
    
    TokenizeStr = str(ResultOfClarifai).split()
    for eachStr in TokenizeStr:
        
        if(WeInterested == 1):
            ListTag.append(eachStr)
            
        if(eachStr.find("name") > 0):
            WeInterested = 1
            
        else:
            WeInterested = 0
    ListTag.pop(0)
    return ListTag

#Function will return a trim list of ingredient with higher accuracy
def TrimList(wholeString, TagList):
    ListTag = []
    FinalList = []
    WeInterested = 0
    
    TokenizeStr = str(wholeString).split("name")
    for eachStr in TokenizeStr:
        subelement = eachStr.split()
        for eachSubElement in subelement:
            if(WeInterested == 1):
                
                #extract first 4 element and convert to double
                Percent = eachSubElement[0:4]
                ListTag.append(Percent)
                WeInterested = 0 
            if(eachSubElement.find("value") > 0):
                WeInterested = 1
            
    index = 0
    for eachTag in TagList:
        if(float(ListTag[index]) > 0.81):
            FinalList.append(eachTag)
        index = index + 1
    return FinalList

#main - support 1 argument
#eg. python ClarifaiFood.py "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Schwartz_smoked_meat_montreal.JPG/300px-Schwartz_smoked_meat_montreal.JPG"
#FoodURL = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Schwartz_smoked_meat_montreal.JPG/300px-Schwartz_smoked_meat_montreal.JPG"#sys.argv[1]
FoodURL = sys.argv[1]
app = ClarifaiApp("Ko672okk_1UH7bhMOwNytXIZh8KZ5E8GoHbzzVxW", "Uu1JVMWQ2hYeB7AwJLuOsyBdbQQix_pnzHBnXOez")
model = app.models.get('food-items-v1.0')
image = ClImage(url=FoodURL)
myvar = model.predict([image])

TagList = RetrieveTags(myvar)

for eachTag in TagList:
    eachTag = eachTag.rstrip('\',')
    eachTag = eachTag.lstrip('\'')

TrimList = TrimList(myvar, TagList)
for eachTrim in TrimList:
    eachTrim = eachTrim.rstrip('\',')
    eachTrim = eachTrim.lstrip('\'')   
    print(eachTrim)

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import sys

def RetrieveTags(ResultOfClarifai):
    ListTag = []
    WeInterested = 0
    
    TokenizeStr = str(ResultOfClarifai).split()
    for eachStr in TokenizeStr:
        
        if(WeInterested == 1):
            ListTag.append(eachStr)
            #print(eachStr)
            
        if(eachStr.find("name") > 0):
            WeInterested = 1
            
        else:
            WeInterested = 0
    ListTag.pop(0)
    return ListTag

#main - support 1 argument
#eg. python ClarifaiFood.py "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Schwartz_smoked_meat_montreal.JPG/300px-Schwartz_smoked_meat_montreal.JPG"
FoodURL = sys.argv[1]

app = ClarifaiApp("Ko672okk_1UH7bhMOwNytXIZh8KZ5E8GoHbzzVxW", "Uu1JVMWQ2hYeB7AwJLuOsyBdbQQix_pnzHBnXOez")
model = app.models.get('food-items-v1.0')
image = ClImage(url=FoodURL)
myvar = model.predict([image])

TagList = RetrieveTags(myvar)
for eachTag in TagList:
    eachTag = eachTag.rstrip('\',')
    eachTag = eachTag.lstrip('\'')
    print(eachTag )

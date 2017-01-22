from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


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

app = ClarifaiApp("Ko672okk_1UH7bhMOwNytXIZh8KZ5E8GoHbzzVxW", "Uu1JVMWQ2hYeB7AwJLuOsyBdbQQix_pnzHBnXOez")
model = app.models.get('food-items-v1.0')
image = ClImage(url='https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Schwartz_smoked_meat_montreal.JPG/300px-Schwartz_smoked_meat_montreal.JPG')
myvar = model.predict([image])

returnCode = RetrieveTags(myvar)
print(str(returnCode))
print("WORK DONE!!!\n")

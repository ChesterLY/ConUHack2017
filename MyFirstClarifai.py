
from clarifai.rest import ClarifaiApp

##def RetrieveSuccess(ResultOfClarifai):
##    print(str(ResultOfClarifai))
##    for eachElement in ResultOfClarifai:
##        if eachElement == "status":
##            #print("\\n")
##            print( eachElement )
##            for subvar in ResultOfClarifai[eachElement]:
##                if subvar == "code":
##                    print("inside code: "+str(ResultOfClarifai[eachElement]))
##                    for subsubvar in ResultOfClarifai[eachElement]:
##                        print(subsubvar + " " + str(ResultOfClarifai[eachElement][subsubvar]))
##                        if(str(ResultOfClarifai[eachElement][subsubvar]) == "Ok"):
##                            return 1
##    return 0


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
        

#main 
app = ClarifaiApp("EUQZxVFF0VrBXlgJm8MBZQKJjw0_HFLz_FHJ3PnJ", "2dpV86IosRzWMUBuua5dM7mJYwjDxU6A-hrfekng")


# import a few labeld images
##app.inputs.create_image_from_url("https://samples.clarifai.com/dog1.jpeg", concepts=["cute dog"], not_concepts=["cute cat"])
##app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog2.jpeg", concepts=["cute dog"], not_concepts=["cute cat"])
##
##app.inputs.create_image_from_url(url="https://samples.clarifai.com/cat1.jpeg", concepts=["cute cat"], not_concepts=["cute dog"])
##app.inputs.create_image_from_url(url="https://samples.clarifai.com/cat2.jpeg", concepts=["cute cat"], not_concepts=["cute dog"])
##
##model = app.models.create(model_id="pets", concepts=["cute cat", "cute dog"])
##
##model = model.train()
##
### predict with samples
##print (model.predict_by_url(url="https://samples.clarifai.com/dog3.jpeg"))







# import a few labeld images
app.inputs.create_image_from_url(url="https://i.kinja-img.com/gawker-media/image/upload/s--d14MWjJC--/mttb7j7xoqsdp1wcgbck.jpg", concepts=["programmer"], not_concepts=["lumberjack"])
app.inputs.create_image_from_url(url="http://blog.builtinperl.com/uploads/covers/4E4926D6-0628-11E6-8654-CE024887B159.jpg", concepts=["programmer"], not_concepts=["lumberjack"])
app.inputs.create_image_from_url(url="http://www.infragistics.com/community/cfs-filesystemfile.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/robert_5F00_kim/8512.shutterstock_5F00_162360971.jpg", concepts=["programmer"], not_concepts=["lumberjack"])

app.inputs.create_image_from_url(url="https://theunaustraliandotnet.files.wordpress.com/2015/09/lumberjack.png", concepts=["lumberjack"], not_concepts=["programmer"])
app.inputs.create_image_from_url(url="https://s-media-cache-ak0.pinimg.com/736x/7c/3e/6c/7c3e6c50d78259d530b7d703501c8c99.jpg", concepts=["lumberjack"], not_concepts=["programmer"])

model = app.models.create(model_id="humanPicture", concepts=["programmer", "lumberjack"])
model = model.train()
# predict with samples
myvar = model.predict_by_filename(filename="C:\\Users\\Frost\\Documents\\conuhacks2017\\sample\\Lumber.jpg")

#print(str(myvar))
#print(str(model.predict_by_filename(filename="C:\\Users\\Frost\\Documents\\conuhacks2017\\sample\\Non-Humn.jpg")))
#print(str(model.predict_by_filename(filename="C:\\Users\\Frost\\Documents\\conuhacks2017\\sample\\Programmeur.jpg")))
ListTag = RetrieveTags(myvar)
print(str(ListTag))
print("WORK DONE!!!\n")

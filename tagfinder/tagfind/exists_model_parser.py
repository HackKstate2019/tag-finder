from .models import Website, Tag

def exists_model_parser(t):
    exists=False

    if Website.objects.filter(url=t[0][0]).exists(): #Checks if the Input Article's URL is already in the Database
        exists=True
    
    if exists==False:
        w=Website(url=str(t[0][0]),title=str(t[0][1]))
        w.save()
        itert = iter(t) #This skips the first iteration of the for loop
        next(itert)
        for p in itert:
            w.tag_set.create(keyword=str(p[0]).lower(),value=int(p[1]))
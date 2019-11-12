from .models import Website, Tag
import time

def exists_model_parser(t):
    start=time.time()
    exists=False

    if Website.objects.filter(url=t[0][0]).exists(): #Checks if the Input Article's URL is already in the Database
        exists=True
    
    # for i in Website.objects.all():
    #     if t[0][0]==i.url:
    #         exists=True
    
    if exists==False:
        w=Website(url=str(t[0][0]),title=str(t[0][1]))
        w.save()
        itert = iter(t) #This skips the first iteration of the for loop
        next(itert)
        for p in itert:
            w.tag_set.create(keyword=str(p[0]).lower(),value=int(p[1]))
    
    print('----------------------------------------------------------------------------------------------------')
    print('------------------Exist_Model_Parser\'s Time Elapsed: ', time.time()-start)

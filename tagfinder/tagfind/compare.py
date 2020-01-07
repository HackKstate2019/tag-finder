import time

from .models import Tag, Website

#Maybe just pass throught the WID & RR and pull the URL & the Title on the other side?

def compare(t):
    start = time.time()
    websDict=dict()
    webs=[]

    itert=iter(t)
    next(itert)
    for tag in itert:
        lowtag=str(tag[0]).lower() #Lowercases the IA's tags
        if Tag.objects.filter(keyword=lowtag).exists():

            wid=Tag.objects.filter(keyword=lowtag).values('website') #Have to use the for loops or we get a TypeError
            for x in wid:
                wid=str((x['website'])) #Tag's Website ID

            val=Tag.objects.filter(keyword=lowtag).values('value')
            for x in val:
                val=(x['value']) #Tag's Value
            rr=(val*tag[1])

            url=Website.objects.filter(id=wid).values('url')
            for x in url:
                url=str((x['url'])) #Tag's Website URL

            title=Website.objects.filter(id=wid).values('title')
            for x in title:
                title=str((x['title'])) #Tag's Article Title

            # for x in test: #Never runs the FOR loop
            #     if url in x:
            #         # x[2]+=rr
            #         print('testtttttt: ',x[2])
            #     else: test.append(tuple((url,title,rr)))
            
            # if testcounter>0: #Testing for URL Matching with If-In
            #     print(f'--------------------------------------------Test for Test. Counter = {testcounter}')
            #     for x in test:
            #         print('X in Test: ', x)
            #         print('X[2] in Test: ', x[2])
            #         print('X[0] in Test: ', x[0])
            #         print('URL of Current Found Tag: ', url)
            #         if x[0]==url:
            #             lst=list(x)
            #             lst[2]+=rr
            #             print('::::::::::::: Current Found Tag URL == X[0] :::::::::::::')
            #             x=tuple(lst)
            #             print('X[2] + Current Tag\'s RR: ', x[2])
            #         if url in x:
            #             print('::::::::::::: Found Current Tag URL IN X :::::::::::::')
            #         print('----------------------------------------------------------------------------------------------------')

            # if testcounter>0: #Kind of worked, but not really. Never got the new tuple to replace the old one.
            #     for x in test:
            #         if x[0]==url:
            #             lst=list(x)
            #             lst[2]+=rr
            #             x=tuple(lst)
            #         else: 
            #             test.append(tuple((url,title,rr)))
            #             print(f'----------Current Tag isn\'t in Test. Appended.')
            # else: 
            #     test.append(tuple((url,title,rr)))
            #     print(f'Adding the first instance to')

            # for x in test:
            #     print('{} : {}'.format(x[2])) #Prints content of test

            if wid in websDict: #Adds the Tag's value to the Website Dictionary
                websDict[wid]+=rr
            else: websDict[wid]=rr
    
    def getKey(item):
        return item[rr]

    webs=list(tuple(([x,y] for x,y in websDict.items())))
    webs=sorted(webs, key=getKey, reverse=True)
    top = []
    test= []

    for i in range(3):
        try:
            top.append(webs[i])
        except:
            top.append(tuple((0,0,0))) #Causing errors.

    print('Webs: ', webs)
    print('Top: ', top)

    for x in top:
        wid=x[0]
        rr=str(x[1])
        url=Website.objects.filter(id=wid).values('url')
        for x in url:
            url=str((x['url'])) #Tag's Website URL
        title=Website.objects.filter(id=wid).values('title')
        for x in title:
            title=str((x['title'])) #Tag's Article Title
        test.append(tuple((url,title,rr)))
        # test.append(tuple(('','','')))


    return test

    



    # print('Webs Test: ', webs[0][0])
    # print('----------------------------------------------------------------------------------------------------')
    # print('------------------Compare\'s Time Elapsed: ', time.time()-start)
    # print('----------------------------------------------------------------------------------------------------')
    # print('------------------WebsDict: ', websDict)
    # print('----------------------------------------------------------------------------------------------------')
    # print('------------------Webs: ', webs)
    # print('----------------------------------------------------------------------------------------------------')
    # print('------------------Test: ', test)
    # print('----------------------------------------------------------------------------------------------------')



    # for i in Website.objects.all():
    #     rr = 0
    #     for k in i.tag_set.all():
    #         for p in t:
    #             if p[0].lower()==str(k).lower():
    #                 rr+=(p[1]*k.value)
    #     webs.append(tuple((i.url,i.title,rr)))

    # for web in webs: #Makes sure that the Input Article can't be Recommended... lol
    #     if web[0]==t[0][0]:
    #         webs.remove(web)

#     webs=sorted(webs, key=getKey, reverse=True)
#     top = []
#     for i in range(3):
#         top.append(webs[i])
#     return top

# 

def pull(c):
    print('C\'s Output: ',c)
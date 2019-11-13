from .models import Website, Tag
import time

def compare(t):
    start = time.time()
    websDict=dict()
    webs=[]
    test=[]

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

            for x in test: #Never runs the FOR loop
                if url in x:
                    x[2]+=rr
                else: test.append(tuple((url,title,rr)))

            if wid in websDict: #Adds the Tag's value to the Website Dictionary
                websDict[wid]+=rr
            else: websDict[wid]=rr

    webs=list(tuple(([x,y] for x,y in websDict.items())))

    print('Webs Test: ', webs[0][0])
    print('----------------------------------------------------------------------------------------------------')
    print('------------------Compare\'s Time Elapsed: ', time.time()-start)
    print('----------------------------------------------------------------------------------------------------')
    print('------------------WebsDict: ', websDict)
    print('----------------------------------------------------------------------------------------------------')
    print('------------------Webs: ', webs)
    print('----------------------------------------------------------------------------------------------------')
    print('------------------Test: ', test)
    print('----------------------------------------------------------------------------------------------------')



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

# def getKey(item):
#     return item[2]
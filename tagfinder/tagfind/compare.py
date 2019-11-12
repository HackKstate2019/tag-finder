from .models import Website, Tag
import time

# s = Tag.objects.filter(keyword=t[tag]).values('website') Returns Website's ID
# s = Tag.objects.filter(keyword=t[tag]).values('value') Returns 
# Website.objects.get(id=s.foreignkey)

def compare(t):
    start = time.time()
    webs=[]

    itert=iter(t)
    next(itert)
    for tag in itert:
        taggy=str(tag[0]).lower() #Lowercases the IA's tags
        if Tag.objects.filter(keyword=taggy).exists():

            wid=Tag.objects.filter(keyword=taggy).values('website') #Have to use the for loops or we get a TypeError
            for x in wid:
                wid=(x['website'])

            val=Tag.objects.filter(keyword=taggy).values('value')
            for x in val:
                val=(x['value'])

            webs.append(tuple((wid,val)))

    print('----------------------------------------------------------------------------------------------------')
    print('------------------Compare\'s Time Elapsed: ', time.time()-start)
    print('----------------------------------------------------------------------------------------------------')
    print('------------------Webs: ', webs)
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
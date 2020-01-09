from .models import Tag, Website

def compare(t):
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

            if wid in websDict: #Adds the Tag's value to the Website Dictionary
                websDict[wid]+=rr
            else: websDict[wid]=rr
    
    def getKey(item):
        return item[rr]

    webs=list(tuple(([x,y] for x,y in websDict.items())))
    webs=sorted(webs, key=getKey, reverse=True) #Sorts the list of websites by RR, making the order descending.
    websorted = []
    top= []

    #Need to make sure that IA is not in websorted.
    print('T: ', t)

    for i in range(3):
        try:
            websorted.append(webs[i])
        except:
            websorted.append(tuple((0,0,0))) #Not 3 Websites, so we pass through a blank one.

    for x in websorted: #Takes the websorted 3 websites and puts them into a final tuple.
        wid=x[0]
        rr=str(x[1])
        url=Website.objects.filter(id=wid).values('url')
        for x in url:
            url=str((x['url'])) #Tag's Website URL
        title=Website.objects.filter(id=wid).values('title')
        for x in title:
            title=str((x['title'])) #Tag's Article Title
        top.append(tuple((url,title,rr)))

    return top
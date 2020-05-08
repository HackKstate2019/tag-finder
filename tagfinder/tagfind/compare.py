from .models import Tag, Website

def compare(t):
    websDict=dict() #Dictionary makes it easy to continually update websites' rr's.
    webs=[]

    itert=iter(t)
    next(itert)
    for tag in itert:
        lowtag=str(tag[0]).lower() #Lowercases the IA's tags
        print('tag: ',tag)
        print('lowtag: ',lowtag)
        if Tag.objects.filter(keyword=lowtag).exists():
            print('found em boss')

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
        else:
            print('nothin boss')
    
    def getKey(item):
        return item[rr]

    print('websdict: ',websDict)

    webs=list(tuple(([x,y] for x,y in websDict.items())))
    webs=sorted(webs, key=getKey, reverse=True) #Sorts the list of websites by RR, making the order descending.
    websorted = []
    top= []

    for i in range(len(webs)):
        websorted.append(webs[i]) #Converts dictionary to tuple, 'cos I feel like it.

    print('websorted: ',websorted)

    ia=Website.objects.filter(url=t[0][0]).values('id') #IA's WID

    print('ia: ',ia)

    for x in websorted: #Takes the websorted 3 websites and puts them into a final tuple.
        wid=x[0]
        for y in ia:
            ia_id=str(y['id'])
            if wid == ia_id: #X's WID = IA's WID
                print('wid same')
                weblist=list(websorted) #Can't change tuples, have to make it a list.
                weblist.remove(x) #Removes IA from Websorted.
                websorted=tuple(weblist) #Reconverts to Tuple, just 'cos.
            else:
                print('wid diff')
                wid=x[0]
                rr=str(x[1])
                url=Website.objects.filter(id=wid).values('url')
                for x in url:
                    url=str((x['url'])) #Tag's Website URL
                title=Website.objects.filter(id=wid).values('title')
                for x in title:
                    title=str((x['title'])) #Tag's Article Title
                top.append(tuple((url,title,rr))) #Adds recommended website to final tuple.

    print('top: ',top)

    while len(top) < 3: #If there're less than 3 recommended websites then we add a pre-made blank one.
        rr=''
        url=Website.objects.filter(id=0).values('url')
        for x in url:
            url=str((x['url'])) #Tag's Website URL
        title=Website.objects.filter(id=0).values('title')
        for x in title:
            title=str((x['title'])) #Tag's Article Title
        top.append(tuple((url,title,rr))) #Adds blank website to final tuple.

    return top
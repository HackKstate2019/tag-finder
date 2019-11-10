from .models import Website, Tag

def compare(t):
    webs=[]
    for i in Website.objects.all():
        rr = 0
        for k in i.tag_set.all():
            for p in t:
                if p[0].lower()==str(k):
                    rr+=(p[1]*k.value)
        webs.append(tuple((i.url,i.title,rr)))

    webs=sorted(webs, key=getKey, reverse=True)
    top = []
    for i in range(3):
        top.append(webs[i])
    return top

def getKey(item):
    return item[2]
from .models import Website, Tag

def print_test(t):
    message='Not Found'
    first=Website.objects.first()

    if t[0][0] in Website.objects.all():
        message='Found'

    if t[0][0]==first:
        message='URL === FIRST'

    # if t[0][0] in first: #Doesn't work (Website not iterable error)
    #     message='URL in FIRST'

    if Website.objects.filter(url=t[0][0]).exists():
        message='FILTER FOUND URL'

    print('----------------------------------------------------------------------------------------------------')
    print(f'------------------URL: {t[0][0]}')
    print(f'------------------TITLE: {t[0][1]}')
    print('----------------------------------------------------------------------------------------------------')
    print(f'------------------TEST OUTPUT: {message}')
    print('----------------------------------------------------------------------------------------------------')
    print(f'------------------WEBSITE.OBJECTS.FIRST(): {first}')
    print('----------------------------------------------------------------------------------------------------')
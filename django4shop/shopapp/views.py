from django.shortcuts import render

# Create your views here.
def mainFunc(request): # 
    return render(request,'main.html')


def page1Func(request):
    return render(request,'page1.html')


def page2Func(request):
    return render(request,'page2.html')


def cartFunc(request): # 장바구니 
    name = request.POST.get("name") 
    price = request.POST["price"]
    # print(name,price)
    product= {'name': name , "price": price}
   
    productlist = []
    
    if 'shop' in request.session: # 세션이 존재한다면
        productlist = request.session['shop'] # 세션에서 제품리스트를 꺼내고 
        productlist.append(product) # 꺼낸 제품목록에 새로운 제품을 추가한다. 
        request.session['shop'] = productlist # 이렇게 만들어진 제품목록을 세션에 담는다.
        
    else: # 없으면 세션 생성 후 제품담기 
        productlist.append(product) # 제품을 담는다. 
        request.session['shop'] = productlist  # 세션에 제품을 넣는다. shop이라는 key에 value값으로 productlist를 넣는다.
        
    print(productlist) # 제품 리스트 출력
    context = {} #dict
    context['products'] = request.session['shop'] # products에 shop의 value를 넣어줌.
    # {'product' : request.session['shop'] }
    return render(request,"cart.html", context)
    

def buyFunc(request):
    if 'shop' in request.session: 
        productlist = request.session['shop']
        
        total = 0
        for p in productlist:
            total += int(p['price'])
        
        print('total : ', total)
        
        # 결제 시스템으로 결제가 완료되었다고 가정하자.
        
        # del request.session['shop'] 세션 내의 특정 키가 제거되어진다.
        request.session.clear() # 세션 내에 모든 키가 제거된다.
        
    return render(request,"buy.html",{'total' : total})     
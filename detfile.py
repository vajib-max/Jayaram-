jaytotal=[]
abitotal=[]
vajitotal=[]
sanjaytotal=[]
for i in range(1,8,1):
    print('---------ROUND',i,'----------')
    p1=int(input('jay = '))
    p2=int(input('abi = '))
    p3=int(input('vaji = '))
    p4=int(input('sanjay = '))
    jaytotal.append(p1)
    abitotal.append(p2)
    vajitotal.append(p3)
    sanjaytotal.append(p4)
    p1=sum(jaytotal)
    print('jay = ',p1)
    p2=sum(abitotal)
    print('abi = ',p2)
    p3=sum(vajitotal)
    print('vaji = ',p3)
    p4=sum(sanjaytotal)
    print('sanjay = ',p4)
if p1<p2 and p1<p3 and p1<p4:
    print('\n\nJAY IS WINNER')
if p2<p1 and p2<p3 and p2<p4:
    print('\n\nABI IS WINNER')
if p3<p1 and p3<p2 and p3<p4:
    print('\n\nVAJI IS WINNER ')
if p4<p1 and p4<p2 and p4<p3:
    print('\n\nSANJAY IS WINNER')

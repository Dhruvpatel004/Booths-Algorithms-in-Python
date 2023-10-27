#Function to perform binary Addition 
def addtion(a,b):
    n=len(a)
    m=len(b)
    l=max(n,m)
    a = a.zfill(l)
    b = b.zfill(l)
    carry=0
    ans=''

    for i in range(l-1,-1,-1):
        tem=carry+int(a[i])+int(b[i])
        if tem<2:
            ans=str(tem)+ans
            carry=0
        elif tem==2:
            ans='0'+ans
            carry=1
        elif tem==3:
            ans='1'+ans
            carry=1
    
    ans = ans.zfill(l)
    return ans

#Function to perform 1's Complement
def ones_complement(num):
    comp=''
    for i in num:
        if i=='0':
            comp+='1'
        else:
            comp+='0'
    return comp

#function to perform 2's Complement
def twos_complement(num):
    one_com=ones_complement(num)
    two_com=addtion(one_com,'1')
    return two_com

#Function to Convet number to binary
def set_bin(num):
    if (num>=0):
        num=bin(num).replace("0b","")
        return num
    else:
        num=bin(num).replace("-0b","")
        return num

#function to set Binary as signed (by 2's complement)
def set_signed(d,num):
    if d>=0:
        return '0'+num
    else:
        return '1'+twos_complement(num)

#main Function Start here
if __name__=='__main__':
    #take input from user 
    multiplicand =int(input("Enter multiplicand : "))
    multiplier=int(input( "Enter multiplier   : "))
    #convert it to binnary
    n1=set_bin(multiplicand)
    n2=set_bin(multiplier)
    m=max(len(n1),len(n2))
    n1=n1.zfill(m)
    n2=n2.zfill(m)
    #set value of br and qr and br1=br'+1 
    br=set_signed(multiplicand,n1)
    qr=set_signed(multiplier,n2)
    br1=twos_complement(br)

    print('br                        :',br)
    print('br\' ( in 2\'s complement ) :',br1)
    print("qr                        :",qr,'\n')

    #set Accumlator with 0
    ac=''
    ac = ac.zfill(m+1)
    qn1='0'
    qn=qr[-1]

    print('Qn\tQn+1\t\t','AC','\t','QR','\t','Qn+1','\t','SC')
    print('----------------------------------------------------')
    print('\t\tInitial\t',ac,'\t',qr,'\t',qn1,'\t',m+1)

    for i in range(m+1):
        qn=qr[-1]

        #Condition for Subtraction
        if qn=='1' and qn1=='0':
            ac=addtion(ac,br1)
            print(qn,'\t',qn1,'\tSub BR\t',br1,'\t\t\t')
            print('\t\t\t',ac,'\t',qr,'\t\t')
        
        #Condition for Addition
        elif qn=='0' and qn1=='1':
            ac=addtion(ac,br)
            print(qn,'\t',qn1,'\tAdd BR\t',br,'\t\t\t')
            print('\t\t\t',ac,'\t',qr,'\t\t')
        
        #performing ASHR
        qn1=qr[-1]
        qr=ac[-1]+qr[:m]
        ac=ac[0]+ac[:m]
        print('\t\tAshr\t',ac,'\t',qr,'\t',qn1,'\t',m-i)

    ans=ac+qr
    if(ans[0]=='1'):
        print('Result : ',ans)   
        ans=twos_complement(ans)
        print('Result in decimal: -',int(ans,2))
    else:
        print('Result : ',ans)   
        print('Result in decimal: ',int(ans,2))

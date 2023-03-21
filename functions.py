#list
def list_contacts():
    
    global l1
    print("list of {} contacts:".format(len(l1)-1))
    
    for i in range(1,len(l1)):
        print(end=".")
        
        for j in range(len(l1[i])):
            print(l1[i][j],"\t",end="")
        print()
        
#search2    
def string_check(inp,check):
    bol=False
       
    for i in range(len(check)-len(inp)+1):
        
            if(inp[0]==check[i]):
                bol=True
                a=0
                
                for x in range(i,i+len(inp)):
                    
                    if(check[x]==inp[a]):
                        a+=1
                    else:
                        bol=False
                        break
    return bol
#search
def SEARCH_CALL(Search_var):
    
    global l1
    value=0
    
    for i in range(1,len(l1)):
        for j in l1[i]:
            
            if string_check(Search_var,j):
                value=i
                break
                
    return value
#add
def ADD_ELE():
    
    a=list((input("Enter contact to be added.").upper()).split())
    val=SEARCH_CALL(a[0])
    
    if(val!=0):
        print("ALREADY EXISTS")
        
    else:
        if(len(a[0])<=6):
            a[0]=a[0]+" "*(6-len(a[0]))
        
        if(len(a[1])==10):
            l1.append(a)
            
        else:
            print("Wrong number")
#delete           
def DEL_ELE(ele):
    
    global l1
    val=SEARCH_CALL(ele)
    
    if(val==0):
        print("NOT FOUND")
        
    else:
        
        for j in l1[val]:
            print(j,end="\t")
        print()
        
        print("INPUT 'YES' FOR DELETE AND 'NO' TO CANCEL")
        
        del_str=input().upper()
        if(del_str=="YES"):
            l1.pop(val)
#edit
def edit_fun(var):
    
    global l1
    val=SEARCH_CALL(var)
    
    for j in l1[val]:
        print(j,end="\t")
    print()
    
    if(val==0):
        return 0
    
    print("YES FOR EDIT, NO TO CANCEL.")
    bol=input().upper()
    
    if(bol=="YES"):
        print("Enter correct values.")
        
        a=list((input().upper()).split())
        if(len(a[0])<=6):
            a[0]=a[0]+" "*(6-len(a[0]))
        
        if(len(a[1])==10):
            l1[val] = a
            
        
    return 1

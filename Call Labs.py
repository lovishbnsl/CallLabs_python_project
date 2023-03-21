import functions.py

l1=[["No contact found"],["HARVEEN MAM","2332673217"],["LOVISHA","7614128901"],["LAVISH","4877488473"],["LOVISH","7214167566"],["CHARVI","7654856878"],["KHUSHI","7894561230"],["MANAN ","1555155522"],["MANYA ","5656568989"],["MANNATPREET","9099980888"],["LUCKSH","3242342342"],["JANVI ","9099983243"],["KUNSH ","6543654396"],["MADHVI","7543654369"]]                                                   
print("\U0001F50D","SEARCH FROM {}".format(len(l1)-1),"CONTACTS")
list_contacts()

print("S FOR SEARCH:","E FOR EDIT:","D FOR DELETE:","A FOR ADD:","C FOR CLOSING:","L FOR ALL CONTACTS")
def loops():
    superb=1
    while superb>0:

        INP=input("Enter Your Choice(s,e,d,a,c,l):").upper()
        if(INP=="S"):

            Search_var=list(input("Enter ELEMENT to be Searched:").upper())
            val=SEARCH_CALL(Search_var)
            for j in l1[val]:
                print(j,end="\t")
            print()

        elif(INP=="C"):
            break

        elif(INP=="A"):

            ADD_ELE()
            list_contacts()

        elif(INP=="D"):

            del_var=input("ENTER CONTACT TO BE DELETED:").upper()
            DEL_ELE(del_var)
            list_contacts()

        elif(INP=="E"):

            edit_var=input("ENTER CONTACTS TO BE EDITED:").upper()
            edit_fun(edit_var)
            list_contacts()


        elif(INP=="L"):

            list_contacts()
loops()

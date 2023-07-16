###################### LIST #######################

lo = [1,2,3,'one','two','three',None,True,False]
for i in lo:
    if isinstance(i,int):
        print(i)

for i in lo:
    if isinstance(i,str):
        print(i) 

for i in lo:
    if isinstance(i,bool):
        print(i) 

for i in lo:
    if isinstance(i,float):
        print(i) 

for i in lo:
    if i is None:
        print(i)

# to delete all strings togther from list
lo = [1,2,3,'one','two','three',None,True,False,10.5,9.8]
lo = [i for i in lo if  not isinstance(i,str)]
print(lo)
# end        
# to delete all int togther from list
lo = [1,2,3,'one','two','three',None,True,False,10.5,9.8]
lo = [i for i in lo if  not isinstance(i,int)]
print(lo)
# end  
# to delete all booleans togther from list
lo = [1,2,3,'one','two','three',None,True,False,10.5,9.8]
lo = [i for i in lo if  not isinstance(i,bool)]
print(lo)
# end   
# to delete all float togther from list
lo = [1,2,3,'one','two','three',None,True,False,10.5,9.8]
lo = [i for i in lo if  not isinstance(i,float)]
print(lo)


# enumerate() method
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits):
    print(index, value)

# end
                   
################################# END LIST ####################    

########################### DICTIONARY ################################

# two ways of creating dictionary using dict constructor
dict1 = dict(name='abu',age=12)
print(dict1)
dict2 = dict({'name':'abu','age':18})
print(dict2)
# end
######################### END DICTIONARY ########################  
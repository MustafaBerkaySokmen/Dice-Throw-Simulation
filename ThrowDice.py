import random
#random.seed(99)

def throw_single_die():
    """
    This function is given to you. DO NOT MODIFY IT. 
    """
    return random.randint(1,6)


def record_dice_throws(throws):
    res={}
    for i in range(throws):
        a=throw_single_die()
        b=throw_single_die()
        tup=(a,b)
        if tup in res:
            res[tup]+=1
        else:
            res[tup]=1
    
    return res
   

def write_dict_to_file(throws_dict):
    f1=open("diceresults.txt","w")
    x=1
    for i in range(1,7):
        for j in range(1,7):
             value=str(throws_dict[(i,j)])
             
             if x<6:
                 x+=1
                 f1.write(value+" " )
             else:
                 x=1
                 f1.write(value+"\n")
                
    f1.close() 
    
    pass


def calculate_frequencies(throws_dict):
    probab=[]
    res2=[(1,1)]
    res3=[(1,2),(2,1)]
    res4=[(1,3),(2,2),(3,1)]
    res5=[(1,4),(2,3),(3,2),(4,1)]
    res6=[(1,5),(2,4),(3,3),(4,2),(5,1)]
    res7=[(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)]
    res8=[(2,6),(3,5),(4,4),(5,3),(6,2)]
    res9=[(3,6),(4,5),(5,4),(6,3)]
    res10=[(4,6),(5,5),(6,4)]
    res11=[(5,6),(6,5)]
    res12=[(6,6)]
    res2count=0
    res3count=0
    res4count=0
    res5count=0
    res6count=0
    res7count=0
    res8count=0
    res9count=0
    res10count=0
    res11count=0
    res12count=0
    for i in throws_dict:
        if i in res2:
            res2count+=throws_dict[i]
    for i in throws_dict:
        if i in res3:
            res3count+=throws_dict[i]
    for i in throws_dict:
        if i in res4:
            res4count+=throws_dict[i]        
    for i in throws_dict:
        if i in res5:
            res5count+=throws_dict[i]        
    for i in throws_dict:
        if i in res6:
            res6count+=throws_dict[i]
    for i in throws_dict:
        if i in res7:
            res7count+=throws_dict[i]
    for i in throws_dict:
        if i in res8:
            res8count+=throws_dict[i]
    for i in throws_dict:
        if i in res9:
            res9count+=throws_dict[i]
    for i in throws_dict:
        if i in res10:
            res10count+=throws_dict[i]                               
    for i in throws_dict:
        if i in res11:
            res11count+=throws_dict[i]                               
    for i in throws_dict:
        if i in res12:
            res12count+=throws_dict[i]
            
            
    probab.append((2,res2count/10000))  
    probab.append((3,res3count/10000))
    probab.append((4,res4count/10000))
    probab.append((5,res5count/10000))
    probab.append((6,res6count/10000))
    probab.append((7,res7count/10000))
    probab.append((8,res8count/10000))
    probab.append((9,res9count/10000))
    probab.append((10,res10count/10000))
    probab.append((11,res11count/10000))
    probab.append((12,res12count/10000))

     
    return probab
    

def main():
    """
    The code given here is for you test your functions. You can modify
    it to perform more tests. When submitting, make sure the code you
    leave under main() does not cause a syntax error. 
    """
    result_dict = record_dice_throws(10000)
    print(result_dict)
    write_dict_to_file(result_dict)
    print(calculate_frequencies(result_dict))

    
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
main()
my_list=[1,2,3,4,5,6,7,8,9]
#my_new_list=list(filter(lambda x : (x%2 ==0),my_list) )
#print(my_new_list)

def f1 (x) :
    if x%2==0 :
        return True
    else:
        return False

my_new_list1=list(filter(f1,my_list))
print(my_new_list1)
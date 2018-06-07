def print_params(x,y,z=3,*posvar,**params):
    print(x,y,z)
    print(posvar)
    print(params)
print_params(1,2,3,4,5,6,7,x1=5,y1=7)


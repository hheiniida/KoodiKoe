from math import sqrt
num=0

#start
def start():
    option=input("Give 1, 2 or q:")
    
    if option == "1":
        num=int(input("Give triangular number:"))
        count_factors(num)

    if option=="2":
       num=int(input("Give minimum number of divisors triangle number should have?"))
       count_second(num)

    if option=="q":
        quit



#return the triangular number of the number:
def count_factors(num): 
    xy=0
    sum_=0
    for i in range(1, num+1):
        xy += 1
        sum_ += xy
    print(sum_)

    list1=[]
    
    for j in range(1, sum_ + 1):
     
       if sum_ % j == 0:
           print(j) 
           list1.append(j)


    L="Divisors and sum of "+ str(sum_) +"th term.txt"
        
    # open file in write mode
    with open(L, 'w') as fp:
        fp.write(str(sum_))
        for item in list1:
            # write each item on a new line
            fp.write("\n"+ str(item))
        


#return minimum number of divisors triangle number
def count_second(num):

# num on jakajien määrä

    apu = 1
    count = 1

    while True:

        dividors = []

        for j in range(1, count + 1):
     
            if count % j == 0:
                dividors.append(j)

        if len(dividors) >= num:
            break

        apu += 1
        count += apu
        
    #print
    print("The triangle number is",str(count),"and divisors are ")
    for div in dividors:
        print(div)
           
    #write into file    
    L="The first triangle number "+ str(num) + ".txt"
    with open(L, "w") as fp:
        fp.write(str(count))  
        for i in dividors:
            # write each item on a new line
            fp.write("\n" + str(i))
        
    

#main
start()

import time
from collections import OrderedDict

#start the timer
start_time = time.time()

#ask the number from the user
input_nro=int(input("Give me the number:"))


counter=0
my_list=[]
my_primes=[]

for num in range(2, input_nro + 1):
    #all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
              break
            else:
                #add all prime numbers in range of 2 to input_nro to a list
                my_list.append(num)

#go though all the primes
for item in my_list:
    if (input_nro % item) == 0:
        my_primes.append(item)

res=list(OrderedDict.fromkeys(my_primes))
print("Prime factors found:", res)
end_time = time.time()
elapsed_time = end_time - start_time
print("It took ", elapsed_time, "seconds to find those")

with open("output.txt", "w") as output_file:
    L="Prime Factors of number "+ str(input_nro)+ "are "+ str(res)+". \n"
    L2="It took "+ str(elapsed_time)+ "seconds to find those."
    output_file.write(str(L))
    output_file.write(str(L2))


# get file as an input
input_file = input("Give the file name: ")
my_list=[]


with open(input_file, 'r') as my_file:

    #split the rows into a,b,c parts
    for line in my_file:
        print(line)
        parts = line.split(" ")
        
        a=parts[0]
        b=parts[1]
        c=parts[2]
        apu=0
        
        my_list=[]

        #go file though line by line
        while apu <= int(c):
            apu += 1

            if int(a) <= int(c): 
                if(apu * int(a))<=int(c):
                    my_list.append(apu * int(a))
                

            if int(b) <= int(c):
                if (apu * int(b)) <int(c):
                    my_list.append(apu * int(b))

        #sort the list and write list to output file        
        my_list.sort()
        my_list = list(dict.fromkeys(my_list))
        output_file= open("output2.txt","a")
        output_file.write(str(c)+":"+ str(my_list)+"\n")

#close files        
my_file.close()
output_file.close()
        



array = []
Maxinum = 0
Minimum = 0
while True:
    
    result = input('value:')
    try:
        temp  = int(result)
        array.append(temp)
    except:
        if result.startswith('done'):
            lenght = len(array)
            
            i = 0
            j=0
            while i < lenght -1:
                
                for j in range(lenght-1):
                       
                        if array[j] > array[ j+ 1 ]:
                            temp_pos = array[j]
                            array[j] = array[j+1]
                            array[j+1] = temp_pos
                        else:
                            pass

                        j+=1
                i+=1

            print(array)
            print(f"Maxinum {array[-1]}")
            print(f"Minimum{array[0]}")    
                
            exit()
        else:
            print('Invalid Input')
            continue

        
    
        
    


    






import csv
pull =  open('pull.csv','w')
csvwriter = csv.writer(pull)
def fnd(_1:int,_2:int,_3:int,_4:int,_5) -> str:
    csvwriter.writerows([str(_1),str(_2),str(_3),str(_4),str(_5)])
    if _5 == None:
        finder = [0,0,0,0]
        with open('short.csv', mode ='r')as file:  
            csvFile = csv.reader(file)   
            for lines in csvFile:  
                    if lines[0] == 'shot':
                         continue
                    a, b = lines[1].split('-')
                    a, b = int(a), int(b)
                    if a < _1 and b > _1:
                         finder[0] = 1

                    a, b = lines[2].split('-')
                    a, b = int(a), int(b)
                    if a < _2 and b > _2:
                         finder[1] = 1

                    a, b = lines[3].split('-')
                    a, b = int(a), int(b)
                    if a < _3 and b > _3:
                         finder[2] = 1

                    a, b = lines[4].split('-')
                    a, b = int(a), int(b)
                    if a < _4 and b > _4:
                         finder[3] = 1
                    if finder[0] ==1 and finder[1] ==1 and finder[2] ==1 and finder[3] ==1:
                         print(lines[0])
                         return lines[0]
                    else:
                        finder = [0,0,0,0]

    else :
         with open('short.csv', mode ='r')as file:  
            csvFile = csv.reader(file)  
            for lines in csvFile: 
                    if lines[0] == 'shot':
                         continue
                    a, b = lines[-1].split('-')
                    a,b = int(a), int(b)
                    if a < _5 and _5:
                         return lines[0]
                    
    

    return None
    
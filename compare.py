import matplotlib.pyplot as plt
plt.xlabel('edges')
plt.ylabel('time in second')
def func():
    my_file=open('/home/neil/Documents/IIITH/sem1/APS/CS3000-Project/outfile1.txt','r')
    read_data = my_file.readlines()
    #print(read_data)
    my_file.close()
    list1 = []
    list2 = []
    lst = []
    for lines in read_data:
        l = lines
        x,y,z= l.split(' ')
        lst.append((float(x),float(y)))
        #print(x)
        #print(y)
    lst.sort(key=lambda x: x[1])
    for i in lst:
        x,y = i
        list1.append(float(x))
        list2.append(float(y))
        #print(x)
        #print(y)
    plt.plot(list1, list2, label="sort")
    my_file=open('/home/neil/Documents/IIITH/sem1/APS/CS3000-Project/outfile2.txt','r')
    read_data = my_file.readlines()
    #print(read_data)
    my_file.close()
    list1 = []
    list2 = []
    lst = []
    for lines in read_data:
        l = lines
        x,y,z = l.split(' ')
        lst.append((float(x),float(y)))
        #print(x)
        #print(y)
    lst.sort(key=lambda x: x[1])
    for i in lst:
        x,y = i
        list1.append(float(x))
        list2.append(float(y))
        #print(x)
        #print(y)
    plt.plot(list1, list2, label="vEB")
    my_file=open('/home/neil/Documents/IIITH/sem1/APS/CS3000-Project/outfile3.txt','r')
    read_data = my_file.readlines()
    #print(read_data)
    my_file.close()
    list1 = []
    list2 = []
    lst = []
    for lines in read_data:
        l = lines
        x,y,z = l.split(' ')
        lst.append((float(x),float(y)))
        #print(x)
        #print(y)
    lst.sort(key=lambda x: x[1])
    for i in lst:
        x,y = i
        list1.append(float(x))
        list2.append(float(y))
        #print(x)
        #print(y)
    plt.plot(list1, list2, label="fib")
    plt.legend()
    plt.show()
func()
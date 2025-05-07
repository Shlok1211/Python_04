try:
    f = open('sample1.txt','r')
    reading1 = f.readline()
    reading2 = f.readline()
    print('Reading file content :')
    print('Line 1:',reading1)
    print('Line 2:',reading2)
    f.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
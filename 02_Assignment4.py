f = open('output.txt','w')
txt1 = input('Enter text to write to the file: ')
f.write(txt1)
print('Data successfully written to output.txt\n')
f.close()

f = open('output.txt','a')
txt2 = input('Enter additional text to append: ')
f.write('\n' + txt2)
print('Data successfully appended\n')
f.close()

f = open('output.txt','r')
reading = f.read()
print('Final content of output.txt: ')
print(reading)
f.close()


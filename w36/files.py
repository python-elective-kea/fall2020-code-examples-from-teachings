


f = open('test.txt', 'r')
print(f.read())

f = open('test.txt')
print(f.readline())

f = open('test.txt')
print(f.readlines())


#s = open('yyy.docx', 'w')
#s.write('Hello from my script file')


s = open('yyy.docx', 'a')
s.write('Hello from my script file')
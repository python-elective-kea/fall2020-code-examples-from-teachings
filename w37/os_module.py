import os

for i in os.listdir():
    print(i)


os.mkdir('Test')
os.chdir('Test')
print(os.listdir())

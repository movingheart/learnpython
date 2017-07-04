i = 0
numbers = []
'''
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d\n" % i
'''

def check_while(num, step):
    numbers = []
    i = 0
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d\n" % i

check_while(6, 2)

print "The numbers:"

for num in numbers:
    print num


    

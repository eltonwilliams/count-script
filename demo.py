i=1

while i<=150:
    print "Count at :",i
    if i == 150/2:
        print "\nhalf way through, almost there\n"
    i+=1

print "\n\n--------------------------------------"
print "\nthis is now an acceptable amount"
i-=1
print "\nthe amount now is",i
print "\n\nnow we will subtract 50 from",i
print i,"- 50"
i-=50
print "\nthe amount now is",i
print "\n\nnow we will count backwards from",i
while i>=0:
    print "Count at :",i
    if i == 50:
        print "\nhalf way through, almost there\n"
    i-=1

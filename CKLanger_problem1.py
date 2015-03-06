n=int(input("Enter an integer: "))
x=n   # stores the integer for print at the end, see below
r=[]  # list to store each 0 or 1 for binary rep.
while (n>0):
    y=int(float(n%2)) # takes integer mod 2
    r.append(y) # appends each y to r
    n=(n-y)/2  # subtracts remainder to get integer part,repeat until quotient is zero
string=""     # to present the elements of r[]
for j in r[::-1]:    # slice for a new reversed list w/o modifying original
    string=string+str(j)
print("The integer",x,"has binary representation",string)




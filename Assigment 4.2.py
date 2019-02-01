def computepay(h,r):
    if h > 40:
	    return 40*r + (h-40)*1.5*r
    else:
	    return h*r

hrs = input("Enter Hours:")
p = computepay(10,20)
print("Pay",p)

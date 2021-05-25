a = 0
n = True
while n == True:
    for x in range(1, 9699690**2+1):
        #print(x, end="")
        for y in range(x + 1, 9699690**2+1):
            #print(y, end="")
            if (x*y) >= 9699690**2:
                n = False
                break
            for z in range(y + 1, 9699690**2+1):
                #print(z)
                if (x*y*z) == 9699690**2:
                    a += 1
                    print(f"A: {a} \nX: {x} || Y: {y} || Z: {z} ")
                elif (x*y) >= 9699690**2:
                    n = False
                    break

print("AAAAAAAAAAAAAAAAAAAAAAAAA: ", end="")
print(a)
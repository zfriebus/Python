def factoral(n):
    if n <= 1:
        return 1
    else:
        return n * factoral(n-1)
    
def main():
    n = int(input("enter a non-negative integer: "))
    m = factoral(n)
    print("The factorial of", (n), "is", (m))
          
          
         
main()




   
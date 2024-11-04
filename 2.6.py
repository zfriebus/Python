def main():
 flowers = input("Enter the names of flowers: ")
 done = [flowers]
 if flowers == "sunflower":
  print("sunflower = 1")
 if flowers == "rose":
  print("rose = 2")
  if flowers == "tulip":
   print("tulip = 3")
   if not "sunflower" or "rose" or "tulip":
     print("try, rose, sunflower, or tulip")
     return flowers
 try:
    print(f"entered {flowers} is {done[flowers]}")
 except IndexError:
    print("IndexError: The index you entered is out of range.")

main()



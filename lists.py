daily = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
steps = []
i = 1

print (range(len(daily)))


for i in range(7):
    Day_of_week = daily[i]
    dailysteps = int(input("How many steps did you have on " + Day_of_week + ": ")) 
    print("You had", {dailysteps}, "on", {daily[i]})
    steps.append(dailysteps)
    i = i + 1
    #total= dailysteps/ range
#average = round(total / len(steps))

"""
If you were standing on the moon right now, your weight would be
16.5 percent of what it is on Earth. You can calculate that by mul-
tiplying your Earth weight by 0.165.
If you gained a kilo in weight every year for the next 15 years,
what would your weight be when you visited the moon each year
and at the end of the 15 years? Write a program using a for loop
that prints your moon weight for each year.
"""

weight = int(input("Enter Your current weight: "))

for i in range(1, 16):
    yr = i
    moon_weight = weight * 0.165
    print("Year %s your weight on the moon is %s" % (yr, moon_weight))
    weight += 1

# The ch-#4 puzzle on moon weight with function with 2 parameters.

def basic_moon_weight(weight, increase):
    for year in range(1, 16):
        moon_wt = weight * 0.165
        weight += increase
        print("Year %s your weight in the moon is %s" % (year, moon_wt))


basic_moon_weight(64, 1)

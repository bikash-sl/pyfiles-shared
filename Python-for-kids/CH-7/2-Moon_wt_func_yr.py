# The ch-#4 puzzle on moon weight with function with 3 parameters.


def basic_moon_weight(weight, gain, no_of_yrs):
    for year in range(1, (no_of_yrs + 1)):
        moon_wt = weight * 0.165
        weight += gain
        print("Year %s your weight in the moon is %s" % (year, moon_wt))


basic_moon_weight(64, 1, 12)

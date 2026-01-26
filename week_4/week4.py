def average(num1, num2, num3):
    """
    Calculates the average of 3 numbers.
    Param: num1 int
    Param: num2 int
    Param: num3 int
    return: average int
    """
    return (num1 + num2 + num3)/3


print(average(7, 5, 9))
print(f"{average(6, 6, 7):.3f}")


"""
2. If you move the function definition after
the calls the program will fail to run because
a function called average is not defined when its called.

3. Again the program fails if you try to use a function parameter
outside of the function itself. This is due to the fact that
a parameters scope is local and not global.
"""

print()


def dog_to_human_years(dog_age):
    """
    Converts a dogs age to the human equivalent.
    Param: dog_age int
    return: years int
    """
    return 24 + (dog_age - 2) * 4


dog_years = [5, 11]
for d in dog_years:
    print(d, "dog years is equivalent to",
          dog_to_human_years(d), "human years.")

print()

appreciation_map = {
    "German": 0.95,
    "Japanese": 0.93,
    "Italian": 1.05,
}


def calculate_car_value(price, years, nation):
    """
    Calculates the estimated value of a car.
    Param: purchase_price int
    Param: years int
    Param: nation str
    returns: estimated_value int
    """
    value = 0
    if nation in appreciation_map:
        value = price * (appreciation_map[nation] ** years)
        print(f"The value of {nation} car will be ${value:.2f}",
              f"after {years} years.")
    else:
        print(f"No data on {nation} cars.")
        return


calculate_car_value(30_000, 10, "German")
calculate_car_value(10_000, 5, "Japanese")
calculate_car_value(45_100, 25, "Italian")

print()

print("Dog age calculator:")
name = input("What is your dog's name? ")
age = int(input(f"How old is {name}? "))
print(f"Your {name} is {dog_to_human_years(age)} human years old.")

print()


def price_of_ice_cream(scoops):
    """
    Calculates the price of an ice cream cone.
    Param: number_of_scoops int
    returns: price int
    """
    return (scoops * 1.15) + 2.25


print("Ice cream cone price calculator: ")
scoops = int(input("How many scoops would you like? "))
print(f"A {scoops}-scoop cone will cost ${price_of_ice_cream(scoops)}.")

print()

months = "Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec".split(",")

cells = """
1980,1.755,1.775,1.718,1.769,1.822,1.832,1.831,1.873,1.825,1.879,1.878,1.920
1981,1.938,2.019,1.992,2.024,2.008,2.006,2.024,2.014,2.042,2.032,2.028,2.064
1982,2.128,2.075,2.061,2.089,2.043,2.060,2.092,2.095,2.105,2.136,2.187,2.163
1983,2.179,2.139,2.091,2.107,2.140,2.141,2.122,2.135,2.193,2.249,2.214,2.184
1984,2.189,2.191,2.171,2.210,2.203,2.193,2.212,2.232,2.301,2.259,2.223,2.231
1985,2.284,2.291,2.290,2.291,2.312,2.276,2.293,2.273,2.345,2.347,2.290,2.294
1986,2.317,2.346,2.331,2.382,2.368,2.325,2.369,2.319,2.360,2.377,2.397,2.405
1987,NULL_,2.468,2.447,2.438,2.481,2.428,2.467,2.482,2.470,2.492,2.449,2.438
1988,2.495,2.475,2.406,2.430,2.457,2.432,2.443,2.442,2.446,2.489,2.471,2.536
1989,2.547,2.560,2.595,2.607,2.591,2.589,2.566,2.614,2.595,2.639,2.629,2.667
1990,2.719,2.656,2.569,2.589,2.585,2.586,2.576,2.634,2.614,2.613,2.574,2.540
1991,2.546,2.522,2.561,2.521,2.561,2.585,2.592,2.605,2.621,2.594,2.588,2.632
1992,2.631,2.638,2.546,2.628,2.577,2.599,2.562,2.615,2.583,2.603,2.531,2.489
1993,2.567,2.551,2.563,2.509,2.411,2.528,2.432,2.548,2.497,2.610,2.596,2.591
1994,2.532,2.515,2.581,2.636,2.638,2.624,2.665,2.646,2.663,2.709,2.683,2.617
1995,2.659,2.550,2.686,2.629,2.634,2.649,2.665,2.667,2.683,2.735,2.610,2.675
1996,2.665,2.673,2.752,2.728,2.825,2.827,2.851,2.966,3.041,3.077,2.978,2.940
1997,2.947,2.928,2.920,2.903,2.876,2.877,2.844,2.927,2.895,2.925,2.928,3.022
1998,3.041,2.996,2.969,3.060,2.995,3.051,3.133,3.147,3.184,3.272,3.373,3.301
1999,3.379,3.291,3.231,3.266,3.195,3.306,3.238,3.250,3.280,3.380,3.336,3.404
2000,3.324,3.340,3.275,3.338,3.347,3.546,3.461,3.542,3.586,3.620,3.320,3.660
2001,3.673,3.609,3.660,3.651,3.633,3.703,3.720,3.841,3.815,3.824,3.463,3.836
2002,3.425,3.810,3.819,3.723,3.800,3.752,3.883,3.783,3.896,3.336,3.816,3.757
2003,3.752,3.788,3.852,3.296,3.739,3.806,3.965,3.976,3.892,3.878,3.858,3.898
2004,3.692,3.808,3.648,3.815,3.744,3.877,4.026,4.051,3.968,3.790,3.777,3.849
2005,3.873,3.790,3.654,3.772,3.948,3.619,3.773,3.796,3.784,3.705,3.514,3.691
2006,3.703,3.766,3.782,3.622,3.674,3.861,3.627,3.602,3.717,3.855,3.875,3.901
2007,4.032,4.019,3.969,3.794,3.876,3.879,3.825,3.895,3.897,3.942,4.225,4.081
2008,4.140,4.041,4.095,4.204,4.076,4.068,4.169,4.249,4.418,4.401,4.397,4.281
2009,4.441,4.349,4.165,4.368,4.282,4.250,4.193,4.279,4.244,4.623,4.431,4.234
2010,4.483,4.388,4.313,4.445,4.563,4.528,4.432,4.421,4.325,4.602,4.490,4.584
2011,4.740,4.990,4.923,4.877,4.614,4.854,4.862,4.792,4.805,5.209,5.218,5.251
2012,5.290,5.030,5.090,5.206,5.048,4.896,4.929,4.846,4.893,5.128,5.036,5.102
2013,5.263,5.184,5.089,5.093,4.831,5.005,4.840,5.034,4.795,4.945,4.885,4.975
2014,5.022,4.979,4.842,5.011,4.911,4.691,4.719,4.751,4.987,4.884,4.863,5.041
2015,5.089,4.955,4.889,4.791,4.696,4.620,4.466,4.597,4.791,4.626,4.684,4.725
2016,4.913,4.851,4.850,4.915,4.801,4.710,4.691,4.710,4.695,4.712,4.615,4.682
2017,4.834,4.870,4.751,4.659,4.631,4.629,4.606,4.688,4.648,4.683,4.567,4.758
2018,4.786,4.670,4.825,4.709,4.588,4.656,4.750,4.662,4.754,4.864,4.786,4.812
2019,4.912,4.981,4.791,4.821,4.850,4.633,4.674,4.682,4.802,4.940,4.935,4.740
2020,4.824,4.884,4.918,4.941,4.934,5.088,4.898,4.950,4.944,4.925,4.846,4.927
2021,5.014,4.937,4.949,4.978,4.685,4.886,4.943,4.918,4.900,4.952,4.770,4.766
2022,4.993,5.048,5.059,5.129,5.352,5.536,5.621,5.638,5.701,5.745,5.724,5.561
2023,5.809,5.722,5.920,5.950,5.807,5.812,5.845,5.904,5.959,6.041,6.014,6.015
2024,5.903,5.885,5.733,6.196,6.000,6.137,6.030,6.357,6.338,6.295,6.447,6.270
2025,6.459,6.255,6.328,6.229,6.466,6.493,6.374,6.505,6.396,NULL_,6.138,6.403
""".split(",")

start = 1980
end = 2025


def calculate_historical_ice_cream_price(year, month):
    """
    Calculates the historical average price of an ice cream cone.
    Param: year int
    Param: month str
    return: price int
    """
    idx = (year - start) * (len(months))
    idx += (months.index(month) + 1)
    return cells[idx]


year = int(input("Enter a year from 1980 to 2025: "))
if year < start or year > end:
    print("Dont have data on that year.")

month = input("Enter a month(Jan, Feb, ...): ")
month = month[0].upper() + month[1:].lower()
if month[:3] in months:
    price = calculate_historical_ice_cream_price(year, month[:3])
    if price != "NULL_":
        print("The avg price of 1/2 gallon of ice-cream in the US",
              f"in the year {year} was {price}.")
    else:
        print("Dont have data for that month specifically.")
else:
    print("Invalid month.")

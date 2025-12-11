def ms_to_kmh(ms):
    km = ms * 3.6
    return km 

speedms = int(input("Give your speed in m/s:  "))
result = ms_to_kmh(speedms)

print("Your speed in km/h is: ",result, "km/h")
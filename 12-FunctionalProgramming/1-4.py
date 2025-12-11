ms_persecond = int(input("Enter your speed in ms: "))

ms_to_km_h = lambda ms: ms * 3.6

km_h = ms_to_km_h(ms_persecond)

print(f'{ms_persecond} m/s = {km_h} km/h')
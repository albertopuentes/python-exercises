input_truck = "toyota tacoma"
input_truck.split()

make = input_truck.split()[0]
model = input_truck.split()[-1]

truck = dict(make = make, model = model)
print(truck)




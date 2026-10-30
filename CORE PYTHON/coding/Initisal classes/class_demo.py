class Fan:
    def __init__(self):
        self.brand="TATA"
        self.color="Grey"
        self.cost=5000
        self.noOfBlades=3
        self.motor="5KV"

    def on(self):
        print("Congrats Fan is on now")
    def off(self):
        print("Fan is off, Do you want to switch it on")
f1=Fan()
print(f1.brand)
print(f1.color)
print(f1.cost)
print(f1.noOfBlades)
print(f1.motor)

f1.on()
f1.off()
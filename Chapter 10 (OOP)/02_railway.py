class RalwayForm:
    formType = "Railway Form"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

shibu = RalwayForm()
shibu.name = "Shibu"
shibu.train = "Rajdhani Express"

shibu.printData()
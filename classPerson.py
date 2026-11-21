from PIL import Image, ImageDraw, ImageFont

class Person:
    def __init__(self, name:str, money:float):
        self.name = name
        self.money = money 
        self.starting_money = money
        self.stuff_done = []

    def work(self):
        self.money += 100
        self.stuff_done.append("worked and earned 100")
        print(f"{self.name} worked and earned 100")

    def deposit(self, amount):
        self.money += amount
        self.stuff_done.append(f"deposited {amount}")
        print(f"{self.name} deposited {amount}")

    def withdraw(self, amount):
        self.money -= amount
        self.stuff_done.append(f"withdrew {amount}")
        print(f"{self.name} withdrew {amount}")

    def buy(self, amount):
        if self.money < amount:
            print(f"{self.name} does not have enough money to buy)")
        elif amount <= 0:
            print(f"{self.name} cannot buy an item with a non-positive amount")
        else:
            self.money -= amount
            self.stuff_done.append(f"bought an item for {amount}")
            print(f"{self.name} bought an item for {amount}")
    def showMoney(self):
        print(f"{self.name} has {self.money}")
    def generate_image(self, filename="summary.png"):
        # Stage 1: Configuring the blank canvas
        img = Image.new("RGB", (500, 120 + 30 * len(self.stuff_done)), "white")
        
        # Stage 2: Configuring the pen
        draw = ImageDraw.Draw(img)
        
        # Stage 3: Configuring the font
        font = ImageFont.load_default(size=20)
        
        # Stage 4: Writing the lines
        y = 20
        draw.text((20, y), f"Name: {self.name}", fill="black", font=font)
        y += 30
        draw.text((20, y), f"Starting Money: {self.starting_money}", fill="black", font=font)
        y += 30
        draw.text((20, y), "Stuff done:", fill="black", font=font)
        for action in self.stuff_done:
            y += 30
            draw.text((40, y), f"- {action}", fill="black", font=font)
            
        y += 40
        draw.text((20, y), f"Ending Money: {self.money}", fill="black", font=font)
        
        # Stage 5: Saving the image
        img.save(filename)
        
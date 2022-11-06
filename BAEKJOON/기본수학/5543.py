hamburger = 2001
beverage = 2001

for i in range(5):
    if i < 3:
        hamburger = min(hamburger, int(input()))
    else:
        beverage = min(beverage, int(input()))

print(hamburger + beverage - 50)

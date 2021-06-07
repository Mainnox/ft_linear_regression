import matplotlib.pyplot as plt
import csv

class Train:
    price = []
    miles = []
    with open('data.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                miles.append(int(row[0]))
                price.append(int(row[1]))
            except:
                pass

train = Train()
print(train.price)
print(train.miles)
plt.plot(train.price, train.miles, 'ro')
plt.xlabel("Price")
plt.ylabel("Miles")
plt.title("After Parsing")
plt.show()

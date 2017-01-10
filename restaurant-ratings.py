restaurant_file = open("scores.txt")

restaurant_ratings = {}

for line in restaurant_file:
    line = line.rstrip().split(":")
    restaurant_name, rating = line 
    # restaurant_name = line[0]
    # rating = line[1]
    restaurant_ratings[restaurant_name] = rating
    restaurant_rate = sorted(restaurant_ratings.items())
    # print restaurant_rate

for restaurant_name, rating in restaurant_rate:
    print "%s is rated at %s." % (restaurant_name, rating)
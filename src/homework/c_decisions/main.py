import decisions
option = int(input("Enter a numerical option:"))
total = input(input("Enter a numerical total"))
result = decisions.get_optoions_ratio(option, total)
print ("Your standing is: " + decisions.get_faculty_rating(result))
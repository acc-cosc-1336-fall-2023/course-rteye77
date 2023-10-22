import dictionary

while True:
    arg = int(input("Choose one: 1-Get p distance matrix | 2-Exit: "))
    if arg == 2:
        break
    lst1 = input("Enter the first list: ").strip('][').split(',')
    lst2 = input("Enter the second list: ").strip('][').split(',')
    lst3 = input("Enter the third list: ").strip('][').split(',')
    lst4 = input("Enter the fourth list: ").strip('][').split(',')
    matrix = [lst1,lst2,lst3,lst4]
    results = dictionary.get_p_distance_matrix(matrix)
    print("Results: ", results)
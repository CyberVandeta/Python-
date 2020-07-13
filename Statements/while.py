# x = 1
# while x < 10:
#     print("your current pack is ", x)
#     x += 1
#     if x == 4:
#         print("you have consumed enough")
#         # continue
#
#     elif x == 6:
#          print("you are too boosy")
#          # continue
#     elif x == 10:
#          print("you are out of stock")
#          # break

x = int(input("Enter your percentage: "))
# x = 1
while x < 100:
    x += 1
    if 35 >= x < 50:
        print("You have pass with 35%")
    elif 50 <= x < 75:
        print("You have passed with second class ")
    elif x >= 75:
        print("you have passed with first class")
    else:
        print("you have failed your exams")
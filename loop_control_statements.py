'''
break--> once executed, it exits the loop.
continue-->skip the current iteration of the loop.
pass--> it does nothing , acts as a placeholder( a person or thing that occupies the position or place of another person or thing)
use case: You can declare a function and do nothing with it then use pass to avoid errors.

def future_function():
    pass  # TODO: Implement this function later


'''
# while True:
    # name=input("Enter your name:")
    # if name != "":# if sting is not empty then only break
    #     break

# phone_number= "123-456-7890"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i,end="")

# for j in range(0,21):
#     if j==15:
#         pass #without if also it is waste , cause it just does nothing 
#     else:   
#      print(j)




# # BREAK & CONTINUE
# lis=[12,21,33,22]
# i=0
# while i<=len(lis):
#     if lis[i]==33:
#         continue
#     print(lis[i])
#     i+=1
# print("out of loop")

# # FOR LOOP IN LIST
# data=["Java","C","Python","Ruby","Pearl"]
# for i in data:
#     if i=="Ruby":
#         break # continue
#     print(i)#prints names 1 by 1
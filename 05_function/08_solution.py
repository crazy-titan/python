# def print_kwargs(name,power):
#     print("Name: ",name," Power: ",power)


# print_kwargs(name = "BabaarSher",power = "Calmness")
# ALL THIS IS an example valid when user will give the arguments name and power both;



# What will happen if user give single input or more input that defined parameters?
# In that case we use **kwargs and we access them in key:value pairs
# otherwise it will give an error



def print_kwargs(**kwargs):
    for key,value in kwargs.items():  #dictionary command
        print(f"{key}:{value}")  # formating , this is also method to print something


print_kwargs(name = "BabaarSher",power = "Calmness")
print_kwargs(name = "BabaarSher")
print_kwargs(name = "BabaarSher",power = "Calmness",enemy = "lomri")

# all the given input will be printed without error, so we will see more on this later
# but right now you have to understand what it is and how its working.
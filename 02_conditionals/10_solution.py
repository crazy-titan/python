pet = "Dog"

age_of_pet = 5

if pet == "Dog" and age_of_pet < 2:
    food = "Puppy food"
elif pet == "Dog" and age_of_pet >= 2:
    food = "Adult dog food"
elif pet == "Cat" and age_of_pet > 5:
    food = "Senior cat food."
elif pet == "Cat" and age_of_pet <= 5:
    food = "Puppy Cat food."

print("You are recommend", food,"for your ",pet)

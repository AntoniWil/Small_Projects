def wake_up():
    print("I'm waking up")
    return "I'm awake now"

def get_out_of_bed():
    print("we got out of bed")
    return "getting out of bed"

def tooth(toothpaste):
    print("I'm brusing my teeth with " + toothpaste)
    return "Our teeth are clean now"

def breakfast(food):
    print("what are we eating today " + food)
    return "we are full now!"

def dressed():
    user_dressed = input("What clothes will you like to were today? ")
    user_shoes = input("what shoes you like to wear? ")
    return "I am wearing " + user_dressed + " with " + user_shoes



def main():
    awake = wake_up()
    print(awake)
    rise = get_out_of_bed()
    print(rise)

    user_tooth = input("what toothpaste will you use? ")
    user_food = input("What breakfast will you eat today? ")
    
    tooth(user_tooth)
    breakfast(user_food)

    clothes = dressed()
    print(clothes)



main()  

















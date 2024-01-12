# JAI SHREE RAM 
# coffee machine 
# TODO : 1 -> print report -> check requriments
# coffee menu 


resource={
    
        "water":1000,
        "milk":1000,
        "coffee":1000,
        
      
    }


menu = {
    "c1": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "price": 15,
    },
    "c2": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "price": 25,
    },
    "c3": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "price": 30,
    }
}
machine_on=True
while machine_on:
    user_choice=input("select c")
    drink=menu[user_choice]
    print(menu[user_choice])
    drink_ig=drink["ingredients"]
    for items in drink_ig:
        if (drink_ig[items] > resource[items]):
            print("not enough\n")
            

 
        
    #process coin
    print("input coins\n ")
    total=0
    total=int(input("1rs coin"))*1
    total+=int(input("2rs coin"))*2
    total+=int(input("5rs coin"))*5
    print(f"here total cost :{total}")        

    drink_cost=drink["price"]
    if total > drink_cost:
        change=total-drink_cost
        print(f"get your changes {change}")
        
    #make a coffee 
    for item in drink_ig:
        ur_drink=resource[items]-drink_ig[item]
        print(f"resourece remaning:{ur_drink}")

    # print(resource)   



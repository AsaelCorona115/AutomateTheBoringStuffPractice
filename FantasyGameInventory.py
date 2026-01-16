#Sample initial inventory for testing
initialInventory = {'gold coin': 42, 'rope': 1}

#Sample loot for testing
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


#Main function
def displayInventory(inventory):
    totalNumberOfItems = 0
    print('Inventory:')

    for i in inventory:
        print(str(inventory[i]) + ' ' + i) 
        value = int(inventory[i])
        totalNumberOfItems += value
    
    print("Total Number of Items: " + str(totalNumberOfItems))
    print()
    print()


    return


def add_to_inventory(inventory, added_items):
   
    for i in added_items:
        if inventory.get(i, 0) != 0:
            inventory[i] += 1
        else: 
            inventory[i] = 1
        
    print("Updated inventory!")
    print()
    displayInventory(inventory)


    return 



displayInventory(initialInventory)
add_to_inventory(initialInventory, dragon_loot)
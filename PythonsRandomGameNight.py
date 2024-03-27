#Task 1: Random Choice Game
items = ["dice", "coin", "top"]
print(f"{items} Memorize the list, I will now remove one item. Next you must guess which item I have removed")

import random
select = random.choice(items)
print(input("Make your choice. What item have I removed? "))

if input == select:
    print("you have chosen wisely,")
else:
    print(f"you have chosen poorly.")

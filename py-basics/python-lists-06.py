mylist = ['apple', 'banana', 'cherry'] #list data type

#access data of list
print(mylist[0])

#change data of list items
mylist[0] = 'newton_apple'
print(mylist[0])

#add new item to the list
mylist.append('strawberry')
print(mylist)

#add new item at specific index
mylist.insert(1, 'orange')
print(mylist)

tropical = ["mango", "pineapple", "papaya"]
print('tropical list: ', tropical)

#add another list to the list
mylist.extend(tropical)
print(mylist)

#add any iterable 
mylist.extend(tuple(tropical))
print(mylist)
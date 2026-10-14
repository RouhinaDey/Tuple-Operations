tuples = ("tuple", False, 3.2, 1)
print(tuples)

#create a tuple
tuples = (7, 6, 5, 8, 3, 1) 
print(tuples)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuples = tuples + (9,)
print(tuples)

#Counts the number of occurrences of item 50 from a tuple
tuple1 = (57, 10, 60, 80, 90)
print(tuple1.count(50))

#create a tuple
tuples = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple[start:stop] the start index is inclusive and the stop index
_slice = tuples[3:5]
#is exclusive
print(_slice)
#if the start index isn't defined, is taken from the beg inning of the tuple
_slice = tuples[:6]
print(_slice)
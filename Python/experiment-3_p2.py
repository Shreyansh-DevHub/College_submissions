#lambdas function with map,filter,reduce 


from functools import reduce 

nums = [1,2,3,4,5,6,7,8,9,10]

#squares each number
squares = list(map(lambda x:x**2,nums))
print("\nsquares , ", squares,"\n")

#filter each number
evens = list(filter(lambda x:x%2 == 0, nums))
print("even number from the list ,", evens,"\n")


#products of all numbers
product = reduce(lambda x,y:x*y,nums)
print("prduct of all the numbers ," ,product,"\n")
print("name: shreyansh singh \nprn no.: 26013010907")
# Problem statement: given an array of elements
# create a product array of same size such that the element at ith position
# in the product array is the product of all the elements in the input array
# except the element at ith position.

######### Method 1 ############
## Using Maths

elements = [1,2,3,4,5]

product = 1
for i in elements:
    if i != 0:
        product *= i

product_list = []

for i in elements:
    if 0 in elements:
        if i == 0:
            product_list.append(int(product))
        else:
            product_list.append(0)
    else:
        product_list.append(int(product/i))

print("-------------------")
print("Using Mathematics: ")
print("-------------------")
print("Original Array: ", elements)
print("Product array: ", product_list)

######### Method 2 ############
## Using List comprehension

elements = [1,2,3,4,5]
new_list = [int(product/i) if i!=0 else int(product) for i in elements]

print("--------------------------")
print("Using List comprehension: ")
print("--------------------------")
print("Original Array: ", elements)
print("Productr Array: ", new_list)

######### Method 3 ############
## Using complex technique

arr =[1,2,3,4,5]
new_arr = []
n = len(arr)

left = [1 for i in range(n)]
right = [1 for i in range(n)]
left[0] = arr[0]
right[n-1] = 1

for i in range(1,n):
    left[i] = left[i-1] * arr[i-1]
    right[n-1-i] = right[n-i] * arr[n-i]
    
for i in range(n):
    new_arr.append(left[i] * right[i])

print("-----------------------")
print("Using left and right product arrays: ")
print("------------------------")
print("Original Array: ", arr)
print("Left Product Array: ", left)
print("Right Productr Array: ", right)
print("Product Array: ",new_arr)

######### Method 4 ############
## Using Brute-Force technique

arr =[1,2,3,4,5]
new_arr = []
n = len(arr)

for i in range(n):
      product = 1
      for j in range(n):
          if i != j:
              product *= arr[j]
      new_arr.append(product)

print("------------------------------")
print("Using Brute-Force logic: ")
print("------------------------------")
print("Original Array: ", arr)
print("Product Array: ",new_arr)
      
      
      
      

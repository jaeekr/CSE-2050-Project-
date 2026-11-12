
############## Miletone 3 ##################
#Recursive catalog total: compute the total value of all product prices using recursion
def recursive_total_price(products):
  """Return the total of all product prices using recursion."""
  if len(products) == 0: #base case
    return 0.0 
  
  return products[0].get_price() + recursive_total_price(products[1:])
  
def fewest_coins(coins, amount, results=None):
  '''fewest coins: use top down memoization'''
  if results is None:
    results={}
  return helper(coins,amount, results)

def helper(coins,amount,results):
  minCoins = -1
  if amount in coins: #base case 1
    return 1
  elif amount ==0:  #base case 0
    return 0 
  elif amount in results:  #case in results
    return results[amount]
  else:
    validCoins = [c for c in coins if c <= amount]
    for i in validCoins:
       sub = helper(coins, amount - i, results)        # change 1
       if sub != -1:                                   # change 2
        numCoins = 1 + sub
        if minCoins == -1 or numCoins < minCoins:     # change 3
          minCoins = numCoins
    results[amount] = minCoins                        # dedented: after the loop
  return minCoins
    

#bubble sort
def bubble_sort(products):
  n=len(products)
  has_swapped = False
  for i in range(n-1):
    for j in range(n-1-i):
      if products[j+1].get_id() < products[j].get_id():
        products[j+1],products[j] = products[j], products[j+1]
        has_swapped = True
    if not has_swapped:
      break




#selection sort
def selection_sort(products):
  n=len(products)

  for i in range(n-1):
    max_j = 0
    for j in range (n-i):
      if products[j].get_id() > products[max_j].get_id():
        max_j = j
    if (n-1-i) != max_j:
      products[n-1-i], products[max_j] = products[max_j], products[n-1-i]


#insertion sort
def insertion_sort(products):
  for i in range(1, len(products)):
    for j in range(i, 0, -1):
      #if switch
      if products[j-1].get_id() > products[j].get_id():
        products[j-1], products[j] = products[j], products[j-1]
      #no switch
      else:
        break
  return products

#binary search
def binary_search(products, product_id, left = 0, right = None):
    if right == None:
      right = len(products)-1

    if left > right:
      return -1

    mid_indx = (right+left)//2

    if product_id == products[mid_indx].get_id():
      return mid_indx
    
    if product_id > products[mid_indx].get_id():
      left = mid_indx + 1
      return binary_search(products, product_id, left, right)
    
    if product_id < products[mid_indx].get_id():
      right = mid_indx - 1
      return binary_search(products, product_id, left, right)


############## Miletone 4 ##################

#merge sort
def merge_sort(products):
  '''sorts products by dividing it into sublists, sorting those sublists and combining them all'''
  if len(products) <= 1:
    return products
  
  mid = len(products)//2
  left = products[:mid]
  right = products[mid:]

  left = merge_sort(left)
  right = merge_sort(right)

  #combine subproblems
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      products[i+j] = left[i]
      i += 1
    else:
      products[i+j] = right[j]
      j += 1
  products[i+j:] = left[i:] + right[j:]
  return products

#quick sort
def quick_sort(products, left = 0, right = None):
  '''sorts products by choosing a pivot and partitioning the list into two sublists'''
  if right is None:
    right = len(products)

  if right - left <= 1:
    return None

  #partitioning around a pivot
  pivot = right-1
  i = left
  j = right-2

  #pivot
  while i < j:
    while products[i] < products[pivot]:
      i += 1
    while products[j] > products[pivot] and i < j:
      j -= 1
    if i< j:
      products[i], products[j] = products[j], products[i]

  if products[i] >= products[pivot]:
    products[i], products[pivot] = products[pivot], products[i]
    pivot = i

  quick_sort(products, left, pivot)
  quick_sort(products, pivot+1, right)

#quick select
def quick_select(products, k, left = 0, right = None):
  '''returns the kth smallest product in the list'''
  if right is None:
    right = len(products)
  
  pivot = right-1
  i = left
  j = pivot - 2
  while i<j:
    while products[i] < products[pivot]:
      i += 1
    while products[j] > products[pivot] and i<j:
      j -= 1
    if products[i]<products[j]:
      products[i], products[j] = products[j], products[i]
      pivot = i
    if pivot == len(products)//2:
      return products[pivot]
    elif pivot > len(products)//2:
      return quick_select(products, left, pivot)
    elif pivot < len(products)//2:
      return quick_select(products, pivot+1, right)
    

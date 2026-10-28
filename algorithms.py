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
  minCoins = amount
  if amount in coins: #base case 1
    return 1
  elif amount ==0:  #base case 0
    return 0 
  elif amount in results:  #case in results
    return results[amount]
  else:
    validCoins = [c for c in coins if c <= amount]
    for i in validCoins:
      numCoins = 1 + helper(coins, amount-i, results)
      if numCoins < minCoins:
          minCoins = numCoins
          results[amount] = minCoins
  return minCoins
          


  
#this is a worse version since but this one doesn't use the helper or results 
def fewest_coins_backup(coins, amount):
  '''fewest coins: use top down memoization'''
  minCoins = amount
  if coins in amount:
    return 1
  elif amount ==0:
    return 0 
  else:
    for i in [c for c in coins if c <= amount]:
      numCoins =  1 + fewest_coins(coins, amount-1)
      if numCoins < minCoins:
        minCoins = numCoins
  return minCoins
    



#bubble sort
def bubble_sort(products):
  n=len(products)
  has_swapped = False
  for i in range(n-1):
    for j in range(n-1-i):
      if products[j+1].get_id > products[j].get_id:
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
      if products[j].get_id > products[max_j].get_id:
        max_j = j
    if (n-1-i) != max_j:
      products[n-1-i], products[max_j] = products[max_j], products[n-1-i]


#insertion sort
def insertion_sort(products):
  pass


#binary search
def binary_search(products, product_id):
  pass

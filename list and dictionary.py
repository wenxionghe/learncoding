# It's Dangerous to Go Alone! Take This
# Add a key to inventory called 'pocket'
# Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'
# .sort() the items in the list stored under the 'backpack' key
# Then .remove('dagger') from the list of items stored under the 'backpack' key
# Add 50 to the number stored under the 'gold' key

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = 500 + 50
print inventory

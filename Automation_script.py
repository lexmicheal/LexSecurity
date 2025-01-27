# Assign the file name to a variable for the allow list
  import_file = "allow_list.txt" 

# Open the file in read mode to read its initial contents
  with open(import_file, "r") as file:

# use .read() to read the imported file and store it in a variable named 'ip_addresses'
  ip_addresses = file.read()

# use .split() to convert ip_addresses from a string to a list
  ip_addresses = ip_addresses.split()
    
For element in remove_list:

  # create conditional statement to evaluate if 'element' is in ip_addresses
    if element in ip_addresses:

  # use the '.remove()' method to remove
  # elements from 'ip_addresses'
     ip_addresses.remove(element)

  # convert 'ip_addresses' back to string so that it can be written into the text file
    ip_addresses = "\n".join(ip_addresses)

  # build 'with' statement to rewrite the original file
    with open(import_file, "w") as file: 
  # rewrite the file, replacing its context with 'ip_addresses'
    file.write(ip_addresses)  




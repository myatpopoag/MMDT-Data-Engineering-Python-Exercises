# Python as a Calculator
# Add 19 and 17
print(19+17)
# Subtract 12 from 99
print(99-12)
# Multiply 27 by 23
print(27*23)
# Divide 99 by 12
print(99/12)

# Calculate and print nine squared
print(9 ** 2 )
# Find the remainder from 337 divided by 27
print(337 % 27)

# Print the data type of current_quarter
current_quarter = 18
print(type(current_quarter))
# Print the data type of 9.75
print(type(9.75))
# Print the data type of revenue_on_target
revenue_on_target = True
print(type(revenue_on_target))

# Create a string variable called name
name = "John Smith"
# Create an integer variable called age
age = 47
# Create a string variable called address
address = "The Shard, London, SE1 9SG"
# Print their information
print(name, age,  address)
#Checking and Updating Conditions
# Create a integer variable called age
age = 47
# Create a boolean variable called is_adult
is_adult = True
# Update John's address
address = "Buckingham Palace, London, SW1A 1AA"
# Print their information
print(address, is_adult)

# Multi-line Strings
# Create review_one
review_one = """I really enjoy the courses,
and they are easy to fit into my busy schedule.
I wish I had started using your platform sooner.
I'll be recommending you to my friends!!"""
# Create review_two
review_two = """One year ago, I was unsure of how to make progress in my career.
Now, I work as a Prompt Engineer, and I can't thank you enough!
Keep up the great work."""
# Print the two reviews individually
print(review_one)
print(review_two)

# Modifying string Variables
# Create a string variable called most_popular_course
most_popular_course = "Intro to Embeddings with the OpenAI API"
# Update the first word
most_popular_course = most_popular_course.replace("Intro", "Introduction")
print(most_popular_course)
# Swap spaces for underscores
most_popular_course = most_popular_course.replace(" ", "_")
print(most_popular_course)
# Change to lowercase
most_popular_course = most_popular_course.lower()
print(most_popular_course)

# Building a party playlists
# Create the playlist variable
playlist = [1, "Blinding Lights", 2, "One Dance", 3, "Uptown Funk"]
# Print the list
print(playlist)
# Find the second song
print(playlist[4])
# Get the last song's artist
print(playlist[-1])
# Print all songs in the playlist
print(playlist[1::3])

# Building a playlist dictionary
# Create the playlist dictionary
playlist = {"The Weeknd": "Blinding Lights","Drake": "One Dance"}
# Print the playlist
print(playlist)
# Print the song by Coldplay
print(playlist["Coldplay"])
# Add a new song
playlist["Usher"] = "Yeah!"
# Print the songs in the playlist
print(playlist.values())

# Last quarter's revenue
# Create a tuple
q3_financials = (325780, 1041, 4271599)
# Print the tuple
print(q3_financials)

# DJ Set
hip_hop = ["Drake", "JAY-Z", "50 Cent", "Drake"]
# Create a set
indie_set = {"Kings of Leon", "Arctic Monkeys", "Stereophonics"}
# Create a set
indie_set = {"Kings of Leon", "MGMT", "Stereophonics"}
# Convert hip_hop to a set
hip_hop_set = set(hip_hop)
# Print the indie and hip_hop sets
print(indie_set, hip_hop_set)

# Checking Inflation
# Create two float variables
inflation_august = 0.4
inflation_september = 0.3
# Check if September inflation is less than August inflation
if(inflation_september<inflation_august):
	print("Inflation decreased")
# Check if September inflation is more than August inflation
elif inflation_september > inflation_august:
  print("Inflation increased")
# Confirm that they are equal
else:
  print("Inflation remained stable")

# On the rental market
# Create integer variables
min_num_beds = 2
min_sq_foot = 750
max_rent = 1900
rent = 2100
num_beds = 2
sq_foot = 800
# Check the number of beds
if(num_beds < min_num_beds):
  print("Insufficient bedrooms")
# Check square feet
elif (sq_foot <= min_sq_foot):
  print("Too small")
# Check the rent
elif (rent > max_rent):
  print("Too expensive")  
# If all conditions met
else:
   print("This looks promising!")

# Looping through a list
user_ids = ["T42YG4KTK", "VTQ39IDQ0", "CRL11YUWX", 
            "K6Y5URXLR", "V4XCBER7V", "IOGQWC61K"]
# Loop through user_ids
for user_id in user_ids:
  # Print the user_id
  print(user_id)

# Updating a variable with for loop
# Create the tickets_sold variable
tickets_sold = 0
# Create the max_capacity variable
max_capacity = 30
# Loop through a range up to and including max_capacity's value
for i in range (1, max_capacity + 1):
  # Add one to tickets_sold in each iteration
  tickets_sold += 1 
print("Sold out:", tickets_sold, "tickets sold!")

# Conditional looping with a dictionary
courses = {"LLM Concepts": "AI", 
           "Introduction to Data Pipelines": "Data Engineering", 
           "AI Ethics": "AI",
           "Introduction to dbt": "Data Engineering", 
           "Writing Efficient Python Code": "Programming",
           "Introduction to Docker": "Programming"}
# Loop through the dictionary's keys and values
for key, value in courses.items():
  # Check if the value is "AI"
  if (value == "AI"):
    print(key, "is an AI course")  
  # Check if the value is "Programming"
  elif (value == "Programming"):
    print(key, "is a Programming course") 
  # Otherwise, print that it is a "Data Engineering" course
  else:
    print(key, "is a Data Engineering course")

# Converting to a while loop
tickets_sold = 0
max_capacity = 10
# Create a while loop
while tickets_sold < max_capacity: 
  # Add one to tickets_sold in each iteration
  tickets_sold += 1
# Print the number of tickets sold
print("Sold out:", tickets_sold, "tickets sold!")

# Conditional while loops
release_date = 26
current_date = 22
# Create a conditional loop while current_date is less than or equal to the release_date
while current_date <= release_date:  
  # Increment current_date by one
  current_date += 1  
  # Promote purchases
  if current_date <= 24:
    print("Purchase before the 25th for early access")  
  # Check if the date is equal to the 25th
  elif current_date == 25:
    print("Coming soon!")
  else:
    print("Available now!")

# Appending to a list
# Create an empty list
authors_below_twenty_five = []
authors = {"Nicholas Sparks": 23, "Judith Krantz": 27, "J. K. Rowling": 21, "Sidney Sheldon": 22}
# Loop through the authors dictionary
for key, value in authors.items():  
  # Check for values less than 25
  if value < 25:    
    # Append the author to the list
    authors_below_twenty_five.append(key)   
print(authors_below_twenty_five)

# Book genre popularity
genre_sales = {"Science Fiction": 5166000000, "Mystery": 80000000, "Romance": 456000000, "Fantasy": 2000000000}
for genre, average_sale in genre_sales.items():    
    # Filter for the maximum sales value
    if average_sale == 5166000000:      
      # Print the genre
      print("Most popular genre: ", genre)
      print("Average sales: ", average_sale)    
    # Filter for the minimum sales value
    elif average_sale == 80000000:     
      # Print the genre
      print("Least popular genre: ", genre)
      print("Average sales: ", average_sale)

# Working with keywords
# Loop through the dictionary
for genre, sale in genre_sales.items():  
  # Check if genre is Horror or Mystery
  if genre == "Horror" or genre == "Mystery":
    print(genre, sale)
  # Check if genre is Thriller and sale is at least 3 million
  elif genre == "Thriller" and sale >= 3000000:
    print(genre, sale)

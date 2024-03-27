# Task 1: The Selective DJ
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

sublist = genres[1:4]
for genre in sublist:
    print(genre)

# Task 2: THe One-Liner Band with List Comprehension
for music in genres:
    print(f"{music} Music")
    
# Task 3: Numerical Beats with range
for count in range(10, 0, -1):
    print (count)
print("The beat drops now!")
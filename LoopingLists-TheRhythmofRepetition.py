# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
track = 0
#Task 1: The for Loop DJ Set
for genre in genres:
     track +=1
     print(f"track: {track} Genre: {genre}" )

#Task 2: The Remix Artist with while
    
     while track <= len(genres):
         print(f"Track {track}: {genres[track-1]} is playing.")
         track += 1
     if genre == "Hip-hop":
         print("this is the genre I was looking for")
         break

#Task 3: Light Show Technician Group
for light in range(len(genres)):
          light_show = genres[light]
          track_number = light + 1
          print(f" The Light show for track {track_number} is ready")
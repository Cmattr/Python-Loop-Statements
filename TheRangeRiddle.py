 # Task 1: Your Mood Today

moods = ["Happy", "Sad", "Energetic", "calm" ]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
import random
for day in days:
    mood = random.choice(moods)
    print(f"On {day} you were feeling {mood}")
    
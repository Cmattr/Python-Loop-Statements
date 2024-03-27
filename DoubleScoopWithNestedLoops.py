# Task 1: Your Mood Tracker
import random
times = ["Morning", "Afternoon", "Evening"]
moods = ["Happy", "Sad", "Energetic", "calm" ]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]

for day in days:
    for time in times:
            mood = random.choice(moods)
            print(f"on {day} {time} you were feeling {mood}")
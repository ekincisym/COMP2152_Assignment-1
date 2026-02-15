"""
Author: Seyma Sibel Ekinci
Assignment: #1
"""


# Step b: Create 4 variables
# Step b: Create 4 variables
gym_member = "Alex Alliton"  # string
preferred_weight_kg = 20.5  # float
highest_reps = 25  # int
membership_active = True  # boolean

# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Bob": (30, 45, 20),
    "Jane": (25, 35, 40),
    "Cloe": (40, 50, 30)
} 

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, minutes in workout_stats.items():
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes

# Update dictionary after iteration
workout_stats.update(workout_stats)

# Step e: Create a 2D nested list called workout_list
workout_list = [list(minutes) for friend, 
                minutes in workout_stats.items() 
                if not friend.endswith("_Total")] # 2D list 

# Step f: Slice the workout_list
print("Yoga and Running minutes:")
for row in workout_list:
    print(f"Yoga: {row[0]} min, Running: {row[1]} min")
    
print("Weightlifting minutes for the last two friends:")
for row in workout_list[-2:]:
    print(f"Weightlifting: {row[2]} min")   

# Step g: Check if any friend's total >= 120
for friend, minutes in workout_stats.items():
    if friend.endswith("_Total") and minutes >= 120:
        name = friend.replace("_Total", "")
        print(f"Great job staying active, {name}!")

# Step h: User input to look up a friend
friend_name = input("Enter a friend's name: ")
if friend_name in workout_stats:
    activities = workout_stats[friend_name]
    total_minutes = workout_stats.get(f"{friend_name}_Total", 0)
    print(f"Workout details for {friend_name}:")
    print(f"Yoga: {activities[0]} min, Running: {activities[1]} min, Weightlifting: {activities[2]} min")
    print(f"Total workout minutes: {total_minutes}")
else:
    print(f"Friend {friend_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
friends_total = {friend: total for friend, total in workout_stats.items() if friend.endswith("_Total")}

# Friend with the highest total workout minutes
highest_friend = max(friends_total, key=friends_total.get).replace("_Total", "")
#  Friend with the lowest total workout minutes
lowest_friend = min(friends_total, key=friends_total.get).replace("_Total", "")
print(f"Friend with the highest workout minutes: {highest_friend}")
print(f"Friend with the lowest workout minutes: {lowest_friend}")
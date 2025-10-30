# Hobby Project 1: Football Match Score Tracker
# Objective: Simulate and track football match score

team1 = input("Enter Team 1 name: ")
team2 = input("Enter Team 2 name: ")

score1 = 0
score2 = 0

while True:
    print(f"\n{team1} {score1} - {score2} {team2}")
    print("1. Goal for Team 1")
    print("2. Goal for Team 2")
    print("3. End Match")

    choice = input("Enter choice: ")
    if choice == "1":
        score1 += 1
    elif choice == "2":
        score2 += 1
    elif choice == "3":
        print(f"\n🏁 Final Score: {team1} {score1} - {score2} {team2}")
        break
    else:
        print("Invalid input.")

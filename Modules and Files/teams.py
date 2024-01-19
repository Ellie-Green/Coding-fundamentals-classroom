file = open("teams.txt", "w")
file.write("Tottenham Hotspur\n")
file.write("Plymouth Argyle\n")
file.write("Wrexham\n")
file.write("Hashtag United\n")
file.write("Birmingham City\n")
file.close()

file = open("teams.txt", "r")
lines = file.readlines()
team1 = lines[0].strip()
team4 = lines[3].strip()
print(f"Team 1 = {team1}")
print(f"Team 4 = {team4}")
file.close

lines[0] = "This is a new line. \n"

print("\nEdited File:")
for line in lines:
    print(line.strip())
file.close()
from recommender import generate_learning_path

level = "Intermediate"
goal = "Python Developer"

path = generate_learning_path(level, goal)

print("Learning Level:", level)
print("Learning Goal:", goal)
print("\nRecommended Learning Path:")

for i, topic in enumerate(path, start=1):
    print(f"{i}. {topic}")
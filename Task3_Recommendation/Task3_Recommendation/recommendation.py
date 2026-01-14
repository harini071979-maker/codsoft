movies = {
    "action": ["John Wick", "Mad Max"],
    "comedy": ["Mask", "Home Alone"]
}

choice = input("Enter genre: ").lower()

if choice in movies:
    print("Recommended:")
    for m in movies[choice]:
        print("-", m)
else:
    print("No data available")

# Mad Libs Game

def mad_libs():
    print("Welcome to Mad Libs Game!")
    print("Please provide the following words:\n")

    # User inputs
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")
    place = input("Enter a place: ")

    # Story template
    story = f"""
    Once upon a time in {place}, there was a {adjective} {noun}.
    Every day, it would {verb} {adverb}.
    People from all around loved the {noun} for its unique talent!
    """

    print("\nHere is your Mad Libs story:")
    print(story)

# Start the game
mad_libs()

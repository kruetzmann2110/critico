"""
Example usage of the Critico package
"""
from critico import Critico


def main():
    # Create a new critic
    critic = Critico("Movie Critic")
    print(f"Created: {critic}")
    print()
    
    # Add some reviews
    print("Adding reviews...")
    critic.add_review("The Shawshank Redemption", 5, "Masterpiece!")
    critic.add_review("The Godfather", 5, "Classic cinema")
    critic.add_review("Pulp Fiction", 4, "Very entertaining")
    critic.add_review("The Dark Knight", 5, "Best superhero movie")
    critic.add_review("Forrest Gump", 4, "Heartwarming")
    print()
    
    # Display all reviews
    print("All Reviews:")
    print("-" * 50)
    for review in critic.get_reviews():
        print(f"Item: {review['item']}")
        print(f"Rating: {'⭐' * review['rating']} ({review['rating']}/5)")
        print(f"Comment: {review['comment']}")
        print(f"Critic: {review['critic']}")
        print("-" * 50)
    
    # Show average rating
    avg_rating = critic.get_average_rating()
    print(f"\nAverage Rating: {avg_rating:.1f}/5.0")
    print(f"\n{critic}")


if __name__ == "__main__":
    main()

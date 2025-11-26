# Critico

Critico is a Python package for critical analysis and reviews. It provides a simple interface for managing reviews and ratings.

## Features

- Add reviews with ratings (1-5 stars)
- Track multiple reviews with comments
- Calculate average ratings
- Simple and intuitive API

## Installation

```bash
pip install -e .
```

## Usage

```python
from critico import Critico

# Create a new critic
critic = Critico("Movie Critic")

# Add reviews
critic.add_review("The Shawshank Redemption", 5, "Masterpiece!")
critic.add_review("Pulp Fiction", 4, "Very entertaining")

# Get all reviews
reviews = critic.get_reviews()

# Calculate average rating
avg_rating = critic.get_average_rating()
print(f"Average Rating: {avg_rating}/5.0")
```

## Running the Example

```bash
python example.py
```

## Running Tests

```bash
python -m unittest discover tests
```

## License

MIT License

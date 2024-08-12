mini_game_rus.py
# Random Word Game

This is a Python-based word guessing game that uses the [RandomWord.com](https://randomword.com/) API to fetch random English words. The words and their definitions are then translated into Russian using the `deep-translator` library. The player has to guess the word based on its definition.

## How It Works

1. The program fetches a random English word and its definition from the `RandomWord.com` website.
2. The word and its definition are then translated into Russian using the `deep-translator` library.
3. The player is prompted to guess the word based on its translated definition.
4. If the player guesses the word correctly, they are congratulated. If not, the correct word is revealed.
5. The player can choose to play again or exit the game.

## Requirements

To run this project, you need to have Python installed on your system along with the following Python libraries:

- `requests`
- `beautifulsoup4`
- `deep-translator`

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4 deep-translator


import requests
import random

def get_random_disney_character():
    page = random.randint(1, 7438)
    page_size = 1
    url = f'https://api.disneyapi.dev/character?pageSize={page_size}&page={page}'

    try:
        response = requests.get(url)
        if response.ok:
            data = response.json()
            characters = data.get('data', [])

            if characters:
                character = characters[0]
                name = character.get('name', 'Unknown')
                films = character.get('films', [])
                short_films = character.get('shortFilms', [])
                tv_shows = character.get('tvShows', [])
                video_games = character.get('videoGames', [])

                print(f"{name}\n")

                print("Films:")
                if films:
                    for film in films:
                        print(f"- {film}")
                else:
                    print("- None")

                print("\nShort films:")
                if short_films:
                    for short_film in short_films:
                        print(f"- {short_film}")
                else:
                    print("- None")

                print("\nTV shows:")
                if tv_shows:
                    for tv_show in tv_shows:
                        print(f"- {tv_show}")
                else:
                    print("- None")

                print("\nVideo Games:")
                if video_games:
                    for video_game in video_games:
                        print(f"- {video_game}")
                else:
                    print("- None")
            else:
                print("Character not found.")
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


get_random_disney_character()

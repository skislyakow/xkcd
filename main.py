import requests


def download_image(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filename, "wb") as file:
        file.writelines(response.iter_content(chunk_size=8192))
    return filename


def main():
    api_url = "https://xkcd.com/353/info.0.json"
    response = requests.get(api_url)
    response.raise_for_status()
    comic_data = response.json()

    image_url = comic_data["img"]
    filename = image_url.split("/")[-1]

    download_image(image_url, filename)
    print(f"Скачан комикс: {filename}")


if __name__ == "__main__":
    main()

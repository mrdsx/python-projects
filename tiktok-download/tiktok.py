import re
import requests


def get_tiktok_video_id(url):
    match = re.search(r'/video/(\d+)', url)
    if match:
        return match.group(1)


def tiktok(url):
    response = requests.get(url)

    video_id = get_tiktok_video_id(response.url)
    print(response.url)

    response = requests.get(f'https://tikcdn.io/ssstik/{video_id}')

    if response.status_code == 200:
        print("Success! Video downloaded.")
        with open(f"{video_id}.mp4", "wb") as file:
            file.write(response.content)
    else:
        print(f"Failed to download video. Status code: {response.status_code}")
        return None


if __name__ == '__main__':
    link = 'https://www.tiktok.com/@ynchq/video/7366967368792362258'
    tiktok(link)

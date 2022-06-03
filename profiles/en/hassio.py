import requests
import constants as Key
import json

TOKEN = Key.TOKEN

baseurl = "https://fridaycontrol.duckdns.org:8123/api/"

headers = {
    "Authorization": "Bearer" + TOKEN,
    "content-type": "application/json",
}

def getAPIStatus():
    url = baseurl
    response = requests.get(url, headers=headers)

    print(response.text)

def getCameraSnapshots():
    cameras = [
        "camera.espcam",
        "camera.espcam2",
        "camera.living_room_camera",
    ]

    for camera in cameras:
        url = baseurl + "camera_proxy/" + camera
        response = requests.get(url, headers=headers)

        with open(camera + ".jpg", "wb") as f:
            f.write(response.content)
        print(f"{camera}: {response.status_code}")

def getEntityStates():
    entities = [
        "camera.espcam",
        "camera.espcam2",
        "camera.living_room_camera",
    ]

    for entity in entities:
        url = baseurl + "states/" + entity
        response = requests.get(url, headers=headers)
        json_object = json.loads(response.text)
        json_formatted_str = json.dumps(json_object, indent=2)

        print(json_formatted_str)

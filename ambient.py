import pyautogui
import time
import numpy as np
from yeelight import discover_bulbs, Bulb, BulbException
from colorsys import rgb_to_hsv, hsv_to_rgb

SATURATION_FACTOR = 1.5
THRESHOLD = 10
INTERVAL_TIME = 0.3

prev_average_color = [0, 0, 0]
bulbs = discover_bulbs()

if not bulbs:
    print("No Yeelight bulbs found in the network.")
    exit()

yeelight_bulbs = [Bulb(bulb["ip"]) for bulb in bulbs]

for bulb in yeelight_bulbs:
    bulb.turn_on()

while True:
    try:
        screenshot = pyautogui.screenshot()
        downsampled_image = screenshot.resize((100, 100))

        image_array = np.array(downsampled_image)
        average_color = np.mean(image_array, axis=(0, 1)).astype(int).tolist()
        color_difference = np.abs(np.array(average_color) - np.array(prev_average_color))

        if np.any(color_difference > THRESHOLD):
            hsv_color = rgb_to_hsv(*[color / 255 for color in average_color])

            modified_saturation = hsv_color[1] * SATURATION_FACTOR
            modified_saturation = max(0, min(1, modified_saturation))

            modified_rgb = hsv_to_rgb(hsv_color[0], modified_saturation, hsv_color[2])
            modified_rgb = [int(component * 255) for component in modified_rgb]

            for bulb in yeelight_bulbs:
                bulb.set_rgb(*modified_rgb)

            prev_average_color = average_color

            print("Updating")

    except BulbException:
        print("Ratelimited")
        time.sleep(2)

    time.sleep(INTERVAL_TIME)

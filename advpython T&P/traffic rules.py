import time

def traffic_light():
    while True:
        print(" red Light - STOP")
        time.sleep(5)
        print(" green Light - GO")
        time.sleep(5)
        print(" yellow light - SLOW DOWN")
        time.sleep(2)

if __name__ == "__main__":
    try:
        traffic_light()
    except KeyboardInterrupt:
        print("\nTraffic light system stopped.")

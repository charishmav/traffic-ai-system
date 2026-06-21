import cv2
import numpy as np

from stable_baselines3 import PPO

from src.detector import VehicleDetector
from src.tracker import VehicleTracker
from src.counter import VehicleCounter


detector = VehicleDetector()

tracker = VehicleTracker()

counter = VehicleCounter()

model = PPO.load(
    "models/ppo_train_model"
)

video = cv2.VideoCapture(
    "videos/input_video.mp4"
)

frame_id = 0


while True:

    ret, frame = video.read()

    if not ret:
        break

    detections = (
        detector.detect(
            frame
        )
    )

    tracks = (
        tracker.update(
            detections
        )
    )

    counts = (
        counter.count(
            tracks
        )
    )

    state = np.array(
        counts,
        dtype=np.float32
    )

    action, _ = (
        model.predict(
            state
        )
    )

    cv2.putText(
        frame,
        f"Action {action}",
        (30, 50),
        1,
        2,
        (0,255,0),
        2
    )

    frame_id += 1

video.release()

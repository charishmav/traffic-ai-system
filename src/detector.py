from ultralytics import RTDETR
import numpy as np


class VehicleDetector:

    def __init__(self):

        self.model = RTDETR(
            "models/rtdetr-l.pt"
        )

        self.vehicle_classes = [
            2,
            3,
            5,
            7
        ]

    def detect(self, frame):

        results = self.model(
            frame,
            conf=0.4,
            verbose=False
        )

        detections = []

        for r in results:

            if r.boxes is None:
                continue

            for box in r.boxes:

                cls = int(box.cls[0])

                if cls in self.vehicle_classes:

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    detections.append(
                        [x1, y1, x2, y2]
                    )

        return np.array(detections)

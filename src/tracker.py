import numpy as np
import torch
from ocsort import OCSort


class VehicleTracker:

    def __init__(self):

        self.tracker = OCSort()

    def update(self, detections, frame=None):

        if len(detections) == 0:

            return np.empty((0, 5))

        conf = np.ones(
            (
                len(detections),
                1
            )
        )

        cls = np.zeros(
            (
                len(detections),
                1
            )
        )

        dets = np.hstack(
            (
                detections,
                conf,
                cls
            )
        )

        tracks = self.tracker.update(
            torch.tensor(dets).float(),
            frame
        )

        return tracks

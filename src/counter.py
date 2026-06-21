class VehicleCounter:

    def __init__(
        self,
        frame_width=1280,
        num_lanes=4
    ):

        self.num_lanes = num_lanes

        self.lane_width = (
            frame_width
            // num_lanes
        )

    def count(self, tracks):

        counts = [0] * self.num_lanes

        for t in tracks:

            x1, y1, x2, y2, _ = t

            lane = int(
                (
                    x1 + x2
                ) / 2
                //
                self.lane_width
            )

            lane = min(
                lane,
                self.num_lanes - 1
            )

            counts[lane] += 1

        return counts

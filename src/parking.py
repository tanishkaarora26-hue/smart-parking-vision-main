from dataclasses import dataclass


@dataclass
class ParkingSummary:
    total_spaces: int
    empty_spaces: int
    occupied_spaces: int

    @property
    def occupancy_percentage(self) -> float:
        if self.total_spaces == 0:
            return 0.0

        return (self.occupied_spaces / self.total_spaces) * 100


def summarize_detections(class_names, class_ids):
    """
    Create a parking summary from YOLO class IDs.

    Class 0 = space-empty
    Class 1 = space-occupied
    """

    empty_spaces = 0
    occupied_spaces = 0

    for class_id in class_ids:
        class_name = class_names[int(class_id)]

        if class_name == "space-empty":
            empty_spaces += 1

        elif class_name == "space-occupied":
            occupied_spaces += 1

    total_spaces = empty_spaces + occupied_spaces

    return ParkingSummary(
        total_spaces=total_spaces,
        empty_spaces=empty_spaces,
        occupied_spaces=occupied_spaces,
    )
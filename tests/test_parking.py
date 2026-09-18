import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.parking import ParkingSummary, summarize_detections

def test_empty_parking_summary():
    summary = ParkingSummary(
        total_spaces=10,
        empty_spaces=10,
        occupied_spaces=0,
    )

    assert summary.total_spaces == 10
    assert summary.empty_spaces == 10
    assert summary.occupied_spaces == 0
    assert summary.occupancy_percentage == 0.0


def test_full_parking_summary():
    summary = ParkingSummary(
        total_spaces=10,
        empty_spaces=0,
        occupied_spaces=10,
    )

    assert summary.occupancy_percentage == 100.0


def test_mixed_parking_summary():
    summary = ParkingSummary(
        total_spaces=20,
        empty_spaces=5,
        occupied_spaces=15,
    )

    assert summary.occupancy_percentage == 75.0


def test_summarize_detections():
    class_names = {
        0: "space-empty",
        1: "space-occupied",
    }

    class_ids = [0, 0, 1, 1, 1]

    summary = summarize_detections(
        class_names,
        class_ids,
    )

    assert summary.total_spaces == 5
    assert summary.empty_spaces == 2
    assert summary.occupied_spaces == 3
    assert summary.occupancy_percentage == 60.0
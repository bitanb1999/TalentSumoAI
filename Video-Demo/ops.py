from dataclasses import dataclass
from typing import Tuple

import numpy as np
import numpy.typing as npt


@dataclass
class Metrics:
    value_threshold: float
    time_min: float
    time_ignore: float
    above: bool


@dataclass
class Segments:
    regions: npt.NDArray[np.bool]
    cumulative_times: npt.NDArray[np.float]
    time_thresholded: npt.NDArray[np.bool]
    total_time: float


@dataclass
class Summary:
    count_per_minute: float
    fraction: float

    def __str__(self):
        return (
            f"Count (/min): {self.count_per_minute:.2f}, Fraction: {self.fraction:.2f}%"
        )


@dataclass
class Bounds:
    bounds: Tuple[float, float, float]
    increasing: bool


def segment(array, timestamps, metrics: Metrics):
    #assert len(timestamps) == len(array)
    array_bool = (
        array > metrics.value_threshold
        if metrics.above
        else array < metrics.value_threshold
    )

    array_bool_expanded = []
    last_true = float("-inf")
    for time, value in zip(timestamps, array_bool):
        if value:
            last_true = time
        array_bool_expanded.append(time - last_true <= metrics.time_ignore)
    array_bool_expanded = np.asarray(array_bool_expanded)

    time_in_state = []
    last_time = 0
    for time, value in zip(timestamps, array_bool_expanded):
        if value:
            prev_time = time_in_state[-1] if time_in_state else 0
            time_in_state.append(prev_time + time - last_time)
        else:
            time_in_state.append(0)
        last_time = time
    time_in_state = np.asarray(time_in_state)

    thresholded = time_in_state > metrics.time_min

    return Segments(array_bool_expanded, time_in_state, thresholded, timestamps[-1])


def summarize(segments: Segments):
    count = sum(
        1
        for i in range(1, len(segments.time_thresholded))
        if not segments.time_thresholded[i - 1]
        and segments.time_thresholded[i]
    )
    if segments.time_thresholded[-1]:
        count -= 1

    count /= segments.total_time / 60
    fraction = float(np.mean(segments.regions.astype(np.float))) * 100

    return Summary(count, fraction)


def score(summary: Summary, bounds: Bounds):
    increasing = bounds.increasing
    bounds = bounds.bounds

    count = summary.count_per_minute
    score = 0
    if count < bounds[0]:
        score = 1
    if bounds[0] <= count < bounds[1]:
        score = 2
    if bounds[1] <= count < bounds[2]:
        score = 3
    if count >= bounds[2]:
        score = 4
    return score if increasing else 5 - score


if __name__ == "__main__":
    summary = Summary(7, 0.67)
    bounds = Bounds((6, 8, 9), False)
    print(score(summary, bounds))

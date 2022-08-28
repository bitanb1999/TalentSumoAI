from all_videos import AllVideos
import numpy as np
from ops import Metrics

from sklearn.linear_model import LinearRegression

videos = AllVideos()

audio_thresh_range = np.linspace(0, 1, 11)

audio_min_threshold_range = np.linspace(0.5, 3, 11)

audio_ignore_range = np.linspace(0, 1, 11)

print(audio_ignore_range)

for thresh in audio_thresh_range:
    for min in audio_min_threshold_range:
        for ignore in audio_ignore_range:
            audio_metrics = Metrics()

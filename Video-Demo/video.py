import os
from typing import Optional
import formatting
import librosa
import numpy as np
import pandas as pd
import sys
from ops import Metrics, segment, Segments, Summary, summarize, Bounds, score

root = "."


def get_gaze_score(df):
    x_mean = df[[f" X_{x}" for x in range(36, 42)]].mean(axis=1)
    y_mean = df[[f" Y_{x}" for x in range(36, 42)]].mean(axis=1)
    z_mean = df[[f" Z_{x}" for x in range(36, 42)]].mean(axis=1)
    magnitude = -1 * (x_mean ** 2 + y_mean ** 2 + z_mean ** 2) ** 0.5

    x_mean = x_mean / magnitude
    y_mean = y_mean / magnitude
    z_mean = z_mean / magnitude

    df["X_u"] = x_mean
    df["Y_u"] = y_mean
    df["Z_u"] = z_mean

    df["gaze_score"] = (
            (df[" gaze_0_x"] - df["X_u"]).abs()
            + (df[" gaze_0_y"] - df["Y_u"]).abs()
            + (df[" gaze_0_z"] - df["Z_u"]).abs()
    )
    return df["gaze_score"].values


class Video:
    def __init__(
            self,
            video: str,
            gaze_metrics: Metrics = Metrics(0.35, 0.5, 0.05, True),
            audio_metrics: Metrics = Metrics(0.1, 0.1, 0.1, False),
            smile_metrics: Metrics = Metrics(50, 0.25, 0.05, True),
            gesture_metrics: Metrics = Metrics(0.5, 0.25, 0.05, True),
            gaze_bounds: Bounds = Bounds((1, 2, 4), False),
            audio_bounds: Bounds = Bounds((1.5, 2, 4), False),
            smile_bounds: Bounds = Bounds((0.5, 1, 2), True),
            gesture_bounds: Bounds = Bounds((1, 2, 5), True),
    ):
        print("anything")
        formatting.format(video,video)
        self.gaze_score: Optional[int] = None
        self.audio_score: Optional[int] = None
        self.smile_score: Optional[int] = None
        self.gesture_score: Optional[int] = None

        self.audio_summary_raw: Optional[Segments] = None
        self.gaze_summary_raw: Optional[Segments] = None
        self.smile_summary_raw: Optional[Segments] = None
        self.gesture_summary_raw: Optional[Segments] = None

        self.smile_metrics = smile_metrics
        self.audio_metrics = audio_metrics
        self.gaze_metrics = gaze_metrics
        self.gesture_metrics = gesture_metrics

        self.smile_bounds = smile_bounds
        self.audio_bounds = audio_bounds
        self.gaze_bounds = gaze_bounds
        self.gesture_bounds = gesture_bounds
        self.gaze_summary: Optional[Summary] = None
        self.audio_summary: Optional[Summary] = None
        self.smile_summary: Optional[Summary] = None
        self.gesture_summary: Optional[Summary] = None

        self.video = video

        self.df = pd.read_csv(
            os.path.join(root, os.path.join("processed", f"{video}.csv"))
        )
        self.timestamps = self.df[" timestamp"].values
        self.gaze_scores = get_gaze_score(self.df)
        self.gaze_scores = (self.gaze_scores - np.min(self.gaze_scores)) / (
                np.max(self.gaze_scores) - np.min(self.gaze_scores)
        )
        self.calculate_gaze_metrics()
  #audio
        self.signal_raw, sr = librosa.load(os.path.join(root, f"{video}.wav"), sr=None)
        self.signal_raw = np.abs(self.signal_raw)
        signal_length = len(self.signal_raw)
        factor = signal_length // 2000
        self.signal_raw = self.signal_raw[: factor * 2000]
        self.signal_raw = np.reshape(self.signal_raw, (factor, 2000))
        self.signal_raw = np.mean(self.signal_raw, -1)
        self.signal_raw = self.signal_raw / np.max(self.signal_raw)
        total_duration = self.timestamps[-1]
        self.audio_timestamps = np.linspace(0, total_duration, len(self.signal_raw))
        self.smile_scores = np.asarray(
            [
                int(x)
                for x in open(os.path.join(root, f"{video}.txt"), "r")
                .readline()
                .split(",")
            ]
        )
        self.calculate_smile_metrics()
  #gesture 

        self.gesture_scores = np.asarray(
            [
                int(x)
                for x in open(
                    os.path.join(root, f"{video}.hands.txt"), "r"
                ).readline()
            ]
        )
        self.calculate_gesture_metrics()
    
    def calculate_gaze_metrics(self):
        self.gaze_summary_raw = segment(
            self.gaze_scores, self.timestamps, self.gaze_metrics
        )
        self.calculate_gaze_summary()

    def calculate_gaze_summary(self):
        self.gaze_summary = summarize(self.gaze_summary_raw)
        self.gaze_score = score(self.gaze_summary, self.gaze_bounds)

    def calculate_smile_metrics(self):
        self.smile_summary_raw = segment(
            self.smile_scores, self.timestamps, self.smile_metrics
        )
        self.calculate_smile_summary()

    def calculate_smile_summary(self):
        self.smile_summary = summarize(self.smile_summary_raw)
        self.smile_score = score(self.smile_summary, self.smile_bounds)

#audio metrics
    def calculate_audio_metrics(self):
        self.audio_summary_raw = segment(
            self.signal_raw, self.audio_timestamps, self.audio_metrics
        )
        self.calculate_audio_summary()

    def calculate_audio_summary(self):
        self.audio_summary = summarize(self.audio_summary_raw)
        self.audio_score = score(self.audio_summary, self.audio_bounds)

#gesture metrics
    def calculate_gesture_metrics(self):
        self.gesture_summary_raw = segment(
            self.gesture_scores, self.timestamps, self.gesture_metrics
        )
        self.calculate_gesture_summary()

    def calculate_gesture_summary(self):
        self.gesture_summary = summarize(self.gesture_summary_raw)
        self.gesture_score = score(self.gesture_summary, self.gesture_bounds)

    def set_audio_metrics(self, audio_metrics: Metrics):
        self.audio_metrics = audio_metrics
        self.calculate_audio_metrics()

    def set_gaze_metrics(self, metrics: Metrics):
        self.gaze_metrics = metrics
        self.calculate_gaze_metrics()

    def set_smile_metrics(self, metrics: Metrics):
        self.smile_metrics = metrics
        self.calculate_smile_metrics()

    def set_gesture_metrics(self, metrics: Metrics):
        self.gesture_metrics = metrics
        self.calculate_gesture_metrics()

if __name__ == "__main__":
    video = Video(
        "try",
        Metrics(0.35, 0.5, 0.05, True),
        Metrics(300, 0.1, 0.1, False),
        Metrics(50, 0.25, 0.05, True),
    )
    print(video.gaze_summary_raw.total_time)

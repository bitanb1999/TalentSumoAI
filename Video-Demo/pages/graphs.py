from math import floor, ceil

import numpy as np
import plotly.express as px
from dash import html, dcc, callback, Output, Input
from plotly import graph_objs as go
from plotly.subplots import make_subplots

from all_videos import AllVideos
from ops import Metrics
from pages.table import (
    AUDIO_COUNT_VS_SCORE,
    GAZE_COUNT_VS_SCORE,
    SMILE_COUNT_VS_SCORE,
    GESTURE_COUNT_VS_SCORE,
)
from video import Video

SESSION_ID_ID = "session-id"
GAZE_GRAPH_ID = "gaze-graph"
AUDIO_GRAPH_ID = "audio-graph"
SMILE_GRAPH_ID = "smile-graph"
HANDS_GRAPH_ID = "hands_graph"
GAZE_SCORE_THRESHOLD_ID = "gaze_score_threshold"
AUDIO_THRESHOLD_ID = "audio_threshold"
SMILE_THRESHOLD_ID = "smile_threshold"
GESTURE_THRESHOLD_ID = "gesture_threshold"
GAZE_DURATION_THRESHOLD_ID = "gaze_duration_threshold"
AUDIO_DURATION_THRESHOLD_ID = "audio_duration_threshold"
SMILE_DURATION_THRESHOLD_ID = "smile_duration_threshold"
GESTURE_DURATION_THRESHOLD_ID = "gesture_duration_threshold"
GAZE_DURATION_IGNORE_ID = "gaze_duration_ignore"
AUDIO_DURATION_IGNORE_ID = "audio_duration_ignore"
SMILE_DURATION_IGNORE_ID = "smile_duration_ignore"
GESTURE_DURATION_IGNORE_ID = "gesture_duration_ignore"

layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(id=GAZE_GRAPH_ID),
                    ],
                    style={"flex": "1"},
                ),
                html.Div(
                    [
                        dcc.Graph(id=AUDIO_GRAPH_ID),
                    ],
                    style={"flex": "1"},
                ),
            ],
            style={"display": "flex", "flex-direction": "row"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(id=SMILE_GRAPH_ID),
                    ],
                    style={"flex": "1"},
                ),
                html.Div(
                    [
                        dcc.Graph(id=HANDS_GRAPH_ID),
                    ],
                    style={"flex": "1"},
                ),
            ],
            style={"display": "flex", "flex-direction": "row"},
        ),
        html.Button('Generate CSV', id='make_csv', n_clicks=0),
        html.Div(id='hidden')
    ],
)

cache: dict[str, dict[str, Video]] = {}

all_videos = AllVideos()
full_df = None


@callback(Output(SESSION_ID_ID, "data"), Input(SESSION_ID_ID, "data"))
def update_session_id(session_id):
    if session_id is None:
        session_id = "session"
    return session_id


@callback(
    Output(GAZE_GRAPH_ID, "figure"),
    Output(AUDIO_GRAPH_ID, "figure"),
    Output(SMILE_GRAPH_ID, "figure"),
    Output(HANDS_GRAPH_ID, "figure"),
    Output("table", "data"),
    Output(GAZE_COUNT_VS_SCORE, "figure"),
    Output(AUDIO_COUNT_VS_SCORE, "figure"),
    Output(SMILE_COUNT_VS_SCORE, "figure"),
    Output(GESTURE_COUNT_VS_SCORE, "figure"),
    Input(GAZE_SCORE_THRESHOLD_ID, "value"),
    Input(GAZE_DURATION_THRESHOLD_ID, "value"),
    Input(GAZE_DURATION_IGNORE_ID, "value"),
    Input(AUDIO_THRESHOLD_ID, "value"),
    Input(AUDIO_DURATION_THRESHOLD_ID, "value"),
    Input(AUDIO_DURATION_IGNORE_ID, "value"),
    Input(SMILE_THRESHOLD_ID, "value"),
    Input(SMILE_DURATION_THRESHOLD_ID, "value"),
    Input(SMILE_DURATION_IGNORE_ID, "value"),
    Input(GESTURE_THRESHOLD_ID, "value"),
    Input(GESTURE_DURATION_THRESHOLD_ID, "value"),
    Input(GESTURE_DURATION_IGNORE_ID, "value"),
    Input("url", "pathname"),
)
def plot_gaze(
        g_threshold,
        g_duration_threshold,
        g_duration_ignore,
        a_threshold,
        a_duration_threshold,
        a_duration_ignore,
        s_threshold,
        s_duration_threshold,
        s_duration_ignore,
        h_threshold,
        h_duration_threshold,
        h_duration_ignore,
        pathname,
):
    global full_df
    g_metrics = Metrics(g_threshold, g_duration_threshold, g_duration_ignore, True)
    all_videos.set_gaze_metrics(g_metrics)

    a_metrics = Metrics(a_threshold, a_duration_threshold, a_duration_ignore, False)
    all_videos.set_audio_metrics(a_metrics)

    s_metrics = Metrics(s_threshold, s_duration_threshold, s_duration_ignore, True)
    all_videos.set_smile_metrics(s_metrics)

    h_metrics = Metrics(h_threshold, h_duration_threshold, h_duration_ignore, True)
    all_videos.set_gesture_metrics(h_metrics)

    df = all_videos.get_data()

    if pathname == "/":
        return go.Figure(), go.Figure(), df.to_dict("records")
    else:
        video_name = pathname.split("/")[-1]

    video = all_videos.get_video(video_name)

    g_segments = video.gaze_summary_raw

    g_fig = make_subplots(specs=[[{"secondary_y": True}]])
    g_fig.add_trace(
        go.Scatter(
            x=video.timestamps, y=video.gaze_scores, mode="lines", name="Gaze Score"
        )
    )
    g_fig.add_trace(
        go.Scatter(
            x=video.timestamps,
            y=g_segments.cumulative_times,
            mode="lines",
            name="Distracted Duration",
        ),
        secondary_y=True,
    )

    max_time = np.max(g_segments.cumulative_times)
    g_fig.add_trace(
        go.Scatter(
            x=video.timestamps,
            y=g_segments.time_thresholded * max_time,
            mode="none",
            fill="tozeroy",
            name="Distraction Thresholded",
        ),
        secondary_y=True,
    )

    a_segments = video.audio_summary_raw

    a_fig = make_subplots(specs=[[{"secondary_y": True}]])
    a_fig.add_trace(
        go.Scatter(
            x=video.audio_timestamps,
            y=video.signal_raw,
            mode="lines",
            name="Audio Volume",
        )
    )
    a_fig.add_trace(
        go.Scatter(
            x=video.audio_timestamps,
            y=a_segments.cumulative_times,
            mode="lines",
            name="Silence Duration",
        ),
        secondary_y=True,
    )

    max_time = np.max(a_segments.cumulative_times)
    a_fig.add_trace(
        go.Scatter(
            x=video.audio_timestamps,
            y=a_segments.time_thresholded * max_time,
            mode="none",
            fill="tozeroy",
            name="Silence Elongated",
        ),
        secondary_y=True,
    )

    # Smile Scores
    s_segments = video.smile_summary_raw

    s_fig = make_subplots(specs=[[{"secondary_y": True}]])
    s_fig.add_trace(
        go.Scatter(
            x=video.timestamps,
            y=video.smile_scores,
            mode="lines",
            name="Smile Score",
        )
    )
    s_fig.add_trace(
        go.Scatter(
            x=video.timestamps,
            y=s_segments.cumulative_times,
            mode="lines",
            name="Happiness Duration",
        ),
        secondary_y=True,
    )

    max_time = np.max(s_segments.cumulative_times)
    s_fig.add_trace(
        go.Scatter(
            x=video.timestamps,
            y=s_segments.time_thresholded * max_time,
            mode="none",
            fill="tozeroy",
            name="Hapiness Elongated",
        ),
        secondary_y=True,
    )

    # gestures Graph

    h_segments = video.gesture_summary_raw

    h_fig = make_subplots(specs=[[{"secondary_y": True}]])
    h_fig.add_trace(
        go.Scatter(
            x=video.timestamps,
            y=video.smile_scores,
            mode="lines",
            name="Gesture Score",
        )
    )
    h_fig.add_trace(
        go.Scatter(
            x=video.timestamps,
            y=h_segments.cumulative_times,
            mode="lines",
            name="Gesture Duration",
        ),
        secondary_y=True,
    )

    max_time = np.max(h_segments.cumulative_times)
    h_fig.add_trace(
        go.Scatter(
            x=video.timestamps,
            y=h_segments.time_thresholded * max_time,
            mode="none",
            fill="tozeroy",
            name="Gesture Elongated",
        ),
        secondary_y=True,
    )

    gaze_scoring = px.scatter(
        data_frame=df,
        x="Estimated Body Language",
        y="Gaze Counts",
        hover_data=["Video"],
        color=[x[:-1] for x in df["Video"]],
        # trendline="ols",
    )
    audio_scoring = px.scatter(
        data_frame=df,
        x="Estimated Audio",
        y="Audio Counts",
        hover_data=["Video"],
        color=[x[:-1] for x in df["Video"]],
        # trendline="ols",
    )

    smile_scoring = px.scatter(
        data_frame=df,
        x="Estimated Confidence",
        y="Smile Count",
        hover_data=["Video"],
        color=[x[:-1] for x in df["Video"]],
        # trendline="ols",
    )

    gesture_scoring = px.scatter(
        data_frame=df,
        x="Estimated Gesture",
        y="Gesture Count",
        hover_data=["Video"],
        color=[x[:-1] for x in df["Video"]],
        # trendline="ols",
    )
    full_df = df
    return (
        g_fig,
        a_fig,
        s_fig,
        h_fig,
        df[["Video"] + list(df.columns[-8:])].to_dict("records"),
        gaze_scoring,
        audio_scoring,
        smile_scoring,
        gesture_scoring,
    )


@callback(Output('hidden', 'content'), Input('make_csv', 'n_clicks'))
def make_csv(n_clicks):
    global full_df
    csv_df = full_df[
        ["Video", "Gaze Counts", "Gaze Fractions", "Audio Counts", "Audio Fractions", "Smile Count", "Gesture Count",
         "Smile Score", "Smile Percentile", "Audio Score", "Audio Percentile", "Gaze Score", "Gaze Percentile",
         "Gesture Score", "Gesture Percentile"]]
    abc_likeability = ['E', 'D', 'C', 'B', 'A']
    csv_df["Likeability"] = [abc_likeability[x] for x in csv_df["Smile Score"]]
    csv_df["Charm"] = [abc_likeability[ceil((x+y)/3)] for x, y in zip(csv_df["Gaze Score"], csv_df["Gesture Score"])]
    csv_df["Rounded Off Gaze Count"] = [ceil(x) for x in csv_df["Gaze Counts"]]
    csv_df.to_csv('metrics_and_scores.csv')

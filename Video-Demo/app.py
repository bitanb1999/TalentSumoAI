from dash import dcc, html, Output, callback, Dash, Input, dash_table

from pages import graphs, table
from pages.graphs import (
    SESSION_ID_ID,
    GAZE_SCORE_THRESHOLD_ID,
    GAZE_DURATION_THRESHOLD_ID,
    GAZE_DURATION_IGNORE_ID,
    AUDIO_THRESHOLD_ID,
    AUDIO_DURATION_THRESHOLD_ID,
    AUDIO_DURATION_IGNORE_ID,
    SMILE_THRESHOLD_ID,
    SMILE_DURATION_THRESHOLD_ID,
    SMILE_DURATION_IGNORE_ID,
    GESTURE_THRESHOLD_ID,
    GESTURE_DURATION_IGNORE_ID,
    GESTURE_DURATION_THRESHOLD_ID,
)
from pages.table import (
    GAZE_COUNT_VS_SCORE,
    AUDIO_COUNT_VS_SCORE,
    SMILE_COUNT_VS_SCORE,
    GESTURE_COUNT_VS_SCORE,
)

layout = html.Div(
    [
        # Stores
        dcc.Store(id=SESSION_ID_ID),
        dcc.Location(id="url", refresh=False),
        dash_table.DataTable(id="table"),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(id=GAZE_COUNT_VS_SCORE),
                    ],
                    style={"flex": "1"},
                ),
                html.Div(
                    [
                        dcc.Graph(id=AUDIO_COUNT_VS_SCORE),
                    ],
                    style={"flex": "1"},
                ),
                html.Div(
                    [
                        dcc.Graph(id=SMILE_COUNT_VS_SCORE),
                    ],
                    style={"flex": "1"},
                ),
                html.Div(
                    [
                        dcc.Graph(id=GESTURE_COUNT_VS_SCORE),
                    ],
                    style={"flex": "1"},
                ),
            ],
            style={"display": "flex", "flex-direction": "row"},
        ),
        html.Div(id="page-content"),
        html.Div(
            [
                html.Div(
                    [
                        html.Label("Gaze Metrics:"),
                        html.Label("Minimum Gaze Score: "),
                        dcc.Slider(0, 1, id=GAZE_SCORE_THRESHOLD_ID, value=0.35),
                        html.Label("Minimum Gaze Duration: "),
                        dcc.Slider(0, 3, id=GAZE_DURATION_THRESHOLD_ID, value=0.5),
                        html.Label("Ignore Gaze Duration: "),
                        dcc.Slider(0, 1, id=GAZE_DURATION_IGNORE_ID, value=0.05),
                    ],
                    style={"flex": "1"},
                ),
                html.Div(
                    [
                        html.Label("Audio Metrics:"),
                        html.Label("Minimum Audio Volume: "),
                        dcc.Slider(0, 1, id=AUDIO_THRESHOLD_ID, value=300),
                        html.Label("Minimum Silence Duration: "),
                        dcc.Slider(0, 3, id=AUDIO_DURATION_THRESHOLD_ID, value=1),
                        html.Label("Ignore Silence Duration: "),
                        dcc.Slider(0, 1, id=AUDIO_DURATION_IGNORE_ID, value=0.05),
                    ],
                    style={"flex": "1"},
                ),
                html.Div(
                    [
                        html.Label("Smile Metrics:"),
                        html.Label("Minimum Smile Value: "),
                        dcc.Slider(0, 100, id=SMILE_THRESHOLD_ID, value=50),
                        html.Label("Minimum Silence Duration: "),
                        dcc.Slider(0, 3, id=SMILE_DURATION_THRESHOLD_ID, value=1),
                        html.Label("Ignore Silence Duration: "),
                        dcc.Slider(0, 1, id=SMILE_DURATION_IGNORE_ID, value=0.05),
                    ],
                    style={"flex": "1"},
                ),
                html.Div(
                    [
                        html.Label("Gesture Metrics:"),
                        html.Label("Minimum GESTURE Value: "),
                        dcc.Slider(0, 1, id=GESTURE_THRESHOLD_ID, value=0.5),
                        html.Label("Minimum Silence Duration: "),
                        dcc.Slider(0, 3, id=GESTURE_DURATION_THRESHOLD_ID, value=1),
                        html.Label("Ignore Silence Duration: "),
                        dcc.Slider(0, 1, id=GESTURE_DURATION_IGNORE_ID, value=0.05),
                    ],
                    style={"flex": "1"},
                ),
            ],
            style={"display": "flex", "flex-direction": "row"},
        ),
    ]
)

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = layout


@callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/":
        return table.layout
    return graphs.layout


if __name__ == "__main__":
    app.run_server(debug=True)

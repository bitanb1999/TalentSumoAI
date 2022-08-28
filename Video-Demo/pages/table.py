from dash import html, dcc

TABLE_PLACEHOLDER_ID = "table-placeholder"
GAZE_COUNT_VS_SCORE = "gaze-scores"
AUDIO_COUNT_VS_SCORE = "audio-scores"
SMILE_COUNT_VS_SCORE = "smile-scores"
GESTURE_COUNT_VS_SCORE = "gesture-scores"

layout = html.Div(
    children=[
        html.Div(id=TABLE_PLACEHOLDER_ID),
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
            ],
            style={"display": "flex", "flex-direction": "row"},
        ),
    ]
)

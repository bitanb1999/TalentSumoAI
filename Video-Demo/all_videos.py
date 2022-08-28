import pandas as pd

from ops import Metrics
from video import Video
from kk import download_file
from math import ceil
class AllVideos:
    def __init__(
            self,
            responses_file: str = "C:/Users/piyan/OneDrive/Desktop/dataset/response.csv",
    ):
        self.responses_file = responses_file
        self.df = pd.read_csv(self.responses_file)
        self.names = self.df["Candidate_ID"]
        self.video_names = []
        
        for i in range(len(self.df["Response"])-1):
           download_file(self.df["Response"][i],f'n{i}')
        self.videos = [Video(f'n{i}') for i in range(len(self.df["Response"])-1)]    
        

    def get_video(self, video_name: str):
        for video in self.videos:
            if video.video == video_name:
                return video

    def set_gaze_metrics(self, metrics: Metrics):
        for video in self.videos:
            video.set_gaze_metrics(metrics)

    def set_audio_metrics(self, metrics: Metrics):
        for video in self.videos:
            video.set_audio_metrics(metrics)

    def set_smile_metrics(self, metrics: Metrics):
        for video in self.videos:
            video.set_smile_metrics(metrics)

    def set_gesture_metrics(self, metrics: Metrics):
        for video in self.videos:
            video.set_gesture_metrics(metrics)

    def get_data(self):
        video_names = []
        video_feedback = []
        gaze_summary_counts = []
        gaze_summary_fractions = []
        est_bodylang = []
        audio_summary_counts = []
        audio_summary_fractions = []
        est_audio = []
        smile_counts = []
        est_hapiness = []
        gesture_count = []
        est_gesture = []

        smile_scores = []
        audio_scores = []
        gaze_scores = []
        gesture_scores = []
        for video in self.videos:
            name = video.video[:]
            number = 1
            video_names.append(video.video)
            feedback_col = f"Comments on video for Q{number}"
            #take the feedback here, if needed
            video_feedback.append("A"
                
            )
            #coming from openface csv file
            gaze_summary_counts.append(video.gaze_summary.count_per_minute)
            gaze_summary_fractions.append(video.gaze_summary.fraction)
           

            smile_counts.append(video.smile_summary.count_per_minute)
            
            gesture_count.append(video.gesture_summary.count_per_minute)
            
            smile_scores.append(video.smile_score)
            audio_scores.append(video.audio_score)
            gaze_scores.append(video.gaze_score)
            gesture_scores.append(video.gesture_score)

           
        return pd.DataFrame(
            {
                "Video": video_names,
                "Feedback": video_feedback,
                "Gaze Counts": gaze_summary_counts,
                "Gaze Fractions": gaze_summary_fractions,
               
                "Smile Count": smile_counts,
                
                "Gesture Count": gesture_count,
               
                "Smile Score": smile_scores,
                "Smile Percentile": pd.Series(smile_counts).rank(pct=True),
              
                "Gaze Score": gaze_scores,
                "Gaze Percentile": pd.Series(gaze_summary_counts).rank(pct=True, ascending=False),
                "Gesture Score": gesture_scores,
                "Gesture Percentile": pd.Series(gesture_scores).rank(pct=True),
            }
        )
a=AllVideos()

csv_df = a.get_data()[
        ["Video", "Gaze Counts", "Gaze Fractions", "Smile Count", "Gesture Count",
         "Smile Score", "Smile Percentile",  "Gaze Score", "Gaze Percentile",
         "Gesture Score", "Gesture Percentile"]]
abc_likeability = ['D', 'D', 'C', 'B', 'A']
'''csv_df["Likeability"] = [abc_likeability[x] for x in csv_df["Smile Score"]]
csv_df["Charm"] = [abc_likeability[ceil((x+y)/3)] for x, y in zip(csv_df["Gaze Score"], csv_df["Gesture Score"])]
csv_df["Rounded Off Gaze Count"] = [ceil(x) for x in csv_df["Gaze Counts"]]
csv_df.to_csv('metrics_and_scores.csv')'''

add = pd.read_csv('output.csv')
add.loc[1]['Video'] = 1
print(add.loc[0]['Video'])

for i in range(1,len(csv_df["Smile Score"])+1):
    add.loc[i]['Video.1'] = abc_likeability[csv_df["Smile Score"][i-1]]
    add.loc[i]['Video.2'] = abc_likeability[ceil((csv_df["Gaze Score"][i-1] + csv_df["Gesture Score"][i-1])/3)]
    add.loc[i]['Video'] = abc_likeability[csv_df["Gesture Score"][i-1]]

add.to_csv('trial1.csv')
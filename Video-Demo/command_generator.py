import argparse
import os

if __name__ == "__main__":
    # Take openface binary path and videos pages as arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b",
        "--binary",
        help="Path to openface binary.",
        default=os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "/home/openface-build/build/bin/FeatureExtraction",
        ),
    )
    parser.add_argument(
        "-r",
        "--root",
        help="Path to pages directory of videos.",
        default=os.path.join(os.path.dirname(os.path.realpath(__file__)), "/input/"),
    )
    parser.add_argument(
        "-d",
        "--host",
        help="Path to destination directory.",
        default=os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "C:/Users/piyan/OneDrive/Desktop/dataset",
        ),
    )
    parser.add_argument(
        "-f", "--force", help="Force overwrite of existing files.", action="store_true"
    )
    args = parser.parse_args()

    videos = [
        x
        for x in os.listdir(args.host)
        if os.path.isfile(os.path.join(args.host, x))
        and (x.endswith(".mp4") or x.endswith(".avi") or x.endswith(".mkv"))
    ]

    processed = os.path.join(args.host, "processed")
    processed_files = {}
    try:
        processed_files = {x[:-4] for x in os.listdir(processed) if x.endswith(".csv")}
    except FileNotFoundError:
        pass
    command_string = f"{args.binary} "

    for video in videos:
        print(video[:-4])
        if video[:-4] not in processed_files:
            command_string += f"-f {os.path.join(args.root, video)} "

    print(command_string)

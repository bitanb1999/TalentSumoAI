import subprocess
import argparse
import os

if __name__ == "__main__":
    # Take source folder name as argument
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--source",
        default="C:/Users/piyan/OneDrive/Desktop/dataset",
        help="Source folder name",
    )
    args = parser.parse_args()

    # Create a list of all files in the source folder
    files = [
        x
        for x in os.listdir(args.source)
        if x.endswith(".mp4") or x.endswith(".mkv") or x.endswith(".avi")
    ]

    # Run ffmpeg on all files in the source folder
    for file in files:
        subprocess.call(
            [
                "ffmpeg",
                "-i",
                os.path.join(args.source, file),
                os.path.join(args.source, "processed", f"{file[:-4]}.wav"),
            ]
        )

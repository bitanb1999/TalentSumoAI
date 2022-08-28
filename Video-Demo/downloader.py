import os
import gdown
import argparse
import pandas as pd

if __name__ == "__main__":
    # Take destination directory and csv file as arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dest",
        type=str,
        default="C:/Users/piyan/OneDrive/Desktop/dataset",
        help="Destination directory",
    )
    parser.add_argument(
        "--csv",
        type=str,
        default="C:/Users/piyan/OneDrive/Desktop/dataset/responses.csv",
        help="CSV file",
    )
    args = parser.parse_args()

    # List all files (not directories) in destination directory
    files = filter(
        lambda x: os.path.isfile(os.path.join(args.dest, x)), os.listdir(args.dest)
    )
    names = set([x[:-5] for x in files])
    # print(names)
    responses = pd.read_csv(args.csv)
    # print(responses.columns)
    undownloaded_rows = responses[~responses["Name"].isin(names)]
    for _, row in undownloaded_rows.iterrows():
        for i in range(1, 7):
            print(row[f"Video for Q{i})"])
            gdown.download(
                row[f"Video for Q{i})"],
                f"{args.dest}/{row['Name']}{i}.mp4",
                quiet=False,
                fuzzy=True,
            )

from google_drive_downloader import GoogleDriveDownloader as gdd



def download_file(real_file_id,name):
    real_file_id=real_file_id.split('/')[5]
    gdd.download_file_from_google_drive(file_id=real_file_id,
                                    dest_path=f'./{name}.mp4')
                                
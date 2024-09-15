import kaggle
import os

def download_dataset(dataset_name, download_path):
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)

download_dataset('dataset/your-dataset-name', './data')

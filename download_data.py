from pathlib import Path

import requests

data_path = Path('./data')

data_files = {
   'summary_listings.csv': r'http://data.insideairbnb.com/united-kingdom/england/london/2021-02-09/visualisations/listings.csv',
   'listings.csv.gz': r'http://data.insideairbnb.com/united-kingdom/england/london/2021-02-09/data/listings.csv.gz',
}

def make_data_dir():
    if data_path.exists():
        return
    data_path.mkdir()

def download_data(name, url):
    print(f'Downloading {name}')
    r = requests.get(url)
    print(f'Done')
    with open(data_path / name, 'wb') as f:
        f.write(r.content)

if __name__ == '__main__':
    to_download = ', '.join(data_files.keys())
    print(f'{to_download} will be downloaded to {data_path.resolve()}')
    make_data_dir()
    for name, url in data_files.items():
        download_data(name, url)

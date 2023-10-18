import argparse
import pandas as pd
import pandas_profiling
from pandas_profiling import ProfileReport

def generate_profile_pandas(file_path, file_type, output_file):
    df = pd.read_csv(file_path)
    profile = ProfileReport(df, title="Data Report", explorative=True)
    if file_type == 'html':
        profile.to_file(output_file + "_report.html")
    elif file_type == 'json':
        # As a JSON string
        json_data = profile.to_json()
        print("json_data: ", json_data)
        # As a file
        profile.to_file(output_file + "_report.json")
    elif file_type == 'jupyter':
        # As a file
        profile.to_widgets()
        profile.to_notebook_iframe()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a pandas profile report.')
    parser.add_argument('--file_path', type=str, help='The name of the input file.')
    parser.add_argument('--file_type', type=str, choices=['html', 'json', 'jupyter'], help='The type of the output file.')
    parser.add_argument('--output_file', type=str, help='The name of the output file.')
    args = parser.parse_args()
    generate_profile_pandas(args.file_path, args.file_type, args.output_file)
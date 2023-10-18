import sweetviz as sv
import pandas as pd
import argparse

def generate_report_sweetviz(csv_path, output_file):
    df = pd.read_csv(csv_path)
    my_report = sv.analyze(df)
    # Default arguments will generate to "SWEETVIZ_REPORT.html"
    my_report.show_html(output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a sweetviz report.')
    parser.add_argument('--csv_path', type=str, help='The path of the input CSV file.')
    parser.add_argument('--output_file', type=str, help='The path of the output HTML file.')
    args = parser.parse_args()
    generate_report_sweetviz(args.csv_path, args.output_file)
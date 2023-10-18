

#    parser = argparse.ArgumentParser(description='Generate a pandas profile report.')
#    parser.add_argument('--file_path', type=str, help='The name of the input file.')
#    parser.add_argument('--file_type', type=str, choices=['html', 'json', 'jupyter'], help='The type of the output file.')
#    parser.add_argument('--output_file', type=str, help='The name of the output file.')
python eda/generate_report_pandas_profiling.py --file_path csv/coco128_annotations.csv --file_type 'html' --output_file report/coco128_annotations

#    parser = argparse.ArgumentParser(description='Generate a sweetviz report.')
#    parser.add_argument('--csv_path', type=str, help='The path of the input CSV file.')
#    parser.add_argument('--output_file', type=str, help='The path of the output HTML file.')
#    args = parser.parse_args()
python eda/generate_report_sweetiz.py --csv_path csv/coco128_annotations.csv --output_file report/coco128_annotations_report.html

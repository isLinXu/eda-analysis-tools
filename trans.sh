

python eda/utils/xml2csv.py -i data/voc128/Annotations -o csv/voc128.csv -l data/voc128/

python eda/utils/yolo2csv.py --txtDir data/yolo128/images/train2017 --imgDir data/yolo128/labels/train2017 --outputFile csv/yolo128.csv

python eda/utils/yolo2csv.py --txtDir /Users/gatilin/PycharmProjects/eda-analysis-tools/data/yolo128/labels/train2017 --imgDir /Users/gatilin/PycharmProjects/eda-analysis-tools/data/yolo128/images/train2017 --outputFile csv/yolo128.csv

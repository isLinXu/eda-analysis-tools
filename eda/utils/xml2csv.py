import argparse
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import seaborn as sns


def xml_to_csv(path):
    """Iterates through all .xml files (generated by labelImg) in a given directory and combines them in a single Pandas datagrame.

    Parameters:
    ----------
    path : {str}
        The path containing the .xml files
    Returns
    -------
    Pandas DataFrame
        The produced dataframe
    """
    classes_names = []
    xml_list = []
    for xml_file in glob.glob(path + "/*.xml"):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall("object"):
            classes_names.append(member[0].text)
            value = (
                root.find("filename").text,
                int(root.find("size")[0].text),
                int(root.find("size")[1].text),
                member[0].text,
                int(member[4][0].text),
                int(member[4][1].text),
                int(member[4][2].text),
                int(member[4][3].text),
            )
            xml_list.append(value)
    column_name = [
        "filename",
        "width",
        "height",
        "class",
        "xmin",
        "ymin",
        "xmax",
        "ymax",
    ]
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    classes_names = list(set(classes_names))
    classes_names.sort()
    return xml_df, classes_names


# 主运行函数
def run(inputDir, outputFile, labelMapDir):
    if inputDir is None:
        inputDir = os.getcwd()
    if outputFile is None:
        outputFile = inputDir + "/labels.csv"

    os.makedirs(os.path.dirname(outputFile), exist_ok=True)
    xml_df, classes_names = xml_to_csv(inputDir)
    xml_df.to_csv(outputFile, index=None)
    print("Successfully converted xml to csv.")
    if labelMapDir:
        os.makedirs(labelMapDir, exist_ok=True)
        label_map_path = os.path.join(labelMapDir, "label_map.txt")
        print("Generate `{}`".format(label_map_path))

        # Create the `label_map.pbtxt` file
        pbtxt_content = ""
        for i, class_name in enumerate(classes_names):
            pbtxt_content = (
                    pbtxt_content
                    + "item {{\n    id: {0}\n    name: '{1}'\n}}\n\n".format(
                i + 1, class_name
            )
            )
        pbtxt_content = pbtxt_content.strip()
        with open(label_map_path, "w") as f:
            f.write(pbtxt_content)


def main():
    parser = argparse.ArgumentParser(description="Convert XML annotations to CSV format")
    parser.add_argument("-i", "--inputDir", help="Path to the directory containing XML files", required=True)
    parser.add_argument("-o", "--outputFile", help="Path to the output CSV file", required=True)
    parser.add_argument("-l", "--labelMapDir", help="Path to the directory to save label_map.pbtxt file", required=True)

    args = parser.parse_args()

    inputDir = args.inputDir
    outputFile = args.outputFile
    labelMapDir = args.labelMapDir

    run(inputDir, outputFile, labelMapDir)


if __name__ == '__main__':
    main()

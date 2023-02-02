import xml.etree.ElementTree as ElementTree
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filepath", help="JaCoCo XML filepath", required=True)
args = parser.parse_args()

tree = ElementTree.parse(args.filepath)
root = tree.getroot()
for package in root.findall('package'):
    package_name = package.get('name')
    for sourcefile in package.findall('sourcefile'):
        sourcefile_name = sourcefile.get('name')
        for line in sourcefile.findall('line'):
            if line.get('mi') == '0':
                line_number = line.get('nr')
                print(f'{package_name}{sourcefile_name}:{line_number}')

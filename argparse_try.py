import argparse

parser = argparse.ArgumentParser(description='Generate classes for provided URLs.')
parser.add_argument('filename', metavar='filename', type=str, default='web_scraping.xlsx',
                    help='Name of xlsx file containing URLs and xpaths.', const=1, nargs='?')
parser.add_argument('sheet_name', metavar='sheet_name', type=str, default='GotoweXPath',
                    help='Name of sheet containing URLs and xpaths.', const=1, nargs='?')

args = parser.parse_args()

filename = args.filename
sheet_name = args.sheet_name
print(filename, sheet_name)
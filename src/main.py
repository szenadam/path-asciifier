import argparse

parser = argparse.ArgumentParser(description='ASCIIfy path.')

parser.add_argument('path', metavar='path', type=str, nargs='+', help='A Directory path')

args = parser.parse_args()

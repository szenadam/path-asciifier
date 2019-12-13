import argparse
from modules.lister import FileLister


def main():
    description = """
        ASCIIfy path. Remove non-ascii characters from file or directory names. 
    """

    # Parse arguments
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('path', metavar='path', type=str, nargs='+', help='A Directory path')
    args = parser.parse_args()

    # List files in directory
    file_lister = FileLister()

    print(file_lister.list_files(args.path[0]))


if __name__ == "__main__":
    main()

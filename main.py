import argparse


def main():
    description = """
        ASCIIfy path. Remove non-ascii characters from file or directory names. 
    """

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('path', metavar='path', type=str, nargs='+', help='A Directory path')

    args = parser.parse_args()

    print(args.accumulate)


if __name__ == "__main__":
    main()

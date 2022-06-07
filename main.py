
from functions import get_header, get_data, make_graph
import sys


def main():
    file_name = "data.csv"
    dotted = False
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        dotted = sys.argv[1]
    elif len(sys.argv) == 2:
        if sys.argv[1] in ["True", "False"]:
            dotted = True if sys.argv[1]=="True" else False
        else:
            file_name = sys.argv[1]
    
    data = get_data(file_name)
    header = get_header(file_name)
    make_graph(data, header, dotted)


if __name__ == "__main__":
    main()

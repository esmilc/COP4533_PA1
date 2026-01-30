import sys
from matching import matching
from read_file import read_file
from write_file import write_file
from verifier import verifier
import time


def main():
    if sys.argv[1] != "match" and sys.argv[1] != "verify":
        print("INVALID ACTION: ", sys.argv[1], ". Must enter 'match' or 'verify'.")
        return -1
    
    if sys.argv[1] == "match":
        if not sys.argv[2]:
            return -1
        filename = sys.argv[2]
        raw_input = read_file(filename)
        
        start = time.perf_counter()
        output = matching(raw_input)
        end = time.perf_counter()
        print("Matching runtime:", end - start, "seconds")

        write_file("output_" + filename, output)
        print("Output written to 'output_" + filename + "'")

if __name__ == '__main__':
    main()
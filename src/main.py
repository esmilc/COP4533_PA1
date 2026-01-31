import sys
from matching import matching
from read_file import read_file
from write_file import write_file
from verifier import verifier
import time


def main():
    if len(sys.argv) <= 1 or (sys.argv[1] != "match" and sys.argv[1] != "verify"):
        print("INVALID ACTION. Must enter 'match' or 'verify'.")
        return -1
    
    if sys.argv[1] == "match":
        if len(sys.argv) <= 2:
            print("ERROR..missing [preference_list.txt]")
            return -1
        filename = sys.argv[2]
        raw_input = read_file(filename)
        
        #start = time.perf_counter()
        output = matching(raw_input)
        #end = time.perf_counter()
        #print("Matching runtime:", end - start, "seconds")

        write_file("output_" + filename, output)
        print("Output written to 'output_" + filename + "'")

    elif sys.argv[1] == "verify":
        if len(sys.argv) < 4:
            print("ERROR..missing [preference.txt] and/or [toVerify.txt]")
            return -1
        prefs = sys.argv[2]
        toVerify = sys.argv[3]
        raw_input_prefs = read_file(prefs)
        raw_input_verify = read_file(toVerify)

        #start = time.perf_counter()
        output = verifier(raw_input_prefs, raw_input_verify)
        #end = time.perf_counter()
        #print("Verifier runtime:", end - start, "seconds")
        
        print("\n*******")
        print(output)
        print("*******")

if __name__ == '__main__':
    main()
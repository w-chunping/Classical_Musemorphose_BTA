import pickle
import argparse
import sys

def read_pickle(file_name):
    try:
        with open(file_name, 'rb') as f:
            data = pickle.load(f)
            print("Contents of the pickle file:")
            print(data)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    except pickle.UnpicklingError:
        print(f"Error: Failed to unpickle the file '{file_name}'.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Read a pickle file.")
    parser.add_argument("file", help="Path to the pickle file")
    args = parser.parse_args()

    read_pickle(args.file)

if __name__ == "__main__":
    main()

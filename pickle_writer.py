import pickle
import argparse
import os

parser = argparse.ArgumentParser(description="Write a pickle file.")
parser.add_argument("--output_file", type=str, default="test", help="Directory to save MIDI files")
args = parser.parse_args()

# Your list
file_list = ['22.pkl']

# Save to a .pkl file
with open(args.output_file, 'wb') as f:
    pickle.dump(file_list, f)

print(f"{args.output_file} saved successfully.")

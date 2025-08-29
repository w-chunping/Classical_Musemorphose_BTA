import numpy as np
import os
from miditok import REMI, TokenizerConfig
from symusic import Score
import argparse

parser = argparse.ArgumentParser(description="Convert tokenized songs (.npy) to MIDI.")
parser.add_argument("--input_dir", type=str, required=True, help="Path to directory with .npy song files")
parser.add_argument("--output_dir", type=str, default="result_test_mozart", help="Directory to save MIDI files")
args = parser.parse_args()

input_dir = args.input_dir
output_dir = args.output_dir

songs = [a[0:-4] for a in list(filter(lambda a: a[-4:] == ".npy", os.listdir(input_dir)))]
print(songs)
if not os.path.exists(output_dir):
  os.mkdir(output_dir)

for song in songs:
  # Load the text file into a NumPy array (assuming each line is a token)
  tokens = np.load(os.path.join(input_dir, f'{song}.npy'), allow_pickle=True)
  tokens = tokens.reshape(1, -1)
  print(tokens)



  BEAT_RES = {(0, 1): 24, (1, 2): 8, (2, 4): 4, (4, 8): 2}
  TOKENIZER_PARAMS = {
      "pitch_range": (21, 109),
      "beat_res": BEAT_RES,
      "num_velocities": 24,
      "special_tokens": ["PAD", "BOS", "EOS"],
      "use_chords": True,
      "use_rests": True,
      "use_tempos": True,
      "use_time_signatures": True,
      "use_programs": False,  # no multitrack here
      "num_tempos": 32,
      "tempo_range": (50, 200),  # (min_tempo, max_tempo)
  }

  # Creating a multitrack tokenizer, read the doc to explore all the parameters
  config = TokenizerConfig(**TOKENIZER_PARAMS)
  tokenizer = REMI(config)

  converted_back_midi = tokenizer(tokens)

  converted_back_midi.dump_midi(os.path.join(output_dir, f"{song}.mid")) # Save the MIDI file
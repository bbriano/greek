import pydub
import sys

alphabet = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"

pronounciation = pydub.AudioSegment.from_file("pronounciation.mp3")

splits = pydub.silence.split_on_silence(pronounciation, min_silence_len=500, silence_thresh=-54)
if len(splits) != len(alphabet):
	print("err: Split amount does not match.", file=sys.stderr)
	exit(1)

for letter,split in zip(alphabet, splits):
	split.export("pronounciation/%s.mp3" % letter)

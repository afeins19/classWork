from nrclex import NRCLex
import numpy as np
import pandas as pd

text = 'Very rude and insulting of Hamilton cast member to treat our great future V.P. Mike Pence to a theater lecture. Couldnt even memorize lines!'

emotion = NRCLex(text)

overall_sentiment = emotion.affect_frequencies
print("Words:")
print(emotion.words)
print("Sentiment:")
print(overall_sentiment)
print("Affect Dict:")
print(emotion.affect_dict)


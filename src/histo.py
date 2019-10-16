#!/usr/bin/env python3

import argparse # builtin
import json # builtin

from PIL import Image # Pillow
import numpy as np

# from matplotlib import pyplot as plt # not necessary



def histogram(image, plot, output):
    img = Image.open(image)
    hist = {}

    bands = img.getbands()
    for ch, band in enumerate(bands):
        hist_item, bins = np.histogram(img.getdata(ch), 256, [0, 256])
        hist[ch] = hist_item.tolist()
        if plot:
            pass
            # plt.plot(hist_item, band.lower())
            # plt.xlim([0, 256])

    if output:
        with open(output, "w") as fh:
            json.dump(hist, fh)
    else:
        print(hist)
        return hist

    if plot:
        pass
        # plt.show()



def main():
    parser = argparse.ArgumentParser(description="Calculates an histogram for each band of the image")

    parser.add_argument("image", help="input image")
    parser.add_argument("--output", metavar="FILE", help="result output file")
    parser.add_argument("--plot", action="store_true", help="show a plot of the histogram to debug")

    args = parser.parse_args()
    return histogram(args.image, args.plot, args.output)



if __name__ == "__main__":
    main()

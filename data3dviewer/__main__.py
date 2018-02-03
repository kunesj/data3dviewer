#!/usr/bin/env python
# encoding: utf-8

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

import sys, os, argparse

import numpy as np
import io3d
import sed3

def main():
    parser = argparse.ArgumentParser(
        description='data3dviewer - Viewer for 3d data (mostly from CT)'
    )
    parser.add_argument(
        'path',
        help='Path to directory with 3d data')
    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        help='Debug mode')
    args = parser.parse_args()

    logging.basicConfig(stream=sys.stdout)
    logger = logging.getLogger()

    logger.setLevel(logging.WARNING)
    if args.debug:
        logger.setLevel(logging.DEBUG)

    # load dicom data
    logger.info("Loading 3d data from: %s" % os.path.abspath(args.path))
    datap = io3d.read(os.path.abspath(args.path), dataplus_format=True)
    data3d = datap["data3d"]
    
    # temporary fix for io3d <-512;511> value range bug
    # this is caused by hardcoded slope 0.5 in dcmreader
    if np.min(data3d) >= -512: data3d = data3d * 2

    # display data
    ed = sed3.sed3(data3d)
    ed.show()

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import os.path
import csv

def main():
    parser = argparse.ArgumentParser(description='Convert CSV file to .htaccess directories for w3id.org')
    parser.add_argument('csv', metavar='CSV', nargs=1,
                       help='CSV file to parse')
    parser.add_argument("--output", default="build",
                        help="Path to populate with .htaccess directories")
    parser.add_argument("--no-header", action="store_false", dest="skip_header",
                        help="Do not skip first line of CSV")
    parser.add_argument("--header", action="store_true", dest="skip_header",
                        help="Skip first line of CSV")
    parser.set_defaults(skip_header=True)


    args = parser.parse_args()
    rows = None
    with open(args.csv[0]) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if rows is None:
                # First line
                rows = []
                if args.skip_header:
                    continue # don't add it
            (z_id,src,linktype,target,created,lastmodified,status,indexed) = row
            rows.append([src,linktype,target])
    rows.sort()
    rows.reverse() # /path/child before /path/ before /path

    for (src,linktype,target) in rows:
        print(src,"->",target)

if __name__ == "__main__":
    main()

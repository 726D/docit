#!/usr/bin/python

import sys, difflib

def main(argv):
    f1 = open(sys.argv[1],"r")
    f2 = open(sys.argv[2],"r")
    f1r = f1.readlines()
    f2r = f2.readlines()

    if sys.argv[1].strip().endswith('feature') or sys.argv[2].strip().endswith('feature'):
        if sys.argv[1]=='/dev/null':
            print "<h2 style='color:orange'>Feature to add to documenation in file {} </h2>".format(sys.argv[2])
            f1r = [""]
        elif sys.argv[2]=='/dev/null':
            print "<h2 style='color:orange'>Feature possibly to be removed from documenation in file {}</h2>".format(sys.argv[1])
            f2r = [""]
        else:
            print "<h2 style='color:red'>Feature probably to be changed in documenation in file {}</h2>".format(sys.argv[1])

        differ = difflib.HtmlDiff()
        t=differ.make_table(f1r,f2r)
        print t
        print "<hr>"

if __name__ == "__main__":
    main(sys.argv[1:])

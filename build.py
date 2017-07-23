import glob, os
from subprocess import call
import sys

def build(run=False):
    os.chdir("static")

    for file_ in glob.glob("*.ipynb"):
        call(["jupyter", "nbconvert", file_, "--to", "slides", '--reveal-prefix', '"reveal.js"', "--config", "slides_config.py"])
        break

    for file_ in glob.glob("*.html"):
        call(["python", "clean_html.py", file_])
        break

    if run:
        os.chdir("..")
        call(["python", "run.py"])

if __name__ == "__main__":
    try:
        build(run=True if sys.argv[1] in ("run", "r", "-r") else False)
    except IndexError:
        build()
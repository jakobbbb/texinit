#!/usr/bin/python3
import argparse
import re
import os

def _list_templates():
    return "\n".join(os.listdir(os.path.expanduser("~/.texinit/")))

def _parse_template(args, templ):
    for k, v in args.items():
        r = re.compile(r"{{(%s)}}" % k.upper())
        templ = r.sub(str(v), templ)
    return templ

def _make_dir(args):
    return os.mkdir(args["destination"])

def _make_make(args):
    print("Creating Makefile for %s from template %s" % (args["destination"], args["make_template"]))
    templ_file = os.path.expanduser("~/.texinit/%s.Makefile" % args["make_template"])
    with open(templ_file, "r") as f:
        templ = f.read()
    makefile = _parse_template(args, templ)
    with open("%s/Makefile" % (args["destination"]), "w+") as f:
        f.write(makefile)

def _make_tex(args):
    print("Creating TeX-File for %s from template %s" % (args["destination"], args["template"]))
    templ_file = os.path.expanduser("~/.texinit/%s.tex" % args["make_template"])
    with open(templ_file, "r") as f:
        templ = f.read()
    texfile = _parse_template(args, templ)
    with open("%s/%s.tex" % (args["destination"], args["destination"]), "w+") as f:
        f.write(texfile)
    ignorefile = os.path.expanduser("~/.texinit/%s.gitignore" % args["make_template"])
    with open(ignorefile, "r") as f:
            ignore = f.read()
    with open("%s/.gitignore" % (args["destination"]), "w+") as f:
        f.write(ignore)

def main():
    p = argparse.ArgumentParser(description="Initialize a TeX document")
    p.add_argument("--no-make", "-n", action="store_true")
    p.add_argument("--make-template", "-m", default="default")
    p.add_argument("--list-templates", "-l", action="store_true")
    p.add_argument("--engine", "-e", default="xelatex")
    p.add_argument("destination", nargs="?", default=None)
    p.add_argument("template", nargs="?", default="default")
    args = vars(p.parse_args())

    if args["list_templates"]:
        print(_list_templates())
        return

    if not args["destination"]:
        print("No destination")
        return 1

    _make_dir(args)

    if not args["no_make"]:
        _make_make(args)

    _make_tex(args)

    print(args)

if __name__ == "__main__":
    r = main()
    exit(r)

# texinit

A small Python script to initialize LaTeX documents.

Templates live at `~/.texinit`

## Installing Templates

There are three types of template, examples for which have been provided
in this repository (`default.*`).  Copy or symlink them to `~/.texinit`
to get started.

## Initializing Documents

Run `texinit mydocument` to initialize a LaTeX document called
`mydocument`.  A folder with the `.tex` file, alongside with a
`Makefile` and `.gitignore` will be created.

With the second positional argument, you can specify which LaTeX
template to use, e.g. `texinit myletter letter`, will initialize from
`~/.texinit/letter.tex`.

You can also specify a `Makefile` template with the option `-m`.

## Template Format

You can access all command line arguments in the templates:

|Syntax|Description|
|---|---|
|{{DESTINATION}}|Name of the document|
|{{TEMPLATE}}|Name of the template|
|{{ENGINE}}|The LaTeX engine that is being used|

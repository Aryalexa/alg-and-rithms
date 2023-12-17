# WC tool

### Objetive
Build our own version of the Unix command line tool wc. Let’s call it ccwc (cc for Coding Challenges).

> The Unix command line tools are a great metaphor for good software engineering and they follow the Unix Philosophies of:
> - Writing simple parts connected by clean interfaces - each tool does just one thing and provides a simple CLI that handles text input from either files or file streams.
> - Design programs to be connected to other programs - each tool can be easily connected to other tools to create incredibly powerful compositions.

### Requirements
- It should display to the standard output.
- Support for the options ``-clmw``
- Support one or more files
- Support standard input. If no files are specified, the standard input is used and no file name is displayed.  The
prompt will accept input until receiving EOF, or [^D] in most environments.
- `-c` and `-m` options are not shown together, the last usage of any of them has the priority.
- The default action is equivalent to specifying the `-c`, `-l` and `-w` options.
- The order of **output** always takes the form of line, word, byte, and file name.


### Examples

Original
```bash
% wc -mlw report1 report2
...
% cat test.txt | wc -l
...
% wc -l
...
```

Ours
```bash
% ./ccwc -mlw report1 report2
...
% cat test.txt | ./ccwc -l
...
```
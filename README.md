# SimplePasswordGenerator

SimplePasswordGenerator will not save any passwords generated.
It generates the password by calling urandom, then performing a sha256 hash over the results.

When calling from the command line, you can either include certain characters or filter certain characters out.
To include certain characters, you use the letter "i" for include, to filter out, you use "f", then you specify the characters.
When including symbols, it's best to put your characters in single quotes, otherwise some of the characters will not be recognized as being sent in.

For example:
python3 main.py i 'abcdefghijklmnopqrstuvwxyz#!@'
python3 main.py f '#$ABDdeg'

You can optionally not put in any parameters and it will ask you to type which letters you'd like filtered out.
python3 main.py

The alphabet is limited to these characters only.:
!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~

To use the single quote in the shell, as a filter or included letter, you must use it outside of the single quotes and escape it.:
escaped quote = \'
In use:
python3 main.py i 'asdf'\'

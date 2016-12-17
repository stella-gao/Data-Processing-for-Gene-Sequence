＃Using 'sed' to find and replace in Linux
sed is the stream editor, but can edit files directly too, with the following:

sed -i -e 's/foo/bar/g' filename
s is used to replace the found expression "foo" with "bar"

g stands for "global", meaning to do this for the whole line. If you leave off the g and "foo" appears twice on the same line, only the first "foo" is changed to "bar".

-i option is used to edit in place on filename.

-e option indicates the expression/command to run.

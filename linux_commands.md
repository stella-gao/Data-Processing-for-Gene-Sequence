# Using 'sed' to find and replace in Linux
sed is the stream editor, but can edit files directly too, with the following:

sed -i -e 's/foo/bar/g' filename
s is used to replace the found expression "foo" with "bar"

g stands for "global", meaning to do this for the whole line. If you leave off the g and "foo" appears twice on the same line, only the first "foo" is changed to "bar".

-i option is used to edit in place on filename.

-e option indicates the expression/command to run.


for example:


remove "hg19_ct_UserTrack_3545_" in a file
```
sed -i -e 's/hg19_ct_UserTrack_3545_//g' Human_coding_transcripts_mRNA.fa
```

replace AAA with BBB in a file
```
sed -i -e 's/AAA/BBB/g' filename.txt
```

replace "; transcript_version " with . in a file
```
sed -i -e 's/"; transcript_version "/./g' human.gtf
```

Using sed/awk to remove anything after first space
```
sed -i -e 's/\s.*$//' cpat_merge_test.fa     
```
Using grep to count the number of a string in a file
```
grep -c '^+1' filename.txt
```
Get line number of a string and all contents at that line
```
grep -nr 'NONCELT024045.1' celegans.out
```

# frag_info
File System Fragmentation calculation CLI utility for Linux (using filefrag command) 


Usage: /path_to/frag_info.py [path_to_directory_to_scan]

Output (example):
<wrap off>

Fragmentation within /home/user/Video

Totally: 124 files (124 not empty) stored within 28844 fragments
Totally 28720 fragments in 124 fragmented files
Fragmentation factor by files {fragmented/total in %}: 100.00%
Fragmentation factor by fragments {(fragments - files)/ files}: 231.613

Fragments per files:<br>
2      fragments: 13.71%<br>
3-10   fragments: 15.32%<br>
11-100 fragments: 45.16%<br>
\> 100  fragments: 25.81%<br>

See detailed log in /tmp/frag.log
<wrap on>

#!/usr/bin/env python3

import sys, subprocess, os, re

if len(sys.argv) > 1:
  wd = sys.argv[1]
  if not os.path.exists(wd):
    print ('Usage: frag_info.py [path_to_scan]\n'
           'When path_to_scan is not specified then it scans from current directory')
    quit()
else:
  wd = os.getcwd()
print('Fragmentation within %s\n' % wd)

cmd = ("find \"%s\" -xdev -type f -exec filefrag '{}' +  | " % wd +
       r"sed -e 's/^\(.*\): \(.*\) extent.* found$/\2 \1/' | "
       "sort -nr > /tmp/frag.log")
subprocess.call([cmd], shell=True)

total = totalf = fragmented = frags = 0
cnt = [0, 0, 0, 0]

with open('/tmp/frag.log', 'rt', newline='\n') as f:
  for line in f:
    totalf += 1
    fr, fn = re.findall(r'(\d+) (.*)', line)[0]
    fr = int(fr)
    if fr > 0:
      total += 1
      frags += fr
      if fr > 1:
        fragmented += 1
        if fr == 2:
          cnt[0] += 1
        elif fr <= 10:
          cnt[1] += 1
        elif fr <= 100:
          cnt[2] += 1
        else:
          cnt[3] += 1

if fragmented:
  cnt = [c / fragmented * 100 for c in cnt]

exfrags = frags - total
tot =  'Totally: %d files (%d not empty) stored within %d fragments\n' % (totalf, total, frags)
tot += ('Totally %d fragments in %d fragmented files\n' % (exfrags, fragmented) if fragmented
                                                                                else '')
tot += ('Fragmentation factor by files {fragmented/total in %%}: %0.2f%%\n' %
                                                                 (fragmented / totalf * 100))
tot += 'Fragmentation factor by fragments {(fragments - files)/ files}: %0.3f\n' % (exfrags / total)
tot += '\nFragments per files:\n'
tot += ('   2   fragments: %0.2f%%\n 3-10  fragments: %0.2f%%\n'
        '11-100 fragments: %0.2f%%\n > 100 fragments: %0.2f%%'
        % (cnt[0], cnt[1], cnt[2], cnt[3]) if fragmented else '')
tot += '\n\nSee detailed log in /tmp/frag.log'
print(tot)

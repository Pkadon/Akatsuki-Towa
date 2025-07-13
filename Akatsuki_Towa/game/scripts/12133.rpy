label avg12133:

play music "ED6104.ogg"
scene avg_bg_038
$ update_narrator('c9591')
window show
with fade_in
play sfx2 "other_7047.ogg"
c9591 '[textdict[1128272]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1128273]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
c9591 '[textdict[1128274]]'
c9591 '[textdict[1128275]]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 5)
c23 '[textdict[1128276]]'
return
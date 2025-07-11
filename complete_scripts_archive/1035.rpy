label avg1035:

play music "ed7201.ogg"
scene avg_bg_010
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
window show
with fade_in
c601 '[textdict[2100584]]'
$ update_portrait('sc053_01 4', 'p60', [l(-32), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[2100585]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[2100586]]'
$ update_portrait('sc053_01 1', 'p60', [l(-32), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[2100587]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[2100588]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[2100589]]'
$ update_portrait('sc053_01 4', 'p60', [l(-32), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[2100590]]'
hide p2
$ update_portrait('sc053_01 4', 'p60', [l(-32), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[2100591]]'
return
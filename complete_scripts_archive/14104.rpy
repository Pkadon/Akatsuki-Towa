label avg14104:
stop music

play music "ed7150.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
window show
with fade_in
c23 '[textdict[1202130]]'
hide p2
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[1202131]]'
hide p2
hide p60
$ update_portrait('sc053_01 1', 'p60', [l(-32), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[textdict[1202132]]'
hide p1
hide p60
$ update_portrait('sc053_01 1', 'p60', [l(-32), dark, flip], 6)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[textdict[1202133]]'
hide p60
hide p2
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202134]]'
hide p2
hide p56
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1202135]]'
hide p2
hide p56
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1202136]]'
hide p56
hide p1
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[1202137]]'
hide p60
hide p1
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 5', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[1202138]]'
hide p1
hide p60
$ update_portrait('sc053_01 5', 'p60', [l(-32), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
c13 '[textdict[1202139]]'
return
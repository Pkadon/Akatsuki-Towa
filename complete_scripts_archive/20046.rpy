label avg20046:
stop music

play music "ED6505.ogg"
scene avg_bg_027
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
play sfx2 "other_7064.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
c21 '[textdict[1002724]]'
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1002725]]'
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1002726]]'
hide p2
hide p1
with fade
c5943 '[textdict[1002727]]'
c5943 '[textdict[1002728]]'
$ update_portrait('st017_01 2', 'p216', [l(-18), light, flip], 6)
c2161 '[textdict[1002729]]'
$ update_portrait('st017_01 2', 'p216', [l(-18), dark, flip], 6)
$ update_portrait('st018_01 4', 'p217', [r(-16), light], 5)
c2173 '[textdict[1002730]]'
hide p216
$ update_portrait('st018_01 4', 'p217', [r(-16), dark], 5)
$ update_portrait('st016_01 2', 'p215', [l(-8), light, flip], 6)
c2151 '[textdict[1002731]]'
$ update_portrait('st018_01 4', 'p217', [r(-16), dark], 5)
$ update_portrait('st016_01 1', 'p215', [l(-8), light, flip], 6)
c2151 '[textdict[1002732]]'
hide p217
$ update_portrait('st016_01 1', 'p215', [l(-8), dark, flip], 6)
c5943 '[textdict[1002733]]'
$ update_portrait('st016_01 1', 'p215', [l(-8), dark, flip], 6)
c5943 '[textdict[1002734]]'
hide p215
$ update_portrait('st017_01 1', 'p216', [l(-18), light, flip], 6)
c2161 '[textdict[1002735]]'
hide p216
$ update_portrait('st016_01 5', 'p215', [l(-8), light, flip], 6)
c2151 '[textdict[1002736]]'
$ update_portrait('st016_01 2', 'p215', [l(-8), light, flip], 6)
c2151 '[textdict[1002737]]'
hide p215
$ update_portrait('st014_01 2', 'p213', [l(-18), light, flip], 6)
c2131 '[textdict[1002738]]'
$ update_portrait('st014_01 2', 'p213', [l(-18), dark, flip], 6)
c5943 '[textdict[1002739]]'
hide p213
$ update_portrait('st016_01 2', 'p215', [l(-8), light, flip], 6)
c2151 '[textdict[1002740]]'
$ update_portrait('st016_01 2', 'p215', [l(-8), dark, flip], 6)
c5943 '[textdict[1002741]]'
$ update_portrait('st016_01 1', 'p215', [l(-8), light, flip], 6)
c2151 '[textdict[1002742]]'
$ update_portrait('st016_01 1', 'p215', [l(-8), dark, flip], 6)
c5943 '[textdict[1002743]]'
$ update_portrait('st016_01 1', 'p215', [l(-8), dark, flip], 6)
c5943 '[textdict[1002744]]'
hide p215
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
with fade
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[textdict[1002745]]'
return
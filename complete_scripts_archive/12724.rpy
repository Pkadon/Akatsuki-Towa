label avg12724:
stop music

play music "ED6301.ogg"
scene avg_bg_070
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1171763]]'
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1171764]]'
hide p1
hide p1304
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1171765]]'
hide p1
hide p1304
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1171766]]'
return
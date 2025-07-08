label avg12722:
stop music

play music "ed9999.ogg"
scene avg_bg_050
window show
with fade_in
c0 '[textdict[1171747]]'
c0 '[textdict[1171748]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1171749]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1171750]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1171751]]'
hide p1
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1171752]]'
hide p1304
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1171753]]'
return
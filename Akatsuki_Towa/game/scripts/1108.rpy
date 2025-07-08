label avg1108:
stop music

play music "ed7106.ogg"
scene avg_bg_013
window show
with fade_in
c0 '[textdict[2102659]]'
c7481 '[textdict[2102660]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[2102661]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[2102662]]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[2102663]]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 6)
c10893 '[textdict[2102664]]'
hide p2
c7481 '[textdict[2102665]]'
c0 '[textdict[2102666]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
play sfxvoice "bcv_oc002_c02_01.ogg"
c23 '[textdict[2102667]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('st004_01 5', 'p204', [l(4), light, flip], 6)
c2041 '[textdict[2102668]]'
return
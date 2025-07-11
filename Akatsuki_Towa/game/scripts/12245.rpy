label avg12245:

play music "ed7102.ogg"
scene avg_bg_015
window show
with fade_in
play sfx2 "other_7047.ogg"
c9963 '[textdict[1121302]]'
$ update_portrait('oc004_01 9', 'p4', [l_entrance(-5), light, flip], 6)
c41 '[textdict[1121303]]'
hide p4
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1121304]]'
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 6)
c9963 '[textdict[1121305]]'
c9963 '[textdict[1121306]]'
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1121307]]'
hide p2
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1121308]]'
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 6)
c9963 '[textdict[1121309]]'
c9963 '[textdict[1121310]]'
hide p4
$ update_portrait('oc001_01 17', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1121311]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1121312]]'
return
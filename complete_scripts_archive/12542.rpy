label avg12542:
stop music

play music "ED6200.ogg"
scene avg_bg_010
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1152924]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1152925]]'
hide p2
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
with fade
c31 '[textdict[1152926]]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1152927]]'
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 5)
c23 '[textdict[1152928]]'
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l_entrance(-5), light, flip], 6)
c41 '[textdict[1152929]]'
hide p4
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l_entrance(-6), light, flip], 6)
c31 '[textdict[1152930]]'
hide p3
hide p2
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
with fade
c43 '[textdict[1152931]]'
hide p4
c0 '[textdict[1152932]]'
return
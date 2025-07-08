label avg10130:
stop music

play music "ed7110.ogg"
scene avg_bg_018
window show
with fade_in
c0 '[textdict[1007298]]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1007299]]'
hide p1
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 14', 'p2', [r_entrance(-3), light], 5)
c23 '[textdict[1007300]]'
hide p1
hide p2
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1007301]]'
hide p2
hide p1
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 13', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1007302]]'
hide p1
hide p2
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1007303]]'
hide p2
hide p1
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1007304]]'
hide p1
hide p2
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "fight_6024.ogg"
c11 '[textdict[1007305]]'
hide p2
hide p1
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 5)
c23 '[textdict[1007306]]'
hide p1
hide p2
$ update_portrait('oc002_01 7', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1007307]]'
play music "ed7106.ogg"
hide p2
hide p1
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
play sfx2 "other_7020.ogg"
c23 '[textdict[1007308]]'
hide p1
hide p2
with fade
play sfx2 "other_7088.ogg"
c9673 '[textdict[1007309]]'
$ update_portrait('oc002_01 18', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[textdict[1007310]]'
hide p2
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 6)
c9673 '[textdict[1007311]]'
hide p2
$ update_portrait('oc001_01 22', 'p1', [l(-2), light, flip], 6)
play sfx2 "fight_6024.ogg"
c11 '[textdict[1007312]]'
hide p1
$ update_portrait('oc001_01 22', 'p1', [l(-2), dark, flip], 6)
c9673 '[textdict[1007313]]'
hide p1
$ update_portrait('oc001_01 22', 'p1', [l(-2), dark, flip], 6)
c9673 '[textdict[1007314]]'
hide p1
$ update_portrait('oc001_01 22', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch04_b.ogg"
c23 '[textdict[1007315]]'
hide p1
hide p2
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1007316]]'
hide p1
hide p2
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
c11 '[textdict[1007317]]'
hide p2
hide p1
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1007318]]'
return
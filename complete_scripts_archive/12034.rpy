label avg12034:
stop music

play music "ed7101.ogg"
scene avg_bg_020
window show
with fade_in
c7171 '[textdict[1120197]]'
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 5)
c2323 '[textdict[1120198]]'
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
c7171 '[textdict[1120199]]'
hide p232
$ update_portrait('st033_01 3', 'p232', [r(-7), r_shake, light], 5)
c2323 '[textdict[1120200]]'
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch20.ogg"
c21 '[textdict[1120201]]'
hide p232
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 5)
c2323 '[textdict[1120202]]'
hide p2
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1120203]]'
hide p232
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st033_01 2', 'p232', [r(-7), r_shake, light], 5)
c2323 '[textdict[1120204]]'
hide p2
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1120205]]'
hide p232
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
c7173 '[textdict[1120206]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
c11 '[textdict[1120207]]'
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 6)
c7173 '[textdict[1120208]]'
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 5)
c2323 '[textdict[1120209]]'
hide p1
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc002_c03_01.ogg"
c21 '[textdict[1120210]]'
hide p2
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1121550]]'
hide p2
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1120211]]'
hide p232
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 6)
c7173 '[textdict[1120212]]'
hide p1
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
c11 '[textdict[1120213]]'
return
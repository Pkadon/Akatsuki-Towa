label avg12034:

$ play_music("ed7101.ogg")
scene avg_bg_020
$ update_narrator('c7171')
window show
with fade_in
c7171 '[convertstrid(1120197)]'
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1120198)]'
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
c7171 '[convertstrid(1120199)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), r_shake, light], 6)
c2323 '[convertstrid(1120200)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch20.ogg"
c21 '[convertstrid(1120201)]'
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1120202)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1120203)]'
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st033_01 2', 'p232', [r(-7), r_shake, light], 6)
c2323 '[convertstrid(1120204)]'
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1120205)]'
hide p232
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
c7173 '[convertstrid(1120206)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
c11 '[convertstrid(1120207)]'
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
c7173 '[convertstrid(1120208)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1120209)]'
hide p1
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc002_c03_01.ogg"
c21 '[convertstrid(1120210)]'
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1121550)]'
hide p2
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1120211)]'
hide p232
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
c7173 '[convertstrid(1120212)]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
c11 '[convertstrid(1120213)]'
return
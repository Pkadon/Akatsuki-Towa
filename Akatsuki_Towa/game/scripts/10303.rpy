label avg10303:
stop music

play music "ed7116.ogg"
scene avg_bg_020
window show
with fade_in
play sfx2 "other_7020.ogg"
c5381 '[textdict[1130125]]'
$ update_portrait('st033_01 2', 'p232', [r_entrance(-7), light], 5)
c2323 '[textdict[1130126]]'
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
c5381 '[textdict[1130127]]'
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
c5381 '[textdict[1130128]]'
hide p232
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 5)
c2323 '[textdict[1130129]]'
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
c5381 '[textdict[1130130]]'
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
c5381 '[textdict[1130131]]'
hide p232
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 5)
c2323 '[textdict[1130132]]'
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
c5381 '[textdict[1130133]]'
hide p232
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 5)
c2323 '[textdict[1130134]]'
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
c5381 '[textdict[1130135]]'
hide p232
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 5)
c2323 '[textdict[1130136]]'
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
c5381 '[textdict[1130137]]'
hide p232
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 5)
c2323 '[textdict[1130138]]'
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
c5381 '[textdict[1130139]]'
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
c5381 '[textdict[1130140]]'
hide p232
$ update_portrait('st033_01 6', 'p232', [r_exit(-7), light], 5)
play sfx2 "other_7020.ogg"
c2323 '[textdict[1130141]]'
hide p232
play music "ed7101.ogg"
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro08.ogg"
c31 '[textdict[1130142]]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 8', 'p4', [r_entrance(-5), light], 5)
c43 '[textdict[1130143]]'
hide p4
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1130144]]'
hide p2
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
c23 '[textdict[1130145]]'
hide p2
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1130146]]'
return
label avg12110:

play music "ed7116.ogg"
scene avg_bg_020
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
play sfx2 "other_7020.ogg"
c11 '[convertstrid(1128090)]'
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
play sfx2 "fight_6024.ogg"
c2323 '[convertstrid(1128091)]'
hide p1
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1128092)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
c11 '[convertstrid(1128093)]'
hide p1
hide p232
c0 '[convertstrid(1128094)]'
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1128095)]'
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128096)]'
hide p232
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
c5383 '[convertstrid(1128097)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1128098)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128099)]'
hide p1
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1128100)]'
hide p2
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128101)]'
hide p232
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
c5383 '[convertstrid(1128102)]' (what_size=(gui.text_size*1.2)) with shake
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1128103)]'
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128104)]'
scene avg_bg_070
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
with fade
play sfx2 "other_7020.ogg"
c33 '[convertstrid(1128105)]'
scene avg_bg_020
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[convertstrid(1128106)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 14', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1128107)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1128108)]'
hide p2
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128109)]'
return
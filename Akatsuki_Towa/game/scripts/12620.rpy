label avg12620:
stop music

play music "ed9999.ogg"
scene avg_bg_050
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
window show
with fade_in
c31 '[textdict[1161828]]'
hide p3
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li19.ogg"
c43 '[textdict[1161829]]'
hide p3
hide p4
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro12.ogg"
c31 '[textdict[1161830]]'
hide p3
hide p4
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 18', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1161831]]'
hide p4
hide p3
$ update_portrait('oc003_01 18', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 5)
c13 '[textdict[1161832]]'
hide p1
hide p3
$ update_portrait('oc003_01 18', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 5)
c23 '[textdict[1161833]]'
hide p3
hide p2
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1161834]]'
hide p2
hide p3
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1161835]]'
hide p3
hide p4
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1161836]]'
hide p4
hide p2
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1161837]]'
hide p2
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1161838]]'
hide p3
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 18', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1161839]]'
hide p1
hide p3
$ update_portrait('oc003_01 18', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 5)
c43 '[textdict[1161840]]'
hide p3
hide p4
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1161841]]'
hide p3
hide p4
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1161842]]'
hide p4
hide p2
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[textdict[1161843]]'
scene avg_bg_070
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
with fade
c13 '[textdict[1161844]]'
hide p1
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
c13 '[textdict[1161845]]'
hide p1
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 5)
c13 '[textdict[1161846]]'
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1161847]]'
return
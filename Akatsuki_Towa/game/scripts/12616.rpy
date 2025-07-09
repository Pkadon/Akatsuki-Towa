label avg12616:
stop music

play music "ed7105.ogg"
scene avg_bg_010
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_na03_b.ogg"
c13 '[textdict[1161616]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 13', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1161617]]'
hide p1
$ update_portrait('oc004_01 13', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1161618]]'
hide p2
$ update_portrait('oc004_01 13', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 5)
c33 '[textdict[1161619]]'
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1161620]]'
hide p3
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1161621]]'
hide p4
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1161622]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 13', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1161623]]'
$ update_portrait('oc003_01 13', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1161624]]'
return
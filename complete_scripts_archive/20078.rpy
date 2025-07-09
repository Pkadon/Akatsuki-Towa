label avg20078:
stop music

play music "ed7105.ogg"
scene avg_bg_045
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
window show
with fade_in
c41 '[textdict[1004000]]'
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 5)
play sfx2 "other_7060.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1004001]]'
hide p4
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
c11 '[textdict[1004002]]'
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 5)
c23 '[textdict[1004003]]'
hide p1
hide p2
with fade
play sfx2 "other_7047.ogg"
c6601 '[textdict[1004004]]'
c6601 '[textdict[1004005]]'
$ update_portrait('oc003_01 2', 'p3', [r_entrance(-6), light], 5)
c33 '[textdict[1004006]]'
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
c6601 '[textdict[1004007]]'
hide p3
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 5)
c23 '[textdict[1004008]]'
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
c6601 '[textdict[1004009]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1004010]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c6601 '[textdict[1004011]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
c23 '[textdict[1004012]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1004013]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1004014]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c6601 '[textdict[1004015]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1004016]]'
return
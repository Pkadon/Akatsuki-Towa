label avg12162:
stop music

play music "ED6104.ogg"
scene avg_bg_011
window show
with fade_in
play sfx2 "other_7047.ogg"
c9661 '[textdict[1128445]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1128446]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1128447]]'
hide p2
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c9641 '[textdict[1128448]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1128449]]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1128451]]'
hide p3
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
c9641 '[textdict[1128452]]'
hide p3
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 5)
c13 '[textdict[1128453]]'
hide p1
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
c9641 '[textdict[1128454]]'
hide p1
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
c9641 '[textdict[1128455]]'
hide p1
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro09.ogg"
c33 '[textdict[1128456]]'
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1128457]]'
hide p1
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[textdict[1128458]]'
hide p2
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
c9641 '[textdict[1128459]]'
play music "ed7511.ogg"
hide p2
play sfx2 "other_7080.ogg"
c5003 '[textdict[1128460]]' with shake
c9641 '[textdict[1128461]]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 5)
c13 '[textdict[1128462]]'
hide p1
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1128463]]'
hide p3
hide p1
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1128464]]'
scene avg_bg_070
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 5)
with fade
play sfx2 "other_7085.ogg"
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1128465]]' with shake
scene avg_bg_011
$ update_portrait('oc003_01 3', 'p3', [l(-6), light, flip], 6)
with fade
c31 '[textdict[1128467]]'
hide p3
$ update_portrait('oc003_01 3', 'p3', [l(-6), dark, flip], 6)
c9643 '[textdict[1128468]]'
hide p3
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1128469]]'
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1128470]]'
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 15', 'p1', [r(-2), light], 5)
c13 '[textdict[1128471]]'
hide p1
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
c9643 '[textdict[1128472]]'
hide p3
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1128473]]'
hide p2
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 5)
play sfx2 "other_7079.ogg"
c13 '[textdict[1128474]]'
return
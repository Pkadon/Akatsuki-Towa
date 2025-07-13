label avg12382:

play music "ed7162.ogg"
scene avg_bg_025
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7047.ogg"
c0 '[textdict[1134013]]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1134014]]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
c10993 '[textdict[1134015]]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1134016]]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
c10993 '[textdict[1134017]]'
hide p2
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1134018]]'
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 6)
c10993 '[textdict[1134019]]'
hide p4
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1134020]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
c10993 '[textdict[1134021]]'
$ update_portrait('oc002_01 21', 'p2', [l_midback(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch21.ogg"
c21 '[textdict[1134022]]'
hide p2
play sfx2 "fight_6022.ogg"
c0 '[textdict[1134023]]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1134024]]' with shake
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 6)
c10993 '[textdict[1134025]]'
hide p1
play sfx2 "fight_6025.ogg"
c0 '[textdict[1134026]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c21 '[textdict[1134027]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
c10993 '[textdict[1134028]]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1134029]]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 6)
c10993 '[textdict[1134030]]'
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1134031]]'
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
c10993 '[textdict[1134032]]'
hide p3
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1134033]]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
c10993 '[textdict[1134034]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1134035]]'
hide p1
$ update_portrait('oc004_01 16', 'p4', [l(-5), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_li10.ogg"
c41 '[textdict[1134036]]'
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 6)
c10993 '[textdict[1134037]]'
$ update_portrait('oc004_01 19', 'p4', [l(-5), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_li22.ogg"
c41 '[textdict[1134038]]'
return
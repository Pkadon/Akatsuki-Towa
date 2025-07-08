label avg20076:
stop music

play music "ed7150.ogg"
scene avg_bg_018
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
window show
with fade_in
c11 '[textdict[1003971]]'
play music "ed7111.ogg"
scene avg_bg_012
with fade
play sfx2 "other_7042.ogg"
c6591 '[textdict[1003972]]'
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1003973]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c6591 '[textdict[1003974]]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1003975]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1003976]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c6591 '[textdict[1003977]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c6591 '[textdict[1003978]]'
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1003979]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c6591 '[textdict[1003980]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
play sfx2 "other_7022.ogg"
c6591 '[textdict[1003981]]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1003982]]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
c6591 '[textdict[1003983]]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1003984]]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
c6591 '[textdict[1003985]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1003986]]'
return
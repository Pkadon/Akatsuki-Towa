label avg14052:
stop music

play music "ED6100.ogg"
scene avg_bg_023
window show
with fade_in
c0 '[textdict[1203033]]'
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 5)
play sfx2 "other_7047.ogg"
c23 '[textdict[1203034]]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
c12021 '[textdict[1203035]]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
c12021 '[textdict[1203036]]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
c12021 '[textdict[1203037]]'
hide p2
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[textdict[1203038]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
c12021 '[textdict[1203039]]'
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 5)
c43 '[textdict[1203040]]'
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
c12021 '[textdict[1203041]]'
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1203042]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1203043]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c12021 '[textdict[1203044]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c12021 '[textdict[1203045]]'
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 5)
c23 '[textdict[1203046]]'
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
c12021 '[textdict[1203047]]'
stop music
scene avg_bg_070
with fade
c0 '[textdict[1203048]]'
play music "ed7124.ogg"
scene avg_bg_059
with fade
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 5)
play sfx2 "other_7047.ogg"
c23 '[textdict[1203049]]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
c12561 '[textdict[1203050]]'
hide p2
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1203051]]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
c12561 '[textdict[1203052]]'
hide p2
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 5)
c13 '[textdict[1203053]]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
c12561 '[textdict[1203054]]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
c12561 '[textdict[1203055]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1203056]]'
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 5)
c43 '[textdict[1203057]]'
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
c12561 '[textdict[1203058]]'
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
c12561 '[textdict[1203059]]'
return
label avg10366:
stop music

play music "ed9999.ogg"
scene avg_bg_049
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1132030]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c21 '[textdict[1132031]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l_entrance(-6), light, flip], 6)
c31 '[textdict[1132032]]'
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 5)
c43 '[textdict[1132033]]'
hide p3
hide p4
play sfx2 "other_7047.ogg"
c0 '[textdict[1132034]]'
$ update_portrait('st040_01 1', 'p1042', [l_entrance(-19), light, flip], 6)
c10421 '[textdict[1132035]]'
$ update_portrait('st040_01 1', 'p1042', [l(-19), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[textdict[1132036]]'
hide p1042
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 1', 'p1042', [l(-19), light, flip], 6)
c10421 '[textdict[1132037]]'
hide p1042
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 1', 'p1042', [l(-19), light, flip], 6)
c10421 '[textdict[1132038]]'
hide p1
$ update_portrait('st040_01 1', 'p1042', [l(-19), dark, flip], 6)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro02.ogg"
c33 '[textdict[1132039]]'
hide p1042
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('st040_01 1', 'p1042', [l(-19), light, flip], 6)
c10421 '[textdict[1132040]]'
hide p3
$ update_portrait('st040_01 1', 'p1042', [l(-19), dark, flip], 6)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li03.ogg"
c43 '[textdict[1132041]]'
hide p1042
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('st040_01 6', 'p239', [l(-19), light, flip], 6)
c2391 '[textdict[1132042]]'
hide p239
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
c2391 '[textdict[1132043]]'
hide p4
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1132044]]'
hide p2
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
c13 '[textdict[1132045]]'
return
label avg12514:

play music "ed7201.ogg"
scene avg_bg_010
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1151052)]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1151053)]'
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1151054)]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "other_7009.ogg"
c21 '[convertstrid(1151055)]'
$ update_portrait('oc002_01 5', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "other_7009.ogg"
c21 '[convertstrid(1151056)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1151057)]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7009.ogg"
c31 '[convertstrid(1151058)]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "other_7009.ogg"
c13 '[convertstrid(1151059)]'
hide p3
hide p1
play sfx2 "other_7085.ogg"
c0 '[convertstrid(1151060)]'
$ update_portrait('oc001_01 5', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "other_7009.ogg"
c13 '[convertstrid(1151061)]'
stop music
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
c10901 '[convertstrid(1151062)]'
play music "ed7511.ogg"
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1151063)]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1151064)]'
hide p3
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
c10901 '[convertstrid(1151065)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[convertstrid(1151066)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch24.ogg"
c21 '[convertstrid(1151067)]' with shake
return
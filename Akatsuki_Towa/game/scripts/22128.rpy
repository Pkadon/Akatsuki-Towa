label avg22128:

play music "ED6200.ogg"
scene avg_bg_036
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1128253)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch20.ogg"
c21 '[convertstrid(1128254)]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128255)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128256)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 13', 'p3', [l(-6), light, flip], 6)
play sfxvoice "bcv_oc003_com_01.ogg"
c31 '[convertstrid(1128257)]'
$ update_portrait('oc003_01 13', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128258)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 6', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128259)]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), l_shake, light, flip], 6)
c31 '[convertstrid(1128260)]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfx2 "other_7079.ogg"
c13 '[convertstrid(1128261)]'
return
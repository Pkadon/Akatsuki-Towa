label avg10023:

play music "ED6518.ogg"
scene avg_bg_008
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 14', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[convertstrid(1002042)]'
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1002043)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1002044)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
play sfx2 "other_7064.ogg"
c13 '[convertstrid(1002045)]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l_exit(-6), light, flip], 6)
c31 '[convertstrid(1002046)]'
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1002047)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1002048)]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1002049)]'
hide p2
$ update_portrait('oc003_01 7', 'p3', [l_entrance(-6), light, flip], 6)
c31 '[convertstrid(1002050)]'
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1002051)]'
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1002052)]'
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1002053)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1002054)]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1002055)]'
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1002056)]'
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1002057)]'
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 5)
c23 '[convertstrid(1002058)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1002059)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7071.ogg"
c31 '[convertstrid(1002060)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1002061)]'
hide p1
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
c7013 '[convertstrid(1002062)]' (what_size=(gui.text_size*1.2)) with shake
$ update_portrait('oc003_01 12', 'p3', [l(-6), l_shake, light, flip], 6)
c31 '[convertstrid(1002063)]'
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 6)
c7013 '[convertstrid(1002064)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1002065)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1002066)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
c7013 '[convertstrid(1002067)]'
c7013 '[convertstrid(1002068)]'
play sfx2 "other_7073.ogg"
c7013 '[convertstrid(1002069)]'
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1002070)]'
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1002071)]'
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1002072)]'
return
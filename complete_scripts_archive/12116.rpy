label avg12116:

play music "ed7111.ogg"
scene avg_bg_047
$ update_portrait('oc005_01 1', 'p5', [r(-6), light], 6)
$ update_narrator('c53')
window show
with fade_in
play sfxvoice "avg_vocal_ji02.ogg"
c53 '[convertstrid(1128203)]'
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
play sfx2 "other_7004.ogg"
c53 '[convertstrid(1128204)]'
$ update_portrait('oc005_01 4', 'p5', [r(-6), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128205)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128206)]'
hide p5
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[convertstrid(1128207)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128208)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128209)]'
hide p3
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
play sfxvoice "bcv_oc002_c02_01.ogg"
c21 '[convertstrid(1128210)]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_c04_01.ogg"
c13 '[convertstrid(1128211)]' with shake
return
label avg12161:

$ play_music("ed7105.ogg")
scene avg_bg_038
$ update_narrator('c9661')
window show
with fade_in
play sfx2 "other_7047.ogg"
c9661 '[convertstrid(1128445)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128446)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1128447)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c9641 '[convertstrid(1128448)]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128449)]'
hide p1
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li07.ogg"
c43 '[convertstrid(1128450)]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1128451)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
c9641 '[convertstrid(1128452)]'
hide p3
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128453)]'
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
c9641 '[convertstrid(1128454)]'
c9641 '[convertstrid(1128455)]'
hide p1
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro09.ogg"
c33 '[convertstrid(1128456)]'
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128457)]'
hide p1
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[convertstrid(1128458)]'
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
c9641 '[convertstrid(1128459)]'
stop music
hide p2
play sfx2 "other_7080.ogg"
c5003 '[convertstrid(1128460)]' with shake
$ play_music("ed7511.ogg")
c9641 '[convertstrid(1128461)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128462)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128463)]'
hide p3
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
play sfxvoice "bcv_oc002_arts_03.ogg"
c21 '[convertstrid(1128464)]'
scene avg_bg_070
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfx2 "other_7085.ogg"
play sfxvoice "avg_vocal_na21.ogg"
c13 '[convertstrid(1128465)]' with shake
scene avg_bg_038
$ update_portrait('oc004_01 3', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
with fade
play sfx2 "other_7079.ogg"
c41 '[convertstrid(1128466)]'
hide p4
$ update_portrait('oc003_01 3', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128467)]'
$ update_portrait('oc003_01 3', 'p3', [l(-6), dark, flip], 5)
c9643 '[convertstrid(1128468)]'
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128469)]'
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1128470)]'
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na11.ogg"
c13 '[convertstrid(1128471)]'
hide p1
c9643 '[convertstrid(1128472)]'
hide p3
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch21.ogg"
c21 '[convertstrid(1128473)]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfx2 "other_7079.ogg"
play sfxvoice "bcv_oc001_sc01_01.ogg"
c13 '[convertstrid(1128474)]'
return
label avg20059:

$ play_music("ed7151.ogg")
scene avg_bg_028
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1002986)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1002987)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1002988)]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
play sfx2 "other_7071.ogg"
c4971 '[convertstrid(1002989)]'
c4971 '[convertstrid(1002990)]'
hide p3
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na08.ogg"
c13 '[convertstrid(1002991)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
c4971 '[convertstrid(1002992)]'
c4971 '[convertstrid(1002993)]'
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
play sfx2 "other_7073.ogg"
c21 '[convertstrid(1002994)]'
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1002995)]'
return
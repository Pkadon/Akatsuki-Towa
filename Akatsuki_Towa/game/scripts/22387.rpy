label avg22387:

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1134040)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1134041)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfx2 "common_wheelwrong.ogg"
c33 '[convertstrid(1134042)]'
$ play_music("ed7511.ogg")
hide p2
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
play sfx2 "other_7080.ogg"
c20161 '[convertstrid(1134043)]'
hide p3
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1134044)]'
hide p2
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na23.ogg"
c13 '[convertstrid(1134045)]'
return
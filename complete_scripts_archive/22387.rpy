label avg22387:

$ play_music("ed7201.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1134040)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1134041)]'
hide p2
$ update_portrait('oc003_01 8', 'p3', [mid(-6), light], 6)
play sfx2 "common_wheelwrong.ogg"
c33 '[convertstrid(1134042)]'
$ play_music("ed7511.ogg")
hide p3
play sfx2 "other_7080.ogg"
c20163 '[convertstrid(1134043)]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1134044)]'
hide p2
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na23.ogg"
c13 '[convertstrid(1134045)]'
return
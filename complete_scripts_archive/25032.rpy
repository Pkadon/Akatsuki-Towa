label avg25032:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7086.ogg"
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1210078)]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6025.ogg"
c23 '[convertstrid(1210079)]'
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfx2 "other_7034.ogg"
c23 '[convertstrid(1210080)]'
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1210081)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210082)]'
return
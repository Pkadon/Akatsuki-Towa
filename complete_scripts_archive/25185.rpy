label avg25185:

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with fade_in
play sfx2 "other_7092.ogg"
c6123 '[convertstrid(1210612)]'
c6123 '[convertstrid(1210613)]'
play sfx2 "other_7092.ogg"
c0 '[convertstrid(1210614)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1210615)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1210616)]'
return
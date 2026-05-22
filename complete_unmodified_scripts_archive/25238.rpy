label avg25238:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210847)]'
hide p1
play sfx2 "other_7057.ogg"
c20213 '[convertstrid(1210848)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1210849)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1210850)]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[convertstrid(1210851)]'
return
label avg25284:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 16', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_ch23.ogg"
c23 '[convertstrid(1211084)]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
play sfx2 "other_7092.ogg"
c13 '[convertstrid(1211085)]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1211086)]'
return
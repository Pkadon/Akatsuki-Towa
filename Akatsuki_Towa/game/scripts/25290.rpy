label avg25290:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6022.ogg"
play sfxvoice "avg_vocal_ch23.ogg"
c23 '[convertstrid(1211104)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1211105)]'
return
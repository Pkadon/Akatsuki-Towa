label avg25176:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "fight_6022.ogg"
c13 '[convertstrid(1210567)]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[convertstrid(1210568)]'
return
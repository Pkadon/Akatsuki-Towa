label avg25043:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1210109)]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210110)]'
return
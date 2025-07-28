label avg25063:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch19.ogg"
c23 '[convertstrid(1210184)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210185)]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch16.ogg"
c23 '[convertstrid(1210186)]'
hide p2
play sfx2 "fight_6003.ogg"
play sfxvoice "avg_vocal_ch27.ogg"
c0 '[convertstrid(1210187)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch23.ogg"
c23 '[convertstrid(1210188)]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[convertstrid(1210189)]'
return
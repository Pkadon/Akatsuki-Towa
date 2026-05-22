label avg25044:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210111)]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch10.ogg"
c23 '[convertstrid(1210112)]'
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[convertstrid(1210113)]'
return
label avg25121:

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with fade_in
play sfx2 "fight_6030.ogg"
c6123 '[convertstrid(1210356)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1210357)]'
hide p2
$ update_portrait('oc001_01 15', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[convertstrid(1210358)]'
return
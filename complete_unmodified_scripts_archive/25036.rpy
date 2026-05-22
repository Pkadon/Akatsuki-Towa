label avg25036:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7080.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
c23 '[convertstrid(1210093)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210094)]'
return
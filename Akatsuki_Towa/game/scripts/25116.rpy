label avg25116:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "elc_5006.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[convertstrid(1210343)]'
return
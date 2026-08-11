label avg25116(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "elc_5006.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1210343)]' (**arg(1, 1210343))
return "avg25116"
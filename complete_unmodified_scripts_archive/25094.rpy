label avg25094(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_select.ogg"
play sfxvoice "bcv_oc001_c01_01.ogg"
get_char('c13') '[convertstrid(1210266)]' (**arg(1, 1210266))
return "avg25094"
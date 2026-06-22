label avg25022:

stop music
scene placeholderbackground
$ update_narrator('c20103')
window show
with fade_in
play sfx2 "other_7079.ogg"
get_char('c20103') '[convertstrid(1210051)]' (**arg(1, 1210051))
get_char('c20103') '[convertstrid(1210052)]' (**arg(2, 1210052))
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_sc01_01.ogg"
get_char('c13') '[convertstrid(1210053)]' (**arg(3, 1210053))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1210054)]' (**arg(4, 1210054))
return
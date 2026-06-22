label avg25091:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "bcv_oc002_c02_01.ogg"
get_char('c23') '[convertstrid(1210260)]' (**arg(1, 1210260))
return
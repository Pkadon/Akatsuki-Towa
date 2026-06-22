label avg25035:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "bcv_oc001_com_01.ogg"
get_char('c13') '[convertstrid(1210092)]' (**arg(1, 1210092))
return
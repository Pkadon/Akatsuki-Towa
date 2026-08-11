label avg25197(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "bcv_oc002_com_01.ogg"
get_char('c23') '[convertstrid(1210664)]' (**arg(1, 1210664))
return "avg25197"
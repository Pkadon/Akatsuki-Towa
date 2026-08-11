label avg25255(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1210946)]' (**arg(1, 1210946))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210947)]' (**arg(2, 1210947))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
get_char('c13') '[convertstrid(1210948)]' (**arg(3, 1210948))
return "avg25255"
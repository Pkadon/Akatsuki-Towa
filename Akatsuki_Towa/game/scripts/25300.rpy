label avg25300(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_select.ogg"
get_char('c13') '[convertstrid(1211157)]' (**arg(1, 1211157))
hide p1
get_char('c20253') '[convertstrid(1211158)]' (**arg(2, 1211158))
get_char('c20253') '[convertstrid(1211159)]' (**arg(3, 1211159))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch04.ogg"
get_char('c23') '[convertstrid(1211160)]' (**arg(4, 1211160))
return "avg25300"
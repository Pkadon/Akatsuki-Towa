label avg25029(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_ch04.ogg"
get_char('c23') '[convertstrid(1210071)]' (**arg(1, 1210071))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1210072)]' (**arg(2, 1210072))
hide p1
$ update_portrait('uc001_01 1', 'p2000', [mid(-2), light], 6)
get_char('c20003') '[convertstrid(1210073)]' (**arg(3, 1210073))
return "avg25029"
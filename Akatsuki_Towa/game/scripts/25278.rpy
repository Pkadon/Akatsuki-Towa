label avg25278(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1211053)]' (**arg(1, 1211053))
hide p1
get_char('c20153') '[convertstrid(1211054)]' (**arg(2, 1211054))
$ update_portrait('oc001_01 21', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na16.ogg"
get_char('c13') '[convertstrid(1211055)]' (**arg(3, 1211055))
hide p1
get_char('c20153') '[convertstrid(1211056)]' (**arg(4, 1211056))
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch18.ogg"
get_char('c23') '[convertstrid(1211057)]' (**arg(5, 1211057))
hide p2
get_char('c20153') '[convertstrid(1211058)]' (**arg(6, 1211058))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1211059)]' (**arg(7, 1211059))
return "avg25278"
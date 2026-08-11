label avg25194(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "fight_6025.ogg"
get_char('c13') '[convertstrid(1210652)]' (**arg(1, 1210652))
hide p1
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1210653)]' (**arg(2, 1210653))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1210654)]' (**arg(3, 1210654))
return "avg25194"
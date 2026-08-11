label avg20141(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1100024)]' (**arg(1, 1100024))
hide p1
$ update_portrait('oc004_01 9', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1100025)]' (**arg(2, 1100025))
hide p4
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1100026)]' (**arg(3, 1100026))
return "avg20141"
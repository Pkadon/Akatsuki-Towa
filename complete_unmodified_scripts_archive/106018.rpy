label avg106018(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc053_01 1', 'p60', [mid(-32), light], 6)
$ update_narrator('c603')
window show
with trans
get_char('c603') '[convertstrid(1219086)]' (**arg(1, 1219086))
$ update_portrait('sc053_01 1', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219087)]' (**arg(2, 1219087))
hide p60
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219088)]' (**arg(3, 1219088))
hide p1
$ update_portrait('sc053_01 2', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219089)]' (**arg(4, 1219089))
$ update_portrait('sc053_01 4', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219090)]' (**arg(5, 1219090))
hide p60
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219091)]' (**arg(6, 1219091))
return "avg106018"
label avg103003(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc022_01 1', 'p30', [mid(-9), light], 6)
$ update_narrator('c303')
window show
with trans
get_char('c303') '[convertstrid(1222413)]' (**arg(1, 1222413))
hide p30
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222414)]' (**arg(2, 1222414))
hide p1
$ update_portrait('sc022_01 1', 'p30', [mid(-9), light], 6)
get_char('c303') '[convertstrid(1222415)]' (**arg(3, 1222415))
$ update_portrait('sc022_01 1', 'p30', [mid(-9), light], 6)
get_char('c303') '[convertstrid(1222416)]' (**arg(4, 1222416))
hide p30
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222417)]' (**arg(5, 1222417))
return "avg103003"
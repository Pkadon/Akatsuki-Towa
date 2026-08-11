label avg102918(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc021_01 1', 'p29', [mid(-17), light], 6)
$ update_narrator('c293')
window show
with trans
get_char('c293') '[convertstrid(1219935)]' (**arg(1, 1219935))
hide p29
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219936)]' (**arg(2, 1219936))
hide p1
$ update_portrait('sc021_01 2', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219937)]' (**arg(3, 1219937))
$ update_portrait('sc021_01 1', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219938)]' (**arg(4, 1219938))
hide p29
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219939)]' (**arg(5, 1219939))
hide p1
$ update_portrait('sc021_01 1', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219940)]' (**arg(6, 1219940))
return "avg102918"
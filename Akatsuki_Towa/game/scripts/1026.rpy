label avg1026(trans=fade_in):

$ play_music("ed7150.ogg")
scene placeholderbackground
$ update_portrait('sc015_01 1', 'p23', [mid(9), light], 6)
$ update_narrator('c233')
window show
with trans
get_char('c233') '[convertstrid(2100539)]' (**arg(1, 2100539))
hide p23
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(2100540)]' (**arg(2, 2100540))
return "avg1026"
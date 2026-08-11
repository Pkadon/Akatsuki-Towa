label avg26002(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1215510)]' (**arg(1, 1215510))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215511)]' (**arg(2, 1215511))
return "avg26002"
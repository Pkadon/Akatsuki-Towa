label avg26015(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1215595)]' (**arg(1, 1215595))
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215596)]' (**arg(2, 1215596))
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215597)]' (**arg(3, 1215597))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215598)]' (**arg(4, 1215598))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215599)]' (**arg(5, 1215599))
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215600)]' (**arg(6, 1215600))
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215745)]' (**arg(7, 1215745))
get_char('c0') '[convertstrid(1215601)]' (**arg(8, 1215601))
get_char('c0') '[convertstrid(1215602)]' (**arg(9, 1215602))
get_char('c0') '[convertstrid(1215603)]' (**arg(10, 1215603))
return "avg26015"
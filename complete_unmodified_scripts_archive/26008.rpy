label avg26008(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1215553)]' (**arg(1, 1215553))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215554)]' (**arg(2, 1215554))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215555)]' (**arg(3, 1215555))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215556)]' (**arg(4, 1215556))
return "avg26008"
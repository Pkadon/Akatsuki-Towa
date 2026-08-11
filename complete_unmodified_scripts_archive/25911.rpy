label avg25911(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1215021)]' (**arg(1, 1215021))
hide p1
$ update_portrait('oc002_01 18', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215022)]' (**arg(2, 1215022))
return "avg25911"
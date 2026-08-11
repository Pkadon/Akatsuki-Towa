label avg25904(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1215007)]' (**arg(1, 1215007))
hide p1
$ update_portrait('oc002_01 18', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215008)]' (**arg(2, 1215008))
return "avg25904"
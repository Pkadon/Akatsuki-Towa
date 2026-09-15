label avg25901(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1215001)]' (**arg(1, 1215001))
$ update_portrait('oc001_01 5', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1215002)]' (**arg(2, 1215002))
return "avg25901"
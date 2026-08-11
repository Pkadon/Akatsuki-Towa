label avg22313(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc004_01 2', 'p4', [mid(-5), light], 6)
$ update_narrator('c43')
window show
with trans
get_char('c43') '[convertstrid(1133256)]' (**arg(1, 1133256))
hide p4
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133257)]' (**arg(2, 1133257))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1133258)]' (**arg(3, 1133258))
hide p2
$ update_portrait('oc003_01 8', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1133259)]' (**arg(4, 1133259))
hide p3
$ update_portrait('oc004_01 8', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1133260)]' (**arg(5, 1133260))
hide p4
$ update_portrait('sc051_01 4', 'p58', [mid(-32), light], 6)
get_char('c583') '[convertstrid(1133261)]' (**arg(6, 1133261))
hide p58
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1133262)]' (**arg(7, 1133262))
return "avg22313"
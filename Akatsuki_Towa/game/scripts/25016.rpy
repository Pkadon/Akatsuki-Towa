label avg25016(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1210033)]' (**arg(1, 1210033))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210034)]' (**arg(2, 1210034))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210035)]' (**arg(3, 1210035))
menu:
    extend ""
    '[convertstrid(1214999)]':
        call avg25025
    '[convertstrid(1215000)]':
        call avg25026
return _return
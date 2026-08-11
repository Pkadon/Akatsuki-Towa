label avg25010(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('uc001_01 1', 'p587', [mid(-2), light], 6)
$ update_narrator('c5873')
window show
with trans
get_char('c5873') '[convertstrid(1210016)]' (**arg(1, 1210016))
hide p587
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210017)]' (**arg(2, 1210017))
hide p1
$ update_portrait('uc001_01 1', 'p587', [mid(-2), light], 6)
get_char('c5873') '[convertstrid(1210018)]' (**arg(3, 1210018))
menu:
    extend ""
    '[convertstrid(1214999)]':
        call avg25011
    '[convertstrid(1215000)]':
        call avg25000
return _return
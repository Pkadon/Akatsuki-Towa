label avg25071(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1210223)]' (**arg(1, 1210223))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210224)]' (**arg(2, 1210224))
menu:
    extend ""
    '[convertstrid(1210240)]':
        call avg25072
    '[convertstrid(1210241)]':
        call avg25072
return _return
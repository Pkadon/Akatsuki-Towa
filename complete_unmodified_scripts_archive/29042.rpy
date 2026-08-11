label avg29042(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1100027)]' (**arg(1, 1100027))
menu:
    extend ""
    '[convertstrid(1100028)]':
        call avg29043
    '[convertstrid(1100029)]':
        call avg29044
return _return
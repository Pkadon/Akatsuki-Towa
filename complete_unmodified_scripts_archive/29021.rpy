label avg29021(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1100007)]' (**arg(1, 1100007))
menu:
    extend ""
    '[convertstrid(1100008)]':
        call avg29022
    '[convertstrid(1100009)]':
        call avg29023
return _return
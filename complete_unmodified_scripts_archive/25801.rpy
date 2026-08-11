label avg25801(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1210341)]' (**arg(1, 1210341))
menu:
    extend ""
    '[convertstrid(1210240)]':
        call avg25117
    '[convertstrid(1210241)]':
        call avg25118
return _return
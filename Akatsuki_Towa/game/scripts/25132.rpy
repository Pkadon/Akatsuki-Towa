label avg25132(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c20133')
window show
with trans
get_char('c20133') '[convertstrid(1210399)]' (**arg(1, 1210399))
menu:
    extend ""
    '[convertstrid(1214995)]':
        call avg25133
    '[convertstrid(1214996)]':
        call avg25026
return _return
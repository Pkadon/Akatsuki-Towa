label avg25212(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c20233')
window show
with trans
get_char('c20233') '[convertstrid(1210738)]' (**arg(1, 1210738))
menu:
    extend ""
    '[convertstrid(1214995)]':
        call avg25213
    '[convertstrid(1214996)]':
        call avg25026
return _return
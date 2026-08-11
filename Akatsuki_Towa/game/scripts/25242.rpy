label avg25242(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c20243')
window show
with trans
get_char('c20243') '[convertstrid(1210880)]' (**arg(1, 1210880))
menu:
    extend ""
    '[convertstrid(1214995)]':
        call avg25243
    '[convertstrid(1214996)]':
        call avg25026
return _return
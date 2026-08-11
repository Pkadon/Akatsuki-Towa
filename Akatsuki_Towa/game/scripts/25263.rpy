label avg25263(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c20133')
window show
with trans
play sfx2 "other_7050.ogg"
get_char('c20133') '[convertstrid(1210983)]' (**arg(1, 1210983))
menu:
    extend ""
    '[convertstrid(1214995)]':
        call avg25264
    '[convertstrid(1214996)]':
        call avg25026
return _return
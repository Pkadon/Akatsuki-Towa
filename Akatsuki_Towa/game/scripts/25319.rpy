label avg25319(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c20243')
window show
with trans
get_char('c20243') '[convertstrid(1211235)]' (**arg(1, 1211235))
menu:
    extend ""
    '[convertstrid(1214995)]':
        call avg25320
    '[convertstrid(1214996)]':
        call avg25026
return _return
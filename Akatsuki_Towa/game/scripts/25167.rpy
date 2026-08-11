label avg25167(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1210547)]' (**arg(1, 1210547))
menu:
    extend ""
    '[convertstrid(1214997)]':
        call avg25168
    '[convertstrid(1214996)]':
        call avg25026
return _return
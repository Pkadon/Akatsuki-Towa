label avg25150(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('uc001_02 2', 'p2014', [mid(6), light], 6)
$ update_narrator('c20143')
window show
with trans
get_char('c20143') '[convertstrid(1210478)]' (**arg(1, 1210478))
menu:
    extend ""
    '[convertstrid(1214999)]':
        call avg25151
    '[convertstrid(1214996)]':
        call avg25026
return _return
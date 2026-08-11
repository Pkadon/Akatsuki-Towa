label avg25051(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('uc001_02 3', 'p2006', [mid(6), light], 6)
$ update_narrator('c20063')
window show
with trans
get_char('c20063') '[convertstrid(1210140)]' (**arg(1, 1210140))
hide p2006
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210141)]' (**arg(2, 1210141))
hide p1
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 6)
get_char('c20063') '[convertstrid(1210142)]' (**arg(3, 1210142))
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 6)
get_char('c20063') '[convertstrid(1210143)]' (**arg(4, 1210143))
menu:
    extend ""
    '[convertstrid(1214999)]':
        call avg25052
    '[convertstrid(1215000)]':
        call avg25000
return _return
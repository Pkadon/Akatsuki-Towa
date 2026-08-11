label avg101208(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc004_01 2', 'p12', [l(-12), light, flip], 6)
$ update_narrator('c121')
window show
with trans
get_char('c121') '[convertstrid(1220680)]' (**arg(1, 1220680))
$ update_portrait('sc004_01 2', 'p12', [l(-12), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1220681)]' (**arg(2, 1220681))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc004_01 1', 'p12', [l(-12), light, flip], 6)
get_char('c121') '[convertstrid(1220682)]' (**arg(3, 1220682))
menu:
    extend ""
    '[convertstrid(1220683)]':
        call avg101209
    '[convertstrid(1220684)]':
        call avg101210
    '[convertstrid(1220685)]':
        call avg101211
return _return
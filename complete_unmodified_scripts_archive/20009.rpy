label avg20009(trans=fade_in):

$ play_music("ed7150.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1000491)]' (**arg(1, 1000491))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
play sfx2 "other_7004.ogg"
get_char('c13') '[convertstrid(1000492)]' (**arg(2, 1000492))
return "avg20009"
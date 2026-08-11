label avg20017(trans=fade_in):

$ play_music("ED6101.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7017.ogg"
get_char('c13') '[convertstrid(1001028)]' (**arg(1, 1001028))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
play sfx2 "other_7064.ogg"
get_char('c13') '[convertstrid(1001029)]' (**arg(2, 1001029))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1001030)]' (**arg(3, 1001030))
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1001031)]' (**arg(4, 1001031))
return "avg20017"
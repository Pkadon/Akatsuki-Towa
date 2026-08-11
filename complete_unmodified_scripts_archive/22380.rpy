label avg22380(trans=fade_in):

$ play_music("ed7304.ogg")
scene placeholderbackground
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7079.ogg"
get_char('c0') '[convertstrid(1133976)]' (**arg(1, 1133976))
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133977)]' (**arg(2, 1133977))
hide p1
$ update_portrait('oc004_01 2', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1133978)]' (**arg(3, 1133978))
hide p4
$ update_portrait('oc003_01 2', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1133979)]' (**arg(4, 1133979))
hide p3
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c23') '[convertstrid(1133980)]' (**arg(5, 1133980))
hide p2
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133981)]' (**arg(6, 1133981))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1133982)]' (**arg(7, 1133982))
return "avg22380"
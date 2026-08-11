label avg20022(trans=fade_in):

$ play_music("ed7150.ogg")
scene placeholderbackground
$ update_portrait('st004_01 2', 'p204', [mid(4), light], 6)
$ update_narrator('c2043')
window show
with trans
get_char('c2043') '[convertstrid(1001637)]' (**arg(1, 1001637))
hide p204
$ update_portrait('sc043_01 1', 'p50', [mid(-20), light], 6)
get_char('c503') '[convertstrid(1001638)]' (**arg(2, 1001638))
hide p50
$ update_portrait('st004_01 1', 'p204', [mid(4), light], 6)
get_char('c2043') '[convertstrid(1001639)]' (**arg(3, 1001639))
hide p204
$ update_portrait('sc043_01 1', 'p50', [mid(-20), light], 6)
get_char('c503') '[convertstrid(1001638)]' (**arg(4, 1001638))
hide p50
$ update_portrait('st004_01 2', 'p204', [mid(4), light], 6)
get_char('c2043') '[convertstrid(1001641)]' (**arg(5, 1001641))
$ update_portrait('st004_01 5', 'p204', [mid(4), light], 6)
get_char('c2043') '[convertstrid(1001642)]' (**arg(6, 1001642))
$ update_portrait('st004_01 1', 'p204', [mid(4), light], 6)
get_char('c2043') '[convertstrid(1001643)]' (**arg(7, 1001643))
hide p204
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1001644)]' (**arg(8, 1001644))
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1001645)]' (**arg(9, 1001645))
return "avg20022"
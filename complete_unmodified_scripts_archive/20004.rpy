label avg20004:

$ play_music("ed9997.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1000214)]' (**arg(1, 1000214))
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000215)]' (**arg(2, 1000215))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000216)]' (**arg(3, 1000216))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000217)]' (**arg(4, 1000217))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000218)]' (**arg(5, 1000218))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1000219)]' (**arg(6, 1000219))
hide p1
play sfx2 "common_remind.ogg"
get_char('c0') '[convertstrid(1000220)]' (**arg(7, 1000220))
get_char('c0') '[convertstrid(1000221)]' (**arg(8, 1000221))
get_char('c0') '[convertstrid(1000223)]' (**arg(9, 1000223))
return
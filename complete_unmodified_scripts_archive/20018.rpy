label avg20018(trans=fade_in):

$ play_music("ed7561.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7088.ogg"
get_char('c13') '[convertstrid(1001032)]' (**arg(1, 1001032))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
get_char('c13') '[convertstrid(1001033)]' (**arg(2, 1001033))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1001034)]' (**arg(3, 1001034))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfx2 "other_7020.ogg"
get_char('c13') '[convertstrid(1001035)]' (**arg(4, 1001035))
return "avg20018"
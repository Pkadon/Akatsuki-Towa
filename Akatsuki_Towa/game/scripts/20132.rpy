label avg20132(trans=fade_in):

$ play_music("ed7300.ogg")
scene avg_bg_071
$ update_portrait('oc001_01 3', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
play sfx2 "other_7049.ogg"
get_char('c11') '[convertstrid(1006660)]' (**arg(1, 1006660))
$ update_portrait('oc001_01 3', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch17.ogg"
get_char('c23') '[convertstrid(1006661)]' (**arg(2, 1006661))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1006662)]' (**arg(3, 1006662))
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro19.ogg"
get_char('c33') '[convertstrid(1006663)]' (**arg(4, 1006663))
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc044_01 2', 'p51', [l(-7), light, flip], 6)
get_char('c511') '[convertstrid(1006664)]' (**arg(5, 1006664))
$ update_portrait('sc044_01 2', 'p51', [l(-7), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1006665)]' (**arg(6, 1006665))
hide p3
play sfx2 "other_7072.ogg"
play sfxvoice "avg_vocal_ji03.ogg"
get_char('c7013') '[convertstrid(1006666)]' (**arg(7, 1006666))
hide p51
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1006667)]' (**arg(8, 1006667))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1006668)]' (**arg(9, 1006668))
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc044_01 3', 'p51', [l(-7), light, flip], 6)
get_char('c511') '[convertstrid(1006669)]' (**arg(10, 1006669))
return "avg20132"
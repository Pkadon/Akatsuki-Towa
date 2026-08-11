label avg22235(trans=fade_in):

$ play_music("ed7202.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "bat_craft_wind_01.ogg"
get_char('c13') '[convertstrid(1121156)]' (**arg(1, 1121156))
hide p1
$ update_portrait('oc004_01 2', 'p4', [mid(-5), light], 6)
play sfxvoice "avg_vocal_li12.ogg"
get_char('c43') '[convertstrid(1121157)]' (**arg(2, 1121157))
hide p4
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1121158)]' (**arg(3, 1121158))
hide p1
$ update_portrait('oc004_01 11', 'p4', [mid(-5), light], 6)
play sfxvoice "avg_vocal_li16.ogg"
get_char('c43') '[convertstrid(1121159)]' (**arg(4, 1121159))
hide p4
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1121160)]' (**arg(5, 1121160))
hide p2
play sfx2 "other_7013.ogg"
get_char('c0') '[convertstrid(1121161)]' (**arg(6, 1121161))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "bat_craft_wind_01.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1121162)]' (**arg(7, 1121162))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1121163)]' (**arg(8, 1121163))
hide p2
$ update_portrait('oc004_01 23', 'p4', [mid(-5), light], 6)
play sfxvoice "avg_vocal_li09.ogg"
get_char('c43') '[convertstrid(1121164)]' (**arg(9, 1121164))
hide p4
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1121165)]' (**arg(10, 1121165))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1121166)]' (**arg(11, 1121166))
hide p1
$ update_portrait('oc004_01 18', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1121167)]' (**arg(12, 1121167))
return "avg22235"
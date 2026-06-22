label avg22385:

$ play_music("ed7201.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7021.ogg"
get_char('c23') '[convertstrid(1133911)]' (**arg(1, 1133911))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133912)]' (**arg(2, 1133912))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1133913)]' (**arg(3, 1133913))
hide p2
play sfx2 "other_7080.ogg"
get_char('c20163') '[convertstrid(1133914)]' (**arg(4, 1133914))
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1133915)]' (**arg(5, 1133915))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc002_c02_01.ogg"
get_char('c23') '[convertstrid(1133916)]' (**arg(6, 1133916))
return
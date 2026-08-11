label avg25160(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c20153')
window show
with trans
play sfx2 "fight_6022.ogg"
get_char('c20153') '[convertstrid(1210517)]' (**arg(1, 1210517))
play sfx2 "other_7080.ogg"
get_char('c20163') '[convertstrid(1210518)]' (**arg(2, 1210518))
get_char('c20153') '[convertstrid(1210519)]' (**arg(3, 1210519))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_c02_01.ogg"
get_char('c23') '[convertstrid(1210520)]' (**arg(4, 1210520))
hide p2
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na24.ogg"
get_char('c13') '[convertstrid(1210521)]' (**arg(5, 1210521))
return "avg25160"
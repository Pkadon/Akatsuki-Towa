label avg25296:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c23') '[convertstrid(1211128)]' (**arg(1, 1211128))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na10.ogg"
get_char('c13') '[convertstrid(1211129)]' (**arg(2, 1211129))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1211130)]' (**arg(3, 1211130))
hide p2
get_char('c20153') '[convertstrid(1211131)]' (**arg(4, 1211131))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1211132)]' (**arg(5, 1211132))
hide p1
play sfx2 "other_7093.ogg"
get_char('c0') '[convertstrid(1211133)]' (**arg(6, 1211133))
get_char('c20153') '[convertstrid(1211134)]' (**arg(7, 1211134))
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1211135)]' (**arg(8, 1211135))
hide p2
get_char('c20153') '[convertstrid(1211136)]' (**arg(9, 1211136))
play sfx2 "other_7086.ogg"
get_char('c0') '[convertstrid(1211137)]' (**arg(10, 1211137))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1211138)]' (**arg(11, 1211138))
return
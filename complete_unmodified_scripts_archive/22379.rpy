label avg22379:

$ play_music("ed7304.ogg")
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1133970)]' (**arg(1, 1133970))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133971)]' (**arg(2, 1133971))
hide p1
play sfx2 "other_7080.ogg"
get_char('c0') '[convertstrid(1133972)]' (**arg(3, 1133972))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1133973)]' (**arg(4, 1133973))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133974)]' (**arg(5, 1133974))
return
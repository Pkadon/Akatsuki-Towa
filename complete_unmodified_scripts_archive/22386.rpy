label avg22386:

$ play_music("ed7201.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch17.ogg"
get_char('c23') '[convertstrid(1133918)]' (**arg(1, 1133918))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133919)]' (**arg(2, 1133919))
hide p1
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1133920)]' (**arg(3, 1133920))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133921)]' (**arg(4, 1133921))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1133922)]' (**arg(5, 1133922))
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133923)]' (**arg(6, 1133923))
return
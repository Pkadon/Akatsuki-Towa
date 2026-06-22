label avg20032:

$ play_music("ed7104.ogg")
scene avg_bg_001
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1002165)]' (**arg(1, 1002165))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1002166)]' (**arg(2, 1002166))
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1002167)]' (**arg(3, 1002167))
return
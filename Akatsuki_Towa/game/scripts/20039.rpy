label avg20039:

$ play_music("ED6200.ogg")
scene avg_bg_010
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1002318)]' (**arg(1, 1002318))
hide p2
$ update_portrait('uc004_02 1', 'p570', [r(-9), light], 6)
get_char('c5703') '[convertstrid(1002319)]' (**arg(2, 1002319))
$ update_portrait('uc004_02 1', 'p570', [r(-9), dark], 5)
$ update_portrait('sc017_01 1', 'p571', [l(-7), light, flip], 6)
get_char('c5711') '[convertstrid(1002320)]' (**arg(3, 1002320))
$ update_portrait('sc017_01 1', 'p571', [l(-7), light, flip], 6)
get_char('c5711') '[convertstrid(1002321)]' (**arg(4, 1002321))
$ update_portrait('sc017_01 1', 'p571', [l(-7), dark, flip], 5)
$ update_portrait('uc004_02 1', 'p570', [r(-9), light], 6)
get_char('c5703') '[convertstrid(1002322)]' (**arg(5, 1002322))
hide p571
hide p570
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
with fade
play sfxvoice "avg_vocal_ch21.ogg"
get_char('c23') '[convertstrid(1002323)]' (**arg(6, 1002323))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c11') '[convertstrid(1002324)]' (**arg(7, 1002324))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1002325)]' (**arg(8, 1002325))
return
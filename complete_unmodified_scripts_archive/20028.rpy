label avg20028:

$ play_music("ed7150.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1001691)]' (**arg(1, 1001691))
hide p2
$ update_portrait('st008_01 1', 'p208', [mid(-19), light], 6)
get_char('c2083') '[convertstrid(1001692)]' (**arg(2, 1001692))
$ update_portrait('st008_01 1', 'p208', [mid(-19), light], 6)
get_char('c2083') '[convertstrid(1001693)]' (**arg(3, 1001693))
hide p208
$ update_portrait('oc002_01 15', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1001694)]' (**arg(4, 1001694))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1001695)]' (**arg(5, 1001695))
hide p1
$ update_portrait('st008_01 1', 'p208', [mid(-19), light], 6)
get_char('c2083') '[convertstrid(1001696)]' (**arg(6, 1001696))
$ update_portrait('st008_01 5', 'p208', [mid(-19), light], 6)
get_char('c2083') '[convertstrid(1001697)]' (**arg(7, 1001697))
$ update_portrait('st008_01 1', 'p208', [mid(-19), light], 6)
get_char('c2083') '[convertstrid(1001698)]' (**arg(8, 1001698))
hide p208
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1001699)]' (**arg(9, 1001699))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1001700)]' (**arg(10, 1001700))
hide p1
$ update_portrait('st007_01 1', 'p207', [mid(-6), light], 6)
get_char('c2073') '[convertstrid(1001701)]' (**arg(11, 1001701))
hide p207
$ update_portrait('st003_01 1', 'p203', [mid(-7), light], 6)
get_char('c2033') '[convertstrid(1001702)]' (**arg(12, 1001702))
hide p203
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1001703)]' (**arg(13, 1001703))
hide p1
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1001704)]' (**arg(14, 1001704))
return
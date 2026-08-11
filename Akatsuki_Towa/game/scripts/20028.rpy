label avg20028(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_006
$ update_narrator('c23')
window show
with trans
$ update_portrait('oc002_01 1', 'p2', [r_entrance(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1001691)]' (**arg(1, 1001691))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('st008_01 1', 'p208', [l(-19), light, flip], 6)
get_char('c2081') '[convertstrid(1001692)]' (**arg(2, 1001692))
$ update_portrait('st008_01 1', 'p208', [l(-19), light, flip], 6)
get_char('c2081') '[convertstrid(1001693)]' (**arg(3, 1001693))
$ update_portrait('st008_01 1', 'p208', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1001694)]' (**arg(4, 1001694))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1001695)]' (**arg(5, 1001695))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st008_01 1', 'p208', [l(-19), light, flip], 6)
get_char('c2081') '[convertstrid(1001696)]' (**arg(6, 1001696))
$ update_portrait('st008_01 5', 'p208', [l(-19), light, flip], 6)
get_char('c2081') '[convertstrid(1001697)]' (**arg(7, 1001697))
$ update_portrait('st008_01 1', 'p208', [l(-19), light, flip], 6)
get_char('c2081') '[convertstrid(1001698)]' (**arg(8, 1001698))
hide p1
$ update_portrait('st008_01 1', 'p208', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1001699)]' (**arg(9, 1001699))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1001700)]' (**arg(10, 1001700))
hide p208
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st007_01 1', 'p207', [l(-6), light, flip], 6)
get_char('c2071') '[convertstrid(1001701)]' (**arg(11, 1001701))
hide p207
$ update_portrait('st003_01 1', 'p203', [l(-7), light, flip], 6)
get_char('c2031') '[convertstrid(1001702)]' (**arg(12, 1001702))
$ update_portrait('st003_01 1', 'p203', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001703)]' (**arg(13, 1001703))
hide p1
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1001704)]' (**arg(14, 1001704))
return "avg20028"
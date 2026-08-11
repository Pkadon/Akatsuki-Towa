label avg12187(trans=fade_in):

$ play_music("ED6200.ogg")
scene avg_bg_027
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
get_char('c21') '[convertstrid(1120700)]' (**arg(1, 1120700))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
get_char('c9803') '[convertstrid(1120701)]' (**arg(2, 1120701))
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120702)]' (**arg(3, 1120702))
hide p1
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c21') '[convertstrid(1120703)]' (**arg(4, 1120703))
$ update_portrait('oc002_01 13', 'p2', [l(-3), dark, flip], 5)
get_char('c9803') '[convertstrid(1120704)]' (**arg(5, 1120704))
get_char('c9803') '[convertstrid(1120705)]' (**arg(6, 1120705))
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c11') '[convertstrid(1120706)]' (**arg(7, 1120706))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
get_char('c9803') '[convertstrid(1120707)]' (**arg(8, 1120707))
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1120708)]' (**arg(9, 1120708))
return "avg12187"
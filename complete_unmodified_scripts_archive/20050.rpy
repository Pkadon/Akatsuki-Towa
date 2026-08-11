label avg20050(trans=fade_in):

$ play_music("ED6505.ogg")
scene avg_bg_027
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1002777)]' (**arg(1, 1002777))
hide p2
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1002778)]' (**arg(2, 1002778))
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1002779)]' (**arg(3, 1002779))
hide p3
$ update_portrait('oc004_01 4', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1002780)]' (**arg(4, 1002780))
$ update_portrait('oc004_01 4', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1002781)]' (**arg(5, 1002781))
$ update_portrait('oc004_01 21', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1002782)]' (**arg(6, 1002782))
$ update_portrait('oc004_01 4', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1002783)]' (**arg(7, 1002783))
hide p4
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c23') '[convertstrid(1002784)]' (**arg(8, 1002784))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1002785)]' (**arg(9, 1002785))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1002786)]' (**arg(10, 1002786))
return "avg20050"
label avg20049:

$ play_music("ED6505.ogg")
scene avg_bg_027
$ update_narrator('c5963')
window show
with fade_in
get_char('c5963') '[convertstrid(1002767)]' (**arg(1, 1002767))
get_char('c5963') '[convertstrid(1002768)]' (**arg(2, 1002768))
get_char('c5963') '[convertstrid(1002769)]' (**arg(3, 1002769))
get_char('c5963') '[convertstrid(1002770)]' (**arg(4, 1002770))
get_char('c5973') '[convertstrid(1002771)]' (**arg(5, 1002771))
get_char('c5973') '[convertstrid(1002772)]' (**arg(6, 1002772))
get_char('c5983') '[convertstrid(1002773)]' (**arg(7, 1002773))
get_char('c5963') '[convertstrid(1002774)]' (**arg(8, 1002774))
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1002775)]' (**arg(9, 1002775))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1002776)]' (**arg(10, 1002776))
return
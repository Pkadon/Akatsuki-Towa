label avg25199(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210668)]' (**arg(1, 1210668))
hide p2
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1210669)]' (**arg(2, 1210669))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1210670)]' (**arg(3, 1210670))
hide p1
$ update_portrait('uc003_01 3', 'p2018', [mid(-26), light], 6)
play sfx2 "other_7085.ogg"
get_char('c20183') '[convertstrid(1210671)]' (**arg(4, 1210671))
hide p2018
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c23') '[convertstrid(1210672)]' (**arg(5, 1210672))
hide p2
$ update_portrait('uc003_01 3', 'p2018', [mid(-26), light], 6)
get_char('c20183') '[convertstrid(1210673)]' (**arg(6, 1210673))
hide p2018
play sfx2 "other_7086.ogg"
get_char('c0') '[convertstrid(1210674)]' (**arg(7, 1210674))
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210675)]' (**arg(8, 1210675))
return "avg25199"
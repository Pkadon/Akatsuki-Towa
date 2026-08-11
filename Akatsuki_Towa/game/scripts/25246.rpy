label avg25246(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na16.ogg"
get_char('c13') '[convertstrid(1210890)]' (**arg(1, 1210890))
hide p1
get_char('c20243') '[convertstrid(1210891)]' (**arg(2, 1210891))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch29.ogg"
get_char('c23') '[convertstrid(1210892)]' (**arg(3, 1210892))
hide p2
get_char('c20243') '[convertstrid(1210893)]' (**arg(4, 1210893))
$ update_portrait('oc001_01 21', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
get_char('c13') '[convertstrid(1210894)]' (**arg(5, 1210894))
return "avg25246"
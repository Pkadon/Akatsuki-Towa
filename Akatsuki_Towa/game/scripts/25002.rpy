label avg25002(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "common_select.ogg"
get_char('c23') '[convertstrid(1210002)]' (**arg(1, 1210002))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1210003)]' (**arg(2, 1210003))
return "avg25002"
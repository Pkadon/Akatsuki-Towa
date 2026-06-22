label avg25024:

stop music
scene placeholderbackground
$ update_narrator('c20103')
window show
with fade_in
get_char('c20103') '[convertstrid(1210058)]' (**arg(1, 1210058))
get_char('c20103') '[convertstrid(1210059)]' (**arg(2, 1210059))
get_char('c20083') '[convertstrid(1210060)]' (**arg(3, 1210060))
get_char('c20103') '[convertstrid(1210061)]' (**arg(4, 1210061))
get_char('c20093') '[convertstrid(1210062)]' (**arg(5, 1210062))
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1210063)]' (**arg(6, 1210063))
hide p2
play sfx2 "common_35rewardholy.ogg"
get_char('c20103') '[convertstrid(1210064)]' (**arg(7, 1210064))
return
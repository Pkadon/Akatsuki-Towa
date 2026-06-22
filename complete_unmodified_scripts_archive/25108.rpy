label avg25108:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1210316)]' (**arg(1, 1210316))
hide p1
get_char('c6123') '[convertstrid(1210317)]' (**arg(2, 1210317))
play sfx2 "other_7092.ogg"
get_char('c0') '[convertstrid(1210318)]' (**arg(3, 1210318))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210319)]' (**arg(4, 1210319))
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
get_char('c13') '[convertstrid(1210320)]' (**arg(5, 1210320))
return
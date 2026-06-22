label avg25191:

stop music
scene placeholderbackground
$ update_portrait('uc003_01 3', 'p2018', [mid(-26), light], 6)
$ update_narrator('c20183')
window show
with fade_in
get_char('c20183') '[convertstrid(1210638)]' (**arg(1, 1210638))
hide p2018
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210639)]' (**arg(2, 1210639))
hide p2
$ update_portrait('uc003_01 3', 'p2018', [mid(-26), light], 6)
get_char('c20183') '[convertstrid(1210640)]' (**arg(3, 1210640))
hide p2018
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na11.ogg"
get_char('c13') '[convertstrid(1210641)]' (**arg(4, 1210641))
hide p1
$ update_portrait('uc003_01 3', 'p2018', [mid(-26), light], 6)
get_char('c20183') '[convertstrid(1210642)]' (**arg(5, 1210642))
hide p2018
play sfx2 "other_7086.ogg"
get_char('c0') '[convertstrid(1210643)]' (**arg(6, 1210643))
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
get_char('c13') '[convertstrid(1210644)]' (**arg(7, 1210644))
return
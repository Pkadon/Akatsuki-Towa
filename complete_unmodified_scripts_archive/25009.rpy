label avg25009(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1210014)]' (**arg(1, 1210014))
hide p1
$ update_portrait('uc001_01 1', 'p587', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
get_char('c5873') '[convertstrid(1210015)]' (**arg(2, 1210015))
return "avg25009"
label avg25172(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_35rewardholy.ogg"
get_char('c13') '[convertstrid(1210553)]' (**arg(1, 1210553))
return "avg25172"
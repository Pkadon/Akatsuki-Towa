label avg29014(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with trans
play sfx2 "common_35rewardholy.ogg"
get_char('c0') '[convertstrid(1100006)]' (**arg(1, 1100006))
return "avg29014"
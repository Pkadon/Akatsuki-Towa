label avg101705(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc009_01 5', 'p17', [l(-13), light, flip], 6)
$ update_narrator('c171')
window show
with trans
get_char('c171') '[convertstrid(1221890)]' (**arg(1, 1221890))
return "avg101705"
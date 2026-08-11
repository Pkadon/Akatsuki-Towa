label avg101707(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
$ update_narrator('c171')
window show
with trans
get_char('c171') '[convertstrid(1221892)]' (**arg(1, 1221892))
return "avg101707"
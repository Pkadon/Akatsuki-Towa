label avg101713(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc009_01 2', 'p17', [l(-13), light, flip], 6)
$ update_narrator('c171')
window show
with trans
get_char('c171') '[convertstrid(1221906)]' (**arg(1, 1221906))
return "avg101713"
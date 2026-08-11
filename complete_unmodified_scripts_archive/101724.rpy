label avg101724(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc009_01 6', 'p17', [l(-13), light, flip], 6)
$ update_narrator('c171')
window show
with trans
get_char('c171') '[convertstrid(1221940)]' (**arg(1, 1221940))
return "avg101724"
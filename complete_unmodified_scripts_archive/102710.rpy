label avg102710(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc019_01 1', 'p27', [l(-18), light, flip], 6)
$ update_narrator('c271')
window show
with trans
get_char('c271') '[convertstrid(1219468)]' (**arg(1, 1219468))
return "avg102710"
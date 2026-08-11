label avg102722(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc019_01 4', 'p27', [l(-18), light, flip], 6)
$ update_narrator('c271')
window show
with trans
get_char('c271') '[convertstrid(1219503)]' (**arg(1, 1219503))
return "avg102722"
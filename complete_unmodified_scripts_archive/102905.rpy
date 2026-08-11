label avg102905(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
$ update_narrator('c291')
window show
with trans
get_char('c291') '[convertstrid(1219913)]' (**arg(1, 1219913))
return "avg102905"
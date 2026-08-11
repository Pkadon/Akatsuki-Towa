label avg101905(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
$ update_narrator('c191')
window show
with trans
get_char('c191') '[convertstrid(1218339)]' (**arg(1, 1218339))
return "avg101905"
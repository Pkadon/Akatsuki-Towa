label avg101906(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc011_01 2', 'p19', [l(-1), light, flip], 6)
$ update_narrator('c191')
window show
with trans
get_char('c191') '[convertstrid(1218340)]' (**arg(1, 1218340))
return "avg101906"
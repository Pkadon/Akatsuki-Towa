label avg101911(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
$ update_narrator('c191')
window show
with trans
get_char('c191') '[convertstrid(1218351)]' (**arg(1, 1218351))
return "avg101911"
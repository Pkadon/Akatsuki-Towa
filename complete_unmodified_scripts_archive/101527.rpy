label avg101527(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
$ update_narrator('c151')
window show
with trans
get_char('c151') '[convertstrid(1221339)]' (**arg(1, 1221339))
return "avg101527"
label avg101607(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc008_01 1', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
window show
with trans
get_char('c161') '[convertstrid(1221547)]' (**arg(1, 1221547))
return "avg101607"
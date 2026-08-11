label avg101611(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc008_01 2', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
window show
with trans
get_char('c161') '[convertstrid(1221557)]' (**arg(1, 1221557))
return "avg101611"
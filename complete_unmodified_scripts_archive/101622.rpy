label avg101622(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
window show
with trans
get_char('c161') '[convertstrid(1221592)]' (**arg(1, 1221592))
return "avg101622"
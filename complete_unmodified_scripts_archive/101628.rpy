label avg101628(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc008_01 1', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
window show
with trans
get_char('c161') '[convertstrid(1221604)]' (**arg(1, 1221604))
return "avg101628"
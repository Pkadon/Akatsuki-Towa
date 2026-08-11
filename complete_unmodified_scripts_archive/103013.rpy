label avg103013(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc022_01 2', 'p30', [mid(-9), light], 6)
$ update_narrator('c303')
window show
with trans
get_char('c303') '[convertstrid(1222444)]' (**arg(1, 1222444))
return "avg103013"
label avg102817(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
$ update_narrator('c283')
window show
with trans
get_char('c283') '[convertstrid(1219750)]' (**arg(1, 1219750))
return "avg102817"
label avg102830(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
$ update_narrator('c283')
window show
with trans
get_char('c283') '[convertstrid(1219799)]' (**arg(1, 1219799))
return "avg102830"
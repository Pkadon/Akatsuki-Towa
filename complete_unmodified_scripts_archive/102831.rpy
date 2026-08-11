label avg102831(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc020_01 5', 'p28', [mid(-10), light], 6)
$ update_narrator('c283')
window show
with trans
get_char('c283') '[convertstrid(1219800)]' (**arg(1, 1219800))
return "avg102831"
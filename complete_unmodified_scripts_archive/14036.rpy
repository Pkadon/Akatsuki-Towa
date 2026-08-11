label avg14036(trans=fade_in):

$ play_music("ed7110.ogg")
scene avg_bg_015
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1202711)]' (**arg(1, 1202711))
get_char('c7521') '[convertstrid(1202712)]' (**arg(2, 1202712))
get_char('c7521') '[convertstrid(1202713)]' (**arg(3, 1202713))
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202714)]' (**arg(4, 1202714))
hide p2
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202715)]' (**arg(5, 1202715))
hide p1
get_char('c0') '[convertstrid(1202716)]' (**arg(6, 1202716))
get_char('c7521') '[convertstrid(1202717)]' (**arg(7, 1202717))
get_char('c7521') '[convertstrid(1202718)]' (**arg(8, 1202718))
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202719)]' (**arg(9, 1202719))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202720)]' (**arg(10, 1202720))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202721)]' (**arg(11, 1202721))
return "avg14036"